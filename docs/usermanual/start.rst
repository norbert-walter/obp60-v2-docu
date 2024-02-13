Inbetriebnahme
==============

In diesem Abschnitt wird erklärt wie eine Erstinbetriebnahme eines OBP60 erfolgt. Die Erstinbetriebnahme kann am einfachsten vorgenommen werden, wenn das Gerät noch nicht im Boot eingebaut ist. Dazu wird das Gerät mit Strom versorgt und die ersten Einstellungen vorgenommen. So können sie die Funktionalität testen, bevor sie das Gerät im Boot einbauen.

Schutzkonzept
-------------

Das OBP60 verfügt über ein mehrstufiges Schutzkonzept. Das soll verhindern, dass sich Störungen im Versorgungsnetz und auf den Datenleitungen im System ausbreiten. Damit wird sichergestellt, dass das OBP60 trotz Störungen nicht komplett ausfällt und in wichtigen Teilen weitesgehend funktionsfähig bleibt. Um dies zu erreichen, sind die Busssysteme:

* NMEA2000
* NMEA0182
* I2C

vom Bordsnetz isoliert aufgebaut.

.. image:: ../pics/Safety_Concept.png
             :scale: 45%

Abb.: Sicherheitskonzept

Im OBP60 ist dazu eine zusätzliche 5V-Stromversorgung enthalten, die die isolierten Schaltungsteile versorgt. Die zusätzliche Stromversorgung hat die Ausgänge ``+5Viso`` und ``GND2``, die am Steckverbinder CN1 und CN2 anliegen. Darüber können auch externe Schaltungen bis 200 mA versorgt werden.

.. warning::
	Verbinden sie die unterschiedlichen Massepotenziale ``GNDS``, ``GND``, ``GND2`` und ``Shield`` niemals miteinander! Dadurch geht die Isolations- und Schutzwirkung verloren. Die Massepotenziale dürfen nicht gleichberechtigt verwendet werden.
	
.. image:: ../pics/Safe_Areas.png
             :scale: 45%

Abb.: Sichere Bereiche

Stromversorgung
---------------

Die Stromversorgung des OBP60 erfolgt über den Steckverbinder CN2. Beim Zuschalten der Versorgungsspannung schaltet sich das OBP60 automatisch ein. Es gibt keinen gesonderten Ein- oder Ausschaltknopf am Gerät. Benutzen sie für die Stromversorgung die Anschlüsse ``+12V`` und ``GNDS``. Dabei wird ``+12V`` mit dem positiven Pol der Batterie verbunden und ``GNDS`` mit dem negativen Pol. Die beiden Anschlüsse der Stromversorgung sind:

* verpolungssicher
* kurzschlussfest
* überspannungssicher
* ESD-geschützt

Der zulässige Spannungsbereich liegt zwischen 10V...28V. Das OBP60 kann in 12V als auch in 24V Bord-Versorgungsnetzen verwendet werden. Bei Spannungen größer 28V wird die interne Sicherung im Gerät ausgelöst.

.. note::
	Im Gerät ist eine selbtsrückstellende Sicherung verbaut, die bei zu hohem Stromverbrauch die Versorgungsspannung selbständig trennt. Sie können die Sicherung zurücksetzen, indem sie die Stromversorgung zum OBP60 trennen und den Grund des übermäßigen Stromverbrauchs beseitigen. Danach warten sie ein paar Minuten und schalten dann die Versorgungsspannung wieder zu.

.. important::
	Die bereitgestellte Stromversorgung des OBP60 sollte im Bordnetz mit einer zusätzlichen Sicherung von mindestens 5A abgesichert werden. Das erfolgt typischer Weise durch das Board-Panel worüber die Stromkreise im Boot zugeschaltet werden können. So vermeiden sie Brände bei aufgescheuerten Versorgungsleitungen im Boot. Die interen Sicherung im OBP60 schützt nur das Gerät und nicht die Versorgungsleitungen!

	
