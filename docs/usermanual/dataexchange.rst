Datenaustausch
==============

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
	* USB via SeaSmart (vollduplex)
	* Über WiFi via SeaSmart (vollduplex)
* NMEA0183
	* Kabelgebunden NMEA0183-Bus (simplex)
	* USB (vollduplex)
	* Über WiFi via TCP (vollduplex)
	* Über externen Multiplexer (simplex)
* I2C (halbduplex)
* 1Wire (halbduplex)

Datenquellen
------------

Als Datenquellen werden Geräte bezeichnet, die überwiegend Daten zur anderen Geräten senden und selber nur Daten zur Parametrierung empfangen. Dazu zählen folgende Geräte:

* GPS-Empfänger (Position, Geschwindigkeit, Richtung)
* Windsensor (Geschwindigkeit, Richtung, Temperatur)
* Tiefen-Sensor (Tiefe, Geschwindigkeit, Wassertemperatur, Entfernung)
* Ruderlage (Winkel)
* Winkelsensoren (Mast, Großbaum, Foil, Trimmklappen)
* Elektro-Sensor (Spannung, Strom, Leistung, Energie)
* Umgebungssensoren (Lufttemperatur, Fuftdruck, Luftfeuchtigkeit, Helligkeit, Niederschlag, Zustand, Bewegung)
* Durchflusssensoren (Kühlwasserfluss, Kühlwassertemperatur)
* Druck- und Zugsensoren (Öldruck, Achterstag, Vorstag)
* Füllstandsensoren (Level für Wasser, Abwasser, Krafstoff)
* Lagesensoren (Roll-, Pitch-, Nick-Winkel, Beschleunigung, Rotation)
* Temperatursensoren (Luft, Kühlwasser, Raum, Kühlschrank, Wasser, Maschinenraum)
* Elektrogeneratoren (Solar, Wind-, Schlepp- Dieselgenerator,
* Radargeräte
* Funkgeräte (Position, AIS-Schiffsverkehr, Anrufer, Meldungen, Notrufe)
* Anzeigegeräte (Multifunktionsdisplays, Plotter)

Datensenken
-----------

Datensenken empfangen Informationen und fühern bestimmte Aktionen aus.

* Ruder-Aktuator (linear, rotatorisch, hydraulisch, elektrisch)
* Relais und Schalter (elektrische Verbraucher wie Ankerwinde, Licht, Positionsleuchten, Lüftung, Heizung, Ladegeräte)
* Anzeigegeräte (Multifunktionsdisplays, Plotter)
* Multimediageräte (Radio, Lautsprecher)

Einige komplexere Geräte können sowohl Datenquelle als auch Datensenke sein, wie z.B. Multifunktionsdisplays oder Plotter.

Nachfolgend werden die Übertragungswege näher beschrieben.

NMEA2000 - Kabelgebunden NMEA2000-Bus
-------------------------------------

Der kabelgebundene NMEA2000-Bus ist der aktuelle Standard in der Bootsvernetzung. Über ein NMEA2000-Backbone auf CAN-Basis werden verschiedene Geräte an das Bussystem angeschlossen. Alle Bus-Teilnehmer können Daten lesen und schreiben. Dabei sind Sensoren Datenlieferanten, die ihre Daten an Displays und Plotter übertragen.
