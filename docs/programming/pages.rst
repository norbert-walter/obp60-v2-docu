Seitenerstellung
================

Um eine neue Seite zu erstellen sind folgende Schritte notwendig:

	1. Anlegen einer neuen Seite unter ``lib\obp60task\PageXXXX.cpp``
	2. Registrierung der Seite in ``lib\obp60task\obp60task.cpp``. Dazu die Funktion ``registerAllPages`` entsprechend erweitern
	3. In ``/lib/obp60task/config.json`` die neue Seite in die jeweiligen Seitenlisten aufnehmen oder Seite in ``/lib/obp60task/gen_set.py`` aufnehmen und damit den relevanten Teil der Datei ``/lib/obp60task/config.json`` neu erzeugen. 

Als Vorlage für eine neue Seite kann z.B. die vorhandene Seite *PageWhite* verwendet werden. Sie enthält nur minimalen Code. In der kopierten Seite ist dann lediglich der Text *White* durch *Beispiel* zu ersetzen.
