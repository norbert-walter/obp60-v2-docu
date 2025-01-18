Geräteaufbau
============

Mechanischer Aufbau
-------------------

.. image:: ../pics/OBP60_Explode_View_Named.png
   :scale: 45%
Abb.: Explosionsansicht

In der oberen Abbildung ist der Aufbau des OBP60 zu sehen. Das Gerät besteht aus einzelnen Komponenten, die im folgenden beschreiben werden.

	* **Touch Pads**
		Die Tasten bestehen aus schwarz eloxierten Inbus-Senkschrauben aus Edelstahl (V2A). Die Tasten werden mit einem Dichtmittel in die Frontschale des Gehäuses eingeschraubt, um Wasserdichtigkeit zu erreichen.
	* **Springs**
		Die Federn hinter den Tasten dienen der elektrischen Kontaktierung der Tasten mit den Sensorflächen auf der Platine.
	* **Front Case**
		Die Frontschale des Gehäuses nimmt die Tasten auf und enthält die eingeklebte Frontscheibe. Die Außenflächen der Frontschale bestehen aus 2 mm dickem Kunststoff. An einigen Stellen ist das Gehäuse hohl und enthält an den Stellen eine Stützstruktur mit einem Füllgrad von 30%. Das Gehäuse ist als Kastenkonstruktion ausgeführt und dadurch verwindungssteif.
	* **Brass Inlets**
		Die Messing-Gewindeeinsätze dienen zur Verstärkung der Gewinde für die Gehäuseschrauben, da der Kunststoff keine ausreichende Festigkeit aufweist, um den nötigen Druck zum Anpressen der Gehäusedichtung aufzubringen. Die Messing-Gewindeeinsätze werden thermisch in den Kunststoff eingeschmolzen und sind gegen eine ungewollte Verdrehung im Kunststoff gesichert.
	* **Glue Film**
		Der Klebefilm wird auf die Frontscheibe aufgetragen und dient zur wasserdichten Befestigung der Frontscheibe an der Innenseite des Gehäuses.
	* **Front Glass**
		Die Frontscheibe aus 3 mm dickem Plexiglas schützt das Display vor Umwelteinflüssen und vor mechanischen Beschädigungen durch harte Schläge. Die Frontscheibe dient zusätzlich als UV-Filter mit hoher Filterwirkung. Die Außenseite der Frontscheibe ist entspiegelt und verhindert direkte Reflexionen des Sonnenlichts. Eine Besonderheit der Frontscheibe ist ihre Fähigkeit, das e-Paper-Display bei Nacht zu beleuchten. Dazu koppeln an der oberen Stirnseite der Scheibe 6 RGB-LEDs Licht in die Plexiglasscheibe ein. Das Licht der LEDs wird an Streukörpern innerhalb des Plexiglases auf das e-Paper-Display umgelenkt. Die Ausleuchtung des Displays erfolgt daher gleichmäßig über die gesamte Displayfläche.
	* **Filter**
		Eine IR-Filterfolie wird zusätzlich auf der Rückseite der Frontscheibe aufgebracht und soll die Infrarotstrahlung des Sonnenlichtes reduzieren und vom e-Paper-Display fernhalten. Die Infrarotstrahlung wird in der Filterfolie absorbiert und an die Frontscheibe abgegeben, denn bei maximaler Sonenneinstrahlung treffen bis zu 10 W an Wärmestrahlung auf das Display.
	* **Display Frame**
		Der Displayrahmen ist eine Art Maske und verdeckt unerwünschte Bereiche des Displays. Zusätzlich ist ein kleiner Steg angebracht, um das Licht der Hintergrundbeleuchtung gegenüber dem Display abzuschirmen, damit kein Fremdlicht in die Glasscheibe des e-Paper-Displays eingekoppelt wird.
	* **Display**
		Das Display ist ein e-Paper-Display, das Scharz/Weiß und 4 Graustufen abbilden kann. Die Auflösung des Displays beträgt 400 x 300 Pixel. Die Pixeldichte auf die Anzeigefläche bezogen liegt bei 120 dpi. E-Paper-Displays benötigen nur bei der Ansteuerung neuer Bildinhalte Energie. Im ausgeschalteten Zustand bleibt der Bildinhalt sichtbar. Damit ist diese Bildschirm-Technologie sehr energiesparend.
	* **Glue Film**
		Der Klebefilm hinter dem Display dient zur Befestigung des Displays auf dem Displayhalter.
	* **Display Holder**
		Der Displayhalter trägt das e-Paper-Display und verhindert ein Verwinden des Displays. Das e-Paper-Display ist sehr empfindlich, denn es besteht aus zwei Glassubstraten mit einer Gesamtdicke von nur 0,7 mm. Über den Displayhalter wird das Display mittels Schrauben mit dem Mainboard verbunden.
	* **Main Board**
		Das Mainboard enthält alle elektronischen Komponenten auf einer zweiseitigen Platine. An der Oberseite des Mainboards ist die LED-Platine für die Hintergrundbeleuchtung angebracht.
	* **Case Seal**
		Die Gehäusedichtung stellt eine wasserdichte Verbindung zwischen der Front- und Rückschale her. Die Dichtung ist dabei als 1 mm dicke Flächendichtung ausgeführt.
	* **Backside Case**
		Die Gehäuserückschale schließt die Rückseite des Gehäuses ab. Sie ist als verwindungssteife Kastenkonstruktion wie die Frontschale ausgeführt.
	* **Backside Seal**
		Die Rückwanddichtung dichtet das Gehäuse gegenüber der Einbauöffnung ab. Die Dichtung besteht aus 2 mm dickem Neoprenmaterial. Damit lassen sich kleine Unebenheiten und leichte Krümmungen überbrücken.
	* **Connectors**
		Für eine einfachen Montage sind an der Rückseite des Gerätes abnehmbare Steckverbinder angebracht. Über die Steckverbinder mit Schraubverbindungen kann das Gerät mit Strom versorgt und an die Bussysteme angeschlossen werden.
		
Main Board
----------

Das Mainboard enthält alle elektrischen und elektronischen Komponenten wie:

	* Dual Core CPU ESP32-S3
	* Stromversorgung
	* Display-Ansteuerung
	* Sensortasten
	* GPS-Empfänger
	* RTC Echtzeituhr
	* Backup-Batterie
	* Buzzer
	* Flash-LED
	* Hintergrundbeleuchtung
	* Isolierte Treiber für Bussysteme (NMEA2000; NMEA0183, I2C)
	* externe Stromversorgung
	* ESD-Schutzschaltungen
	* USB-C

.. image:: ../pics/PCB_Top_Side_Named.png
   :scale: 45%
Abb.: Mainboard Oberseite

.. image:: ../pics/PCB_Bottom_Side_Named.png
   :scale: 45%
Abb.: Mainboard Unterseite

Platinen
--------

Die Platinen für das Mainboard und die Hintergrundbeleuchtung wurden als zweiseitig bestückte SMD-Platine mit Durchkontaktierungen, Stopplack und Bedruckung ausgeführt.

.. image:: ../pics/PCB_Empty_Top_Side.png
   :scale: 45%
Abb.: Unbestückte Platinen-Oberseite

.. image:: ../pics/PCB_Empty_Bottom_Side.png
   :scale: 45%
Abb.: Unbestückte Platinen-Unterseite

Schaltplan und Fertigungsdaten
------------------------------

Der Schaltplan und die Platine wurden mit dem Online-Entwicklungstool EasyEDA erstellt. Nachfolgend sind die Unterlagen für eine Fertigung aufgeführt.

* `Schaltplan V2.1 [PDF] <../_static/files/Schematic_OBP60_V2.1.pdf>`_
* `Gerber Daten [ZIP] <../_static/files/Gerber_OBP60_V2.1.zip>`_
* `Bauteilliste [TXT] <../_static/files/BOM_OBP60_V2.1.txt>`_
* `Bestückung [HTML] <../_static/files/ibom_multifunktionsdisplay_V2.1.html>`_
* `3D-Daten der Kunststoff-Teile [ZIP] <../_static/files/OBP60_3D_Parts_V2.1.zip>`_

.. image:: ../pics/Lizenz_by-nc-sa_eu.png
   :scale: 45%

Die Fertigungsdaten von Schaltplan, Gerber-Daten und Bauteilliste und die 3D-Daten unterliegen der `Common Creative Lizenz (CC) BY BC SA 4.0`_. Das OBP60 darf unter Nennung der Urheber nachgebaut oder modifiziert werden. Es entstehen keinerlei Kosten für eine private Nutzung ohne kommerzielle Absichten. Eine kommerzielle Verwertung wird durch die Lizenz ausgeschlossen. Abgeleitete Werke unterliegen der selben Lizenz. Wenn Sie eine kommerzielle Nutzung des OBP60 beabsichtigen, kontaktieren Sie uns über das `Kontaktformular`_. Es besteht die Möglichkeit, ein nicht exklusives Nutzungsrecht über eine kommerzielle Lizenz zu erwerben.

.. _Common Creative Lizenz (CC) BY BC SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.de
.. _Kontaktformular: https://open-boat-projects.org/de/kontakt

Schaltungsbeschreibung
----------------------
