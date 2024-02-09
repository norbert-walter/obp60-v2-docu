Technische Daten
================

.. image:: ../pics/OBP60_Case_Front_t.png
   :scale: 20%

Funktionen
----------

* E-Ink Display (tageslichttauglich)
* Nummerische Anzeigeseiten für 1, 2, 3 und 4 Werten (Werte frei wählbar)
* Grafische Anzeigeseiten (feste Werte)
* Trendanzeige für Werte
* Grenzwertüberschreitung akustisch und optisch
* 6 Sensor-Tasten (Wischgesten-tauglich)
* Akustischer Signalgeber (Buzzer)
* Optischer Signalgeber (RGB-LED)
* LED Displaybeleuchtung (RGB-LEDs)
* NMEA2000 (vollduplex, isoliert)
* NMEA0183 (RX oder TX, konfigurierbar, isoliert)
* NMEA2000/NMEA0183 Gateway (bidirektional)
* I2C (isoliert)
* 1Wire (nicht isoliert)
* Spannungsausgang 5V für ext. Sensorik
* USB-C (OTG, Debug, NMEA0183)
* Batteriemonitor (12V Spannungsmessung)
* BMP280 (Temperatur, Luftdruck)
* GPS-Empfäger (GPS, Glonas, Baidu, int. oder ext. GPS-Antenne)
* WiFi 2.4GHz (HTTP, TCP, UDP)
* Bluetooth (aktuell ungenutzt)
* Batterie Tiefentladeschutz < 9.0V
* Low Power Modus


Aufbau
------

.. image:: ../pics/OBP60_Explode_View.png
   :scale: 20%


Spezifikation
-------------

+----------------------+----------------------+
| Versorgungsspannung  | 12...33 V            |
+----------------------+----------------------+
| Stromverbrauch       | 2 W                  |
+----------------------+----------------------+
| Prozessor            | ESP32-S3, Dual Core  |
+----------------------+----------------------+
| Clock Speed          | 240 MHz              |
+----------------------+----------------------+
| RAM                  | 512 kB               |
+----------------------+----------------------+
| Flash                | 16 MB                |
+----------------------+----------------------+
| PSRAM                | 8 MB                 |
+----------------------+----------------------+
| Displaygröße         | 400 x 300 pix        |
+----------------------+----------------------+
| Refteshrate          | 1 Hz                 |
+----------------------+----------------------+
| Sensortasten         | kapazitiv            |
+----------------------+----------------------+
| NMEA0183             | max. 115.2 kBd, 30m  |
+----------------------+----------------------+
| NMEA2000             | 250 kBit/s, 50m      |
+----------------------+----------------------+
| I2C-Bus              | 5V, 100 kBit/s, 10m  |
+----------------------+----------------------+
| 1Wire-Bus            | 3.3V, 10m            |
+----------------------+----------------------+
| 5V Ausgang           | 250 mA, isoliert     |
+----------------------+----------------------+
| ESD-Schutz           | 2 kV                 |
+----------------------+----------------------+
| Schutzgrad           | IP68, frontseitig    |
+----------------------+----------------------+
| Abmessungen          | 110 x 115 x 30 mm    |
+----------------------+----------------------+
| Gewicht              | 350 g                |
+----------------------+----------------------+

Anschlussbelegung
-----------------
.. image:: ../pics/Bus_Systems.png
   :scale: 50%
