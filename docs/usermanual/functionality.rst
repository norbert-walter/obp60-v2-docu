Funktionsweise
==============

Bussysteme
----------

Das OBP60 ist ein Datenanzeigegerät für den Marinebereich mit dem verschiedenste Informationen aus Bussystemen ausgelesen und angezeigt werden. Zu den typischen Bussystemen im Marinebereich, die verwendet werden können gehören:

* NMEA0183 (RS485, isoliert)
* NMEA2000 (CAN, isoliert)

Damit lässt sich das OBP60 in vorhandene Bootsnetze integrieren und kann selbst Daten einspeisen und auslesen. Darüber hinaus gibt es noch Sensornetzwerke wie:

* I2C-Bus (5V, isoliert)
* 1Wire-Bus (3.3V, nicht isoliert)

Diese beiden Busssysteme kommen aus dem Elektronikbereich und sind dort oft anzutreffen. Über diese beiden Busse lassen sich günstige Sensoren anbinden und dessen Daten anzeigen. Über den isolierten I2C-Bus können recht einfach und sicher eigene Hardwareerweiterungen eingebunden werden.

Gateway
-------

Im OBP60 ist ein Gateway intergriert, das Daten zwischen dem NMEA0183-Bus und dem NMEA2000-Bus bidirektional austauschen kann. Dabei werden die Daten des einen Busses in die Daten des anderen Busses übersetzt. Die Übersetzung funktioniert dabei in beide Richtungen.

.. note::
   Dabei ist zu beachten, dass nicht alle Daten des NMEA2000-Busses in Daten des NMEA0183-Busses übersetzt werden können, weil teilweise keine geeigneten Telegramme in NMEA0183 existieren.
   
WiFi-Verbindung
---------------

Das OBP60 verfügt über eine WiFi-Funktionalität im 2.4 GHz Funkbereich. Darüber kann das Gerät mit dem Internet oder mit anderen WiFi-Netzwerken verbunden werden und mit anderen Geräten kommunizieren. So lassen sich z.B. Daten aus den Bussystemen an einen Laptop, PC oder Handy übertragen und dort verwenden oder von dort beziehen.

Konfiguration
-------------

Das OBP60 hat einen Access Point und einen kleinen Webserver intergriert mit denen das Gerät konfiguriert werden kann. Im Gegensatz zu anderen kommerziellen Geräten erfolgt die Konfiguration des OBP60 ausschließlich webbasiert. Dazu kann z.B. ein Handy benutzt werden. So ist die Konfiguration des Gerätes deutlich einfacher und komfortabkler. Im Gerät lassen sich bis zu 10 Anzeigeseiten frei definieren. Der Anwender kann zwischen nummerischen und grafischen Anzeigeseiten auswählen. Für jede nummerische Anzeigeseite können beliebige Daten der Bussysteme angezeigt werden. Bei den grafischen Anzeigeseiten sind die Dateninhalte vorgegeben, da sie spezielle Funktionalitäten bieten.

Anzeige und Bedienung
---------------------

Als Anzeige wird ein E-Ink Display verwendet. Es besitzt einen hohen Kontrast und eine gute Ablesbarkeit auch bei starkem Sonnenlicht. Zudem verbraucht es sehr wenig Energie. Beim Nachtbetrieb ist das Display beleuchtet. Die Hintergrundfarbe kann frei gewählt werden. So lässt sich das OBP60 auch gut mit anderen Anzeigegeräten kombinieren und eine einheitliches Aussehen erreichen. Eine kleine Flash-LED und ein Buzzer signalisieren dem Anwender optisch und akustisch Gernzwertüberschreitungen. Die Grenzwerte lassen sich frei einstellen.

Die Auswahl der Anzeigeseiten erfolgt über kapazitive Sensor-Tasten, indem mit einer Wischgeste über die Tasten die nächste Seite angesteuert wird. Die Sensitivität der Tasten lässt sich einstellen. Gegen versehentliche Auslösung können die Tasten auch gesperrt werden. Je nach Anzeigeseite können einige Einstellungen über die Tasten vorgenommen werden. Die Einstellungen gelten dann ausschließlich für die Anzeigeseite und werden gespeichert, so dass die Einstellungen beim Seitenwechsel erhalten bleiben.  
