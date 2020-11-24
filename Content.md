# Inhalt des Tutorials

- Vorwort
- Kapitel 1 fortgeschrittene Klassen
- Kapitel 2 Klassendekoratoren
- Whatever
- Metaklassen

## Vorwort

### Allgemein

So Leude, mein letztes Python-Tutorial ist schon 5 Monate her und inzwischen habe
ich einerseits Lust ein neues zu machen und andererseits auch wieder ein paar
Dinge gelernt, welche ich euch überhaupt zeigen könnte.

### Kritik

Zuerst sei gesagt, ich habe die Kritikpunkte unter dem letzten Tutorial alle
gelesen und ich möchte mich auch daran halten. Ersteinmal habe ich in diesem Post
auf die Farben verzichtet. Als zweites habe ich das ganze Tutorial auf GitHub
gepackt, mit Code, mit Kommentaren und weiteren Texten, welche detaillierter
auf die Inhalte eingehen.

Insagesamt wird dieses Tutorial auf mehrere Beiträge gesplitted, einfach weil
das Thema zu groß ist, ja, sogar wenn ich die maximale Größe eines Bildes hier
ausnutzen würde, würde ein Beitrag nicht reichen. Außerdem möchte ich die
einzelnen Beiträge kürzer halten.

### Hater

Für die, die sagten pr0 sei nicht die Plattform für sowas, bitte Minus geben und
weiterziehn.

### Prerequisites / Vorraussetzungen

Um die gezeigten Inhalte zu verstehen solltet ihr bereits die Grundlagen von
Python kennen. Dazu gehört allgemein die Syntax, ihr solltet wissen, wie man
Funktionen und Klassen erstellt und eventuell soagr, dass alle Funktionen
sogenannte 'First-Class-Objects' sind. Des Weiteren solltet ihr auch ungefähr
wissen, wie Vererbungen/Inheritance funktionieren. Die letzte Vorraussetzung
sind dann noch 'Closures / Decorators', welche ich bereits in meinem ersten
'Tutorial' erklärt habe (Link im Kommentar).

## Kapitel 1: Fortgeschrittene Klassen

Um das Klassendesign im fortgeschrittenen Stil zu verstehen möchte ich bei den
'Dunder'- oder 'Magic'-Methods anfangen.(Dunder steht für 'Double Underscores').
Jeder der in Python bereits eine Klasse geschrieben hat wird mindestens die

\_\_init\_\_(self, ...)

verwendet haben. 'Dunder'-Methods sind Methoden, welche **nicht** direkt über ihre
Bezeichnung aufgerufen, sondern über die Syntax oder andere 'Built-In' Methoden
von Python.

Beispiel: Die 'Dunder'-Method \_\_len\_\_(self) wird über die 'Built-In' Method
len() aufgerufen. Was diese \_\_len\_\_(self) Methode am Ende durchführt ist
komplett euch überlassen. Die einzige Vorraussetzung ist, dass diese Methode
einen Integer >=0 zürkgibt. Bevor ihr die Vorraussetzung erfüllt, könnt ihr
ausführen, berechnen und hacken was ihr wollt, solange die Vorrausetzung erfüllt
wird, ist alles in Ordnung mit der Implementation. Sobald man aber in dieses
Thema des fortgeschrittenen Designs kommt ist man mindestens an einem Punkt, wo
man den Code wiederverwenden will, wenn nicht sogar für Andere bereitstellen
muss/möchte. Also sollte man sich fragen, was würde jemand anderes bei der
Verwendung einer 'Dunder'-Method eigentlich erwarten? Bzw. warum sollte man
diese Methode überhaupt anwenden. \_\_len\_\_(self) ist nur ein Beispiel.

Für Vergleiche oder arithmetische Operationen gilt das Gleiche.
\_\_add\_\_(self, other): # instance1 + instance2 -> instance1.\_\_add\_\_(instance2)
\_\_sub\_\_(self, other): # instance1 - instance2 -> instance1.\_\_sub\_\_(instance2)
