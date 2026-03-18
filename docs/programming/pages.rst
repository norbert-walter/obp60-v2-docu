Seitenerstellung
================

Um eine neue Seite zu erstellen sind folgende Schritte notwendig:

	1. Anlegen einer neuen Seite unter ``lib\obp60task\PageXXXX.cpp``
	2. Registrierung der Seite in ``lib\obp60task\obp60task.cpp``. Dazu die Funktion ``registerAllPages`` entsprechend erweitern
	3. In ``/lib/obp60task/config.json`` die neue Seite in die jeweiligen Seitenlisten aufnehmen oder Seite in ``/lib/obp60task/gen_set.py`` aufnehmen und damit den relevanten Teil der Datei ``/lib/obp60task/config.json`` neu erzeugen. 

Als Vorlage für eine neue Seite kann z.B. die vorhandene Seite ``PageDigitalOut.cpp`` verwendet werden. Sie enthält nur minimalen Code und zeigt die typische Verwendung der Grafik- und Anzeigefunktionen. In der kopierten Seite sind dann lediglich alle Texte *PageDigitalOut* durch *PageMySample* zu ersetzen und die Datei unter dem Namen ``PageMySample.cpp`` abzuspeichern. Alle erstellten Seiten müssen dem Schema ``PageXXXX.cpp`` folgen.

Zugriff auf Daten
=================

Für manche Seiten ist im Quellcode fest vorgegeben, welche Werte verwendet werden: 

 .. code-block:: c++

     int displayPage(PageData &pageData)
     {
       GwConfigHandler *config = commonData->config;
       double value1 = 0;
       // Get boat values for Keel position
       value1 = commonData->data.rotationAngle; // Raw value without unit convertion

Alternativ könenen in der Page Description sowohl feste als auch über die Web-Oberfläche konfigurierbare Werte angegeben werden. Diese stehen innerhalb der Seite als ``pageData.values[i]`` zur Verfügung, wobei die Web-konfigurierbaren Werte vor den fest konfigurierten Werten stehen. 

 .. code-block:: c++

    int displayPage(PageData &pageData){
      GwConfigHandler *config = commonData->config;
      // Get config data
      GwApi::BoatValue *bvalue1;
      // Get value for AWA
      bvalue1 = pageData.values[4];
        ....
    }
    PageDescription registerPageWindRoseFlex(
      "WindRoseFlex", // Page name
      createPage,     // Action
      4,              // Number of bus values depends on selection in Web configuration
      {"AWA", "AWS", "TWA", "TWS"},    // fixed  values we need in the page. They are inserted AFTER the web-configured values.	
      true            // Show display header on/off
    );

Darstellung von Daten
=====================

Wie die Zeichenketten aus den Rohdaten erzeugt werden, ist in ``OPB60Foramtter.cpp`` festgelegt, wo auch die Umrechungen in verschiedene Einheiten hinterlegt sind. Folgendermaßen kann zunächst eine eventuell vorhandene Kalibrierung auf den Wert angewendet werden und dann eine Zeichenkette in der gewählten Einheiten und nach den ausgewähten Formatierungsvorgaben erzeugt werden:

.. code-block:: c++
   
   // Check if boat data value is to be calibrated
   calibrationData.calibrateInstance(bvalue1, logger); 
   // Formatted value as string including unit conversion and switching decimal places
   String svalue1 = formatValue(bvalue1,*commonData).svalue;    
   // Unit of value
   String unit1 = formatValue(bvalue1,*commonData).unit;        

Zur Darstellung der Werte wird typischerweise eine Schriftart aus der Familie DSEG7 verwendet. Eine Besonderheit dieser Schriftart ist die Breite der Zeichen. Leerzeichen, Punkt und Doppelpunkt sind sehr viel schmaler als die Ziffern. Für eine Ziffer, bei der keins der 7 Segmente angezeigt wird, wird das Zeichen ``!`` verwendet. So lassen sich auch Abstände erzeugen, die genau so breit sind wie eine Ziffer. Daher wird in OBB60Formatter bei einer Darstellung, die 2 Ziffern verwendet (d.h. bei einer Nachkommastelle für Zahlen unter 10 und 2 Ziffern ohne Nachkommastelle für Zahlen zwischen 10 und 99) folgendermaßen die Zahl rechtsbündig ausgerichtet:

.. code-block:: c++

   if (precision == "1") {
     //
     //All values are displayed using a DSEG7* font. In this font, ' ' is a very short space, and '.' takes up no space at all. 
     //For a space that is as long as a number, '!' is used. For details see  https://www.keshikan.net/fonts-e.html
     //
     fmt_dec_1 = "!%1.1f";  //insert a blank digit and then display a two-digit number
     fmt_dec_10 = "!%2.0f"; //insert a blank digit and then display a two-digit number
     fmt_dec_100 = "%3.0f"; //dispay a three digit number
   } else {
     fmt_dec_1 = "%3.2f";
     fmt_dec_10 = "%3.1f";
     fmt_dec_100 = "%3.0f";
   }

Falls auf einer Seite eine andere Schriftart zur Darstellung verwendet werden soll, muss die Formatierung auf der Seite selbst aus dem Zahlenwert erfolgen, um die Ausgabe von Ausrufezeichen zu verhindern.

Konfigurationswerte
===================

Manchmal ist es notwendig über die Web-Konfigurationsoberfläche Konfigurationen für bestimmte Einstellwerte vorzunehmen. Dabei wird Variablen ein Wert zum Startzeitpunkt der Software zugewiesen, den der User über die Konfigurationsoberfläche nachträglich ändern kann. Die Konfigurationswerte werden in einer JSON-Konfigurationsdatei mit dem Namen ``config_obp60.json`` definiert. Ein typischer Eintrag für einen Konfigurationswert sieht so aus:

.. code-block:: json

	{
	  "name": "waterTank",
	  "label": "Water Tank [l]",
	  "type": "number",
	  "default": "0",
	  "check": "checkMinMax",
	  "min": 0,
	  "max": 5000,
	  "description": "Water tank capacity [0...5000l]",
	  "category": "OBP60 Settings",
	  "capabilities": {
		"obp60":"true"
	  }
	},

.. code-block:: json

	{
        "name": "batteryVoltage",
        "label": "Battery Voltage [V]",
        "type": "list",
        "default": "12V",
        "description": "Battery Voltage [12V|24V]",
        "list": [
            "12V",
            "24V"
        ],
        "category": "OBP60 Settings",
        "capabilities": {
            "obp60":"true"
        },
		 "condition": [
            { "battery": ["available"] }
        ]
    },
	
Die Datei ``config_obp60.json`` enthält eine Vielzahl von Konfigurationswerten. Die Bedeutung der Werte ist nachfolgend beschrieben.

* **name**: Varianblenname im Programm (Kleinschreibung, max. 12 Zeichen)
* **label**: Variablenname in der Web-Konfigurationsoberfläche	

* **type**: Typ der Variable
	* **number**: Zahlenwert
	* **string**: Textwert
	* **list**: Liste von Auswahlwerten
	
* **default**: Defaultwert der Variable	

* **check**: Prüfanweisung
	* **checkMinMax**: Variablenwert auf Min, Max prüfen und ggf. begrenzen
	
* **min**: Min-Wert
* **max**: Max-Wert
* **description**: Beschreibungstext (die Kombination *\n* erzeugt eine Zeilenumbruch)
* **category**: Kategorie in der vertikalen Menüstruktur (wird automatisch angelegt, wenn nicht vorhanden)

* **capabilities**: Anzeigemöglichkeit für unterschiedliche Hardwareversionen
	* **"obp60":"true"**: Nur anzeigen, wenn Capabilitie für obp60 in Datei ``obp60task.h`` definiert ist
	
* **condition**: Anzeigebedingung (UND-Verknüpft bei mehreren Einträgen)
	* **"battery": ["available"]**: Nur anzeigen, wenn Variable *batery* den Wert *available* hat


Darstellung grafischer Inhalte
==============================

Auf dem Display lassen sich sowohl textbasierte als auch grafische Elemente platzieren. Die Grundlage für diese Operationen wird durch die GFX-Grafik-Lib bereitgestellt. Die Bibliothek wurde von Adafruit initiiert, um verschiedenste Grafikdisplays mit einem einheitlichen Befehlssatz ansprechen zu können. Viele Treiber-Hersteller für Displays orientieren sich an der Lib und haben eigene Adaptionen vorgenommen, die in weiten Teilen mit dem Befehlssatz identisch sind. Für das e-Paper-Display gibt es aber einige Einschränkungen und es stehen nicht alle Befehle der Adafruit-GFX-Lib zur Verfügung.

In diesem `PDF-Dokument <../_static/files/adafruit-gfx-graphics-library.pdf>`_ können die grundlegenden Befehle der Adafruit-GFX-Lib eingesehen werden. Darüber hinausgehend können Sie den kompletten Funktionsumfang der Lib als `Klassen Referenz`_ hier online abrufen.

.. _Klassen Referenz: https://adafruit.github.io/Adafruit-GFX-Library/html/class_adafruit___g_f_x.html

Das Koordinatensystem des Grafikdisplays ist so organisiert, dass sich in der linken oberen Ecke der Nullpunkt befindet. Alle Koordinatenangaben beziehen sich auf diesen Ursprung.

.. image:: /pics/Draw_Coordinates.png
             :scale: 50%

Abb.: Koordinatensystem

Im Projekt wird die Hilfsfunktion *getdisplay()* verwendet, in die alle GFX-Befehle eingebettet sind. Die nachfolgenden Beschreibungen zu den Grafikfunktionen gelten sowohl für das schwarz/weiß e-Paper-Display als auch für das Farb-TFT-Display und können gleichwertig benutzt werden. Je nach Displaytyp werden die Farben monchrom oder farbig dargestellt.  

Farbraum
--------

Der Farbraum für Grafikdisplays folgt dem RGB565-Farbschema. Dabei werden 16 Bits auf die jeweiligen Farben Blau, Grün und Rot zugeordnet. Die Farbauflösung ist bei Grün um 1 Bit höher gegenüber Rot und Blau. Dadurch können Mischfarben trotz geringer Bitanzahl deutlich besser abgebildet werden. Mit dem RGB565-Farbschema lassen sich 65.536 verschiedene Farben abbilden. Das RGB565-Farbschema ist für kleine Mikrocontroller ein guter Kompromiss zwischen Hardwareaufwand und Detailtiefe in der Farbwiedergabe und ist der meist verwendete Farbstandard in diesem Bereich. Auf PCs wird dagegen meist das RGB888-Farbschema verwendet mit dem bis zu 16.777.216 Farben abgebildet werden können. Wer mehr über das `RGB-Farbschema`_ wissen möchte, kann in dieser Beschreibung weitere Informationen finden.

.. _RGB-Farbschema: https://barth-dev.de/online/rgb565-color-picker/

.. image:: /pics/RGB565_Color_System.png
             :scale: 80%

Abb.: RGB565-Farbschema

Die 16 Bits des Farbschemas werden in zwei Byte aufgeteilt. Ein High-Byte und ein Low-Byte.

.. image:: /pics/RGB565_MSB_LSB.png
             :scale: 80%
			 
Abb.: RGB565 High- und Low-Byte			 

Mit diesen beiden Bytes wird die Farbe eines Pixels definiert. In der folgenden Tabelle sind für einige Farben der HEX-Farbcode und der Farbname exemplarisch dargestellt.

.. code-block:: c++

	// TFT color definitions
	#define BLACK 0x0000
	#define BLUE 0x001F
	#define RED 0xF800
	#define GREEN 0x07E0
	#define CYAN 0x07FF
	#define MAGENTA 0xF81F
	#define YELLOW 0xFFE0
	#define WHITE 0xFFFF
	
Es gibt noch deutlich mehr Farbnamen, die man in dieser `Farbtabelle`_ nachlesen kann. Für das E-Paper-Display gibt es zwei eigene Farbnamen. 

.. _Farbtabelle: https://github.com/newdigate/rgb565_colors

.. code-block:: c++

	// EPD color definitions
	#define GxEPD_BLACK 0x0000
	#define GxEPD_WHITE 0xFFFF

In den Anzeigeseiten wird die Farbauswahl zentral über folgende Weise gesteuert. In *commonData* sind die aktuellen Farben hinterlegt, die im Display verwendet werden sollen. *fgcolor* und *bgcolor* definieren dabei die Vordergrund- und Hintergrundfarbe, die man zentral in der Webkonfiguration ausgewählen kann (normale oder inverse Darstellung). Die Farben beziehen sich dabei immer auf Schwarz und Weiß, damit sie in verschiedenen Displaytypen einheitlich angezeigt werden können.

.. code-block:: c++

	getdisplay().setTextColor(commonData->fgcolor);

Text
----

.. code-block:: c++

	getdisplay().setFont(Arial);        // Set text font 
	getdisplay().setTextColor(color);   // Set text color
	getdisplay().setCursor(x, y);       // Set cursor for text position
	getdisplay().print("A");            // Print text

.. image:: /pics/Draw_Character.png
             :scale: 80%

Abb.: Platzierung eines Schriftzeichens

Linie
-----

.. code-block:: c++

	getdisplay().drawLine(x0, y0, x1, y1, color);	// Draw single line

.. image:: /pics/Draw_Line.png
             :scale: 80%

Abb.: Linie

Viereck
-------

.. code-block:: c++

	getdisplay().drawRect(x0, y0, width, hight, color);	// Draw rect
	getdisplay().fillRect(x0, y0, width, hight, color);	// Draw filled rect

.. image:: /pics/Draw_Rect.png
             :scale: 80%

Abb.: Vierecks

Viereck gerundet
----------------

.. code-block:: c++

	getdisplay().drawRoundRect(x0, y0, width, hight, radius, color);	// Draw round rect
	getdisplay().fillRoundRect(x0, y0, width, hight, radius, color);	// Draw filled round rect

.. image:: /pics/Draw_RoundRect.png
             :scale: 80%

Abb.: Vierecks mit runden Ecken

Diese Funktion kann sehr gut zum Zeichen von Bedienknöpfen verwendet werden. Mit ihr wurde eine weiter Funktion erstellt, mit der sich Bedienknöpfe anzeigen lassen.

.. code-block:: c++
	drawButtonCenter(x, y, width, hight, textButtonLabel, fgcolor, bgcolor, textBehindButton);


Dreieck
-------

.. code-block:: c++

	getdisplay().drawTriangle(x0, y0, x1, y1, x2, y2, color);	// Draw triangle
	getdisplay().fillTriangle(x0, y0, x1, y1, x2, y2, color);	// Draw filled triangle

.. image:: /pics/Draw_Triangle.png
             :scale: 80%

Abb.: Dreiecks

Kreis
-----

.. code-block:: c++

	getdisplay().drawCircle(x0, y0, radius, color); // Draw circle
	getdisplay().fillCircle(x0, y0, radius, color); // Draw filled circle

.. image:: /pics/Draw_Circle.png
             :scale: 80%
			 
Abb.: Kreises

Bild
----

Mit dem nachfolgenden Befehl können Bilder als 1Bit-Scharz/Weiß-Bilder angezeigt werden. Über den Parameter color kann die Farbe des aktiven Pixels festgelegt werden. Bei einem e-Paper-Display ist das Schwarz oder Weiß und bei einem TFT-Display eine beliebige Farbe. Somit ist es möglich, auch reine Scharz/Weiß-Bilder auf einem Farbdisplay darzustellen.

Bevor Sie Bilder nutzen können, müssen die Bilder in eine C-compatible Schreibweise umgewandelt werden. Mit folgenden Tools ist das möglich:

	* **Image2LCD** - 1Bit-Bild (C-Code)
		* Scan mode: Einstellung auf Horizontal
		* Bit order: Einstellung auf MSB first
	* **Gimp** - XBitmap-Bild (xbm-Datei)
		* Scan mode: Fix horizontal
		* Bit order: Fix LSB fist

Darüber werden die Bilder als eine Array-Struktur direkt im Quellcode abgelegt und können über eine Variable im Code aufgerufen und zur Anzeige gebracht werden. Beispielhaft ist hier der C-Code für ein Icon als XBitmap-Bild zu sehen.

.. code-block:: c++

	static unsigned char xbm_icon[] PROGMEM = {
	   0x00, 0x00, 0xe0, 0x01, 0x18, 0x06, 0x04, 0x08, 0x04, 0x08, 0x02, 0x10,
	   0xf2, 0x13, 0xf2, 0x13, 0x02, 0x10, 0x04, 0x08, 0x04, 0x0c, 0x18, 0x1e,
	   0xe0, 0x39, 0x00, 0x70, 0x00, 0xe0, 0x00, 0xc0 }; 

Das eigentliche Bild ist unter dem Namen (xbm_icon) als Hex-Array nutzbar.

.. code-block:: c++

	displayDrawBitmap(x, y, image1Bit, width, hight, color);			// Draw 1Bit b&w bitmap image (MSB first) on e-paper display or TFT display
	getdisplay().drawXBitmap(x, y, imageXBitmap, width, height, color);	// Draw XBitmap image (LSB first) on e-paper display or TFT display

Für farbige Bilder mit 64.000 Farben nach dem RGB565-Standard kann folgende Funktion verwendet werden.

.. code-block:: c++

	drawRgb565Image(x, y, imageRGB565, width, height);    // Draw a RGB565 image (LSB first)
	createRgb565StripeImage(imageRGB565, width, height);  // Create a stripe image as test image (LSB first)


Spezialfunktionen
=================

Die Spezialfunktionen ermöglichen displayspezifische Aktionen, die je nach Displaytechnologie unterschiedlich behandelt werden müssen. Die Funktionen dienen zur Initialisierung der Displayfunktionen und werden zentral je nach verwendeten Displaytyps in ``obp60task.cpp`` und in OBP60Extensions.ccp aufgerufen. Die Befehle werden nicht im Code einer Anzeigeseite verwendet.

e-Paper-Display
---------------

.. code-block:: c++

	getdisplay().init(115200);      // Display init
	getdisplay().setRotation(0);    // Set display orientation
	getdisplay().powerOff();        // Activae StandBy mode
	getdisplay().fillScreen(color); // Clear screen or fill screen with a color

TFT-Display
-----------

.. code-block:: c++

	getpaneldisplay().init();               // Display init
	getpaneldisplay().setRotation(0);       // Set display orientation
	getpaneldisplay().powerSave(true);      // Activate power save mode
	getpaneldisplay().fillScreen(color);    // Clear screen or fill screen with a color
	getpaneldisplay().setPanelOffset(x, y); // Set panel offset for display 

Funktionen zur Display-Aktualisierung
-------------------------------------

Die Funktionen *displayFirstPage()* und *displayNextPage()* steuern die Aktualisierung der Displayinhalte und folgen einem seitenbasierten Renderkonzept, wie es bei e-Paper-Displays verwendet wird. Bei TFT-Farbdisplays erfolgt die Ausgabe normalerweise direkt durch Schreiben in den Framebuffer des Display-Controllers, sodass dieses Verfahren dort nicht zwingend erforderlich ist. Dennoch werden die Funktionen aus Kompatibilitätsgründen beibehalten.

Die Darstellung erfolgt in zwei Schritten: Zunächst werden mittels Grafikbefehlen die Bilddaten erzeugt. Anschließend übernimmt *displayNextPage()* die Übertragung dieser Daten in den Framebuffer und führt die eigentliche Aktualisierung des Bildschirms durch. Dieses Vorgehen ermöglicht eine standardisierte Darstellung von Displayinhalten für verschiedene Displaytypen und eine klare Trennung zwischen Rendering und Anzeigeaktualisierung.

Die Funktionen *displaySetFullWindow()* und *displaySetPartialWindow()* werden aus Kompatibilitätsgründen ebenfalls bei einem TFT-Display verwendet. Der Displayinhalt wird jedoch nicht aufgefrischt, da das bei TFT-Displays nicht notwendig ist. Die Befehle müssen aber trotzdem im Code einer Anzeigeseite verwendet werden, um ein identisches Anzeigeverhalten über alle Displaytypen hinweg zu ermöglichen.

.. code-block:: c++

	displayFirstPage();     // Show fist display content
	displayNextPage();      // Show next display content
	displaySetFullWindow(); // Full display refresh for e-paper display 
	displaySetPartialWindow(x, y, width, height); // Partial display refresh for e-paper display
