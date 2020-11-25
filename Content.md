# Inhalt des Tutorials

- Vorwort
- Kapitel 1 Fortgeschrittenes (Klassen) Design
- Kapitel 2 Spezielle Funktionsdekoratoren für Klassen
- Kapitel 3 Klassendekoratoren
- Kapitel 4 Metaklassen
  <br/><br/>

## Vorwort

### Allgemein

So Leude, mein letztes Python-Tutorial ist schon 5 Monate her und inzwischen habe ich einerseits Lust ein neues zu machen und andererseits auch wieder ein einige Dinge gelernt, welche ich euch überhaupt zeigen könnte.
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
Funktionen und Klassen erstellt und eventuell soagr, dass alles in Python Objekte sind. Klassen sind Objekte, Funktionen sind Objekte, selbst eine Variable ist nur ein Objekt einer bestimmten Klasse. Des Weiteren solltet ihr auch ungefähr
wissen, wie Vererbungen/Inheritance funktionieren. Die letzte Vorraussetzung
sind dann noch 'Closures / Decorators', welche ich bereits in meinem ersten
'Tutorial' erklärt habe (Link im Kommentar).
<br/><br/>

### Disclaimer

Jeder macht Fehler. Ich beanspruche keineswegs Vollständig- oder Richtigkeit der hier gezeigten Inhalte. Für weitere Details und noch tiefergehende Informationen empfehle ich grundsätzlich die [Python-Dokumentation](https://docs.python.org/3/).

Ich möchte mit diesem 'Tutorial' einen tieferen Einblick in die elementaren Dinge von Python vermitteln. Auch ich habe währen des Schreibens viel nachlesen und recherchieren müssen. Ich biete hiermit lediglich eine zusammengefasste Form der Informationen an, welche ich auf eine Weise darstellen möchte, wie ich sie mir bei Tutorials von Anderen selbst gewünscht hätte.
<br/><br/><br/>

## Kapitel 1: Fortgeschrittenes (Klassen) Design

### 1.0 Style-Guides

Ich möchte am Anfang einmal auf die Style-Guides und ein paar Zitate/Aussagen von Python-Core-Developer hinweisen. Ich möchte bezüglich dem Styling keine Ratschläge geben oder verschiedene Guides vergleichen. Es gibt [PEP8](https://www.python.org/dev/peps/pep-0008/), es gibt eine [Vorlage von Google](https://google.github.io/styleguide/pyguide.html) und sicherlich noch andere, aber selbst Raymond Hettinger sagte in seinem Vortrag:

> "PEP8 is not a weapon for beating other people in the head. It's a stlye
> guide, a guide, not a lawbook." - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

und

> "Isn't it great, when you write code that is PEP8 compliant and out of a room of 500 people one person can figure it out?" - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

Im Vortrag weist er mit diesen Aussagen darauf hin, dass man die Qualität von Code nicht nach dem Grad der Übereinstimmung von PEP8 bestimmen sollte, sondern ein bisschen weiter denken muss, um den nächsten Lesern das Leben zu vereinfachen. PEP8 hat nicht zu Allem eine Antwort, das wäre unmöglich, deswegen sollte man sich selbst Gedanken machen, wie man seinen Stil im Coden so umsetzt, dass dieser am Ende von (im besten Fall) jedem verstanden werden kann.

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/) gefällt mir am besten, wenn ich über die Wege für clean code nachdenke.
<br/><br/>

### 1.1 Klassen Recap

Wie, wann und wo man Klassen verwenden sollte oder nicht möchte ich gar nicht disskutieren. Ich sebst verwende Klassen auch manchmal, wo der ein oder andere sicherlich sagen würde, dass die dort überflüssig seien. Der Hauptgrund warum ich Klasse überhaupt verwende ist 'Encapsulation'. Das heißt so viel wie, dass die Daten und die Methoden, welche jene Daten modifizieren einfach zusammengepackt werden, damit eine eineindeutiger Zusammenhang besteht.

Die einzige Regel die auch ich grundsätzlich beachte ist aus folgendem Zitat abzuleiten. (Das heißt natürlich nicht, dass man sofort ab 2 zugehörigen Methoden und init eine Klasse schreiben sollte, aber ich denke ihr versteht den Punkt.)

> "The signature of 'this should't be a class' is, that it has two methods one of which is
> init. Any time you see that, you should probably think 'hey, maybe I just need one method'."
> \- Jack Diederich in [YoutTube: Stop Writing Classes](https://youtu.be/o9pEzgHorH0)

<br/>

### 1.2 'Dunder'-Methods

Um das Klassendesign im fortgeschrittenen Stil zu verstehen möchte ich bei den
'Dunder'- oder 'Magic'-Methods anfangen. (Dunder steht für 'Double Underscores'). Diese speziellen Methoden erfüllen einzigartige Aufgaben, welche durch die allgemeine Syntax und die 'Built-In' Methods abgerufen/aufgefragt werden können.

#### 1.2.1 Allgemein

Jeder der in Python bereits eine Klasse geschrieben hat wird mindestens die

```py
def __init__(self, arg1, arg2, ...)
```

verwendet haben. 'Dunder'-Methods sind Methoden, welche im allgemeinen Fall **nicht** direkt über ihre Bezeichnung aufgerufen, sondern über die Syntax oder andere 'Built-In' Methods von Python. Sie **können** zwar über die Bezeichnung der 'Dunder'-Methods direkt aufgerufen werden, aber es widerspricht ihrem Sinn, da diese eben durch die Syntax und die 'Built-In'-Methods aufgerufen werden sollen. (Ausgenommen innerhalb der Klassendefinition selbst, dazu später mehr.)
<br/>
<sub>Ich kenne ehrlich gesagt keinen Fall indem man außerhalb der Klassendefinition die 'Dunder'-Methods über ihre Bezeichnung verwenden sollte.</sub>

```py
# 'Falscher' Weg (Funktioniert, aber man macht es nicht)
# __new__ erstellt eine leere Instanz einer Klasse
my_class_instance = MyClass.__new__(MyClass)
# __init__ initialisiert die übergebene Instanz
MyClass.__init__(my_class_instance, arg1, arg2, ...)


# Richtiger Weg
# Beim Instanziieren einer Klasse über den richtigen Konstrukor wird die __new__ Method automatisch vor der Initialisierung durchgeführt.
my_class_instance = MyClass(arg1, arg2, ...)
```

Ab diesem Punkt sollte klar sein, dass man jede Klassen-Methode, welche ein self-Argument hat auch über die Bezeichnung der Klasse selbst aufgerufen werden kann, wenn man eine Instanz dieser Klasse an der ersten Position übergibt.

<br/><br/>
Beispiel für die Verwendung von 'Dunder'-Methods durch 'Built-In'-Methods:

Die 'Dunder'-Method \_\_len\_\_(self) wird über die 'Built-In' Method
len() aufgerufen. Was diese \_\_len\_\_(self) Methode am Ende durchführt ist
komplett euch überlassen. Die einzige Vorraussetzung ist, dass diese Methode
einen Integer >=0 zurück gibt. Bevor ihr die Vorraussetzung erfüllt, könnt ihr
ausführen, berechnen und hacken was ihr wollt, solange die Vorrausetzung erfüllt wird, ist alles in Ordnung mit der Implementation.

Sobald man aber in dieses Thema des fortgeschrittenen Designs kommt ist man mindestens an einem Punkt, wo man den Code wiederverwenden will, wenn nicht sogar für Andere bereitstellen muss/möchte. Also sollte man sich fragen, was würde jemand anderes bei der Verwendung einer 'Dunder'-Method eigentlich erwarten? Bzw. warum sollte man diese Methode überhaupt auf die Klasse anwenden können?

<sub>(Randnotiz: \_\_len\_\_(self) ist übrigens die Falback-Methode für \_\_bool\_\_(self). Das heißt, wenn keine Dunder-Bool-Method definiert ist wird die Dunder-Len-Method verwendet. Alles was >0 ist entspricht dann eben True)</sub>
<br/>

Für Vergleiche oder arithmetische Operationen gilt das Gleiche.

```py
def __add__(self, other):
# -> instance1 + instance2
# -> instance1.__add__(instance2)

# gt -> Greater Than
def __gt__(self, other):
# -> instance1 > instance2
# -> instance1.__gt__(instance2)
...
```

<sub>(Hint: Die standard Libary functools bietet einen Classdecorator (@total_ordering), welcher einen Shortcut für die Vergleichsoperationen liefert. Das heißt, statt alle Dunder-Methoden für '>', '<', '==', '!=', '>=', '<=' selbst zu implementieren müsstet ihr nur '==' und eine der anderen implementieren und hättet dennoch alle Verglichsoperationen zur verfügung.)</sub>

<br/>

Ich selbst hatte keine Idee, wie man eine allgemeine Zusammenfassung für die 'Dunder'-Methods formulieren könnte. Das hat jemand anderes aber sehr gut hinbekommen.

> A dunder method is an implicit function, that is being called behind the
> scenes of an explicit operation or a function. \- Iakshayarora7 (https://www.djangospin.com/python-dunder-methods-attributes/)

<br/>

Python-Dokumentation über (alle?) Special 'Dunder' Methods: https://docs.python.org/3/reference/datamodel.html#special-method-names

<br/><br/>

#### 1.2.2 \_\_repr\_\_() oder \_\_str\_\_() ?

Wenn man gute und ausgereifte Klassen designen will, dann sollte man auf diese beiden 'Dunder'-Methods nicht verzichten. Sie können in jeder Klasse ihren Platz finden, da sie lediglich Informationen enthalten, welche die Klasse und ihren Inhalt beschreiben sollen.

<sub>(Randnotiz: Die \_\_repr\_\_ Method ist die Fallback-Methode für den Fall dass str() auf ein Objekt angewendet wird und keine \_\_str\_\_ Method definiert ist. Umgekehert ist dies nicht der Fall. Wendet man repr() auf ein Obejkt an wird **nicht** die \_\_str\_\_ Method als Alternative verwendet, falls es keine \_\_repr\_\_ Method gibt.)</sub>

<br/>
__str__(self)

Die Dunder-str-Method ist dazu gedacht, eine Darstellung des Objekts zurückzugeben, welche für den Benutzer einfach zu lesen und zu verstehen ist. Sie muss einen String zurückgeben. Was ihr am Ende für einen String durch die Dunder-str-Methode zurück gibt ist euch überlassen. Der Sinn sollte am folgenden Beispiel klar werden.

Kleines Beispiel:

```py
 class PC:
     def __init__(self, prozessor, grafikkarte):
        self.prozessor = prozessor
        self.grafikkarte = grafikkarte

    def __str__(self):
        msg = ""
        msg += f"\nDiese Instanz ist von der Klasse: {self.__class__.__name__}"
        msg += "\nSie hat folgende Attribute:"

        for key, value in self.__dict__.items():
            msg += f"\n\t{key}: \t{value} \t| ({type(value)})"

        return msg

MeinPc = PC('Ryzen 7', 'RTX2070Super')
print(MeinPc)
```

Ausgabe, hervorgerufen durch print(MeinPc):

<pre>
> Diese Instanz ist von der Klasse: PC
> Sie hat folgende Attribute:
>        prozessor:      Ryzen 7         | (class 'str')
>        grafikkarte:    RTX2070Super    | (class 'str')
</pre>

<sub>Eigentlich wird die der Type mit den <> dargestellt (<class 'str'>). Aufgrund der verwendeten Markuplanguage (.md) funktioniert das da nicht.</sub>

<br/>
__repr__(self)

Repr ist die Kurzform für 'Representation'. Die Dunder-repr-Method wird durch die 'Built-In' Methoden repr() aufgerufen. Der Rückgabewert der Dunder-repr-Method muss ebenfalls ein String sein. Und laut Python Dokumentation soll dieser String der Pythonausdruck sein, um jene Instanz zu erzeugen. Wenn das nicht möglich ist soll eine 'sinnvolle Beschreibung' zurückgegeben werden.

Was heißt das nun, 'der Pythonausdruck, um jene Instanz zu erzeugen'?

PC Beispiel:

```py
class PC:
    def __init__(self, prozessor, grafikkarte):
        self.prozessor = prozessor
        self.grafikkarte = grafikkarte

    def __repr__(self):
        argument_string_list = [f"{key}='{value}'" for key, value in self.__dict__.items()]
        init_string = ', '.join(argument_string_list)
        return f'{self.__class__.__name__}({init_string})'

meine_pc_instanz = PC('Ryzen 7', 'RTX2070Super')

print(repr(meine_pc_instanz))
```

Was zu folgender Ausgabe führen wird:

<pre>
> PC(prozessor='Ryzen 7', grafikkarte='RTX2070Super')
</pre>

<sub>(Randnotiz 1: Die Single-Quotes sind in diesem Fall hardcoded um alle Argumente. Das funktioniert in diesem Fall nur, weil es bei sich bei Allen um Strings handelt. Man müsste die Dunder-repr-Method noch expliziter gestalten, um verschiedene Datentypen richtig zu unterscheiden. Dieses Beispiel geht lediglich allgemein auf die Dunder-repr-Method ein.)</sub>

<sub>(Randnotiz 2: Wer die join() Method nich kennt sollte sich die anschauen. Sie nimmt eine iteriebares Obejekt and und verknüpft alle Elemente zu einem String, sofern sich die str() Method auf die Inhalte anwenden lässt. Wenn sich die Elemente nicht in einen String umwandeln lassen wird ein TypeError erhoben. Der erste Teil (In diesem Fall ', ') ist der Seperator. Der Seperator wird zwischen die einzelnen Teilelemente gepackt)</sub>
<br/><br/><br/>

#### 1.2.3

Das \_\_dict\_\_ einer Instanz enthält **ausschließlich** die Attribute, welche nur innerhallb der Instanz gültig sind. Wohingegen der Aufruf von dir(instance) \_\_dir\_\_ einer Instanz die Attribute **UND** die

<pre>
>
>
>
>
</pre>

```

```
