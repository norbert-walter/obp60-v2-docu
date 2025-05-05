Fragen und Antworten
====================

**Warum flackert der Bildschirm in regelmäßigen Abständen?**

	Das Flackern des Bildschirmes dienst zum Auffrischen des Bildschirminhaltes. In regelmäßigen Abständen muss das Display den Bildschirminhalt durch einen Voll-Refresh komplett erneuern, um Geisterbilder zu entfernen und den Kontrast aufzufrischen. Dazu wird der Bildinhalt invertiert, mehrmals gelöscht und wieder vollständig aufgebaut.

**Wie kann ich das flackern des Bildschirms reduzieren?**

	Die Zeitpunkt eines Voll-Refreshes hängt von einigen Faktoren ab. In den ersten 5 Minuten nach einem Neustart des Gerätes erfolgt jede Minute ein Voll-Refresh, um eine Temperaturanpassung des Displays aus einem kalten Zustand heraus zu ermöglichen. Nach jedem Seitenwechsel wird ebenfalls ein Voll-Refresh ausgeführt. Das gilt für die Seite die zu letzt aufgerufen wurde und die mindestens 4s lang angezeigt wird. Dieses Verhalten bei Seitenwechsel lässt sich über den Parameter **Refresh** abstellen. Das ist aber mit dem Nachteil verbunden, dass sich Geisterbilder alter Seiten nicht vollständig entfernen lassen. Zusätzlich lässt sich festlegen in welchen Intervallen ein Voll-Refresh generell ausgeführt wird. Die Zykluszeit kann im Bereich von 1...10 min über den Parameter **Full Refresh Time** eingestellt werden. Der Voll-Refresh lässt sich zusätzlich über den Parameter **Fast Refresh** beschleunigen. Dann laufen die Voll-Refreshes schneller ab. Die Beschreibungen zu den Refresh-Einstellungen finden Sie im Kapitel :ref:`Config - OBP Display`. Die Einstellungen zum Bildschirm-Refresh haben auch Auswirkungen auf den Bildschirmkontrast unter Sonneneinwirkung.

**Warum verblasst das Display unter Sonneneinwirkung?**

	Bei extremer Sonneneinwirkung erhitzt sich das e-Paper-Display auf und verursacht einen Kontrastverlust bei der partiellen Bildschirmaktualisierung. Das Bild wird zunehmend grau und es entstehen einige Streifen im Display. Das Display ist nicht defekt. Der Zustand lässt sich durch einen Voll-Refresh beseitigen.

**Was kann man dagegen tun?**

	Der Effekt kann reduziert werden, indem direkte Sonnenstrahlung auf das Display vermieden wird. Eine andere Möglichkeit zur Verbesserung besteht darin, die Voll-Refreshes in kürzeren Zyklen ausführen zu lassen. Im Kapitel :ref:`Config - OBP Display` finden Sie eine Tabelle zu sinnvollen Einstellungen unter verschiedenen Bedingungen. Auch der Stromverbrauch des Gerätes hat einen Einfluss auf den Kontrastverlust, da die Verlustwärme im Gerät ebenfalls zur Temperaturerhöhung beiträgt.

**Welche Möglichkeiten bestehen den Stromverbrauch zu reduzieren?**

	Der Stromverbrauch lässt sich reduzieren, indem der Access Point standardmäßig nach einer vorgegebenen Zeit abgeschaltet wird. Zusätzlich kann der Prozessortakt reduziert werden. Einige Geräte wie das OBP60 verfügen über spezielle Stromsparfunktionen über den Parameter **Power Mode**. Details zu Stromsparfunktionen finden Sie im Kapitel :ref:`Config - OBP Hardware`.
	

**Warum startet mein OBP60 nicht, wenn ich die Spannung zuschalte?**

	Das Problem liegt am Softstart-Verhalten des StepDown- Wandler, der die 12V Versorgungsspannung in eine 5V-Gerätespannung umwandelt. Die Zeitdauer des Softstarts ist auf 5 ms begrenzt. Beim Start wird kurzzeitig recht viel Strom gezogen, weil die internen Kondensatoren geladen werden. Ist der Leitungswiderstand zu groß, läuft der Startprozess nicht schnell genug ab und der StepDown-Wandler startet nicht. Er hängt dann in einem undefinierten Zustand und kommt aus diesem Zustand nicht mehr heraus. Empfehlenswert sind für Stromversorgungskabel Leiterquerschnitte von 0,5...0,75 mm2. Das Kabel sollte direkt an der Schalttafel angeschlossen sein und so kurz wie möglich sein und keine weiteren Abgänge haben. Überlängen des Kabels hinter der Verkleidung sollten vermieden werden. Ebenso das abgreifen von Strom an anderen Geräten. Hilfsweise kann man hinten am 12V-Eingang einen Elektrolytkondensator von ca. 470...1000 uF parallel anschließen. Damit sollte sich das Problem reduzieren lassen.

**Warum funktionieren WiFi-Verbindungen nicht richtig?**

	WiFi-Verbindungen sind auf das 2,4 GHz Frequenzband begrenzt. Andere Teilnehmer außerhalb des eigenen Access Point nutzen das selbe Frequenzband und müssen sich die Bandbreite mit anderen Teilnehmern teilen. In größeren Häfen kann es dazu kommen, dass die Bandbreite aller Kanäle durch zu viele Teilnehmer ausgelastet ist. In diesem Fall kommt es zu Verzögerungen bei der Datenübertragung. Sie müssen dann mit einem trägen Ansprechverhalten der Messdaten im Display rechnen, wenn die Daten über WiFi-Verbindungen übertragen werden. Leitungsgebundene Datenübertragungen aus Bussystemen wie NMEA2000 oder NMEA0183 sind davon nicht betroffen. Etwas Abhilfe kann die Auswahl der Übertagungskanäle Kanäle 1 und 13 bewirken, da sie sich an den Rändern des 2,4 GHz Frequenzbereiches befinden und nur einen Nachbarkanal haben.
	
	.. image:: ../pics/WiFi_Channels.png
             :scale: 35%

**Das GPS bekommt beim OBP60 keinen Fix. Was kann ich tun?**

	Beim OBP60 befindet sich die GPS-Antenne auf der Rückseite des Displays. Sind direkt hinter dem Display Metallteile oder Metallflächen, so kann der GPS-Empfang behindert oder unmöglich sein. Sorgen Sie dafür, dass sich keine größeren Metallteile oder Metallflächen hinter dem Display befinden. Kann der Empfang nicht verbessert werden, so besteht die Möglichkeit eine externe GPS-Antenne zu verwenden. Sie sollten die GPS-Antenne möglichst an einer Stelle positionieren, bei der die Antenne freie Sicht zum Himmel hat. Damit erzielen Sie die beste GPS-Empfangsleistung und hohe Positionsgenauigkeiten. In einigen Fällen verursachen Stromversorgungsgeräte mit Schaltreglern wie z.B. bei LED-Beleuchtungen unzulässige Störungen, die sich auf die Empfangsleistung von GPS-Signalen auswirken können. Versuchen Sie in solchen Fällen systematisch die Störquelle zu ermitteln, indem sie Geräte zu- und abschalten und die Auswirkungen auf die GPS-Empfangsqualität beobachten. 