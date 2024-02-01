OBP60 Technische Daten
==================

==================
 |TOP_IMG|_
==================

.. |TOP_IMG| image:: /pictures/OBP60_Case_Front.png
             :scale: 20%

WiFi & Bluetooth 5 (LE) boards based ESP32-S3-WROOM-1. 
`[Buy it]`_

.. _[Buy it]: https://www.aliexpress.com/item/1005004643475363.html

Funktionen
------------------

* CPU: ESP32-S3
* USB-C (OTG, Debug, NMEA0183)
* E-Ink Display
* 6 Sensor-Tasten (Wischgesten-tauglich)
* Akustischer Signalgeber (Buzzer)
* Optischer Signalgeber (RGB-LED)
* LED Displaybeleuchtung (RGB-LEDs)
* NMEA 2000 (vollduplex, isoliert)
* NMEA 0183 (RX oder TX, konfigurierbar, Isoliert)
* I2C (isoliert)
* 1Wire
* Batteriemonitor (12V Spannungsmessung)
* BMP280 (Temperatur, Luftdruck)
* GPS-Empfänger (GPS, Glonas, Baidu, interne Mini GPS-Antenne)
* WiFi 2.4GHz (HTTP, TCP, UDP)
* Bluetooth (aktuell ungenutzt)
* Batterie Tiefentladeschutz < 9.0V
* Low Power Modus


Tutorials
------------------

* :doc:`../tutorials/s3/get_started_with_micropython_s3`
* :doc:`../tutorials/s3/get_started_with_arduino_s3`

Dokumentation
------------------

* `Schaltung V1.0.0[PDF] <../_static/files/sch_s3_v1.0.0.pdf>`_
* `Abmessungen V1.0.0[PDF] <../_static/files/dim_s3_v1.0.0.pdf>`_
* `ESP32-S3-WROOM-1 Datasheet <https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf>`_


Technische Daten
------------------

+----------------------+---------------+
| Versorgungsspannung  | 12...33 V     |
+----------------------+---------------+
| Stromverbrauch       | 2 W (3 W)     |
+----------------------+---------------+
| Clock Speed          | 240 MHz       |
+----------------------+---------------+
| RAM                  | 512 kB        |
+----------------------+---------------+
| Flash                | 16 MB         |
+----------------------+---------------+
| PSRAM                | 8 MB          |
+----------------------+---------------+
| Displaygröße         | 400 x 300 pix |
+----------------------+---------------+
| Refteshrate          | 1 Hz          |
+----------------------+---------------+
| Sensortasten         | kapazitiv     |
+----------------------+---------------+
| NMEA0183             | 115.2 kBd     |
+----------------------+---------------+
| NMEA2000             | 250 kBit/s    |
+----------------------+---------------+
| I2C-Bus              | 5V, 10 kBit/s |
+----------------------+---------------+
| 1Wire-Bus            | 3.3V          |
+----------------------+---------------+
| 5V Ausgang           | 250 mA        |
+----------------------+---------------+
| ESD-Schutz           | 2 kV          |
+----------------------+---------------+
| Size                 | 110x115x30 mm |
+----------------------+---------------+
| Weight               | 350 g         |
+----------------------+---------------+

Anschlussbelegung
------------------

.. image:: ../_static/boards/s3_v1.0.0_4_16x9.jpg
   :target: ../_static/boards/s3_v1.0.0_4_16x9.jpg

