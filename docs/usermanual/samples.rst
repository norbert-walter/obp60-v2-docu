Beispielkonfiguration
=====================

OBP60 Yachta AvNav
------------------

Im folgenden Beispiel wird gezeigt wie man mit einem **OBP60** eine Datenübertragung zum **Windsensor Yachta** und zu einem NMEA2000-Netzwerk aufbauen und die Daten in der Navigationsapp AvNav auf einem Tablett nutzen kann. Das OBP60 dient dabei als zentrale Datenbasis, in der alle Daten zusammenlaufen. Die Datenübertragung erfolgt über WiFi-Netzwerkverbindungen, die ein LTE-Router zur Verfügung stellt. Der Vorteil eines LTE-Routers besteht darin, dass sie alle Geräte an Bord mit einer WiFi-Internetverbindung versorgen können und die Geräte im WiFi-Netzwerk untereinander kommunizieren können. Der LTE-Router schottet das eigene WiFi-Netzwerk gegenüber dem Internet ab, so dass von außerhalb niemand auf Ihr internes Netzwerk Zugriff erhält. Somit lassen sich auch Geräte wie Handys, Tabletts oder Laptops an Bord mit dem Internet verbinden und alle Geräte haben Zugriff auf die Daten der Sensoren und können über einen Web-Browser darauf zugreifen. Die Naviationssoftware AvNav wird dabei auf einem Android-Tablett installiert und zur Navigation genutzt.

.. _NMEA2000-Gateway: https://open-boat-projects.org/de/nmea2000-gateway-mit-m5stack-atom/

.. tip::
	Grundsätzlich ließe sich der Access Point vom OBP60 auch als zentraler WiFi-Router nutzen. Die Leistungsfähigkeit ist aber deutlich geringer als bei einem LTE-Router. Wir empfehlen ausdrücklich die Verwendung eines dedizierte LTE- oder WiFi-Routers. Sie vermeiden damit Probleme bei der Kommunikation der Geräte untereinander.

.. image:: ../pics/Use_Case_5.png
             :scale: 60%	
Abb.: Beispielkonfiguration OBP60, Yachta, AvNav

Die Konfiguration läuft in folgenden Schritten ab:

* LTE-Router einrichten
* OBP60 mit NMEA2000-Netzwerk und Windsensor Yachta verbinden
* AvNav mit dem OBP60 verbinden

LTE-Router einrichten
^^^^^^^^^^^^^^^^^^^^^

Als LTE-Router können Sie sowohl mobile Geräte als auch stationäre Geräte verwenden. Mobile Geräte haben den Vorteil, dass sie autark über eine Batterie über einen längeren Zeitraum funktionieren und auch außerhalb des Bootes an Land bei Ausflügen benutzt werden können. Stationäre Geräte bieten sich an, wenn man maximale Empfangsleistung benötigt und in Küstennähe unterwegs ist und große Entfernungen zur nächsten Mobilfunk-Basisstation überbrücken möchte. In solchen Fällen bietet es sich an, Mobilfunkantennen oben im Mast zu installieren und die Antenne per Kabel mit dem stationären Router zu verbinden.

.. tip::
	Achten Sie beim Kauf des LTE-Routers, dass der Router im Dualband-Modus in den zwei WiFi-Frequenzbereichen 2.4 GHz und 5 GHz **gleichzeitig** arbeiten kann und über 4G/5G-Mobilfunk-Standard verfügt. So profitieren sie von einer leistungsfähigen Internet- und WiFi-Verbindung im 5 GHz Bereich und umgehen die meist überfüllten 2.4 GHz Frequenzbereiche. Solche Router können Daten zwischen beiden Frequenzbereichen problemlos austauschen. Ein ausgedientes Handy im Hotspot-Mode leistet ähnliches wie ein LTE-Router und kann eine günstige Alternative darstellen.

.. image:: ../pics/LTE-Router_TP-Link_M7450.png
             :scale: 20%	
Abb.: Mobiler 4G-LTE-Dualband-Router TP-Link M7450

	* Leistungsdaten
		- 4G/LTE Mobilfunkstandard 50 MBit/s
		- WiFi Dualband 2.4 GHz **oder** 5 GHz 300 MBit/s [#f2]_
		- 3000 mAh LiPo-Akku
		- 15 Stunden autarke Laufzeit
		- 32 WiFi-Geräte einbindbar
		- 32 GB SD-Card-Speicher
		- USB-, SMB- und FTP-Share für Filme und Musik von SD-Card
		- `Dokumentation <../_static/m7450.pdf>`_
	.. [#f2] Kein gleichzeitiger Dualbetrieb möglich

.. warning::
	Der LTE-Router TP-Link M7450 kann nicht gleichzeitig in beiden Frequenzbändern arbeiten. Daher müssen Sie den TP-Link M7450 fest auf das Frequenzband 2.4 GHz einstellen. Das OBP40 und der M5Stack ATOM CAN arbeiten nur im 2.4 GHz Bereich.
	
		
.. image:: ../pics/LTE-Router_RUT360.png
             :scale: 30%	
Abb.: Stationärer 4G-LTE-Dualband-Router RTU360

	* Leistungsdaten
		- 4G/LTE Mobilfunkstandard 50 MBit/scale
		- WiFi Dualband 2.4 GHz und 5 GHz 300 MBit/s
		- 2x LAN CAT6 100 MBit/s
		- Externe Antennen für LTE und WiFi
		- 12V Versorgungseingang
		- 230V AC-Netzteil
		- `Online-Dokumentation`_
		- `Quick-Installation Guide`_
		
.. _Online-Dokumentation: https://wiki.teltonika-networks.com/view/RUT360_Manual
.. _Quick-Installation Guide: https://wiki.teltonika-networks.com/view/QSG_RUT360

Der verwendete LTE-Router wird entsprechend der Bedienungsanleitung in Betrieb genommen. Für eine Internetverbindung benötigen Sie einen Mobilfunk-Datenvertrag. Die meisten Mobilfunkfirmen bieten preisgünstige Datentarife an. Empfehlenswert sind Volumenverträge, die ein festes Datenvolumen für eine vorgegebene Zeitdauer bieten. Wählen Sie einen Tarif aus, der Ihrem Datenverbrauch entspricht. Das Datenvolumen können Sie ebenfalls in allen Ländern der EU uneingeschränkt nutzen, so wie Sie das in Ihrem Heimatland gewohnt sind.

Für das Konfigurationsbeispiel wird davon ausgegangen, dass die Geräte folgende IP-Adressen vom Router zugewiesen bekommen:

	* MyBoat - WiFi-SSID
	* MySecret - WiFi Passwort
	* 192.168.1.1   - LTE-Router
	* 192.168.1.101 - OBP60
	* 192.168.1.102 - Windsensor Yachta
	* 192.168.1.103 - Android-Tablett mit AvNav

.. hint::
	In Ihrem konkreten Fall können die IP-Adressen abweichen. Verwenden Sie dann die IP-Adressen, die den Geräten vom Router zugewiesen worden sind.

Datenübertragung
^^^^^^^^^^^^^^^^

Das folgende Schema zeigt die Datenübertragung und welche Geräte Server oder Client bei der Datenübertragung sind.

.. image:: ../pics/Data_Transmission_2.png
             :scale: 80%
Abb.: Schema Datenübertragung
	
Konfiguration OBP60
^^^^^^^^^^^^^^^^^^^

.. image:: ../pics/OBP60_OneValue_tr.png
             :scale: 30%
Abb.: OBP60

Das OBP60 wird mit dem WiFi-Netzwerk des LTE-Routers verbunden. Der TCP-Server ist so konfiguriert, dass zum Tablett Daten übertragen werden können. Die TCP-Client-Verbindung dient zur Kommunikation mit dem Windsensor Yachta. Das OBP60 ist per Kabel mit dem NMEA2000-Netzwerk des Bootes verbunden. Sensordaten die im OBP60 vorliegen, wie z.B. die Windsensor-Daten, werden auch in den NMEA2000-Bus übertragen.

Nehmen Sie folgende Einstellungen vor:

+---------------------------+---------------------+
|Einstellung                |OBP60                |
+===========================+=====================+
|:ref:`Config - System`     |                     |
+---------------------------+---------------------+
|System Name                |OBP60V2              |
+---------------------------+---------------------+
|:ref:`Config - WiFi Client`|                     |
+---------------------------+---------------------+
|WiFi Client                |on                   |
+---------------------------+---------------------+
|WiFi Client SSID           |MyBoat               |
+---------------------------+---------------------+
|WiFi Client Password       |MySecret             |
+---------------------------+---------------------+
|:ref:`Config - Converter   |                     |
+---------------------------+---------------------+
|NMEA2000 Out               |on                   |
+---------------------------+---------------------+
|:ref:`Config - TCP Server` |                     |
+---------------------------+---------------------+
|TCP Port                   |10110                |
+---------------------------+---------------------+
|NMEA0183 Out               |on                   |
+---------------------------+---------------------+
|NMEA0183 In                |on                   |
+---------------------------+---------------------+
|To NMEA2000                |on                   |
+---------------------------+---------------------+
|SeaSmart Out               |on                   |
+---------------------------+---------------------+
|:ref:`Config - TCP Client` |                     |
+---------------------------+---------------------+
|Enable                     |on                   |
+---------------------------+---------------------+
|Remote Port                |6666                 |
+---------------------------+---------------------+
|Remote Address             |192.168.1.102        |
+---------------------------+---------------------+
|NMEA0183 Out               |off                  |
+---------------------------+---------------------+
|To NMEA2000                |on                   |
+---------------------------+---------------------+
|SeaSamart Out              |off                  |
+---------------------------+---------------------+

Nach der Konfiguration sollten Sie im Status nachfolgende Informationen sehen. Das OBP60 ist als WiFi-Client beim LTE-Router angemeldet und hat die IP-Adresse 192.168.1.101 zugewiesen bekommen. Das OBP60 ist als TCP-Client mit dem Windsensor Yachta verbunden. Über diese Verbindung werden Winddaten als NMEA0183-Telegramme empfangen. Unter Clients werden die Anzahl der Geräte angezeigt, die als TCP-Client mit dem OBP60 verbunden sind. Wenn das Tablet mit dem OBP60 verbunden ist, sollte ein Gerät angezeigt werden. Der NMEA2000-Status wird als Online angezeigt, wenn Daten mit dem NMEA2000-Bus ausgetauscht werden. Die Anzahl der ausgetauschten NMEA2000-Telegramme sieht man unter NMEA2000 In/Out. Wenn ein Tablett mit dem OBP60 per TCP verbunden ist, sieht man die Anzahl der ausgetauschten NMEA0183-Telegramme unter TCP In/Out.

+---------------------------+---------------------+
|Statusmeldungen            |OBP60                |
+===========================+=====================+
|:ref:`Status`              |                     |
+---------------------------+---------------------+
|WiFi Client Connected      |true                 |
+---------------------------+---------------------+
|WiFi Client IP             |192.168.1.101        |
+---------------------------+---------------------+
|#Clients                   |2                    |
+---------------------------+---------------------+		
|NMEA2000 State             |[0] Online           |
+---------------------------+---------------------+	
|NMEA2000 In                |Telegrammeanzahl     |
+---------------------------+---------------------+
|NMEA2000 Out               |Telegrammeanzahl     |
+---------------------------+---------------------+
|TCP In                     |Telegrammeanzahl     |
+---------------------------+---------------------+
|TCP Out                    |Telegrammeanzahl     |
+---------------------------+---------------------+

Die Verbindung des OBP60 mit dem NMEA2000-Netzwerk erfolgt wie im nachfolgenden Bild angezeigt. Ist das OBP60 ein normaler Teilnehmer des Bussystems, so muss die Terminierung deaktiviert sein.

.. image:: ../pics/OBP60_NMEA2000_Connection.png
			:scale: 50%
Abb. CAN-Bus Anbindung OBP60

Konfiguration Yachta
^^^^^^^^^^^^^^^^^^^^

.. image:: ../pics/Yachta_Wind_Sensor.png
             :scale: 100%

Der Windsensor Yachta ist so konfiguriert, dass er im WiFi-Netzwerk des LTE-Routers eingebucht ist. Der Windsensor stellt über den Port 6666 dem M5Stack Winddaten zur Verfügung. Es werden dabei nur Daten vom Windsensor Yachta zum M5Stack übertragen. 

Folgende Einstellungen werden für den Windsensor Yachta vorgenommen:

+---------------------------+---------------------+
|Einstellung                |Yachta               |
+===========================+=====================+
|**Network Settings**       |                     |
+---------------------------+---------------------+
|WLAN Client SSID           |MyBoat               |
+---------------------------+---------------------+
|WLAN Client IP             |MySecret             |
+---------------------------+---------------------+
|Connection Timeout         |30s                  |
+---------------------------+---------------------+
|WLAN Sever SSID            |Yachta               |
+---------------------------+---------------------+
|WLAN Server Password       |********             |
+---------------------------+---------------------+
|AP Channel                 |1                    |
+---------------------------+---------------------+
|Server Mode                |HTTP (JSON/NMEA)     |
+---------------------------+---------------------+
|mDNS Service               |on                   |
+---------------------------+---------------------+
|**Device Settings**        |                     |
+---------------------------+---------------------+
|Wind Sensor Type           |Yachta 2.0           |
+---------------------------+---------------------+

.. tip::
	Der Windsensor Yachta lässt sich in einen Demo-Mode versetzen. So kann die Funktionalität außerhalb des Bootes getestet werden. Der Windsensor liefert dann simulierte Winddaten. Über **Server Mode** kann der Simulationsmodus mit der Einstellung ``Demo Mode`` aktiviert werden.

Nach der Konfiguration sollten unter **Device Info** im Windsensor Yachta folgende Statusmeldungen zu sehen sein:

+---------------------------+---------------------+
|Statusmeldungen            |Yachta               |
+===========================+=====================+
|**Network Parameter**      |                     |
+---------------------------+---------------------+
|WLAN Client SSID           |MyBoat               |
+---------------------------+---------------------+
|WLAN Client IP             |192.168.1.102        |
+---------------------------+---------------------+
|Connection Quality         |>50%                 |
+---------------------------+---------------------+	

Tablett Konfiguration
^^^^^^^^^^^^^^^^^^^^^

.. image:: ../pics/Tablet_AVnav_Charts.png
             :scale: 10%

Das Android-Tablett wird in das WiFi-Netzwerk des LTE-Routers hinzugefügt und anschließend die App AvNav aus dem Play-Sore installiert. Details zur Konfiguration entnehmen Sie dem Handbuch zum Tablett. Die Daten eines GPS-Empfängers im Tablett lassen sich ebenfalls im NMEA0183- und NMEA2000-Netzwerk nutzen.

+---------------------------+---------------------+
|Einstellung                |Android-Tablett      |
+===========================+=====================+
|**Einstellungen WiFi**     |                     |
+---------------------------+---------------------+
|WiFi                       |on                   |
+---------------------------+---------------------+
|WiFi Client SSID           |MyBoat               |
+---------------------------+---------------------+
|WiFi Client Password       |MySecret             |
+---------------------------+---------------------+
|App-Installation           |AvNav                |
+---------------------------+---------------------+

Nachfolgend wird gezeigt, wie man Busdaten über ein Tablett in AvNav nutzen kann. Die Datenübertragung erfolgt über WiFi. Das Tablett tauscht dabei die Daten mit dem M5Stack über einen TCP-Verbindung aus. Dabei wird das Tablett als TCP-Client an die M5Stack ATOM CAN angedockt. Unter AvNav wird die Verbindung als TCPReader eingerichtet.

.. image:: ../pics/Android_Start_Page.jpg
             :scale: 40%	
Abb.: Startseite AvNav für Android

Unter AvNav klicken Sie auf der Startseite oben rechts das Symbol mit den 3 Strichen.

.. image:: ../pics/AVnav_Server_Status_Icon.png

Sie gelangen dann auf die Seite zum Serverstatus. Dort können Sie über das Plus-Symbol weitere Verbindungen zum AvNavServer einrichten.

.. image:: ../pics/AVnav_Add_Icon.png

Für die bidirektionale Kommunikation über USB wählen Sie **TCPReader**.

.. image:: ../pics/Android_Select_Handler.jpg
             :scale: 40%	
Abb.: Verbindungstypen

Unter **IP-Address** tragen Sie die IP-Adresse des M5Stack ein und als **Port** die 10110. Um nicht nur Daten senden, sondern auch empfangen zu können, aktivieren Sie **SendOut**.

.. image:: ../pics/Android_Select_Handler_TCPReader.jpg
             :scale: 40%	
Abb.: Einstellungen zur TCPReader-Verbindung

Nach der Übernahme aller Daten ist die neue Verbindung im Server-Status als TCPReader-Verbindung zu sehen.

.. image:: ../pics/Android_Server_Status_2.jpg
             :scale: 40%	
Abb.: Server-Status
