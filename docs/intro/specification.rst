Technische Daten
================

.. raw:: html

   <style>
       /* Container & Layout */
       .sphinx-gallery-container {
           position: relative;
           width: var(--galerie-breite, 400px);
           height: var(--galerie-hoehe, 420px);
           max-width: 100%;
           overflow: hidden;
           background: transparent;
           border-radius: 15px;
		   margin: 20px 0; /* Left orientated*/
           /*margin: 20px auto;*/ /* Center orientated */
       }

       .sphinx-gallery {
           display: flex;
           width: 100%;
           height: 100%;
           overflow-x: auto;
           scroll-snap-type: x mandatory;
           scroll-behavior: smooth;
           -ms-overflow-style: none; 
           scrollbar-width: none; 
       }
       .sphinx-gallery::-webkit-scrollbar { display: none; }

       .sphinx-slide {
           position: relative;
           min-width: 100%;
           height: 100%;
           scroll-snap-align: start;
           background: transparent;
       }

       .sphinx-slide img {
           width: 100%;
           height: 100%;
           object-fit: cover;
           display: block;
           border-radius: 15px;
           margin-bottom: 0 !important; /* Override for Sphinx Themes */
       }

       /* Labeling */
       .sphinx-caption {
           position: absolute;
           top: 15px;
           left: 50%;
           transform: translateX(-50%);
           color: white !important;
           margin: 0;
           font-family: 'Ubuntu', Arial, sans-serif;
           font-size: 16px;
           text-align: center;
           width: 90%;
           font-weight: bold;
           text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
           pointer-events: none;
       }

       /* Navigation */
       .sphinx-nav-btn {
           position: absolute;
           top: 50%;
           transform: translateY(-50%);
           background: rgba(255, 255, 255, 0.3);
           backdrop-filter: blur(4px);
           -webkit-backdrop-filter: blur(4px);
           border: none;
           width: 45px;
           height: 45px;
           cursor: pointer;
           font-size: 20px;
           border-radius: 50%;
           z-index: 10;
           transition: 0.3s;
           display: flex;
           align-items: center;
           justify-content: center;
       }
       .sphinx-nav-btn:hover { background: rgba(255, 255, 255, 0.8); }
       #sph-backBtn { left: 15px; }
       #sph-nextBtn { right: 15px; }
   </style>

   <div class="sphinx-gallery-container" style="--galerie-breite: 400px; --galerie-hoehe: 440px;">
       <button class="sphinx-nav-btn" id="sph-backBtn">❮</button>
       
       <div class="sphinx-gallery" id="sph-gallery">
           <div class="sphinx-slide">
               <img src="https://obp60-v2-docu.readthedocs.io/de/latest/_images/OBP60_WindPlot2.png" alt="Windplot 2">
               <h3 class="sphinx-caption">Windplot 2 Diagrams</h3>
           </div>
           <div class="sphinx-slide">
               <img src="https://obp60-v2-docu.readthedocs.io/de/latest/_images/OBP60_WindPlot.png" alt="Windplot 1">
               <h3 class="sphinx-caption">Windplot 1 Diagram</h3>
           </div>
           <div class="sphinx-slide">
               <img src="https://obp60-v2-docu.readthedocs.io/de/latest/_images/OBP60_Voltage.png" alt="Voltage">
               <h3 class="sphinx-caption">Voltage</h3>
           </div>
       </div>

       <button class="sphinx-nav-btn" id="sph-nextBtn">❯</button>
   </div>

   <script>
       (function() {
           const gal = document.getElementById('sph-gallery');
           const nxt = document.getElementById('sph-nextBtn');
           const bck = document.getElementById('sph-backBtn');

           function doScroll(dir) {
               const amt = gal.offsetWidth;
               const max = gal.scrollWidth - gal.offsetWidth;
               if (dir === 'next') {
                   if (gal.scrollLeft >= max - 5) {
                       gal.scrollTo({ left: 0, behavior: 'smooth' });
                   } else {
                       gal.scrollBy({ left: amt, behavior: 'smooth' });
                   }
               } else {
                   if (gal.scrollLeft <= 5) {
                       gal.scrollTo({ left: max, behavior: 'smooth' });
                   } else {
                       gal.scrollBy({ left: -amt, behavior: 'smooth' });
                   }
               }
           }

           nxt.addEventListener('click', () => doScroll('next'));
           bck.addEventListener('click', () => doScroll('back'));
       })();
   </script>


Funktionen
----------

* E-Paper Display (tageslichttauglich)
* Numerische Anzeigeseiten für 1, 2, 3 und 4 Werte (Werte frei wählbar)
* Grafische Anzeigeseiten (feste Werte)
* Trendanzeige für Werte
* Grenzwertüberschreitung akustisch und optisch
* 6 Sensor-Tasten (geeignet für Wischgesten)
* Akustischer Signalgeber (Buzzer)
* Optischer Signalgeber (RGB-LED)
* LED-Displaybeleuchtung (RGB-LEDs)
* NMEA2000 (vollduplex, isoliert)
* NMEA0183 (RX oder TX, konfigurierbar, isoliert)
* NMEA2000/NMEA0183 Gateway (bidirektional)
* I2C (isoliert)
* 1Wire (nicht isoliert)
* Spannungsausgang 5V (max. 200mA) für externe Sensorik
* USB-C (OTG, Debug, NMEA0183)
* Batteriemonitor (12V-Spannungsmessung)
* Umgebungssensor BMP280 (Temperatur, Luftdruck)
* GPS-Empfäger (GPS, Glonass, Baidu, interne oder externe GPS-Antenne)
* WiFi 2.4GHz (HTTP, TCP, UDP)
* Bluetooth (aktuell ungenutzt)
* Batterie-Tiefentladeschutz < 9.0V
* Low Power Modus


Aufbau
------

.. image:: ../pics/OBP60_Explode_View.png
   :scale: 45%


Spezifikation
-------------

+----------------------+-----------------------------+
| Versorgungsspannung  | 10...28 V                   |
+----------------------+-----------------------------+
| Stromverbrauch       | 0.5...3.5 W, typisch 1 W    |
+----------------------+-----------------------------+
| Prozessor            | ESP32-S3, Dual Core         |
+----------------------+-----------------------------+
| Clock Speed          | 80, 160, 240 MHz            |
+----------------------+-----------------------------+
| RAM                  | 512 kB                      |
+----------------------+-----------------------------+
| Flash                | 16 MB                       |
+----------------------+-----------------------------+
| PSRAM                | 8 MB                        |
+----------------------+-----------------------------+
| Displaygröße         | 400 x 300 pix, 120 dpi      |
+----------------------+-----------------------------+
| Refreshrate          | 1 Hz                        |
+----------------------+-----------------------------+
| Sensortasten         | kapazitiv                   |
+----------------------+-----------------------------+
| NMEA0183-Bus         | RS485, max. 115.2 kBd, 30 m |
+----------------------+-----------------------------+
| NMEA2000-Bus         | CAN, 250 kBit/s, 30 m       |
+----------------------+-----------------------------+
| I2C-Bus              | 5V, 100 kBit/s, 10 m        |
+----------------------+-----------------------------+
| 1Wire-Bus            | 3.3V, 10 m                  |
+----------------------+-----------------------------+
| 5V-Ausgang           | 200 mA, isoliert            |
+----------------------+-----------------------------+
| ESD-Schutz           | 8 kV                        |
+----------------------+-----------------------------+
| Schutzgrad           | IP68, frontseitig           |
+----------------------+-----------------------------+
| Abmessungen          | 110 x 115 x 30 mm           |
+----------------------+-----------------------------+
| Gewicht              | 280 g                       |
+----------------------+-----------------------------+

Anschlussbelegung
-----------------
.. image:: ../pics/Bus_Systems.png
   :scale: 50%
   
.. image:: ../pics/Logo_ESP32-S3_t.png
   :scale: 60%
   
Schaltplan
----------

* `Schaltplan V2.1 [PDF] <../_static/files/Schematic_OBP60_V2.1.pdf>`_


Maßbilder
---------

* `Maßbild [PDF] <../_static/files/Drawing_OBP60_V2.pdf>`_

   
Nutzbare und konvertierbare Telegramme
--------------------------------------

**NMEA0183**
    * AIVDM, AIVDO, DBK, DBS, DBT, DPT, GGA, GLL, GSA, GSV, HDG, HDM, HDT, MTW, MWD, MWV, RMB, RMC, ROT, RSA, VHW, VTG, VWR, XDR, XTE, ZDA
    
**NMEA2000**
    * 126992, 127245, 127250, 127251, 127257, 127258, 127488, 127489, 127505, 127508, 128259, 128267, 128275, 129025, 129026, 129029, 129033, 129038, 129039, 129283, 129284, 129539, 129540, 129794, 129809, 129810, 130306, 130310, 130311, 130312, 130313, 130314, 130316
	
Nutzbare I2C-Sensorik
---------------------

**Umgebungssensoren**
	* BMP085, BMP180, BMP280, BME280, SHT20, HTU21
	
**Spannungs- und Stromsensoren**
	* INA226, INA219 (in Vorbereitung)
	
**Winkelsensoren**
	* AS5600, MT6701 (in Vorbereitung)
	
**Port-Erweiterungen**
	* PCF8574 (in Vorbereitung)
	
**Echtzeit-Uhren**
	* DS1388
	
Nutzbare 1Wire-Sensorik
-----------------------

**Temperatursensoren**
	* DS18B20
