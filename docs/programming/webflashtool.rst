Web-Flashtool
=============

Mit dem Web-Flashtool kann die Firmware für das OBP60 mit einem Webbrowser über eine USB-Verbindung in das Gerät übertragen werden. Dazu wird das OBP60 über die USB-C-Buchse mit einem PC oder Laptop verbunden und der **Chrome-** oder **Edge-Webbrowser** gestartet. Im OBP60 ist ein USB-Seriell-Konverter integriert, über den die Datenübertragung durchgeführt wird. Mit dem USB-C-Kabel lässt sich nur die Firmware übertragen. Ein Betrieb des Gerätes ist damit nicht möglich. 

.. note::
	Andere Webbrowser als Chrome oder Edge werden derzeit nicht unterstützt, da die Funktionalität für den Zugriff auf eine serielle Schnittstelle in anderen Webbrowsern nicht implementiert ist.
	
.. warning::
	Beachten Sie, dass das Web-Flashtool nur für ein OBP60 verwendet werden kann, das als Prozessor einen **ESP32-S3 N16R8** und als Display ein GDEY042T81 verwenden. Sofern Sie andere Hardware benutzen, müssen Sie sich eine angepasste Firmwareversion für ihre Hardware kompilieren. Folgen Sie den Anweisungen im Kapitel **Kompilieren und Download**.  
	
Für den Flash-Vorgang benötigt man folgende Materialien:
	* OBP60
	* USB-C zu USB-A Verbindungskabel < 1,5m
	* Drahtbrücke 5 cm
	* PC mit Chrome- oder Edge-Browser

**1. OBP60 in den Flash-Modus setzen**
	Öffnen Sie die hintere Gehäusreabdeckung und Stellen Sie mit der Drahtbrücke eine Verbindung von ``GND`` (CN2) zum ``Pin 27`` (ESP32-S3) her. Dann verbinden Sie das OBP60 mit dem PC über das USB-Verbindungskabel. Sobald sie USB-Schnittstelle erkannt wird, erfolgt eine Tonausgabe auf dem PC. Sie können dann die Drahtbrücke zwischen ``GND`` und ``Pin 27`` trennen. Der ESP32-S3 befindet sich jetzt im Flash-Modus.
	
	.. image:: ../pics/ESP32-S3_Pin27.png
	   :scale: 40%
	Abb.: Pin27 am OBP60
	
	.. image:: ../pics/Bridge_GND-Pin27.png
	   :scale: 40%
	Abb.: Brücke zwischen ``GND`` und ``Pin 27``
	
	
**2. Flashtool starten**

	Rufen Sie als nächstes die Webseite des `Online-Flashtools`_ auf.

	.. _Online-Flashtools: https://norbert-walter.github.io/obp60-v2-docu/flash_tool/esp_flash_tool.html

	.. image:: ../pics/Web_Flasher1.png
	   :scale: 50%
	Abb.: Startseite Web-Flashtool

	Drücken Sie dann auf **Connect** und wählen die entsprechende serielle Schnittstelle aus. Je nachdem, welches Betriebssystem Sie verwenden, sind die Schnittstellen verschieden bezeichnet.

	* **Windows:** USB JTAG/serial debug unit COMx
	* **Linux:** /dev/ttyACM0

	.. image:: ../pics/Serial_Connection.png
	   :scale: 50%
	Abb.: Auswahl der Schnittstelle

.. note::
	Beachten Sie, dass durchaus noch andere serielle Schnittstellen im System benutzt werden. Wählen Sie die Schnittstelle aus, die nach dem Anstecken des OBP60 an den USB-Port im System neu auftaucht. Bereits bestehende Schnittstellen dürfen Sie nicht nutzen, sie werden bereits anderweitig verwendet.
	
**3. Firmware übertragen**
	.. image:: ../pics/Web_Flasher2.png
	   :scale: 50%
	Abb.: Start Flashvorgang
	
	Starten Sie den Installationsvorgang über ``INSTALL OBP60 V2 FIRMWARE``. Nach erfolgreicher Übertragung wird eine Meldung ausgeben.
	
	.. image:: ../pics/Web_Flasher3.png
	   :scale: 50%
	Abb.: Übertragung der Firmware
	
	
**4. OBP60 starten**
	Entfernen Sie das USB-Verbindungskabel und versorgen Sie das OBP60 über ``+12V`` und ``GND`` von **CN2** mit 12V. Beim Starten der Firmware erfolgt ein kurzer Piepton. Nach kurzer Zeit sollte eine Anzeigeseite zu sehen sein. Je nach Einstellung wird vorher noch das OBP-Logo und der QR-Code für den WiFi-Zugang angezeigt.
	
	.. image:: ../pics/OBP60_FourValue2_tr.png
	   :scale: 30%
	Abb.: Anzeigeseite