Funktionsweise
==============

Bussysteme
----------

.. image:: ../pics/NMEA_Bus.png
             :scale: 35%

Das OBP60 ist ein Datenanzeigegerät für den Marinebereich, mit dem verschiedenste Informationen aus Bussystemen ausgelesen und angezeigt werden. Zu den typischen Bussystemen im Marinebereich, die das OPB60 verarbeitet, gehören:

* NMEA0183 (RS485, isoliert)
* NMEA2000 (CAN, isoliert)

Damit lässt sich das OBP60 in vorhandene Bootsnetze integrieren. Es kann selbst Daten einspeisen und auslesen. Darüber hinaus verarbeitet das OPB60 weitere Sensornetzwerke wie:

* I2C-Bus (5V, isoliert)
* 1Wire-Bus (3.3V, nicht isoliert)

Diese beiden Busssysteme kommen aus dem Elektronikbereich. Über diese beiden Busse lassen sich günstige Sensoren anbinden, um deren Daten anzuzeigen. Über den isolierten I2C-Bus können zudem recht einfach und sicher eigene Hardwareerweiterungen eingebunden werden.

Gateway
-------

.. image:: ../pics/NMEA_Gateway.png
             :scale: 20%

Im OBP60 ist ein Gateway integriert, das Daten zwischen NMEA0183 und NMEA2000 bidirektional austauschen kann. Dabei werden die Daten des einen Busses in die Daten des anderen Busses übersetzt. Die Übersetzung funktioniert dabei in beide Richtungen.

.. note::
   Dabei ist zu beachten, dass nicht alle NMEA2000-Daten in NMEA0183-Daten übersetzt werden können, weil dafür nicht immer geeignete Telegramme in NMEA0183 existieren.
   
WiFi-Verbindung
---------------

Das OBP60 verfügt über eine WiFi-Funktionalität im 2.4 GHz Funkbereich. Darüber hinaus kann das Gerät mit dem Internet oder mit anderen WiFi-Netzwerken verbunden werden und so mit anderen Geräten kommunizieren. So lassen sich z.B. Daten aus den Bussystemen an einen Laptop, einen PC oder ein Handy übertragen oder von dort beziehen. Damit ist es möglich, die Sensordaten auch in Drittanbieter-Software wie Navionics, NMEA-Remote oder WinGPS zu verwenden.

Konfiguration
-------------

Das OBP60 hat einen Access Point und einen kleinen Webserver integriert, mit denen das Gerät konfiguriert werden kann. Im Gegensatz zu anderen kommerziellen Geräten erfolgt die Konfiguration des OBP60 ausschließlich webbasiert. Dazu kann z.B. ein Handy benutzt werden. So ist die Konfiguration des Gerätes deutlich einfacher und komfortabler. Im Gerät lassen sich bis zu 10 Anzeigeseiten frei definieren. Der Anwender kann zwischen numerischen und grafischen Anzeigeseiten auswählen. Für jede numerische Anzeigeseite können beliebige Daten der Bussysteme angezeigt werden. Bei den grafischen Anzeigeseiten sind die Dateninhalte vorgegeben, da sie spezielle Funktionalitäten bieten.

Anzeige und Bedienung
---------------------

.. image:: ../pics/Front_View_Screen.png
             :scale: 20%

Als Anzeige wird ein E-Paper Display verwendet. Es besitzt einen hohen Kontrast und eine gute Ablesbarkeit auch bei starkem Sonnenlicht. Zudem verbraucht es sehr wenig Energie. Beim Nachtbetrieb ist das Display beleuchtbar. Die Hintergrundfarbe kann frei gewählt werden. So lässt sich das OBP60 auch gut mit anderen Anzeigegeräten kombinieren, um ein einheitliches Aussehen zu erreichen. Eine kleine Flash-LED und ein Buzzer signalisieren dem Anwender optisch und akustisch Grenzwertüberschreitungen. Die Grenzwerte lassen sich frei einstellen.

Die Auswahl der Anzeigeseiten erfolgt über kapazitive Sensortasten, indem mit einer Wischgeste über die Tasten die nächste Seite angesteuert wird. Die Sensitivität der Tasten lässt sich einstellen. Gegen versehentliche Auslösung können die Tasten auch gesperrt werden. Je nach Anzeigeseite können einige Einstellungen auch über die Tasten vorgenommen werden. Die Einstellungen gelten dann ausschließlich für die Anzeigeseite und werden gespeichert, sodass die Einstellungen beim Seitenwechsel erhalten bleiben.