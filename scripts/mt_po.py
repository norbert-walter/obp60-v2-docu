#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mt_po.py — Machine Translation für Sphinx-PO-Kataloge mit Google Translate (v2, API-Key),
inkl. reST-Masking, Plural-Support, Batching und optionalem Throttling.

Env-Variablen:
  GOOGLE_API_KEY        # dein Google Cloud Translation API-Key (v2, Basic)
  TARGET_LANG=en        # Zielsprache (ISO, z. B. en, fr, es). Default: de
  REWRITE_FUZZY=true    # fuzzy-Einträge neu befüllen (Default: true)
  REWRITE_FILLED=false  # bereits gefüllte, nicht-fuzzy Einträge überschreiben (Default: false)
  DNT=Foo,Bar           # Kommagetrennte „Do Not Translate“-Phrasen (optional)
  BATCH_SIZE=128        # max. 128 Texte/Request (Default: 128)
  THROTTLE_SECONDS=0.2  # Pause zwischen Requests in Sekunden (Default: 0; setze z. B. 0.2 bei knapper Quote)

Aufruf (im Workflow mit working-directory=docs):
  python ../scripts/mt_po.py
oder explizit:
  python scripts/mt_po.py docs/locale/<TARGET_LANG>/LC_MESSAGES
"""
import os
import sys
import re
import html
import time
import requests
import polib
from itertools import islice
from typing import Dict, List, Tuple

# --------------------- Konfiguration aus ENV ---------------------
TARGET_LANG     = os.getenv("TARGET_LANG", "de").strip()
REWRITE_FUZZY   = os.getenv("REWRITE_FUZZY", "true").lower() == "true"
REWRITE_FILLED  = os.getenv("REWRITE_FILLED", "false").lower() == "true"
DNT_LIST        = [s.strip() for s in os.getenv("DNT", "").split(",") if s.strip()]
BATCH_SIZE      = int(os.getenv("BATCH_SIZE", "128"))
THROTTLE_SECONDS = float(os.getenv("THROTTLE_SECONDS", "0"))

# --------------------- Utilities ---------------------
def chunked(iterable, n):
    it = iter(iterable)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            return
        yield chunk

def need_nplurals(po: polib.POFile) -> int:
    m = re.search(r"nplurals\s*=\s*(\d+)", po.metadata.get("Plural-Forms", "") or "")
    return int(m.group(1)) if m else 2

# --------------------- Google v2 (API key) ---------------------
def google_translate_batch(texts: List[str], target: str) -> List[str]:
    """Übersetzt eine Liste von Strings (max. ~128) in einem Request."""
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_API_KEY missing")
    url = "https://translation.googleapis.com/language/translate/v2"
    payload = {"q": texts, "target": target, "format": "text"}
    try:
        r = requests.post(url, params={"key": key}, json=payload, timeout=60)
        if r.status_code >= 400:
            # Response enthält hilfreiche Fehlerdetails (quotaExceeded, billingNotEnabled, etc.)
            raise RuntimeError(f"Google Translate v2 error {r.status_code}: {r.text[:500]}")
        data = r.json()
        outs = [html.unescape(t["translatedText"]) for t in data["data"]["translations"]]
        return outs
    except requests.RequestException as ex:
        raise RuntimeError(f"HTTP error calling Google Translate v2: {ex}")

# --------------------- Masking für reST & Platzhalter ---------------------
MASK_PATTERNS: List[re.Pattern] = [
    re.compile(r"``[^`]+``"),                # inline code
    re.compile(r":[\w.-]+:`[^`]+`"),         # :role:`...`
    re.compile(r"`[^`]+`_"),                 # `text`_
#    re.compile(r"\*\*[^*\n]+\*\*"),          # **bold**
#    re.compile(r"\*[^*\s][^*\n]*\*"),        # *italic*
    re.compile(r"\|[^|\n]+\|"),              # |subst|
    # Platzhalter:
    re.compile(r"%\([^)]+\)[#0\- +]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[hlL]?[diouxXeEfFgGcrs%]"),
    re.compile(r"%(?:\d+\$)?[diouxXeEfFgGcrs%]"),
    re.compile(r"\{[^\{\}\n]+\}"),
]

def build_dnt_patterns(lst: List[str]) -> List[re.Pattern]:
    return [re.compile(re.escape(p)) for p in lst]

DNT_PATTERNS = build_dnt_patterns(DNT_LIST)

def mask_text(s: str) -> Tuple[str, Dict[str, str]]:
    table: Dict[str, str] = {}
    i = 0
    def sub_all(pats: List[re.Pattern], txt: str) -> str:
        nonlocal i
        for pat in pats:
            def repl(m):
                nonlocal i
                k = f"[[[[M{i}]]]]"
                table[k] = m.group(0)
                i += 1
                return k
            txt = pat.sub(repl, txt)
        return txt
    s = sub_all(MASK_PATTERNS, s)
    if DNT_PATTERNS:
        s = sub_all(DNT_PATTERNS, s)
    return s, table

def unmask_text(s: str, table: Dict[str, str]) -> str:
    for k, v in table.items():
        s = s.replace(k, v)
    return s

def translate_many_preserving_markup(texts: List[str]) -> List[str]:
    """Maskiert jeden Text, übersetzt im Batch, und demaskiert wieder."""
    masked, tables = [], []
    for t in texts:
        m, tab = mask_text(t)
        masked.append(m)
        tables.append(tab)
    outs = google_translate_batch(masked, TARGET_LANG.lower())
    return [unmask_text(o, tab) for o, tab in zip(outs, tables)]

# --------------------- PO-Logik ---------------------
def should_translate_entry(e: polib.POEntry) -> bool:
    if not e.msgid.strip():
        return False
    has_translation = bool(e.msgstr.strip()) if not e.msgid_plural else any((v or "").strip() for v in e.msgstr_plural.values())
    is_fuzzy = "fuzzy" in (e.flags or [])
    if not has_translation:
        return True
    if is_fuzzy and REWRITE_FUZZY:
        return True
    if REWRITE_FILLED:
        return True
    return False

def process_plural(e: polib.POEntry, nplurals: int) -> bool:
    """Einfacher Plural: Index 0 aus msgid, alle weiteren aus msgid_plural."""
    changed = False
    for i in range(nplurals):
        current = e.msgstr_plural.get(i, "")
        if current.strip() and not REWRITE_FILLED and not ("fuzzy" in e.flags and REWRITE_FUZZY):
            continue
        src = e.msgid if i == 0 else (e.msgid_plural or e.msgid)
        tr = translate_many_preserving_markup([src])[0]
        if e.msgstr_plural.get(i, "") != tr:
            e.msgstr_plural[i] = tr
            changed = True
    if "fuzzy" not in e.flags:
        e.flags.append("fuzzy")
        changed = True or changed
    return changed

def process_po_file(path: str) -> bool:
    po = polib.pofile(path)
    npl = need_nplurals(po)
    changed = False

    # 1) Plural-Einträge separat behandeln (der Einfachheit halber aktuell einzeln)
    for e in po:
        if e.msgid_plural and should_translate_entry(e):
            if process_plural(e, npl):
                changed = True

    # 2) Singuläre Einträge sammeln und in Batches übersetzen
    pending_entries: List[polib.POEntry] = [e for e in po if not e.msgid_plural and should_translate_entry(e)]
    total = len(pending_entries)
    if total:
        print(f"Translating {total} singular entries in {path} (batch={BATCH_SIZE})")
    for group in chunked(pending_entries, BATCH_SIZE):
        texts = [e.msgid for e in group]
        translated = translate_many_preserving_markup(texts)
        for e, tr in zip(group, translated):
            if e.msgstr != tr:
                e.msgstr = tr
                changed = True
            if "fuzzy" not in e.flags:
                e.flags.append("fuzzy")
                changed = True
        if THROTTLE_SECONDS > 0:
            time.sleep(THROTTLE_SECONDS)

    if changed:
        po.save(path)
        print(f"Updated {path}")
    return changed

def default_po_dir() -> str:
    # Standard: locale/<TARGET_LANG>/LC_MESSAGES relativ zum aktuellen Arbeitsverzeichnis
    return os.path.join("locale", TARGET_LANG.lower(), "LC_MESSAGES")

# --------------------- Main ---------------------
if __name__ == "__main__":
    po_dir = sys.argv[1] if len(sys.argv) > 1 else default_po_dir()
    if not os.path.isdir(po_dir):
        sys.stderr.write(f"PO directory not found: {po_dir}\n")
        sys.exit(2)
    print(f"Google v2 MT for {TARGET_LANG} in {po_dir} (REWRITE_FUZZY={REWRITE_FUZZY}, REWRITE_FILLED={REWRITE_FILLED}, BATCH_SIZE={BATCH_SIZE}, THROTTLE_SECONDS={THROTTLE_SECONDS})")

    for root, _, files in os.walk(po_dir):
        for fn in files:
            if fn.endswith(".po"):
                process_po_file(os.path.join(root, fn))
