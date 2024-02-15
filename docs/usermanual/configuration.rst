Konfiguration
=============

Nachdem die Stromversorgung zugeschaltet wurde, startet die Firmware des OBP60. Nach Abschluss der Initialisierungsphasees ertönt ein Piepton. Im Display wird zuerst das Open Boat Projects-Logo angezeigt, gefolgt von einem QR-Code, der die Zugangsdaten zum Access Point anzeigt. Beide Bilder sind für einige Sekunden sichtbar. Sie können mit Ihrer Handy-Kamera den QR-Code scannen und sich dann in das WiFi-Netz des OBP60 mit folgenden Zugangsdaten einloggen:

* **SSID:** OBP60V2
* **Passwort:** esp32nmea2k

Nachdem Sie im WiFi-Netzwerk eigebucht sind, öffnen Sie in einem Web-Browser die Adresse OBP60V2.local oder die IP-Adresse 192.168.15.1. Sie gelangen so auf die Benutzeroberfläche des OPB60 und können den aktuellen Status des Geräts überprüfen. Auf der Benutzeroberfläche befinden sich vier Tabs, mit denen verschiedene Bereiche der Konfiguration ausgewählt werden können:

* **Status** - Statusanzeige mit Übersicht der Bussysteme
* **Config** - Allgemeine Konfigurationsseite
* **XDR** - Konfigurationsseite für NMEA0183 XDR-Sentences
* **Data** - Dashboard zur Datenanzeige
* **Update** - Seite für das Firmware-Update

.. note::
	Beachten Sie, dass beim erstmaligen Aufruf der Konfigurationsoberfläche kein Passwort beim Speichern der Konfiguration notwendig ist. Als **Default-Passwort** wird **esp32admin** verwendet. Ändern Sie das Passwort für ihre Belange ab, verwenden Sie dabei nur Zeichen des ASCII-Zeichensatzes. Die Passwortabfrage kann auch deaktiviert werden.

Status
------

Auf der Statusseite sieht man im oberen Bereich den Ethernet-Verbindungsstatus. Die Informationen haben folgende Bedeutung:

**Version**
	Aktuelle Firmware-Version
**Access Point IP**
	IP-Adresse des Access Points
**WiFi Client connected**
	Zeigt an, ob das OBP60 mit einem anderen externen WiFi-Netzwerk als Client verbunden ist
**WiFi Client IP**
	IP-Adresse, die das Gerät vom externen WiFi-Netzwerk erhalten hat
**# TCP Clients**
	Anzahl externer TCP-Clients, die sich am OBP60 angemeldet haben
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

Wenn Sie auf das Fragezeichen hinter **Version** klicken, werden alle Telegramme angezeigt, die das OBP60 verarbeiten kann. Detailliertere Informationen zu den empfangenen Telegrammen sehen Sie, wenn Sie die Zeile des Bussystems aufgeklappen. Im Anhang finden Sie eine Tabelle mit allen NMEA0183- und NMEA2000-Telegrammen, die verarbeitet werden können.

.. note::
	Zum besseren Verständnis ist zu beachten, dass das OBP60 ein eigenes, unabhängiges WiFi-Netzwerk aufbaut, diese Funktion wird auch als Access Point bezeichnet. Die Anzahl der TCP-Clients in der Statuszeile bezieht sich dabei immer nur auf die Clients, die sich beim OBP60 im Access Point-Modus anmelden.
	Das OBP60 kann darüber hinaus Teil eines anderen externen WiFi-Netzwerks sein, in dem es sich dort als Client anmeldet. In dem Fall wird das eigene WiFi-Netz des OBP60 mit dem externen WiFi-Netz gebrückt. Alle Daten des OPB60 sind dann in beiden Netzwerken verfügbar. 
	
Config
------

XDR
---

Über die Konfigurationsseite <XDR> können XDR-Sentences für NMEA0183 erstellt werden. XDR-Sentences sind Telegramme für generische Sensorwerte, die verwendet werden, wenn sich kein geeignetes NMEA0183-Telegramm findet, mit dem man die Sensorwerte übertragen kann. Es ist ein universelles Telegramm zur Übertragung von Sensordaten. XDR-Sentences werden immer dann benutzt, wenn Daten aus dem I2C-Bus, dem 1Wire-Bus oder interne Sensordaten vom ESP32 übertragen werden sollen. Sofern nicht zugewiesene Sensordaten im OBP60 vorhanden sind, können diese über ein XDR-Mapping zugewiesen werden. Damit sind diese Daten als NMEA0183-Telegramme allgemein nutzbar.

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
	
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+
|Messwert          | Sensor-Typ      | ´Beispiele für Messdaten        | Einheit         | Name des Sensors            |
+==================+=================+=================================+=================+=============================+
| Luftdruck        | "P" Druck       | 0.8..1.1 oder 800..1100         | "B" Bar         | "Barometer"                 |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+
| Lufttemperatur   | "C" Temperatur  | 2 Dezimalstellen                | "C" Celsius     | "TempAir" or "ENV_OUTAIR_T" |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+
| Pitch            | "A" Winkel      |-180..0 runter    0..180 hoch    | "D" Degrees     | "PTCH" or "PITCH"           |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+
| Rolling          | "A" Winkel      |-180..0 links     0..180 rechts  | "D" Degrees     | "ROLL"                      |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+
| Wassertemperatur | "C" Temperatur  | 2 decimals                      | "C" Celsius     | "ENV_WATER_T"               |
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+


Update
------

Um die Firmware eines Gerätes zu aktualisieren, können Sie die **Registerkarte Update** verwenden. Es gibt zwei Arten von Firmware-Updates.

**Initial Firmware-Update**
	Beim Initial Firmware-Update wird der komplette Flash-Speicher des OBP60 gelöscht. Anschließend werden alle Firmware-Bestandteile im Flash gespeichert. Dabei wird eine initiale Konfiguration erstellt. Eine vorherige alte Konfoguration wird überschrieben. Die Initial Firmware-Updates verwenden den Dateinamen **xxx-all.bin**.
	
**Normales Firmware-Update**
	Beim normalen Firmware-Update wird nur der Programmteil der Firmware aktualisiert. Eine vorhandene Konfiguration bleibt dabei erhalten und ist nach dem Firmware-Update wieder nutzbar. Normale Firmware-Updates verwenden den Dateinamen **xxx-update.bin**.

Die letzte aktuelle Firmware können Sie auf folgender Webseite herunter laden:

https://github.com/norbert-walter/esp32-nmea2000-obp60/releases

Unter <Releases> sind eine Reihe verfügbarer Firmware-Updates für das OBP60 zu finden. Beachten Sie dabei die jeweilige Hardware-Version, für die Sie eine Firmware herunterladen wollen.

Für ein Firmware-Update laden Sie sich die gewünschte Firmware als Datei herunter und speichern Sie die Datei auf Ihrem Gerät. Über die Taste ``Choose File`` wählen Sie die heruntergeladene Datei aus. Es wird dann der Firmware-Type und die Firmware-Version angezeigt. Sollte die Firmware nicht zur verwendeten Hardware passen, erhalten Sie eine entsprechende Meldung. Die Firmware kann dann nicht geflasht werden. Über die Taste ``Upload`` starten Sie den Flash-Vorgang. Im Fortschrittsbalken sehen Sie den Verlauf des Vorgangs. Nach einem erfolgreichen Firmware-Update wird ein Reboot des Systems durchgeführt. In dieser Zeit ist die Web-Konfigurationseite offline (roter Punkt). Nach kurzer Zeit ist die Seite wieder online (grüner Punkt). Dann ist das System wieder betriebsbereit.

.. warning::
	Beachten Sie, dass Sie bei einem Firmware-Update auf eine ältere Version ein Initial Firmware Update durchführen müssen. So vermeiden Sie Komplikationen mit den gespeicherten Konfigurationsdaten. Unter Umständen ist das System nicht nutzbar und kann komplett einfrieren. Ein Firmware-Update über die Konfigurationsseiten ist dann nicht mehr möglich und die Firmware muss über USB geflasht werden.

Wie man die Firmware eines OBP60 über USB flasht, ist unter xxx beschrieben.	

Sicherheit im WiFi-Netzwerk
---------------------------

Sie sollten das OBP60 nur mit vertrauenswürdigen WiFi-Netzwerken verbinden. Es gibt im Gerät nur einen sehr begrenzten Schutz gegen Netzwerk-Sniffing oder Denial-of-Service-Angriffe. Solange Sie das eigene autarke WiFi-Netz des OBP60 nutzen, können fremde Personen ihr WiFi-Netz nicht verwenden. Auf diese Weise läuft die Datenübertragung läuft in ihrem eigenen WiFi-Netzwerk geschützt. Verbinden Sie das Gerät niemals ohne eine Firewall direkt mit dem Internet und vermeiden Sie direkte Verbindungen zu offenen Hafen-Netzwerken. Dadurch können auch fremde Personen auf Ihre Geräte im Netzwerk zugreifen.

.. note::
	Sie können die Sicherheit erhöhen, indem Sie einen separaten WiFi- oder LTE-Router in ihrem Boot verwenden. Die Router können so eingerichtet werden, dass sie ein eigenes WiFi-Netz aufspannen können, mit dem alle Geräte an Bord verbunden sind. Gängige Reiserouter verfügen in der Regel über eine bereits eingeschaltete Firewall, über die Sie Ihr eigenes WiFi-Netz mit dem Internet verbinden können. Die Firewall verhindert fremden Zugriff von außen auf Ihre Geräte. So haben alle Geräte in Ihrem Netz einen gemeinsamen Internet-Zugriff und sind zugleich ausreichend geschützt.

.. image:: ../pics/WiFi_Channels.png
             :scale: 35%

Die Verbindungsqualität von WiFi-Netzwerken hängt maßgeblich von der Auslastung der Funkkanäle ab, die in Ihrer Umgebung aktuell benutzt werden, denn Sie teilen sich die selben Funkkanälen mit anderen Teilnehmern anderer WiFi-Netze. Das OBP60 nutzt die Funkkanäle des 2.4 GHz-Frequenzbandes. Bei hoher Auslastung wie z.B. in Häfen kann die Verbindungsqualität des eigenen WiFi-Netzwerks dadurch beeinträchtigt sein. Sie müssen dann mit Verzögerungen bei der Datenübertragung rechnen, insbesondere, wenn Sie TCP-Datenverbindungen zum oder vom OBP60 nutzen. Moderne Reiserouter bieten häufig eine Automatik in ihrer Konfiguration an, die die Kanalauswahl optimieren hilft. Stellen Sie aber auf alle Fälle sicher, dass in solchen Situationen die Bootsführung nicht beeinträchtig wird.

.. note::
	Verwenden Sie bei hoher Kanalauslastung Kanäle mit geringer Auslastung. Die Kanäle 1, 13 und 14 haben keine Nachbarkanäle und sind deutlich robuster gegen hohe Auslastung als die anderen Kanäle. Am besten eignet sich der Kanal 13, da er seltener benutzt wird. In den USA kann auch der Kanal 14 verwendet werden.

Bei Änderungen der Konfiguration des OPB60 werden Sie immer nach dem Admin-Passwort gefragt. Die Übertragung des Passwortes erfolgt dabei immer verschlüsselt. Wenn Sie jedoch das Passwort für den WLAN-Zugangspunkt oder das WiFi-Client-Passwort ändern, wird es im Klartext gesendet. Wenn Sie das ``Remember me`` für das Admin-Passwort aktivieren, wird es im Klartext in Ihrem Browser gespeichert. Um es von dort zu entfernen, verwenden sie ``ForgetPassword``.
