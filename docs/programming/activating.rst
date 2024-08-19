Kompilieren und Download
========================

Die Firmware zum OBP60 kann recht einfach selber an eigene Bedürfnisse angepasst werden. Der Source-Code befindet sich zentral auf Github im Internet. Alle Software-Revisionen sind dort verfügbar. Es können bei Bedarf aktuelle oder ältere Versionen benutzt werden. Als Betriebssysteme werden Linux, Windows und Mac iOS unterstützt. Zum Kompilieren der Firmware gibt es zwei Möglichkeiten.

	* Verwendung von Gitpod (webbasiert in Cloud)
	* Visual Studio Code mit PlatformIO Plugin (lokal auf dem PC)
	
Gitpod
------

Gitpod ist eine standardtisierte Entwicklungsumgebung die webbasiert ist und in der Cloud läuft. So ist es möglich auf jedem Rechner, der über einen aktuellen Webbrowser verfügt eine Code-Entwicklung durchzuführen ohne Installation von irgendwelchen Softwarebestandteilen. Zur Benutzung des Dienstes ist eine Anmeldung notwendig. Die Code Entwicklungsumgebung in Anlehnung an PlatformIO befindet sich jederzeit in einem aktuellen Zustand und bedarf keiner externen Abhängigkeiten. Das System ist sofort benutzbar und ist besonders für Anfänger geeignet oder für kleine Änderungen, die unterwegs mal schnell durchgeführt werden sollen. Die Benutzung von Github ist in der Free-Variante kostenfrei, unterliegt jedoch einigen Einschränkungen bezüglich Nutzungszeit und bereitgestellter Rechnerhardware. Aktuell sind 50 Stunden Nutzungszeit pro Monat frei und vollkommen ausreichend für einfache Änderungen. Wer mehr Zeit benötigt oder schnellere Hardware einsetzen möchte, kann den kostenpflichtigen Service von Gitpod nutzen. Weitere Details findet man auf der `Webseite von Gitpod`_.

.. _Webseite von Gitpod: https://www.gitpod.io

**Der Workflow bei Gitpod sieht folgendermaßen aus:**

	1. OBP60-Github-Projekt in eigenes Github-Repository forken
	2. Gitpod-Link zum Projekt öffnen
	3. In Gitpod Entwicklungsumgebung und Hardware auswählen
	4. Start eines Containers mit der Entwicklungsumgebung und Download des Projektes aus dem eigenen Github-Repository
	5. Source-Code in der Entwicklungsumgebung ändern und kompilieren
	6. Download des Binary-Files
	7. Aktualisierung der Änderungen im eigenen Github-Repository

   
Github-Projekt forken
^^^^^^^^^^^^^^^^^^^^^

Als erstes wird das Original-Projekt zum OBP60 in das eigene private Repository geforkt. Ein Fork ist so zu sagen eine Aufgabelung bzw. eine Abtrennung des Source-Codes in einen neuen Zweig. Durch einen Fork entsteht eine Kopie des Original-Projektes in ihrem privaten Repository. So können Sie Änderungen am Code vornehmen und in ihrem Repository speichern. Der neu entstandene Code ist dann eine Erweiterung oder Modifikation des Original-Projektes. Nur mit einem Fork ist es möglich, Code-Änderungen zu sichern.

.. image:: ../pics/Github_Fork.png
   :scale: 40%
Abb.: Fork erstellen

Melden Sie sich als erstes bei Github an und gehen dann in das `Original-Projekt zum OBP60`_ und drücken oben rechts auf die Schaltfläche **Fork**. Sie werden danach gefragt, ob sie der Quelle vertrauen und können dann einen neuen Projketnamen vergeben oder den originalen Projektnamen benutzen. Kopieren Sie sich danach den Link zu ihren Github-Projekt aus der Browser-Zeile. Sie sollten dann einen ähnlichen Link haben wie diesen:

.. _Original-Projekt zum OBP60: https://github.com/norbert-walter/esp32-nmea2000-obp60

https://github.com/MyPrivatRepositoryName/esp32-nmea2000-obp60

Den Part *MyPrivatRepositoryName* müssen Sie durch ihren eigenen Repositorynamen ersetzen.


Gitpod-Link öffnen
^^^^^^^^^^^^^^^^^^

Das Gitpad-Projekt wird über den Repositorynamen des Github-Projetes aufgerufen:

https://gitpod.io/#https://github.com/MyPrivatRepositoryName/esp32-nmea2000-obp60

Sie gelangen dann auf die Startseite von Gitpod und müssen sich dort anmelden. Loggen Sie sich dort mit dem bereits vorhandenen Github-Account ein.

.. image:: ../pics/Gitpod_Login.png
   :scale: 40%
Abb.: Login bei Gitpod mit Github-Account

Gitpod-Settings
^^^^^^^^^^^^^^^

Danach können Sie die Default-Einstellungen übernehmen. Sie sind schon korrekt auf das Projekt eingestellt.

.. image:: ../pics/Gitpod_New_Workplace.png
   :scale: 40%
Abb.: Einstellungen für Gitpod

Container-Start
^^^^^^^^^^^^^^^

Nach der Bestätigung der Einstellungen für Gitpod wird ein neuer Container gestartet und allle notwendigen Softwarebestandteile in den Container geladen. Der Vorgang kann etwas Zeit beanspruchen.

.. image:: ../pics/Gitpod_Workplace.png
   :scale: 40%
Abb.: Fertiger Workplace

Codeänderung und Kompilieren
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um den Code kompilieren zu können müssen Sie folgende Befehle nacheinander in das Terminal-Fenster unten rechts einfügen. Sie könen dazu die Copy & Paste Funktion benutzen.

cd /workspace/esp32-nmea2000-obp60
bash /workspace/esp32-nmea2000-obp60/lib/obp60task/run

Nach dem letzen Befehl werden in den Workplace alle notwendigen Tool-Chains und Bibliotheken geladen. Dieser Vorgang kann einige Minuten dauern. Danach beginnt der eigentliche Kompiliervorgang, der ebenfalls einiges an Zeit benötigt.

.. image:: ../pics/Gitpod_Compile_Project.png
   :scale: 40%
Abb.: Source-Code kompilieren

Wenn der Kompiliervorgang erfolgreich abgeschlossen ist, sollten Sie folgende Meldung sehen. 

.. image:: ../pics/Gitpod_Compile_Finish.png
   :scale: 40%
Abb.: Kompilierung beendet

Binary-Download
^^^^^^^^^^^^^^^

Source-Code Aktualisierung
^^^^^^^^^^^^^^^^^^^^^^^^^^


