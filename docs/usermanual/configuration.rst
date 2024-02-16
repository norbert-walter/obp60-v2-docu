Konfiguration
=============

Nachdem die Stromversorgung zugeschaltet wurde startet die Firmware des OBP60 und es ertönt ein Piepton nach der Initialisierungsphase. Im Display wird als erstes das Open Boat Projects Logo angezeigt gefolgt von einem QR-Code, der die Zugangsdaten zum Access Point anzeigt. Beide Bilder sind für einige Sekunden sichtbar. Sie können mit der Handy-Kamera den QR-Code scannen und sich in das WiFi-Netz des OBP60 mit folgenden Zugangsdaten einloggen:

* **SSID:** OBP60V2
* **Passwort:** esp32nmea2k

Nachdem sie im WiFi-Netzwerk eigebucht sind, öffnen Sie in einen Web-Browser die Adresse OBP60V2.local oder die IP-Adresse 192.168.15.1. Sie gelangen auf die Benutzeroberfläche und können den Status einsehen. Auf der Benutzeroberfläche befinden sich 4 Tabs mit denen verschiedene Bereiche der Konfiguration ausgewählt werden können:

* **Status** - Statusanzeige mit Übersicht der Bussysteme
* **Config** - Allgemeine Konfigurationsseite
* **XDR** - Konfigurationsseite für NMEA0183 XDR-Sentences
* **Data** - Dashboard zur Datenanzeige
* **Update** - Seite zum Firmware-Update

.. note::
	Beachten sie, dass beim erstmaligen Aufruf der Konfigurationsoberfläche kein Passwort beim Speichern der Konfiguration notwendig ist. Als **Default-Passwort** wird **esp32admin** verwendet. Ändern sie das Passwort auf ihre Belange ab und verwenden sie nur Zeichen des ASCII Zeichensatzes. Die Passwortabfrage kann auch deaktiviert werden.

Status
------

Auf der Statusseite sieht man im oberen Bereich den Ethernet-Verbindungsstatus. Die Informationen haben folgende Bedeutung:

**Version**
	Aktuelle Firmware-Version
**Access Point IP**
	IP-Adresse des Access Points``
**WiFi Client connected**
	Zeigt an, ob das OBP60 mit einem anderen externen WiFi-Netzwerk als Client verbunden ist
**WiFi Client IP**
	IP-Adresse die das Gwerät vom anderen WiFi-Netzwerk erhalten hat
**# TCP Clients**
	Anzahl externer TCP-Clients die sich am OBP60 angemeldet haben
**NMEA2000 in**
	Anzahl der NMEA2000 Telegramme die empfangen wurden
**NMEA2000 out**
	Anzahl der NMEA2000 Telegramme die gesendet wurden
**TCP in**
	Anzahl der NMEA0183 Telegramme die über TCP empfangen wurden
**TCP out**
	Anzahl der NMEA0183 Telegramme die über TCP gesendet wurden
**USB in**
	Anzahl der NMEA0183 Telegramme die über USB empfangen wurden
**USB out**
	Anzahl der NMEA0183 Telegramme die über USB gesendet wurden
**Serial in**
	Anzahl der NMEA0183 Telegramme die über RS485 empfangen wurden
**Serial out**
	Anzahl der NMEA0183 Telegramme die über RS485 gesendet wurden

Wenn sie auf das Fragezeichen hinter **Version** klicken, werden alle Telegramme angezeigt, die das OBP60 verarbeiten kann. Detailliertere Informationen zu den empfangenen Telegrammen sehen sie, wenn sie die Zeile des Bussystems aufgeklappen. Im Anhang finden sie eine Tabelle mit allen NMEA0183 und NMEA2000 Telegrammen, die verarbeitet werden können.

.. note::
	Zum besseren Verständnis ist zu beachten, dass das OBP60 eigenständig ein WiFi-Netzwerk aufbauen und damit autark arbeiten kann. Das OBP60 kann aber auch zusätzlich Teil eines anderen externen WiFi-Netzwerks sein, in dem es sich als Client dort anmeldet. In dem Fall ist das lokale WiFi-Netz des OBP60 mit dem externen WiFi-Netz gebrückt und alle Daten sind in beiden Netzwerken verfügbar. Die Anzahl der TCP Clients in der Statuszeile bezieht sich dabei immer nur auf Clients die sich beim OBP60 anmelden.
	
Config
------

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
	
+------------------+-----------------+---------------------------------+-----------------+-----------------------------+
|Messwert          | Sensor-Typ      | ´Beispiele für messdaten        | Einheit         | Name des Sensors            |
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

Über die XDR Konfigurationsseite lassen sich 30 XDR-Telegramme individuell erstellen.

.. image:: ../pics/XDR_1.png
             :scale: 50%

Dazu öffnet man als erstes über ``Show Unmapped`` eine Liste der nicht verknüpften Sensordaten.

.. image:: ../pics/XDR_Show_Unmapped.png
             :scale: 50%
             
In der Liste sehen sie welche Daten zur Verfügung stehen. Über ``+`` werden die Daten in die letzte frei verfügbare XDR-Konfiguration automatisch eingefügt und der richtigen Kategorie zugeordnet. Der Sensorname muss noch im Feld **Transducer** hinzugefügt werden. 

.. image:: ../pics/XDR_2png
             :scale: 50%

Nach der Zuordnung des Sensornamens wird unter **Example** ein Beispiel für das XDR-Telegramm angezeigt. Danach können alle Einstellungen noch individuell geändert werden. Die Erklärung zu den Einstellungen ist nachfolgend aufgeführt.

**Direction**
    Über Direction lässt sich einstellen wie Sensordaten eingelesen werden sollen und wohin sie übertragen werden. 
    **off** - Die Sensordaten werden nicht benutzt. Damit können sie ein bereits konfiguriertes XDR-Telegramm deaktivieren.
    **bidir** - Die Sensordaten werden zwischen NMEA0183 und NMEA2000 ausgetauscht
    **to2K** - Das Sensordaten werden nur nach NMEA2000 gesendet
    **from2k** - Unbekannte Sensordaten von NMEA2000 werden eingelesen
     
**Category**
    Über Category kann Sensor-Typ zugeordnet werden. 
    **Temperature** - Temperatursensoren für Luft, Wasser, Kühlschrank
    **Humidity** - Luftfeuchtigkeitssensoren
    **Pressure** - Drucksensoren für Luftdruck und andere Drücke wie z.B. Öldruck
    **Fluid** - Sensoren für Flüssigkeiten wie Durchfluss und Füllstand
    **Battery** - Batteriesensoren für Spannung, Strom, Leistung, Baterietemperatur
    **Engine** - Motorsensoren für Drehzahl, Anstellung, Trimmklappen, Öl, Kühlwasser
    **Attitude** - Höhendaten aus GPS-Sensor ermittelt
    
**Source**
    Über Source lässt sich die Quelle der Sensordaten genauer einstellen. Je nach verwendeten Sensortyp stehen verschiedene Sensor-Quellen zur Verfügung
    
**Field**
    Mit Field kann genauer beschrieben werden wie die Sensordaten zu verstehen sind. Es sind Zusatzdaten die kontextabhängig je nach verwendeten Sensor-Typ einstellabr sind. So kann z.B. festgelegt werden, ob es sich um einen Anzeigewert oder um einen Einstellwert handelt.
    
**Instance**
    Mit Instance kann festgelegt werden, ob es mehrere Sensoren des selben Typs gibt. Das kann z.B. auftreten, wenn zwei Motoren in einem Boot verbaut sind und zwei Tankwerte angezeigt werden sollen. Mit Hilfe einer Instanz-Nummer werden die Sensoren unterschieden. An den Sensornamen wird dann z.B. **#1** angefügt. Die Arte der Instanzierung kann folgendermaßen festgelegt werden:
        **singel** - Es wird ein Sensor instanziert, dem einen freie Instanz-Nummer zugeordnet werden kann. So können z.B. zwei Sensoren die selben Daten in ein XDR-Telegramm übertragen werden, wenn die Sensoren redundant sind.
        **ignore** - Es existiert nur genau ein einziger Sensor dieses Typs.
        **auto** - Die Instanzierung wird automatisch übernommen. Sobals ein neuer Sensor des gleichen Typs und der selben Source verwendet wir, wird eine neue Instanz des Sensors angelegt.
        
**Transducer**
    Über Transducer wird der Sensorname festgelegt. Es handelt sich dabei im eine Klartextbeschreibung des Sensors mit ASCII Zeichen. Verwenden sie nur Buchstaben und Zahlen ohne Freizeichen und Sonderzeichen.
    
**Example**
    Beispiel wie der Inhalt des XDR-Telegramms aussehen wird.
    
    
Update
------

Um die Firmware eines Gerätes zu aktualisieren, können Sie die **Registerkarte Update** verwenden. Es gibt zwei Arten von Firmware-Updates.

**Initial Firmware-Update**
	Beim Initial Firmware-Update wird der komplette Flash-Speicher des OBP60 gelöscht und anschließend alle Firmware-Bestandteile im Flash gespeichert. Dabei wird eine initiale Konfiguration erstellt. Eine vorherige alte Konfoguration wird überschrieben. Die Initial Firmware Updates verwenden den Dateinamen **xxx-all.bin**.
	
**Normales Firmware-Update**
	Beim normalen Firmware-Update wird nur der Programmteil der Firmware aktualisiert. Eine vorhandene Konfiguration bleibt dabei erhalten und ist nach dem Firmware-Update wieder nutzbar. Normale Firmware-Updates verwenden den Dateinamen **xxx-update.bin**.

Die letzte aktuelle Firmware können sie auf folgender Webseite herunter laden:

https://github.com/norbert-walter/esp32-nmea2000-obp60/releases

Unter Releases sind eine Reihe verfügbarer Firmware-Updates für das OBP60 zu finden. Beachten sie dabei die jeweilige Hardware-Version für die sie eine Firmware herunterladen wollen.

Für ein Firmware-Update laden sie sich die gewünschte Firmware als Datei herunter und speichern sie die Datei auf ihrem Gerät. Über die Taste ``Choose File`` wählen sie die heruntergeladene Datei aus. Es wird dann der Firmware-Type und die Firmware-Version angezeigt. Sollte die Firmware nicht zur verwendeten Hardware passen, so erhalten sie eine Meldung. Die Firmware kann dann nicht geflasht werden. Über die Taste ``Upload`` starten sie den Flash-Vorgang. Im Fortschrittsbalken sehen sie den Verlauf des Vorgangs. Nach einem erfolgreichen Firmware-Update wird eine Reboot des Systems durchgeführt. In dieser Zeit ist die Web-Konfigurationseite offline (roter Punkt). Nach kurzer Zeit ist die Seite wieder online (grüner Punkt). Dann ist das System wieder betriebsbereit.

.. warning::
	Beachten sie, dass sie bei einem Firmware-Update auf eine ältere Version ein Initial Firmware Update durchführen müssen. So vermeiden sie Komplikationen mit den gespeicherten Konfigurationsdaten. Unter Umständen ist das System nicht nutzbar und kann komplett einfrieren. Ein Firmware-Update über die Konfigurationsseiten ist dann nicht mehr möglich und die Firmware muss über USB geflasht werden.

Wie man die Firmware eines OBP60 über USB flasht, ist unter xxx beschrieben.	

Sicherheit im WiFi-Netzwerk
---------------------------

Sie sollten das OBP60 nur mit vertrauenswürdigen WiFi-Netzwerken verbinden. Es gibt nur einen sehr begrenzten Schutz gegen Netzwerk-Sniffing oder Denial-of-Service-Angriffe. Solange sie das eigene autarke WiFi-Netzt des OBP60 nutzen, können fremde Personen ihr WiFi-Netzt nicht verwenden. Die Datenübertragung läuft geschützt in ihrem eigenen WiFi-Netzwerk. Verbinden sie das Gerät niemals direkt mit dem Internet ohne eine Firewall und vermeiden sie direkte Verbindungen zu offenen Hafen-Netzwerken. Damit können auch fremde Personen auf ihre Geräte im Netzwerk zugreifen.

.. note::
	Sie können die Sicherheit erhöhen, indem sie einen separaten WiFi- oder LTE-Router in ihrem Boot verwenden. Die Router können so eingerichtet werden, dass sie ein eigenes WiFi-Netz aufspannen können, in dem alle Geräte an Bord verbunden sind. Über eine Firewall ist das eigene WiFi-Netz mit dem Internet verbunden. So haben auch alle Geräte einen Internet-Zugriff und sind ausreichend geschützt. Die Firewall verhindert fremden Zugriff von außen auf ihre Geräte.

.. image:: ../pics/WiFi_Channels.png
             :scale: 35%

Die Verbindungsqualität von WiFi-Netzwerken hängt maßgeblich von der Auslastung der Funkkanäle ab, die aktuell benutzt werden. Sie teilen sich die selben Funkkanälen mit anderen Teilnehmern anderer WiFi-Nnetzte. Das OBP60 nutzt die Funkkanäle des 2.4 GHz Frequenzbandes. Bei hoher Auslastung, wie z.B. in Häfen, kann die Verbindungsqualität des eigenes WiFi-Netzwerks beeinträchtigt sein. Sie müssen dann mit Verzögerungen bei der Datenübertragung rechnen, insbesondere dann, wenn sie TCP-Datenverbindungen zum oder vom OBP60 nutzen. Stellen sie sicher, dass sie in solchen Situationen die Bootsführung beherrschen.

.. note::
	Verwenden sie bei hoher Kanalauslastung Kanäle mit geringer Auslastung. Die Kanäle 1, 13 und 14 haben keine Nachbarkanäle und sind deutlich robuster gegen hohe Auslastung als die anderen Kanäle. Am besten eignet sich der Kanal 13, da er seltener benutzt wird. In den USA kann auch der Kanal 14 verwendet werden.

Bei Änderungen der Konfiguration werden sie nach dem Admin-Passwort gefragt. Die Übertragung des Passwortes erfolgt dabei immer verschlüsselt. Wenn sie jedoch das Passwort für den WLAN-Zugangspunkt oder das WiFi-Client-Passwort ändern, wird es im Klartext gesendet. Wenn sie das ``Remember me`` für das Admin-Passwort aktivieren, wird es im Klartext in Ihrem Browser gespeichert. Um es von dort zu entfernen, verwenden sie ``ForgetPassword``.
