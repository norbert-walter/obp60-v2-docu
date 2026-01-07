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
