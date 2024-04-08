Datenaustausch
==============

Interne Datenverarbeitung
-------------------------

Die Firmware des OBP60 besteht aus zwei Teilen. Der erste Teil ist das **NMEA2000-Gateway** und der zweite Teil die **Hardwareansteuerung** des OBP60. Das `NMEA2000-Gateway`_ ist ein Open Source Projekt von Andreas Wellenvogel. Es ist eine Software mit der man bidirektionale Datenkonvertierungen zwischen NMEA2000 und NMEA0183 durchführen kann. Die Software ist so gestaltet, dass sie unterschiedliche kommerzielle Hardware unterstützen kann. So läuft das NMEA2000-Gateway z.B. auf einer Reihe von Produkten der Firma `M5Stack`_ wie dem **M5Stack Atom** aber auch auf ESP32-Entwicklerboards wie dem **ESP32 Node MCU**. Es werden ESP32-CPUs in unterschiedlicher Ausprägung unterstützt, wie der ESP32-Wroom und ESP32-S3. Die Hardwareansteuerung des OBP60 ist über eigenständige Tasks implementiert und nutzt die Grundfunktionalität des NMEA2000-Gateways.

.. _NMEA2000-Gateway: https://open-boat-projects.org/de/nmea2000-gateway-mit-m5stack-atom/
.. _M5Stack: https://shop.m5stack.com/collections/all-products/m5stack-atom

.. image:: ../pics/Data_Flow_Map.png
             :scale: 60%	
Abb.: Datenflussschema

Die gesamte Datenverarbeitung sämtlicher Bussysteme und Konvertierungen ist Bestandteil des NMEA2000-Gateways. Neben NMEA2000 (**CAN**) und NMEA0183 (**RS485**) werden weitere Bussysteme wie **I2C** und **1Wire** unterstützt. Die Hauptaufgabe des NMEA2000-Gateways besteht darin, alle ankommenden Daten der Busssysteme zu empfangen und in einem gemeinsamen Daten-Pool abzubilden. Diese Daten können über die Webseite **Data** eingesehen werden. Erweiterte Sensorik, die nicht Bestandteil von NMEA2000 und NMEA0183 sind, können über I2C und 1Wire eingefügt werden. So lassen sich preisgünstige Sensoren nutzen. Damit die Daten der erweiterten Sensorik im NMEA2000- und NMEA0183-Netzwerk genutz werden können, werden sie über NMEA0183 als universelle `XDR-Datensätze`_ in den Daten-Pool eingefügt. Als XDR-Datensätze können die Daten dann auch nach NMEA2000 konvertiert werden, sofern im Konverter entsprechende Übersetzungen implementiert sind. Als Ausgabeschnittstellen stehen CAN, RS485 und WiFi zur Verfügung. Über die CAN-Schnittstelle lassen sich nur NMEA2000-Daten austauschen. Über RS485 und WiFi (TCP) lassen sich sowohl NMEA0183-Daten als auch NMEA2000-Daten austauschen, sofern die NMEA2000-Daten in SeaSmart-Telegrammen durch NMEA0183 getunnelt werden.

.. _XDR-Datensätze: https://obp60-v2-docu.readthedocs.io/de/latest/usermanual/configuration.html#xdr

Der Datenaustausch im OBP60 kann auf verschiedene Weise erfolgen. Grundsätzlich stehen mehrere Übertragungsarten über verschiedene Übertragungswege zur Verfügung:

Übertragungsarten
-----------------

* Simplex
	* Daten können in nur eine Richtung übertragen werden
* Halbduplex
	* Daten können abwechselnd, aber nicht gleichzeitig, in beide Richtungen fließen
* Vollduplex
	* Daten können in beide Richtungengleichzeitig gleichzeitig übertragen werden. 
	
Übertragungswege
----------------

* NMEA2000
	* Kabelgebunden NMEA2000-Bus (halbduplex)
	* Über WiFi via SeaSmart (vollduplex)
* NMEA0183
	* Kabelgebunden NMEA0183-Bus (simplex)
	* USB (vollduplex)
	* Über WiFi via TCP (vollduplex)
	* Über externen Multiplexer (simplex)
* **I2C** (halbduplex)
* **1Wire** (halbduplex)

Datenquellen
------------

Als Datenquellen werden Geräte bezeichnet, die überwiegend Daten zur anderen Geräten senden und selber nur Daten zur Parametrierung empfangen. Dazu zählen folgende Geräte:

* GPS-Empfänger (Position, Geschwindigkeit, Richtung)
* Windsensor (Geschwindigkeit, Richtung, Temperatur)
* Tiefen-Sensor (Tiefe, Geschwindigkeit, Wassertemperatur, zurückgelegte Strecke)
* Winkelsensoren (Ruderlage, Mast, Großbaum, Foil, Trimmklappen)
* Elektro-Sensor (Spannung, Strom, Leistung, Energie)
* Umgebungssensoren (Lufttemperatur, Fuftdruck, Luftfeuchtigkeit, Helligkeit, Niederschlag, Zustand, Bewegung)
* Durchflusssensoren (Kühlwasserfluss, Kühlwassertemperatur)
* Druck- und Zugsensoren (Öldruck, Achterstag, Vorstag)
* Füllstandsensoren (Level für Wasser, Abwasser, Krafstoff)
* Lagesensoren (Roll-, Pitch-, Nick-Winkel, Beschleunigung, Rotation, Magnetfeld)
* Temperatursensoren (Luft, Kühlwasser, Raum, Kühlschrank, Wasser, Maschinenraum)
* Elektrogeneratoren (Solar, Wind-, Schlepp- Dieselgenerator,
* Radargeräte (Umgebungskarte
* Funkgeräte (Position, AIS-Schiffsverkehr, Anrufer, Meldungen, Notrufe)
* Anzeigegeräte (Multifunktionsdisplays, Plotter)
* Videokameras (Bild, Ton, Bewegung)

Datensenken
-----------

Datensenken empfangen Informationen und führen bestimmte Aktionen aus.

* Ruder-Aktuator (linear, rotatorisch, hydraulisch, elektrisch)
* Relais und Schalter (elektrische Verbraucher wie Ankerwinde, Licht, Positionsleuchten, Lüftung, Heizung, Ladegeräte)
* Winkelaktuator (Trimmklappen, Foil-Einstellung)
* Anzeigegeräte (Multifunktionsdisplays, Plotter)
* Multimediageräte (Radio, Lautsprecher)

Einige komplexere Geräte können sowohl Datenquelle als auch Datensenke sein, wie z.B. Multifunktionsdisplays oder Plotter.

Nachfolgend werden die Übertragungswege näher beschrieben.

NMEA2000 - Kabelgebunden NMEA2000-Bus
-------------------------------------

Der kabelgebundene NMEA2000-Bus ist der aktuelle Standard in der Bootsvernetzung. Über ein NMEA2000-Backbone auf CAN-Basis werden verschiedene Geräte an das Bussystem angeschlossen. Alle Bus-Teilnehmer können Daten lesen und schreiben. Dabei sind Sensoren Datenlieferanten, die ihre Daten an Displays und Plotter übertragen. Das NMEA2000-Backbone kann Sensoren auch mit Strom versorgen. Die Einspeisung der Versorgunsgspannung erfolgt über einen Plotter oder über ein Einspeisekabel.

.. image:: ../pics/NMEA2000_Sample_Setup_Plotter.png
             :scale: 60%	
Abb.: NMEA2000-Bussystem mit Sensoren und Anzeigegeräten

Für den Betrieb von NMEA2000 muss nichts speziell konfiguriert werden. Die Standardeinstellungen sind so gesetzt, dass ein Betrieb problemlos möglich ist. Bei Bedarf kann das Senden von NMEA2000-Telegrammen unterbunden werden. Dann ist nur ein Empfang von NMEA2000-Telegrammen möglich. Die Einstellungen zu NMEA2000 findet man unter `Config - Converter`_.

.. _Config - Converter: https://obp60-v2-docu.readthedocs.io/de/latest/usermanual/configuration.html#config-converter

NMEA2000 - WiFi via SeaSmart
----------------------------

Über das SeaSmart-Protokoll besteht die Möglichkeit, NMEA2000-Telegramme über Ethernet und WiFi übertragen zu können. Dazu werden die Binärdaten der NMEA2000-Telegramme in propritäre NMEA0183-Telegramme eingebettet. Ein SeaSmart-Telegramm sieht wie folgt aus:

    $PCDIN,a--a,b--b,b,cc,d--d*hh<CR><LF>

    Feldnummer:
	    * a - PGN im Binärform
	    * b - Zeitstempel im Binärform
	    * c - Source-ID
	    * d - PGN-Daten im Binärform
	    * hh - Checksumme

    Beispiele:	
	    * $PCDIN,01F211,0B9CF01B,03,008061480D0000FF*5C
		
Der Vorteil ist, dass sich SeaSmart-Telegramme genauso wie NMEA0183-Telegramme übertragen lassen. Damit ist es möglich, NMEA2000-Telegramme drahtlos über Wifi von einem OBP60 zu einem anderen OBP60 zu übertragen. Diese Funktion kann z.B. genutzt werden, um Bus-Sensordaten von einem OBP60 oder einem `NMEA2000-Gateway`_ auf einem OBP60-Tochtergerät anzeigen zu lassen.

.. _NMEA2000-Gateway: https://open-boat-projects.org/de/nmea2000-gateway-mit-m5stack-atom/

.. image:: ../pics/SeaSmart1.png
             :scale: 60%	
Abb.: Datenübertragung via WiFi OBP60 - OBP60

.. image:: ../pics/SeaSmart2.png
             :scale: 60%	
Abb.: Datenübertragung via WiFi M5Stack - OBP60

.. hint::
	Beide Geräte müssen sich im selben WiFi-Netzwerk befinden und unterschiedliche Netzwerknamen und IP-Adressen besitzen. Dabei muss ein Gerät als TCP-Server und das andere Gerät als TCP-Client konfiguriert sein und auf beiden Geräten **SeaSmart out** aktiviert werden.
	
Tabelle mit den Settings:


	
