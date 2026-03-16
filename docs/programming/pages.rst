Seitenerstellung
================

Um eine neue Seite zu erstellen sind folgende Schritte notwendig:

	1. Anlegen einer neuen Seite unter ``lib\obp60task\PageXXXX.cpp``
	2. Registrierung der Seite in ``lib\obp60task\obp60task.cpp``. Dazu die Funktion ``registerAllPages`` entsprechend erweitern
	3. In ``/lib/obp60task/config.json`` die neue Seite in die jeweiligen Seitenlisten aufnehmen oder Seite in ``/lib/obp60task/gen_set.py`` aufnehmen und damit den relevanten Teil der Datei ``/lib/obp60task/config.json`` neu erzeugen. 

Als Vorlage für eine neue Seite kann z.B. die vorhandene Seite *PageWhite* verwendet werden. Sie enthält nur minimalen Code. In der kopierten Seite ist dann lediglich der Text *White* durch *Beispiel* zu ersetzen.

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

Darstellung grafischer Inhalte
==============================

Auf dem Display lassen sich sowohl textbasierte als auch grafische Elemente platzieren. Die Grundlage für diese Operationen wird durch die GFX-Grafik-Lib bereitgestellt. Die Bibliothek wurde von Adafruit initiiert, um verschiedenste Grafikdisplays mit einem einheitlichen Befehlssatz ansprechen zu können. Viele Treiber-Hersteller für Displays orientieren sich an der Lib und haben eigene Adaptionen vorgenommen, die in weiten Teilen mit dem Befehlssatz identisch sind. Für das e-Paper-Display gibt es aber einige Einschränkungen und es stehen nicht alle Befehle der Adafruit-GFX-Lib zur Verfügung.

In diesem `PDF-Dokument <../_static/files/adafruit-gfx-graphics-library.pdf>`_ können die grundlegenden Befehle der Adafruit-GFX-Lib eingesehen werden. Darüber hinausgehend können Sie den kompletten Funktionsumfang der Lib als `Klassen Referenz`_ hier online abrufen.

.. _Klassen Referenz: https://adafruit.github.io/Adafruit-GFX-Library/html/class_adafruit___g_f_x.html

Das Koordinatensystem des Grafikdisplays ist so organisiert, dass sich in der linken oberen Ecke der Nullpunkt befindet. Alle Koordinatenangaben beziehen sich auf diesen Ursprung. Im Projekt wird die Hilfsfunktion getdisplay() verwendet, in die alle GFX-Befehle eingebettet sind.

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

Abb.: Platzierung einer Linie

Viereck
-------

.. code-block:: c++

	getdisplay().drawRect(x0, y0, width, hight, color);	// Draw rect
	getdisplay().fillRect(x0, y0, width, hight, color);	// Draw filled rect

.. image:: /pics/Draw_Rect.png
             :scale: 80%

Abb.: Platzierung eines Vierecks

Viereck gerundet
----------------

Diese Funktion kann sehr gut zum Zeichen von Bedienknöpfen verwendet werden.

.. code-block:: c++

	getdisplay().drawRoundRect(x0, y0, width, hight, radius, color);	// Draw round rect
	getdisplay().fillRoundRect(x0, y0, width, hight, radius, color);	// Draw filled round rect

.. image:: /pics/Draw_RoundRect.png
             :scale: 80%

Abb.: Platzierung eines Vierecks mit runden Ecken


Dreieck
-------

.. code-block:: c++

	getdisplay().drawTriangle(x0, y0, x1, y1, x2, y2, color);	// Draw triangle
	getdisplay().fillTriangle(x0, y0, x1, y1, x2, y2, color);	// Draw filled triangle

.. image:: /pics/Draw_Triangle.png
             :scale: 80%

Abb.: Platzierung eines Dreiecks

Kreis
-----

.. code-block:: c++

	getdisplay().drawCircle(x0, y0, radius, color); // Draw circle
	getdisplay().fillCircle(x0, y0, radius, color); // Draw filled circle

.. image:: /pics/Draw_Circle.png
             :scale: 80%
			 
Abb.: Platzierung eines Kreises

Bild
----

Mit dem nachfolgenden Befehl können Bilder als 1Bit-Scharz/Weiß-Bilder angezeigt werden. Über den Parameter color kann die Farbe des aktiven Pixels festgelegt werden. Bei einem e-Paper-Display ist das Schwarz oder Weiß und bei einem TFT-Display eine beliebige Farbe. Somit ist es möglich, auch reine Scharz/Weiß-Bilder auf einem Farbdisplay darzustellen.

Bevor Sie Bilder nutzen können, müssen die Bilder in eine C-compatible Schreibweise umgewandelt werden. Mit folgenden Tools ist das möglich:

	* **Image2LCD** - 1Bit-Bild (C-Code)
		* Scan mode: Einzustellen auf Horizontal
		* Bit order: Einstellen auf MSB first
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

Die Spezialfunktionen ermöglichen displayspezifische Aktionen, die je nach Displaytechnologie unterschiedlich behandelt werden müssen.

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

.. code-block:: c++

	displayFirstPage();     // Show fist display content
	displayNextPage();      // Show next display content
	displaySetFullWindow(); // Full display refresh for e-paper display 
	displaySetPartialWindow(x, y, width, height); // Partial display refresh for e-paper display
