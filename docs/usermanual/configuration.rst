Konfiguration
=============

Nachdem die Stromversorgung zugeschaltet wurde, startet die Firmware des OBP60. Nach Abschluss der Initialisierungsphase ertönt ein Piepton. Im Display wird zuerst das Open Boat Projects-Logo angezeigt, gefolgt von einem QR-Code, der die Zugangsdaten zum Access Point anzeigt. Beide Bilder sind für einige Sekunden sichtbar. Sie können mit Ihrer Handy-Kamera den QR-Code scannen und sich dann in das WiFi-Netz des OBP60 mit folgenden Zugangsdaten einloggen:

.. image:: ../pics/QR_Code_WiFi.png
             :scale: 50%

* **SSID:** OBP60V2
* **Passwort:** esp32nmea2k

Nachdem Sie im WiFi-Netzwerk eigebucht sind, öffnen Sie in einem Web-Browser die Adresse **OBP60V2.local** oder die IP-Adresse **192.168.15.1**. Sie gelangen so auf die Benutzeroberfläche des OPB60 und können den aktuellen Status des Geräts überprüfen. Auf der Benutzeroberfläche befinden sich Tabs, mit denen verschiedene Bereiche der Konfiguration ausgewählt werden können:

* **Status** - Statusanzeige mit Übersicht der Bussysteme
* **Config** - Allgemeine Konfigurationsseite
* **XDR** - Konfigurationsseite für NMEA0183 XDR-Sentences
* **Data** - Dashboard zur Datenanzeige
* **Update** - Seite zum Firmware-Update
* **Help** - Aufruf der Github-Projektseite

.. note::
	Beachten Sie, dass beim erstmaligen Aufruf der Konfigurationsoberfläche kein Passwort beim Speichern der Konfiguration notwendig ist. Als **Default-Passwort** wird **esp32admin** verwendet. Ändern Sie das Passwort für ihre Belange ab, verwenden Sie dabei nur Zeichen des ASCII-Zeichensatzes. Die Passwortabfrage kann auch deaktiviert werden.

Status
------

Auf der Statusseite sieht man im oberen Bereich den Ethernet-Verbindungsstatus.

.. image:: ../pics/Status_1.png
             :scale: 60%

Die Informationen haben folgende Bedeutung:

**Version**
	Aktuelle Firmware-Version
**Access Point IP**
	IP-Adresse des Access Points
**WiFi Client connected**
	Zeigt an, ob das OBP60 mit einem anderen externen WiFi-Netzwerk als Client verbunden ist
**WiFi Client IP**
    IP-Adresse, die dem OBP60 zugewiesen wurde 
**NMEA2000 in**
	Anzahl der NMEA2000-Telegramme, die empfangen wurden
**NMEA2000 out**
	Anzahl der NMEA2000-Telegramme, die gesendet wurden
**TCP in**
	Anzahl der NMEA0183-Telegramme, die über TCP empfangen wurden
**TCP out**
	Anzahl der NMEA0183-Telegramme, die über TCP gesendet wurden
**USB in**
	Anzahl der NMEA0183-Telegramme, die über USB empfangen wurden
**USB out**
	Anzahl der NMEA0183-Telegramme, die über USB gesendet wurden
**Serial in**
	Anzahl der NMEA0183-Telegramme, die über RS485 empfangen wurden
**Serial out**
	Anzahl der NMEA0183-Telegramme, die über RS485 gesendet wurden

Wenn Sie auf das Fragezeichen hinter **Version** klicken, werden alle Telegramme angezeigt, die das OBP60 verarbeiten kann. Detailliertere Informationen zu den empfangenen Telegrammen sehen Sie, wenn Sie die Zeile des Bussystems aufklappen. Im Anhang finden Sie eine Tabelle mit allen NMEA0183- und NMEA2000-Telegrammen, die verarbeitet werden können.

.. note::
	Zum besseren Verständnis ist zu beachten, dass das OBP60 ein eigenes, unabhängiges WiFi-Netzwerk aufbaut, diese Funktion wird auch als Access Point bezeichnet. Die Anzahl der TCP-Clients in der Statuszeile bezieht sich dabei immer nur auf die Clients, die sich beim OBP60 im Access Point-Modus anmelden.
	Das OBP60 kann darüber hinaus Teil eines anderen externen WiFi-Netzwerks sein, indem es sich dort als Client anmeldet. In dem Fall wird das eigene WiFi-Netz des OBP60 mit dem externen WiFi-Netz gebrückt. Alle Daten des OPB60 sind dann in beiden Netzwerken verfügbar. 
	
Config
------

Die Konfigurationsseite unterteilt sich in zwei Bereiche. Die Firmware basiert auf dem NMEA2000-Gateway-Projekt und nutzt die gesamte Grundstruktur dieses Software-Projektes. Die Funktionalität des OBP60 ist als eigenständiger Task in der NMEA2000-Gateway-Firmware implementiert. Der erste Bereich enthält die Konfiguration für das NMEA2000-Gateway. Im zweiten Bereich ist die Konfiguration zur OBP60 Hardware und Software zu finden. Den zweiten Bereich erkennt man an dem Prefix OBP.

**Konfiguration zum NMEA2000-Gateway**

.. image:: ../pics/Config_1.png
             :scale: 60%
			 
Auf der Konfigurationsseite sind im oberen Bereich verschiedene Tasten zu sehen. Die Bedeutung der Tasten ist nachfolgend aufgeführt:

* **Reload Config** - Erneutes laden der Konfiguration
* **Forget Pass** - Entfernen des Login-Passwortes aus dem Cach-Speiches des Browsers
* **Save & Restart** - Speichern der Konfiguration mit anschließendem Neustart der Firmware
* **Export** - Export einer Konfiguration als JSON-File
* **Import** - Import einer Konfiguration über ein JSON-File
* **Factory Reset** - Rücksetzen aller Einstellungen auf Werkszustand

Config - System
---------------

.. image:: ../pics/Config_System.png
             :scale: 60%

Unter **System** werden grundlegende Einstellungen vorgenommen wie:

**System Name**
	* System-Name zum OBP60. Hier kann ein Namen verwendet werden der aus bis zu 10 ASCII-Zeichen besteht. Dabei dürfen nur Buchstaben und Zahlen verwendet werden. Zusätzlich sind das Minus-Zeichen und der Unterstrich erlaubt. Sonderzeichen sind nicht erlaubt, da dieser Gerätename auch als SSID im WiFi-Netzwerk verwendet wird.
	
**NMEA0183 ID**
	* Hier kann festgelegt werden, welcher Prefix als Geräte ID im NMEA0183-Telegramms verwendet wird. Es lassen sich verschiedene Geräte ID einstellen. Details dazu sind unter folgendem `Link`_ zu finden.

.. _Link: https://de.wikipedia.org/wiki/NMEA_0183

**Stop AP Time**
	* Hierüber kann angegeben werden, nach wlcher Zeit der WiFi Access Point abgeschaltet werden soll. Die Angabe der Zeit erfolgt in Sekunden. Wird 0s verwendet, so bleibt der WiFi Access Point dauerhaft an.
	
**AP Password**
	* An dieser Stelle wird das Passwort für den WiFi Access Point angegeben. Es dürfen nur Zeichen des ASCII-Zeichensatzes verwendet werden.
	
**AP IP**
	* Hier kann die IP-Adresse des WiFi Access Point eingestellt werden. Per Default steht die IP-Adresse auf 192.168.15.1. In Ausnahmefällen kann die IP auf eine andere Adresse eingestellt werden.
	
**AP Mask**
	* An diese Stelle wird die Subnetz-Maske für den WiFi Access Point angegeben. Per Default steht die Subnetz-Maske auf 255.255.255.0 
	
.. warning::	
	Achten Sie darauf, dass das Subnetz verschieden zu anderen Subnetzen ist, in das sich das OBP60 als WiFi-Client eingebunden hat und das Sie eine korrekte Subnetz-Maske verwenden. Das Subnetz ist über die ersten drei Zahlen der IP-Adresse gekennzeichnet. Beachten Sie das nicht, so können Netzwerkploblemen auftreten in dessen Folge Sie die Konfigurationsseiten nicht mehr öffnen können. In den meisten Fällen wird eine Änderung der IP-Adresse oder der Subentz-Maske nicht notwendig sein. Ändern Sie die IP und Subnetz-Maske nur, wenn Sie über Netzwerkerfahrung verfügen und die Auswirkung der Änderungen verstehen.

**Use Admin Pass**
	* Hiermit kann festgelegt werden, ob für Änderungen der Konfiguration ein Passwort notwendig ist.
	
**Admin Password**
	* An der Stelle wird das Admin Passwort eingegeben. Es dürfen nur Zeichen des ASCII-Zeichensatzes verwendet werden.
	
**Show All Data**
	* Ist der Wert auf ``on``, so werden im Data-Bereich alle Sensordaten angezeigt. Mit ``off`` können alle Sensordaten auf der Data-Seite deaktiviert werden.
	
**Log Level**
	* Über **Log Level** lässt sich der Grad der Benachichtigung über die USB-C-Schnittstelle einstellen. Hierbei gibt es folgende Einstellungen:
		* ``off`` - Keine Logging-Ausgaben
		* ``error`` - Nur Fehlermeldungen ausgeben
		* ``log`` - Nur Fehlermeldungen und Statusinformationen ausgeben
		* ``debug`` - Alle Meldungen inklusive Debug-Meldungen ausgeben 
		
.. note::
	Wenn Sie beabsichtigen über die USB-C-Schnittstelle einen NMEA0183-Datenaustausch durchzuführen, dann sollten Sie den **Log Level** auf ``off`` stellen. Beachten Sie das nicht, so kann es zu Störungen bei der Datenauswertung kommen, da Logging-Daten und NMEA0183-Telegramme gemischt ausgegeben werden.

XDR
---

Über die Konfigurationsseite XDR können XDR-Sentences für NMEA0183 erstellt werden. XDR-Sentences sind Telegramme für generische Sensorwerte, die verwendet werden, wenn sich kein geeignetes NMEA0183 Telegramme findet, mit dem man die Sensorwerte übertragen kann. Es ist ein universelles Telegramm zur Übertragung von Sensordaten. XDR-Sentences werden immer dann benutzt, wenn Daten aus dem I2C-Bus, dem 1Wire-Bus oder interne Sensordaten vom ESP32 übertragen werden sollen. Sofern nicht zugewiesene Sensordaten im OBP60 vorhanden sind, können diese über ein XDR-Mapping zugewiesen werden. Damit sind diese Daten als NMEA0183 Telegramme allgemein nutzbar und werden im OBP60 dargestellt. Die Daten lassen sich dann auch über NMEA0183 in andere Systeme übertragen und dort nutzen.

Ein XDR-Sentence ist folgendermaßen aufgebaut:

**Sensor Werte**

    $--XDR,a,x.x,b,c--c,x--x*hh<CR><LF>

    Feld Nummer:
	    * a - Sensor-Typ
	    * x.x - Messwerrt
	    * b - Einheit des Messwertes
	    * c - Name des Sensors
	    * x - Weitere Sensordaten
	    * hh - Checksumme

    Beispiele:	
	    * $IIXDR,C,19.52,C,TempAir*19
	    * $IIXDR,P,1.02481,B,Barometer*29
	
+------------------+-----------------+---------------------------------+-----------------+-----------------------------------+
|Messwert          | Sensor-Typ      | Beispiele für Messdaten         | Einheit         | Name des Sensors                  |
+==================+=================+=================================+=================+===================================+
| Luftdruck        | **P** Druck     | 0.8..1.1 oder 800..1100         | **B** Bar       | **Barometer**                     |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------------+
| Lufttemperatur   | **C** Temperatur| 2 Dezimalstellen                | **C** Celsius   | **TempAir** oder **ENV_OUTAIR_T** |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------------+
| Pitch            | **A** Winkel    |-180..0 runter    0..180 hoch    | **D** Degrees   | **PTCH** oder **PITCH**           |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------------+
| Rolling          | **A** Winkel    |-180..0 links     0..180 rechts  | **D** Degrees   | **ROLL**                          |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------------+
| Wassertemperatur | **C** Temperatur| 2 Dezimalstellen                | **C** Celsius   | **ENV_WATER_T**                   |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------------+

Über die XDR Konfigurationsseite lassen sich 30 XDR-Telegramme individuell erstellen.

.. image:: ../pics/XDR_1.png
             :scale: 60%

Dazu öffnet man als erstes über ``Show Unmapped`` eine Liste der nicht verknüpften Sensordaten.

.. image:: ../pics/XDR_Show_Unmapped.png
             :scale: 60%
             
In der Liste sehen Sie welche Daten zur Verfügung stehen. Über ``+`` werden die Daten in die letzte frei verfügbare XDR-Konfiguration automatisch eingefügt und der richtigen Kategorie zugeordnet. Der Sensorname muss noch im Feld **Transducer** hinzugefügt werden. 

.. image:: ../pics/XDR_2.png
             :scale: 60%

Nach der Zuordnung des Sensornamens wird unter **Example** ein Beispiel für das XDR-Telegramm angezeigt. Danach können alle Einstellungen noch individuell geändert werden. Die Erklärung zu den Einstellungen ist nachfolgend aufgeführt.

**Direction**
    Über Direction lässt sich einstellen wie Sensordaten eingelesen werden sollen und wohin sie übertragen werden:
     
    * **off** - Die Sensordaten werden nicht benutzt. Damit können sie ein bereits konfiguriertes XDR-Telegramm deaktivieren.
    * **bidir** - Die Sensordaten werden zwischen NMEA0183 und NMEA2000 ausgetauscht
    * **to2K** - Das Sensordaten werden nur nach NMEA2000 gesendet
    * **from2k** - Sensordaten werden von NMEA2000 eingelesen
     
**Category**
    Über Category kann Sensor-Typ zugeordnet werden:
     
    * **Temperature** - Temperatursensoren für Luft, Wasser, Kühlschrank
    * **Humidity** - Luftfeuchtigkeitssensoren
    * **Pressure** - Drucksensoren für Luftdruck und andere Drücke wie z.B. Öldruck
    * **Fluid** - Sensoren für Flüssigkeiten wie Durchfluss und Füllstand
    * **Battery** - Batteriesensoren für Spannung, Strom, Leistung, Batterietemperatur
    * **Engine** - Motorsensoren für Drehzahl, Anstellung, Trimmklappen, Öl, Kühlwasser
    * **Attitude** - Höhendaten aus GPS-Sensor ermittelt
    
**Source**
    Über Source lässt sich die Quelle der Sensordaten genauer einstellen. Je nach verwendeten Sensortyp stehen verschiedene Sensor-Quellen zur Verfügung
    
**Field**
    Mit Field kann genauer beschrieben werden, wie die Sensordaten zu verstehen sind. Es sind Zusatzdaten die kontextabhängig je nach verwendeten Sensor-Typ einstellbar sind. So kann z.B. festgelegt werden, ob es sich um einen Anzeigewert oder um einen Einstellwert handelt.
    
**Instance**
    Mit Instance kann festgelegt werden, ob es mehrere Sensoren des selben Typs gibt. Das kann z.B. auftreten, wenn zwei Motoren in einem Boot verbaut sind und zwei Tankwerte angezeigt werden sollen. Mit Hilfe einer Instanz-Nummer werden die Sensoren unterschieden. An den Sensornamen wird dann z.B. \#1 angefügt. Die Arte der Instanziierung kann folgendermaßen festgelegt werden:
    
    * **singel** - Es wird ein Sensor instanziiert, dem einen freie Instanz-Nummer zugeordnet werden kann. So können z.B. zwei Sensoren die selben Daten in ein XDR-Telegramm übertragen, wenn die Sensoren redundant sind.
    * **ignore** - Es existiert nur genau ein einziger Sensor dieses Typs.
    * **auto** - Die Instanziierung wird automatisch übernommen. Sobals ein neuer Sensor des gleichen Typs und der selben Source verwendet wir, wird eine neue Instanz des Sensors angelegt.
        
**Transducer**
    Über Transducer wird der Sensorname festgelegt. Es handelt sich dabei um eine Klartextbeschreibung des Sensors mit ASCII Zeichen. Verwenden sie nur Buchstaben und Zahlen ohne Freizeichen und Sonderzeichen.
    
**Example**
    Beispiel wie der Inhalt des XDR-Telegramms aussehen wird.
    
Data
----

.. image:: ../pics/Data_1.png
             :scale: 60%
             
Unter Data werden alle Sensordaten aller Bussysteme angezeigt, die derzeit verarbeitet werden können. Sensordaten die nicht verfügbar sind werden mit ``---`` gekennzeichnet. Man kann die Datenanzeige auch so konfigurieren, dass nur aktuelle Daten angezeigt werden. Die nicht verfügbaren Daten sind dann ausgeblendet.

.. image:: ../pics/Data_2.png
             :scale: 60%

.. note::
    Die Beschränkung der Datenanzeige auf aktuelle Daten führt dazu, dass sich die Anordnung der Daten ändert, wenn einige Sensordaten nicht mehr verfügbar sind. Die Datenfelder werden dann ausgeblendet. Wenn sie ein festes Anzeigeformat haben wollen, lassen sie sich alle Daten anzeigen.  

Update
------

Um die Firmware eines Gerätes zu aktualisieren, können Sie die Registerkarte ``Update`` verwenden. Es gibt zwei Arten von Firmware-Updates.

**Initial Firmware-Update**
	Beim Initial Firmware-Update wird der komplette Flash-Speicher des OBP60 gelöscht. Anschließend werden alle Firmware-Bestandteile im Flash gespeichert. Dabei wird eine initiale Konfiguration erstellt. Eine vorherige alte Konfiguration wird überschrieben. Die Initial Firmware-Updates verwenden den Dateinamen **xxx-all.bin**.
	
**Normales Firmware-Update**
	Beim normalen Firmware-Update wird nur der Programmteil der Firmware aktualisiert. Eine vorhandene Konfiguration bleibt dabei erhalten und ist nach dem Firmware-Update wieder nutzbar. Normale Firmware-Updates verwenden den Dateinamen **xxx-update.bin**.

Die letzte aktuelle Firmware können Sie auf folgender Webseite herunterladen:

https://github.com/norbert-walter/esp32-nmea2000-obp60/releases

Unter **Releases** sind eine Reihe verfügbarer Firmware-Updates für das OBP60 zu finden. Beachten Sie dabei die jeweilige Hardware-Version, für die Sie eine Firmware herunterladen wollen.

.. image:: ../pics/Update.png
             :scale: 60%

Für ein Firmware-Update laden sie sich die gewünschte Firmware als Datei herunter und speichern sie die Datei auf ihrem Gerät. Über die Taste ``Choose File`` wählen sie die heruntergeladene Datei aus. Es wird dann der Firmware-Type, der Chip-Type und die Firmware-Version angezeigt. Sollte die Firmware nicht zur verwendeten Hardware passen, so erhalten sie eine Meldung. Die Firmware kann dann nicht geflasht werden. Über die Taste ``Upload`` starten sie den Flash-Vorgang. Im Fortschrittsbalken sehen Sie den Verlauf des Vorgangs. Nach einem erfolgreichen Firmware-Update wird eine Reboot des Systems durchgeführt. In dieser Zeit ist die Web-Konfigurationsseite offline (roter Punkt). Nach kurzer Zeit ist die Seite wieder online (grüner Punkt). Dann ist das System wieder betriebsbereit.

.. warning::
	Beachten Sie, dass Sie bei einem Firmware-Update auf eine ältere Version ein **Initial Firmware Update** durchführen müssen. So vermeiden Sie Komplikationen mit den gespeicherten Konfigurationsdaten. Unter Umständen ist das System nicht nutzbar und kann komplett einfrieren. Ein Firmware-Update über die Konfigurationsseiten ist dann nicht mehr möglich und die Firmware muss über USB geflasht werden.

Wie man die Firmware eines OBP60 über USB flasht, ist unter xxx beschrieben.

Help
----

Unter Help erfolgt ein Sprung ins Internet zur Github-Seite auf der das Projekt gehostet wird. Dort sind einige weitergehende Informationen zum NMEA2000-Gateway zu finden, das die Basis für diese Firmware ist.

.. note::
    Die Github-Seite lässt sich nur aufrufen, wenn das OBP60 auf das Internet zugreifen kann.

Sicherheit im WiFi-Netzwerk
---------------------------

Sie sollten das OBP60 nur mit vertrauenswürdigen WiFi-Netzwerken verbinden. Es gibt im Gerät nur einen sehr begrenzten Schutz gegen Netzwerk-Sniffing oder Denial-of-Service-Angriffe. Solange Sie das eigene autarke WiFi-Netz des OBP60 nutzen, können fremde Personen ihr WiFi-Netz nicht verwenden. Auf diese Weise läuft die Datenübertragung in ihrem eigenen WiFi-Netzwerk geschützt. Verbinden Sie das Gerät niemals ohne eine Firewall direkt mit dem Internet und vermeiden Sie direkte Verbindungen zu offenen Hafen-Netzwerken. Dadurch können auch fremde Personen auf Ihre Geräte im Netzwerk zugreifen.

.. note::
	Sie können die Sicherheit erhöhen, indem Sie einen separaten WiFi- oder LTE-Router in Ihrem Boot verwenden. Die Router können so eingerichtet werden, dass Sie ein eigenes WiFi-Netz aufspannen können, mit dem alle Geräte an Bord verbunden sind. Gängige mobile Router verfügen in der Regel über eine bereits eingeschaltete Firewall, über die Sie Ihr eigenes WiFi-Netz mit dem Internet verbinden können. Die Firewall verhindert fremden Zugriff von außen auf Ihre Geräte. So haben alle Geräte in Ihrem Netz einen gemeinsamen Internet-Zugriff und sind zugleich ausreichend geschützt.

.. image:: ../pics/WiFi_Channels.png
             :scale: 35%

Die Verbindungsqualität von WiFi-Netzwerken hängt maßgeblich von der Auslastung der Funkkanäle ab, die in Ihrer Umgebung aktuell benutzt werden, denn Sie teilen sich die selben Funkkanälen mit anderen Teilnehmern anderer WiFi-Netze. Das OBP60 nutzt die Funkkanäle des 2.4 GHz-Frequenzbandes.

.. warning::
	Bei hoher Auslastung wie z.B. in Häfen kann die Verbindungsqualität des eigenen WiFi-Netzwerks dadurch beeinträchtigt sein. Sie müssen dann mit Verzögerungen bei der Datenübertragung rechnen, insbesondere, wenn Sie TCP-Datenverbindungen zum oder vom OBP60 nutzen. Stellen Sie aber auf alle Fälle sicher, dass in solchen Situationen die Bootsführung nicht beeinträchtig wird.

.. note::
	Verwenden Sie bei hoher Kanalauslastung Kanäle mit geringer Auslastung. Die Kanäle 1, 13 und 14 haben keine Nachbarkanäle und sind deutlich robuster gegen hohe Auslastung als die anderen Kanäle. Am besten eignet sich der Kanal 13, da er seltener benutzt wird. In den USA kann auch der Kanal 14 verwendet werden. Moderne mobile Router bieten häufig eine Automatik in ihrer Konfiguration an, die die Kanalauswahl optimieren kann.

Bei Änderungen der Konfiguration des OPB60 werden Sie immer nach dem Admin-Passwort gefragt. Die Übertragung des Passwortes erfolgt dabei immer verschlüsselt. Wenn Sie jedoch das Passwort für den WLAN-Zugangspunkt oder das WiFi-Client-Passwort ändern, wird es im Klartext gesendet. Wenn Sie das ``Remember me`` für das Admin-Passwort aktivieren, wird es im Klartext in Ihrem Browser gespeichert. Um es von dort zu entfernen, verwenden Sie ``Forget Password``.