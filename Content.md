# Inhalt des Tutorials

- Vorwort
- Kapitel 1 fortgeschrittenes Klassen-Design
- Kapitel 2 Klassendekoratoren
- Whatever
- Metaklassen
  <br/><br/>

## Vorwort

### Allgemein

So Leude, mein letztes Python-Tutorial ist schon 5 Monate her und inzwischen habe ich einerseits Lust ein neues zu machen und andererseits auch wieder ein paar Dinge gelernt, welche ich euch überhaupt zeigen könnte.
<br/><br/>

### Kritik

Zuerst sei gesagt, ich habe die Kritikpunkte unter dem letzten Tutorial alle
gelesen und ich möchte mich auch daran halten. Ersteinmal habe ich in diesem Post auf die Farben verzichtet. Als zweites habe ich das ganze Tutorial auf GitHub gepackt, mit Code, mit Kommentaren und weiteren Texten, welche detaillierter auf die Inhalte eingehen.

Insagesamt wird dieses Tutorial auf mehrere Beiträge gesplitted, einfach weil
das Thema zu groß ist, ja, sogar wenn ich die maximale Größe eines Bildes hier
ausnutzen würde, würde ein Beitrag nicht reichen. Außerdem möchte ich die
einzelnen Beiträge kürzer halten.
<br/><br/>

### Hater

Für die, die sagten pr0 sei nicht die Plattform für sowas, bitte Minus geben und weiterziehn.
<br/><br/>

### Prerequisites / Vorraussetzungen

Um die gezeigten Inhalte zu verstehen solltet ihr bereits die Grundlagen von Python kennen. Dazu gehört allgemein die Syntax, ihr solltet wissen, wie man
Funktionen und Klassen erstellt und eventuell soagr, dass alle Funktionen sogenannte 'First-Class-Objects' sind. Des Weiteren solltet ihr auch ungefähr
wissen, wie Vererbungen/Inheritance funktionieren. Die letzte Vorraussetzung
sind dann noch 'Closures / Decorators', welche ich bereits in meinem ersten
'Tutorial' erklärt habe (Link im Kommentar).
<br/><br/><br/>

## Kapitel 1: Fortgeschrittenes Klassen-Design

<br/>

### 1.0 Recap Klassen

Wie, wo, wann und warum man Klassen verwenden sollte möchte ich hier gar Nicht disskutieren. Auch werde ich keine Vergleiche oder Ratschläge über unterschiedliche Programmierstyles geben. Es gibt [PEP8](https://www.python.org/dev/peps/pep-0008/), es gibt eine [Vorlage von Google](https://google.github.io/styleguide/pyguide.html), aber selbst Raymond Hettinger sagte in seinem Vortrag:

> "PEP8 is not a weapon for beating other people in the head. It's a stlye
> guide, a guide, not a lawbook." - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

und

> "Isn't it great, when you write code that is PEP8 compliant and out of a room of 500 people one person can figure it out?" - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/) ist meiner Meinung nach die beste Formulierung für clean code.

Ich sebst verwende Klassen auch manchmal, wo der ein oder andere sicherlich sagen würde, dass die dort überflüssig seien. Der Hauptgrund warum ich Klasse überhaupt verwende ist 'Encapsulation'. Das heißt so viel wie, dass die Daten und die Methoden, welche jene Daten modifizieren einfach zusammengepackt werden, damit eine eineindeutiger Zusammenhang besteht.

Die einzige Regel die auch ich grundsätzlich beachte ist aus folgendem Zitat abzuleiten. (Das heißt natürlich nicht, dass man sofort ab 2 zugehörigen Methoden und init eine Klasse schreiben sollte, aber ich denke ihr versteht den Punkt.)

> "The signature of 'this should't be a class' is, that it has two methods one of which is
> init. Any time you see that, you should probably think 'hey, maybe I just need one method'."
> \- Jack Diederich in [YoutTube: Stop Writing Classes](https://youtu.be/o9pEzgHorH0)

<br/>

### 1.1 'Dunder'-Methods

Um das Klassendesign im fortgeschrittenen Stil zu verstehen möchte ich bei den
'Dunder'- oder 'Magic'-Methods anfangen. (Dunder steht für 'Double Underscores'). Diese speziellen Methoden erfüllen einzigartige Aufgaben, welche durch die allgemeine Syntax und die 'Built-In' Methods abgerufen/angefragt werden können.

#### 1.1.1 Allgemein

Jeder der in Python bereits eine Klasse geschrieben hat wird mindestens die

```py
def __init__(self, args):
```

verwendet haben. 'Dunder'-Methods sind Methoden, welche **nicht** direkt über ihre Bezeichnung aufgerufen, sondern über die Syntax oder andere 'Built-In' Methods von Python.
<br/>

Beispiel: Die 'Dunder'-Method \_\_len\_\_(self) wird über die 'Built-In' Method
len() aufgerufen. Was diese \_\_len\_\_(self) Methode am Ende durchführt ist
komplett euch überlassen. Die einzige Vorraussetzung ist, dass diese Methode
einen Integer >=0 zurück gibt. Bevor ihr die Vorraussetzung erfüllt, könnt ihr
ausführen, berechnen und hacken was ihr wollt, solange die Vorrausetzung erfüllt wird, ist alles in Ordnung mit der Implementation.

Sobald man aber in dieses Thema des fortgeschrittenen Designs kommt ist man mindestens an einem Punkt, wo man den Code wiederverwenden will, wenn nicht sogar für Andere bereitstellen muss/möchte. Also sollte man sich fragen, was würde jemand anderes bei der Verwendung einer 'Dunder'-Method eigentlich erwarten? Bzw. warum sollte man diese Methode überhaupt anwenden.

<sub>(Randnotiz: \_\_len\_\_(self) ist übrigens die Falback-Methode für \_\_bool\_\_(self). Das heißt, wenn keine Dunder-Bool-Method definiert ist wird die Dunder-Len-Method verwendet. Alles was >0 ist entspricht dann eben True)</sub>
<br/>

Für Vergleiche oder arithmetische Operationen gilt das Gleiche.

```py
def __add__(self, other):
# -> instance1 + instance2
# -> instance1.__add__(instance2)

def __sub__(self, other):
# -> instance1 - instance2
# -> instance1.__sub__(instance2)
...
```

Ich selbst hatte keine Idee, wie man eine allgemeine Zusammenfassung für die 'Dunder'-Methods formulieren könnte. Das hat jemand anderes aber sehr gut hinbekommen.

> A dunder method is an implicit function, that is being called behind the
> scenes of an explicit operation or a function. \- Iakshayarora7 (https://www.djangospin.com/python-dunder-methods-attributes/)

Python-Dokumentation über (alle?) Special 'Dunder' Methods:
https://docs.python.org/3/reference/datamodel.html#special-method-names

<br/>

#### 1.2.2 \_\_repr\_\_() oder \_\_str\_\_() ?

Wenn man gute und ausgereifte Klassen designen will, dann sollte man auf diese beiden 'Dunder'-Methods nicht verzichten. Sie können in jeder Klasse ihren Platz finden, da sie Informationen enthalten, welche den Inhalt der Klasse beschreiben soll. Der Unterschied ist nicht sehr einfach zu erklären. Im Internet kursieren verschiedene Erklärungen, welche sich manchmal stark voneinenader Unterscheid.

<br/>
__str__(self)

Die Dunder-str-Method ist dazu gedacht, eine Darstellung des Objekts zurückzugeben, welche für den Benutzer einfach zu lesen und zu verstehen ist. Sie muss einen String zurückgeben.

Kleines Beispiel:

```py
 class PC:
     def __init__(self, prozessor, grafikkarte):
        self.prozessor = prozessor
        self.grafikkarte = grafikkarte

    def __str__(self):
        msg = ""
        msg += f"\nDiese Instanz ist von der Klasse: {self.__class__.__name__}"
        msg += f"\nSie hat folgende Attribute:"

        for key, value in self.__dict__.items():
            msg += f"\n\t{key}: \t{value} \t| ({type(value)})"

        return msg

MeinPc = PC('Ryzen 7', 'RTX2070Super')
print(MeinPc)
```

Ausgabe:

<pre>
> Diese Instanz ist von der Klasse: PC
> Sie hat folgende Attribute:
>        prozessor:      Ryzen 7         | (class 'str')
>        grafikkarte:    RTX2070Super    | (class 'str')
</pre>

<sub>Eigentlich wird die der Type mit den <> dargestellt (<class 'str'>). Aufgrund der verwendeten Markuplanguage (.md) funktioniert das da nicht.</sub>

<br/>
__repr__(self)

<br/><br/><br/>
Das \_\_dict\_\_ einer Instanz enthält **ausschließlich** die Attribute, welche nur innerhallb der Instanz gültig sind. Wohingegen der Aufruf von dir(instance) \_\_dir\_\_ einer Instanz die Attribute **UND** die

<pre>
>
>
>
>
</pre>
