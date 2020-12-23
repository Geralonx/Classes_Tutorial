# Fortgeschrittenes Klassendesign

## Inhalt des Tutorials

- [Vorwort](#vorwort)
  - [Allgemein](#allgemein)
  - [Für wen ist dieses Tutorial geeignet?](#für-wen-ist-dieses-tutorial-geeignet?)
  - [Kritik](#kritik)
  - [Prerequisites / Vorraussetzungen](#prerequisites-/-vorraussetzungen)
  - [Source-Code und Kommentare](#source-code-und-kommentare)
  - [IDE](#ide)
  - [Disclaimer](#disclaimer)
  - [Korrektur meiner Aussage im ersten Tutorial](#korrektur-meiner-aussage-im-ersten-tutorial)

<br/>

---

## Vorwort

Das Tutorial beginnt im Ordner [Vorbereitende Erklärungen](https://github.com/Geralonx/Classes_Tutorial/tree/main/Vorbereitende_Erklaerungen)
und setzt sich anschließend in Kapitel 1-6 fort.

### Allgemein

So Leude, mein letztes Python-Tutorial ist schon 6 Monate her und inzwischen habe ich einerseits Lust ein neues zu machen und andererseits auch wieder einige Dinge gelernt, welche ich euch überhaupt zeigen könnte.

Der Textteil des Tutorials ist vollständig in deutsch gehalten. Es kann vorkommen, dass gewissen Codebeispiele englische Bezeichnungen enthalten. Dort fehlt es noch etwas an Konsistenz. Dies sollte aber kein Problem bezüglich dem Verständnis sein.

Warum mach ich das überhaupt? Ehrlich gesagt mache ich das weniger für Andere, als für mich selbst. Ich bin der Meinung, wenn man Anderen etwas richtig erklären kann, dann hat man es auch wirklich verstanden. Die Zeit, die ich hier rein investiere, ist in erster Line für mich selbst, um einerseits neue Dinge zu lernen und die Dinge anschließend zu festigen. Die Informationen, die ich für dieses Tutorial zusammentrage, stammen aus vielen Quellen und beispielsweise auch Videomaterial, welches mehrere Stunden beinhaltet. Ich fasse diese Informationen in einer Form zusammen, wie ich sie für sinnvoll und zusammenhängend halte. Für mich entsteht in diesem Prozess ein Dokument, welches die Wesentlichen Dinge zu dem Thema beinhaltet, um die gezeigten Inhalte zu verstehen und dies anschließend auf die nicht gezeigten Inhalte übertragen kann.

Andere Leute machen auch Tutorials und wahrscheinlich sogar deutlich besser als ich. Wer mit der Einstellung, "Warum sollte ich mir **DEIN** Tutorial durchlesen, wenn es andere/bessere gibt?", hierher kommt sollte einfach wieder gehen und sich eben die besseren Tutorials durchlesen und mich nicht mit sowas nerven. Für alle Anderen, die ernsthaft interessiert sind und mein erstes Tutorial sogar ganz gut fanden, stelle ich diese Tutorial Repo gerne zur Verfügung und bin im Anschluss auch für weitere Fragen/Disskussionen gerne da.

Bitte den [Disclaimer](#disclaimer) beachten.

---

### Für wen ist dieses Tutorial geeignet?

Dieses Tutorial geht schnell über Python-Grundlagen hinaus und befasst sich im Kern mit Klassen, deren speziellen Methoden ('Dunder'-Methods) und wie im Hintergund impliziete Prozesse bei der Definition und Instanziierung von Klassen durchgeführt werden. Wenn du nur wissen willst, wie man allgemein Klassen in Python schreibt und verwendet, dann wird dieses Tutorial nicht das richtige für dich sein.

David Beazley hat vor einigen jahren ein Tutorial über Metaprogrammierung gegeben, an welchem ich mich auch Teilweise bediene (wird aber alles auch referenziert), in dem er in 3 Stunden vorführt, wie man mit diesem Programmierstil über die Grenzen der normalen Vernwendung von Python hinaus geht.

> "It's basicly walking trough a class and it's like doing brain surgery on it. It's probably a really bad idea." \- David Beazley in [YouTube: Python 3 Metaprogramming](https://youtu.be/sPiWg5jSoZI)

<sub>(Am Ende 'hackt' er den import, sodass er Sourcecode über ein XML File direkt importieren kann. Ist ganz interesannt zu sehen, dass auch diese Kern-Machinery von Python offen zur Verfügung steht.)</sub>

<br/>

Wenn man einmal versteht, was bei den Prozessen der Erstellung, Initialisierung, Zugriff, Vererbung, etc. von Klassen stattfindet, dann kann man auch exakt an diesen Stellen seinen eigenen Eingriff vornehmen und den Prozess modifizieren. Da im Wesentlichen **alles** in Python ein Objekt ist, ist es möglich jedes Objekt so anzupassen, wie man es benötigt. Und das ganze auf einer Ebene, wo der Endbenutzer der Klassen gar nicht mehr mitbekommt, was im Hintergrund alles passiert.

Metaklassen sind eigentlich für 99% der Nutzer von Python unrelevant. Das benötigen hauptsächlich Framework/Libary Entwickler. Aber bis zu dem Kapitel soll dieses Tutorial allgemein die fortgeschrittene Vernwednung von Klassen beschreiben. Und das ist bestimmt für mehr als 1% der Leute interesannt.

---

### Kritik

Zuerst sei gesagt, ich habe die Kritikpunkte unter dem letzten Tutorial alle gelesen und ich möchte mich auch daran halten. Ersteinmal habe ich mich für dieses Tutorial entschieden nur einen Info-Post zu erstellen und das Tutorial selbst auf GitHub zu halten. Dort gibt es auch alle Erklärungen mit Beispielcode, welcher in meinen Augen auch sehr detailliert Komentiert ist.

Insgesamt wird dieses Tutorial in mehreren Kapiteln und Unterordnern sortiert sein. Es ist insgesamt sehr groß geworden aber in meinen Augen ist in diesem Tutorial ein sehr großer Teil bezüglich Klassen und Design in Python abgedeckt.

---

### Prerequisites / Vorraussetzungen

Um die gezeigten Inhalte zu verstehen solltet ihr bereits die Grundlagen von Python kennen. Dazu gehört allgemein die Syntax, wie man Funktionen und Klassen erstellt und eventuell soagr, dass **alles** in Python Objekte sind. Klassen sind Objekte, Funktionen sind Objekte, selbst eine int/float/str/list/... - Variable ist nur ein Objekt einer bestimmten Klasse. Des Weiteren solltet ihr auch ungefähr wissen was Vererbungen/Inheritance sind. Ich werde es nochmal im Detail erklären, dennoch geht es auch bei dem Thema eher um die Tiefe statt die einfache Anwendung. Dictionarys! In Python findet man überall Dictonarys, weswegen es essentiell ist, dass ihr diese im Vorfeld kennt und wisst was man damit machen kann. (dict.keys(), dict.values(), dict.items(), Dicts sind mutable Objekte...) Die letzte Vorraussetzung sind dann noch 'Closures / Decorators', welche ich bereits in meinem ersten 'Tutorial' erklärt habe (Link im Kommentar).

---

### Source-Code und Kommentare

Für jedes gezeigte Beispiel im Text gibt es ein entsprechendes File, auf das auch verlinkt wird. Source-Code-Files die mit einem \_E beginnen sind zusätzliche Beispiele, die nicht im Tutorial-Text vorkommen.

Um den Fließtext im Tutorial möglichst kompakt zu halten habe ich dort auf einfache Kommentare verzichtet, aber in den Source-Code-Files sind immer Kommentare vorhanden.Auch wenn dieses Tutorial sich nicht primär an Anfänger richtet und ich auch in den Vorraussetzungen geschrieben habe, dass dies für Leute gedacht ist, die die Grundlagen von Klassen bereits kennen habe ich mich dazu entschieden, für dieses Tutorial alles zu kommentieren, egal wie lächerlich einfach/übertrieben/offensichtlich es ist. Damit bnekommen auch unerfahrene die Chance dies zu lesen und zu verstehen.

DIE BEISPIELE DIENEN LEDIGLICH ZUR ERKLÄRUNG DER ABLÄUFE UND PROZESSE IN PYTHON. ICH SPRECHE KEINE ALLGEMEINE EMPFEHLUNG AUS, DIE GEZEIGTEN BEISPIELE IN GENAU DIESER FORM ANZUWENDEN.

### IDE

Da es in dem ersten Beitrag auch zur Sprache kam erwähne ich es hier nochmal explizit, ich arbeite vollständig mit VSCode und habe mir diese IDE inwzischen schon recht stark Modifiziert. Color-Themes, Boilerplates/Snippets, indentation und bracket Colors, Autoformatting und ein paar Andere. Für einige ist es sicher zu bunt, mir gefällts halt.

---

### Disclaimer

Jeder macht Fehler. Ich beanspruche keineswegs Vollständig- oder Richtigkeit der hier gezeigten Inhalte. Für weitere Details und noch tiefergehende Informationen empfehle ich grundsätzlich die [Python-Dokumentation](https://docs.python.org/3/).

Ich möchte mit diesem 'Tutorial' einen tieferen Einblick in die elementaren Dinge von Python vermitteln. Auch ich habe währen des Schreibens viel nachlesen und recherchieren müssen. Ich biete hiermit lediglich eine zusammengefasste Form der Informationen an, welche ich auf eine Weise darstellen möchte, wie ich sie für logisch und verständlich halte.

Diese Zusammenfassung/Tutorial soll eigenständig sein. Ich habe Informationen auch für gleiche Themen aus verschiedenen Quellen zusammengetragen, wodurch dieses gesamte Tutorial sehr groß geworden ist. Vielleicht bin ich auch einfach zu doof, um Kurzfassungen zu verstehen, aber dieses Tutorial ist in einer Form wo ich denke, dass dies alles enthält, ohne dass man in 10 verschiedene Quellen gucken muss, um eine einzige Sache zu verstehen.

---

### Korrektur meiner Aussage im ersten Tutorial

In meinem ersten Tutortial über Clousers und Decorators habe ich gesagt, dass man \*args und \*\*kwargs nicht umbenennen sollte und immer als \*args und \*\*kwargs verwenden sollte, auch wenn Python nur auf die Sternchen achtet und die Bezeichner frei wählbar sind. Ich bin bei meinen Recherchen auch darauf gestoßen, dass es sogar von Core-Developern empfohlen wird die Bezeichner umzubennenen, wenn dies das Verständnis vereinfacht. Wenn die \*args für den Input für eine bestimmte Gruppe an Daten verwendet wird und das \* nur dafür genutzt wird, dass man eine beliebige Anzahl von Argumenten übergeben kann, dann kann es ja hilfreich sein, den Bezeichner genau zu bennenen.

Beispiel:

```py
def summe(*args):
    summe = 0
    for zahl in args:
        summe += zahl
    return summe

# Das sollte man in folgende Form ändern, da diese Funktion im wesentlich eine
# belibige Anzahl von Zahlen erwartet und nicht eine belibige Anzahl von belibigen Argumenten:
def summe(*zahlen):
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe
```
