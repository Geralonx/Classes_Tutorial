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

verwendet haben.
