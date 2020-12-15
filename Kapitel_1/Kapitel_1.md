# Inhalt

- [Kapitel 1 Fortgeschrittenes Klassen Design](#kapitel-1-fortgeschrittenes-klassen-design)

  - [1.0 Style-Guides](#10-Style-Guides)
  - [1.1 Klassen Recap](#11-klassen-recap)
    - [1.1.1 Allgemein](#111-allgemein)
    - [1.1.2 Public, Private und Protected](#112-public,-private-und-protected)
    - [1.1.3 Klassenattribute](#113-klassenattribute)
  - [1.2 'Dunder'-Methods](#12-'dunder'-methods)
    - [1.2.1 Allgemein](#121-allgemein)
    - [1.2.2 \_\_repr\_\_ oder \_\_str\_\_](#122-__repr__-oder-__str__)
    - [1.2.3 \_\_enter\_\_ und \_\_exit\_\_](#123-__enter__-und-__exit__)
    - [1.2.4 \_\_doc\_\_ Attribut](#124-__doc__-attribut)
    - [1.2.5 \_\_call\_\_ Method](#125-__call__-method)
    - [1.2.6 Weitere 'Dunder'-Methods](#126-weitere-'dunder'-methods)
  - [1.3 Attribut Zugriff](#13-attribut-zugriff)
    - [1.3.1 Allgemein](#131-allgemein)
    - [1.3.2 List/Dict Zugriff](#132-list/dict-zugriff)
    - [1.3.3 Descriptor Zugriff](#133-Descriptor-zugriff)
    - [1.3.4 Zusammenfassung](#134-zusammenfassung)

## Kapitel 1: Fortgeschrittenes Klassen Design

Das Thema von fortgeschrittenem Design hat den wesentlichen Hintergrund des 'Code Reuse'. Die Inhalte gehen auch hauptsächlich in diese Richtung, um zu zeigen, an welchen Stellen man 'sorgfältiger' arbeiten sollte, um die Wiederverwendung möglichst sicher und einfach zu gesalten.

---

### 1.0 Style-Guides

Ich möchte am Anfang einmal auf die Style-Guides und ein paar Zitate/Aussagen von Python-Core-Developer hinweisen. Ich möchte bezüglich dem Styling keine Ratschläge geben oder verschiedene Guides vergleichen. Es gibt [PEP8](https://www.python.org/dev/peps/pep-0008/), es gibt eine [Vorlage von Google](https://google.github.io/styleguide/pyguide.html) und sicherlich noch andere, aber selbst Raymond Hettinger sagte in seinem Vortrag:

> "PEP8 is not a weapon for beating other people in the head. It's a stlye
> guide, a guide, not a lawbook." - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

und

> "Isn't it great, when you write code that is PEP8 compliant and out of a room of 500 people one person can figure it out?" - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

Im Vortrag weist er mit diesen Aussagen darauf hin, dass man die Qualität von Code nicht nach dem Grad der Übereinstimmung von PEP8 bestimmen sollte, sondern ein bisschen weiter denken muss, um den nächsten Lesern das Leben zu vereinfachen. PEP8 hat nicht zu Allem eine Antwort, deswegen sollte man sich selbst Geanken machen, wie man seinen Stil im Coden so umsetzt, dass dieser am Ende von (im besten Fall) jedem verstanden werden kann.

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/) gefällt mir am besten, wenn ich über die Wege für clean code nachdenke.

---

### 1.1 Klassen Recap

#### 1.1.1 Allgemein

Wie, wann und wo man Klassen verwenden sollte oder nicht möchte ich gar nicht disskutieren. Ich sebst verwende Klassen auch manchmal dort, wo der ein oder andere sicherlich sagen würde, dass sie dort überflüssig seien. Der Hauptgrund warum ich Klasse überhaupt verwende ist 'Encapsulation'. Das heißt so viel wie, dass die Daten und die Methoden, welche jene Daten modifizieren, einfach zusammengepackt werden, damit ein eineindeutiger Zusammenhang besteht.

Die einzige Regel die auch ich grundsätzlich beachte ist aus folgendem Zitat abzuleiten. (Das heißt natürlich nicht, dass man sofort ab 2 zugehörigen Methoden und init eine Klasse schreiben sollte, aber ich denke ihr versteht den Punkt.)

> "The signature of 'this should't be a class' is, that it has two methods one of which is
> init. Any time you see that, you should probably think 'hey, maybe I just need one method'."
> \- Jack Diederich in [YoutTube: Stop Writing Classes](https://youtu.be/o9pEzgHorH0)

<br/>

#### 1.1.2 Public, Private und Protected

Meine beste Sprache ist Python, ich habe C und C++ als erste Sprachen gelernt, aber damit habe ich schon ewig nicht gearbeitet. Weswegen ich hier nicht generell für alle OOP-Sprachen sprechen kann. Mein Verständnis für Public, Private, Protected kommt eben aus C++ und das liegt bei mir schon Jahre zurück. Also verzeiht, wenn ich diesbezüglich nicht alles so genau weiß und hier etwas Erkläre, was selbtsverständlich ist, wenn man sich in der anderen Sprache tief genug auskennt.

**Public**<br/>
Man kann eigentlich sagen, dass **ALLES** innerhalb einer Python Klasse public ist. Es gibt Konzepte und Conventionen, welche die Idee von Private und Proteced nachahmen sollen, aber wenn man sich auskennt, dann kann man auch diese Dinge ohne Aufwand umgehen. (An dieser Stelle fehlt mir die Erfahrung in anderen OOP-Sprachen, um zu wissen, ob dies auch dort einfach zu umgehen ist.)

**Private**<br/>
Wer aus anderen objektorentieren Sprachen kommt wird das Konzept von Public, Proteced und Private kennen. Soetwas gibt es in Python nicht. Wer jetzt schonmal die Basics von Klassen in Python kennt wird vielleicht den Finger heben und Fragen: "Was ist denn mit den \_\_vars und \_\_methods()?" (Zwei führende Unterstriche, falls dies im Text nicht deutlich raus kommt.)

Wenn der Python-Interpreter innerhalb einer Klasse ein Attrribut oder Methode mit zwei führenden Unterstrichen und maximal einem nachfolgenden Unterstrich erkennt, führt dieser ein sogenanntes 'Name Mangling' durch. Das heißt, er bennent die Attribute und die Methoden, die dieser Form folgen, schlicht und ergreifend einfach um.

Code: [\_1_public_private.py](_1_public_private.py)

```py
01  class PC:
02     def __init__(self, cpu, gpu, ram):
03         self.cpu = cpu
04         self.gpu = gpu
05         self.__ram = ram
06
07  pc_instanz = PC('Ryzen 7', 'RTX2070Super', 'GSkill')
08
09  print(pc_instanz.cpu)
10  print(pc_instanz.gpu)
11  print(pc_instanz.__ram)
```

<pre>
> Ryzen 7
> RTX2070Super
> Traceback (most recent call last):
>   File "f:/Python-Projects/Projects/Classes_Tutorial/name_mangeling.py", line 11, in <module>
>     print(pc_instanz.__ram)
> AttributeError: 'PC' object has no attribute '__ram'
</pre>

So gesehen besteht von Außen kein direkter Zugriff auf das Attribut \_\_ram. Der Grund dafür ist, es gibt dieses Attribut gar nicht mehr. Wenn man wissen will, was in einem Obejkt enthalten ist, dann muss man sich das \_\_dict\_\_ Attribut anschauen. Es enthält **alle** Attribute und Methoden die zu jenem Objekt zugewiesen wurden. Bei einer Instanz heißt das also, alles was zu _self_ zugewiesen wird. Gebe ich dieses \_\_dict\_\_ nun aus sehen wir, was die Instanz wirklich enthält.

```py
print(pc_instanz.__dict__)
```

<pre>
> {'cpu': 'Ryzen 7', 'gpu': 'RTX2070Super', '_PC__ram': 'GSkill'}
</pre>

Wir sehen, dass _cpu_ und _gpu_ wie zu erwarten enthalten sind, aber wir sehen auch, dass unser _\_\_ram_ wieder da ist. Das Name Mangling hat dafür gesorgt, dass der Klassenname mit einem führenden Unterstrich an den Anfang des Attributs gesetzt wurde.

Versuche ich folgendes

```py
print(pc_instanz._PC__ram)
```

<pre>
> GSkill
</pre>

habe ich dennoch Zugang zu den eigentlich 'privaten' Attributen innerhalb einer Klasse.

Dennoch findet diese Form Anwendung. Das Name Mangling verhindert eben Namespace Kollisionen, wenn die Klasse vererbt wird. Das heißt, wenn ich aus irgendeinem Grund sicherstellen muss, dass ein Attribut oder eine Methode für eine Klasse durch Vererbung nicht verändert werden darf, dann erreiche ich das mit dieser Form. Denn würde ich ein weiteres \_\_ram Attribut in einer vererbten Klasse erstellen, dann würde dies durch das Name Mangling den Namen der vererbten Klasse vorgestellt bekommen. Damit würden sich die beiden Attribute von der Bezeichnung unterscheiden.

<sub>(Randnotiz 1: Warum kann ich innerhalb von Klassen dann mit self.\_\_ram an das Attribut kommen? Ganz einfach, der Interpretert bennent innerhalb einer Klasse ALLE vorkommenden Attribute und Methoden mit 2 führenden Untersichten mittels Name Mangling um. Außerhalb von Klassen eben nicht.)
</sub>

<br/>

**Protected**<br/>
Protected, also das Attribute und Methoden nur von der Klasse und von vererbten Klassen 'gesehen/verwendet' werden können gibt es gar nicht. (Warum auch, nicht einmal ein echtes Private gibt es.)

Unter Python Entwicklern gibt es die Convention, dass 'protected' innerhalb von Klassen mittels einem führenden Unterstrich gekennzeichnet werden. Das ist aber lediglich ein Hinweis für Andere. Der Python-Interpreter selbst behandelt Attribute und Methoden mit einem führenden Unterstrich nicht anders als ohne.

<br/>

#### 1.1.3 Klassenattribute

Klassenattribute sind Attribute, welche nicht im Instanz-Dict gespeichert werden, sondern bereits vor der Instanziierung in das Klassen-Dict eingetragen sind.

Klassenattribute existieren **nur** auf Klassenebene. Wenn man über eine Instanz auf ein Klassenattribut zugreift ist das möglich, weil Python, sobald das Attribut auf Instanzebene nicht zu finden ist, in der Klasse weiter sucht. Dies zieht sich auch durch Vererbungen durch.

Code: [\_2_Klassenattribute_1.py](_2_Klassenattribute_1.py)

```py
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"

pc_instanz = PC()

print("Instanz Dict: ", pc_instanz.__dict__)
print("Klassen Dict: ", PC.__dict__)
print("Zugriff über Instanz: ", pc_instanz.klassen_attribut)
```

<pre>
> Instanz Dict: {}
> Klassen Dict: { ..., 'klassen_attribut': 'Ich bin ein Klassenattribut', ...}
> Zugriff über Instanz: Ich bin ein Klassenattribut
</pre>

Wenn man weiß, dass man das Klassenattribut über das Instanz-Objekt lesen kann, dann stell ich mir die Frage, was passiert, wenn man es über die Instanz versucht zu schreiben.

```py
pc_instanz.klassen_attribut = "Neuer Wert"
print(pc_instanz.klassen_attribut)
```

<pre>
> Neuer Wert
</pre>

Super, das funktioniert auch, aber was ist jetzt passiert? Um wirklich zu wissen, welche Daten zu welcher Instanz/Klasse gehören müssen wir ja nur das \_\_dict\_\_ ausgeben.

```py
print("Instanz Dict: ", pc_instanz.__dict__)
print("Klassen Dict: ", PC.__dict__)
```

<pre>
> Instanz Dict:  {'klassen_attribut': 'Neuer Wert'}
> Klassen Dict:  {..., 'klassen_attribut': 'Ich bin ein Klassenattribut', ...}
</pre>

Die leere Instanz hat nun ein eigenes Attribut mit dem Bezeichner 'klassen_attribut' bekommen und das echte Klassenattribut blieb unverändert. Der richtige Weg mit Klassenattributen umzugehen ist immer, dass man über die Instanz auf die Klasse zugreift und anschließend auf das Attribut. Das sieht dann folgendermaßen aus:

Code: [\_3_Klassenattribute_2.py](_3_Klassenattribute_2.py)

```py
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"

    def __init__(self):
        self.attr1 = self.__class__.klassen_attribut # Zeile 1
        self.attr2 = type(self).klassen_attribut     # Zeile 2
        self.attr3 = PC.klassen_attribut             # Zeile 3
```

Zeile 1 und Zeile 2 funktionieren **exakt** gleich, da type(self) immer die eigene Klasse zurück gibt, welche aber auch bereits in self.\_\_class\_\_ enthalten ist (Ihr könnt ja beide Statements mal ausgeben, dann werdet ihr es ja sehen). Ich persönlich bevorzuge die Schreibweise von Zeile 1.

**Hardcoding, wie in Zeile 3, sollte immer vermieden werden**. Spätestens, wenn diese Klassen vererbt werden, bekommt ihr Probleme. Einfache Zeile 3 vergessen. Im Kapitel zu Vererbungen zeige ich da nochmal ein ähnliches Beispiel.

<sub>(Randnotiz 1: Ja, auch wenn das Klassenattribut nur innerhalb der Klasse verwendet wird sollte man explizit über die self.**class** drauf zugreifen. Warum? Stellt euch vor, eure Klasse verwendet intern ein Klassenattribut und ein Benutzer der Klasse von außen weiß dies aber nicht. Nun schreibt er von Hand in seine Instanz exakt dieses Attribut herrein, warum auch immer. Würde man innerhalb der Klasse mit der Instanz drauf zugreifen, dann würde man plötzlich das neue Attribut der Instanz verwenden, statt dem richtigen der Klasse.)
</sub>
<br/><br/>

**Vererbung von Klassenattirbuten**<br/>

Durch Vererbung von 'Klasse 1' (Elternklasse) auf 'Klasse 2' (Kindklasse) ist das Klassenattribut auch dort verfügbar, **aber** es wird nicht im \_\_dict\_\_ der 'Klasse 2' aufgeführt. Erstellt ihr eine Instanz von 'Klasse 2' habt ihr mit einem Klassenattribut innerhalb 'Klasse 1' Zugriff auf ein Attribut, welches ihr weder im Instanz-Dict der erstellen Klasse, noch im Klassen-Dict der verwendeten Klasse seht. Das ist meiner Meinung nach... Naja beschissen, zumal ein Klassenattribut der 'Klasse 1' durch die Instanzen von Klasse 1 verändert werden könnte, welche sich anschließend auch in den Instanzen der 'Klasse 2' wiederspiegeln. Seid einfach Vorsichtigt, wenn ihr Klassenattribute verwendet und macht sie im Zweifel lieber 'privat'.

Code: [\_4_Klassenattribute_3.py](_4_Klassenattribute_3.py)

```py
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"

class PC2(PC):
    pass

pc2_instanz = PC2()

print(pc2_instanz.__dict__)
print(PC2.__dict__)
print(pc2_instanz.klassen_attribut)
```

<pre>
> {}
> {'__module__': '__main__', '__doc__': None}
> Ich bin ein Klassenattribut
</pre>

<sub>(Randnotiz 1: Ich habe bisher nicht sehr viel mit Klassenattributen gearbeitet, lediglich habe ich sie als 'Konstanten' verwendet, welche ich einmal im Kopf der Klasse definiert und anschließend nur gelesen habe. Ich denke aber ich würde sie einfach immer 'privat' machen, einfach um nicht ausversehen aus vererbten Klassen auf etwas zugreifen zu können, was ich erstmal ewig suchen müsste. Ob man das so macht weiß ich nicht.)</sub>

<sub>(Randnotiz 2: Natürlich, wenn ihr jetzt verstanden habt wie es geht, dann ist der Zugriff immernoch möglich, aber es verhindert im ersten Schritt Kollisionen, wenn man über sowas gar nicht nachdenkt. (Beispielsweise könnte man ja alle Elternklassen auslesen und anschließend das Dict jener und mit dem Namen der Klasse nach Allem suchen was dem Muster f"\_{parent_class}\_\_" folgt.) Des Weiteren könnt ihr damit immernoch Attribute vor Anfängern oder unwissenden 'verstecken', denen beispielsweise nur die Kindklassen zur Verfügung stehen.)</sub>

---

### 1.2 'Dunder'-Methods

Um das Klassendesign im fortgeschrittenen Stil zu verstehen und anwenden zu können muss man die Idee hinter den 'Dunder'-Methods kennen (Dunder steht für 'Double Underscores'). Diese speziellen Methoden erfüllen einzigartige Aufgaben, welche durch die allgemeine Syntax und die 'Built-In' Methoden von Python aufgerufen/abgefragt werden. Ich werde selbstverständlich nicht alle im Detail vorstellen und zeigen, sondern anhand von einzelnen Beispielen die Funktion von 'Dunder'-Methods erklären und auf ein paar besondere hinweisen. Um sie sinnvoll anzuwenden zu können müsst ihr sowieso die Dokumentation lesen, da es für manche 'Dunder'-Methods gewisse Regeln gibt, wie beispielsweise, dass die Rückgabe ein nur bestimmten Datentyp sein darf oder in einem definierten Bereich liegen muss.

<br/>

#### 1.2.1 Allgemein

Jeder der in Python bereits eine Klasse geschrieben hat wird mindestens die

```py
def __init__(self, arg1, arg2, ...)
```

verwendet haben. 'Dunder'-Methods sind Methoden, welche im allgemeinen Fall **nicht** direkt über ihre Bezeichnung aufgerufen werden, sondern über die Syntax oder andere 'Built-In' Methods von Python. Sie **können** zwar über die Bezeichnung der 'Dunder'-Methods direkt aufgerufen werden, aber es widerspricht ihrem Sinn. (Ausgenommen innerhalb der Klassendefinition selbst, dazu später mehr.)

<sub>(Ich kenne ehrlich gesagt keinen Fall indem man außerhalb der Klassendefinition die 'Dunder'-Methods über ihre Bezeichnung verwenden sollte.)</sub>

Code: [\_5_dunder_init.py](_5_dunder_init.py)

```py
# 'Falscher' Weg (Funktioniert, aber man macht es nicht)
# __new__ erstellt ein leers Objekt einer Klasse
instanz1 = MyClass.__new__(MyClass)
# __init__ initialisiert die übergebene Instanz
MyClass.__init__(instanz1, arg1, arg2, ...)


# Richtiger Weg
# Beim Instanziieren einer Klasse über den richtigen Konstrukor werden die
# __new__ (und __prepare__) Methoden automatisch implizit vor der Initialisierung durchgeführt.
instanz2 = MyClass(arg1, arg2, ...)
```

Dieses Beispiels sollte verdeutlichen, dass man zum einen auch jede 'Dunder'-Methode über ihre Bezeichung aufrufen kann. Außerdem sollte auch klar sein, dass jede Methode einer Klasse direkt über die Klasse selbst aufgerufen werden kann, wenn man an der ersten Stelle die Instanz als das _self_-Argument übergibt.

<sub>(Randnotiz 1: Der Aufruf über die Instanz selbst übergibt das _self_-Argument implizit.)</sub>

<br/>
Beispiel für die Verwendung von 'Dunder'-Methods durch 'Built-In'-Methods:

Die 'Dunder'-Method \_\_len\_\_(self) wird über die 'Built-In' Method
len() aufgerufen. Was diese \_\_len\_\_(self) Methode am Ende durchführt ist
komplett euch überlassen. Die einzige Vorraussetzung ist, dass diese Methode
einen Integer >=0 zurück gibt. Bevor ihr die Vorraussetzung erfüllt, könnt ihr
ausführen, berechnen und hacken was ihr wollt, solange die Vorrausetzung erfüllt wird, ist alles in Ordnung mit der Implementation einer 'Dunder'-Method.

Sobald man aber in dieses Thema des fortgeschrittenen Designs kommt ist man mindestens an einem Punkt, wo man den Code wiederverwenden will, wenn nicht sogar für Andere bereitstellen muss/möchte. Also sollte man sich fragen, was würde jemand anderes bei der Verwendung einer 'Dunder'-Method eigentlich erwarten? Bzw. warum sollte man diese Methode überhaupt auf die Instanz einer Klasse anwenden können?

Will ich die Instanz meiner Klasse mittels for-Loop durchlaufen, dann benötige ich die 'Dunder'-Methods \_\_iter\_\_ und \_\_next\_\_. Will ich zwei Instanzen miteinander verrechnen oder vergleichen können, dann benötige ich die 'Dunder'-Methods \_\_add\_\_, \_\_sub\_\_, \_\_gt\_\_, ... usw.

<sub>(Randnotiz 1: \_\_len\_\_(self) ist übrigens die Fallback-Methode für \_\_bool\_\_(self). Das heißt, wenn keine Dunder-bool-Method definiert ist wird die Dunder-len-Method verwendet. Alles was >0 ist wird von Python als True interpretiert.)</sub>
<br/>

Code: [\_6_dunder_other.py](_6_dunder_other.py)

```py
def __add__(self, other):
# > instance1 + instance2
# > instance1.__add__(instance2)
# > MyClass.__add__(instance1, instance2)
# > int.__add__(10, 20)

# gt -> Greater Than
def __gt__(self, other):
# > instance1 > instance2
# > instance1.__gt__(instance2)
...
```

<sub>(Randnotiz 2: Das _other_ Argument in den Vergleichs- und Rechenoperationen kann **alles** sein, was auf der rechten Seite des '+' steht. Behaltet es im Hinterkopf, an solchen stellen evnetuell ein instance/type Checking durchzuführen, damit ihr das abfangt, falls nötig. [_5_dunder_other.py]) </sub>

<sub>(Hint: Die standard Libary functools bietet einen Classdecorator (@total_ordering), welcher einen Shortcut für die Vergleichsoperationen liefert. Das heißt, statt alle Dunder-Methoden für '>', '<', '==', '!=', '>=', '<=' selbst zu implementieren müsstet ihr nur '==' und eine der größer oder kleiner als Methode implementieren und hättet dennoch alle Verglichsoperationen zur verfügung.)</sub>

Ich selbst hatte keine Idee, wie man eine allgemeine Zusammenfassung für die 'Dunder'-Methods formulieren könnte. Das hat jemand anderes aber sehr gut hinbekommen.

> A dunder method is an implicit function, that is being called behind the
> scenes of an explicit operation or a function. \- Iakshayarora7 (https://www.djangospin.com/python-dunder-methods-attributes/)

<br/>

Python-Dokumentation über (alle?) Special 'Dunder' Methods:

https://docs.python.org/3/genindex-_.html

https://docs.python.org/3/reference/datamodel.html#special-method-names

<br/>

#### 1.2.2 \_\_repr\_\_ oder \_\_str\_\_

Wenn man gute und ausgereifte Klassen designen will, dann sollte man auf diese beiden 'Dunder'-Methods nicht verzichten. Sie können in jeder Klasse ihren Platz finden, da sie lediglich Informationen enthalten, welche die Klasse und ihren Inhalt beschreiben sollen.

<sub>(Randnotiz 1: Die \_\_repr\_\_ Method ist die Fallback-Methode für den Fall dass str() auf ein Objekt angewendet wird und keine \_\_str\_\_ Method definiert ist. Umgekehert ist dies nicht der Fall. Wendet man repr() auf ein Objekt an wird **nicht** die \_\_str\_\_ Method als Alternative verwendet, falls es keine \_\_repr\_\_ Method gibt.)</sub>

<br/>

**\_\_str\_\_(self)**

Die Dunder-str-Method ist dazu gedacht, eine Darstellung des Objekts zurückzugeben, welche für den Benutzer einfach zu lesen und zu verstehen ist. Sie **muss** einen String zurückgeben. Was ihr am Ende für einen String durch die Dunder-str-Methode zurück gibt ist euch überlassen. Der Sinn sollte am folgenden Beispiel klar werden.

Code: [\_7_dunder_str_pc.py](_7_dunder_str_pc.py)

**PC Beispiel:**

```py
 class PC:
     def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def __str__(self):
        msg = ""
        msg += f"\nDiese Instanz ist von der Klasse: {self.__class__.__name__}"
        msg += "\nSie hat folgende Attribute:"

        for key, value in self.__dict__.items():
            msg += f"\n\t{key}: \t{value!r} \t| ({type(value)})"

        return msg

pc_instanz = PC('Ryzen 7', 'RTX2070Super')
print(pc_instanz)
```

<pre>
> Diese Instanz ist von der Klasse: PC
> Sie hat folgende Attribute:
>        cpu:      'Ryzen 7'         | (class 'str')
>        gpu:      'RTX2070Super'    | (class 'str')
</pre>

Man könnte noch Elternklassen anzeigen oder über Metaklassen viele weitere Informationen bereitstellen, wenn man sowas braucht. Die Frage ist halt, wofür möchte man str(instanz) am Ende verwenden. Eine schnelle, leserliche Information über die Inhalte? Zustände der Instanz? Eine detailliertere Beschreibung eines Prozesses? Ich denke das muss jeder selbst nach Anwendungsfall entscheiden.

<sub>(Randnotiz 2: Eigentlich wird die der Type mit den <> dargestellt (<class 'str'>). Aufgrund der verwendeten Markuplanguage (.md) funktioniert das da nicht.)</sub>

<sub>(Randnotiz 3: Warum sollte ich die Klasse der Attribute ausgeben, ist das nicht eindeutig? Für die 'Built-In' Klassen wie str, int, list, ... scheint es überflüssig zu sein. Angenommen ihr verwendet eigene Klassen, die die Funktionalität der Grundklassen erweitern. Eine eigene Klasse z.b. <class '\_\_main\_\_.SizedStr'>, welche das Attribut auf eine maximale Länge limitiert, würde dem Benutzer eine Erklärung geben, was dort eigentlich hintersteckt, statt dass dieses Attribut ein normaler String wäre, wie es im ersten Augenblick erscheint.)
</sub>

<br/>

**\_\_repr\_\_(self)**

Repr ist die Kurzform für 'Representation'. Die Dunder-repr-Method wird durch die 'Built-In' Methoden repr() aufgerufen. Der Rückgabewert der Dunder-repr-Method muss ebenfalls ein String sein. Und laut Python Dokumentation soll dieser String der Pythonausdruck sein, um jene Instanz zu erzeugen. Wenn das nicht möglich ist soll eine 'sinnvolle Beschreibung' zurückgegeben werden.

Was heißt das nun, 'der Pythonausdruck, um jene Instanz zu erzeugen'?

<br/>

**Allgemeines Beispiel eines repr eines 'Built-In' Datentyps:**

Code: [\_8_dunder_repr_simple.py](_8_dunder_repr_simple.py)

```py
my_string = 'Hallo'

print(my_string) # __str__()

print(repr(my_string)) # __repr__()
```

<pre>
> Hallo
> 'Hallo'
</pre>

Der repr() zeigt also eine Darstellung, mit der ein neues Objekt jener Instanz erzeugt werden kann.

Code: [\_9_dunder_repr_pc.py](_9_dunder_repr_pc.py)

**PC Beispiel:**

```py
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def __repr__(self):
        argument_string_list = [f'{key}={value!r}' for key, value in self.__dict__.items()]
        init_string = ', '.join(argument_string_list)
        return f'{self.__class__.__name__}({init_string})'

pc_instanz = PC('Ryzen 7', 'RTX2070Super')

print(repr(pc_instanz))
```

<pre>
> PC(cpu='Ryzen 7', gpu='RTX2070Super')
</pre>

<sub>(Randnotiz 1: Wer die join() Method nich kennt sollte sich die anschauen. Sie nimmt eine iteriebares Obejekt and und verknüpft alle Elemente zu einem String, sofern sich die str() Method auf die Elemente anwenden lässt. Wenn sich die Elemente nicht in einen String umwandeln lassen wird ein TypeError erhoben. Der erste Teil (In diesem Fall ', ') ist der Seperator. Der Seperator wird zwischen die einzelnen Teilelemente gepackt.)</sub>

<sub>(Randnotiz 2: Der repr, also die Represenation eines Objekts, wird von VSCode beispielsweise beim Debuggen verwendet. Wenn man an einem Breakpoint steht, sieht man die Variablen an der Seite. Hinter der Variable steht eben die Representation. Ob und wie es von anderen IDEs verwendet wird weiß ich nicht. Ohne \_\_repr\_\_-Method würde dort allgemein (\_\_main\_\_.\_\_class_name\_\_ objekt at 0x....) stehen, also Objekt der Klasse XY aus dem Main-File an Memoryposition 0x....)</sub>

<br/>

#### 1.2.3 \_\_enter\_\_ und \_\_exit\_\_

Enter und Exit werden von den sogeannten 'Contextmanagern' verwendet. Im Wesentlichen kommt dies zur Anwendung, wenn man vor der durchzuführenden Aufgabe etwas vorbereiten muss und nach erledigen der Aufgabe etwas nachbearbeiten (oder Aufräumen muss). Einige von euch werden es sicherlich schonmal von der 'Built-In' Methode _open()_ Gebrauch gemacht haben. Sie öffnet eine Datei und lädt den Zugang zu dieser in eine Variable.

Wenn man eine Datei öffnet, dann sollte man sie auch wieder schließen. Die _open()_ Methode führt das Schließen mittels der \_\_exit\_\_ aus, wenn ein Contextmanager verwendet wird. Der Contextmanager wird mit dem Keyword _with_ verwendet. Ein anderes Beispiel sind Frameworks die eine Verbindung irgendwohin erstellen (Server, Datenbank, ...). Im Enter werden diese Verbindugen aufgebaut und im Exit wird diese Verbindung eben geschlossen. Schaut euch dazu einfach weitere Beispiele an, falls ihr das benötigt.

[Kein Code Beispiel]

```py
with open('sample_file.txt') as f:  # Hier wird die Enter Methode ausgeführt
    content = f.read()
# Hier, unmittelbar nach dem Verlassen des with-Blocks, wird der Exit durchgeführt

# OHNE CONTEXTMANAGER
f = open('sample_file.txt')
content = f.read()
f.close()
```

Würde man das Schließen der Datei vergessen, dann wäre die Datei im System blockiert, da noch eine andere Stelle dort zugreift.

<br/>

#### 1.2.4 \_\_doc\_\_ Attribut

Dokumentiert eure Sachen. Muss man das noch sagen? In Python kann man die Dokumentation einer Klasse oder Funktion als _doc_-String hinterlegen. Der String wird in 3 Anführungszeichen am Kopf der Funktion oder Klasse geschrieben (es gehen doppelte \" und einfache \', aber typischerweise werden doppelte verwendet. [PEP 257 - Docstrings](https://www.python.org/dev/peps/pep-0257/)).

Das \_\_doc\_\_ Attribut ist in jedem Objekt vorhanden, auch wenn keiner vom Autor gesetzt wird. Dann is der Wert eben None.

Lest euch die Style-Guides zu dem Doc-Attribut durch. Dort gibt es schöne Anregungen, wie man eine Klasse oder Funktion ordentlich dokumentiert.

Code: [\_10_pc_doc.py](_10_pc_doc.py)

```py
class PC:
    """Dies ist die Dokumentation der Klasse: PC

    Multiline-Strings sind automatisch mit berücksichtig.
    Es wird sogar mit formatiert. Klasse! Oder?"""

    def __init__(self, cpu, gpu):
        '''Das funktioniert auch bei einfachen Funktionen!
            Parameters:
                arg1: any

            Rückgabe: 1'''
        self.cpu = cpu
        self.gpu = gpu

def outer_func(arg1):
    '''Das funktioniert auch bei einfachen Funktionen!
    Parameters:
        arg1: any

    Rückgabe: 1'''
    print(arg1)
    return 1


print(PC.__doc__, "\n")
print(PC.__init__.__doc__, "\n")
print(outer_func.__doc__, "\n")
```

<pre>
> Dies ist die Dokumentation der Klasse: PC
>
>     Multiline-Strings sind automatisch mit berücksichtig.
>     Es wird sogar mit formatiert. Klasse! Oder?
>
> Jetzt Dokumentieren wir die __init__
>         Was eine schöne Funktion.
>
> Das funktioniert auch bei einfachen Funktionen!
>     Parameters:
>         arg1: any

>     Rückgabe: 1
</pre>

Bei komplexeren Methoden werden häufig Input- und Outputargumente erklärt. Welcher Datentyp sie haben, was passiert, welche restricstions gelten. Also alles was irgendwie hilfreich ist, um den Teil zu verwenden.

Es gibt des Weiteren ein standard Libary names _doctest_. Dieses Modul kann die Funktion von einem Objekt mittels dem Docstring überprüfen, sofern der Docstring dazu designed wurde. Ob man das machen sollte oder nicht, keine Ahnung. Es gibt die Möglichkeit, aber auch dort sollte man es nicht übertreiben und versuchen damit _unittests_ zu ersetzten.

<br/>

#### 1.2.5 \_\_call\_\_ Method

Mittels der Dunder-call-Method kann man die Instanzen einer Klasse aufrufbar machen. Wer sich mit Funktionen und deren Implementation schon tiefer auskennt wird auch wissen, dass Funktionen in Python auch nur ein Objekt der Klasse 'function' sind.

Code: [\_11_function_class.py](_11_function_class.py)

```py
def func(x):
    return x+1

print(type(func))
```

<pre>
> class 'function'
</pre>

Dies ließe sich auch 1 zu 1 so implementieren:

```py
class func_class:
    def __call__(self, x):
        return x+1

instanz = func_class()

print(instanz(1))
```

<pre>
> 2
</pre>

Die \_\_call\_\_-Method wird noch interesannt und wichtig, wenn man Metaklassen verwendet, da der Metklassen-Call bei der Instanziierung vor der \_\_init\_\_ der eigentlichen Klasse durchgeführt wird. Für manche Anwendungsfälle ist diese Tatsache hilfreich, dass man mittels Metaklasse in den Prozess der Instanziierung eingreifen kann.

<br/>

#### 1.2.6 Weitere 'Dunder'-Methods

Während den Recherchen habe ich diese Seite gefunden, welche nochmal einen detaillierteren Überblick über viele 'Dunder'-Methods präsentiert. Wer noch mehr wissen will, einfach reinschauen. https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15

Allgemeine Zusammenfassung ist, wenn ihr mit eurer Klasse irgendeine Standardoperation (+, -, <, >, aufruf, len(), bool(), str(), dir(), ...) verwenden wollte, dann schaut einfach nach der speziellen 'Dunder'-Method dafür nach und ihr könnt das sauber dafür implementieren, statt euch irgendwelche Adapter workarounds zu basteln.

---

### 1.3 Attribut Zugriff

Man muss zwischen dem Attributzugriff in Python in 3 Kategorien unterscheiden. Der Punkt, warum ich dies extra erkläre ist, dass dort häufig eine Verwirrung entsteht, wie dieser überhaupt abläuft. Die meiste Verwirrung entsteht eigentlich dadurch, dass es zwei Methoden gibt, welche den 'normalen' Zugriff übernehmen.

https://twitter.com/raymondh/status/1337505615204106240

https://blog.peterlamut.com/2018/11/04/python-attribute-lookup-explained-in-detail/

<br/>

#### 1.3.1 Allgemein

Unter dem 'Normalen' Zugriff verbergen sich zwei 'Dunder'-Methods

\_\_getattribute\_\_<br/>
\_\_getattr\_\_

Der Zugriff auf ein Attribut ist 'Hardwired' auf \_\_getattribute\_\_. Das heißt, man kann dem Aufruf dieser 'Dunder'-Method nicht ausweichen. Wenn eine Klasse eine Method nicht spezifiziert, dann wird im \_\_mro\_\_-Verlauf weiter nach dem einer passenden Methode gesucht. (\_\_mro\_\_ wird später im [Kapitel 3.3 \_\_mro\_\_ und super()](<#33-__mro__-und-super()>) weiter im Detail erklärt.)

Das letzte Element im \_\_mro\_\_ ist das 'object', welches eine default Implementation der \_\_getattribute\_\_ beinhaltet. Diese führt den Zugriff aus und erhebt einen AttributeError, falls jenes Attribut nicht existiert. Wenn ein AttributError kommt, dann wird als Fallback die \_\_getattr\_\_-Methode durchlaufen.

Es ist natürlich möglich, dass ihr in eurer Klasse eine \_\_getattribute\_\_-Method definiert und den Zugriff dort nicht weiterleitet oder umleitet, wenn ihr das wollt. Aber das ist häufig nicht zu Empfehlen, da in der default Implementation vor dem eigentlichen Zugriff noch einige Dinge überprüft werden. Beispielsweise ob es sich bei dem angefragten Attribut um einee Discriptor Instanz handelt.

<br/>

#### 1.3.2 List/Dict Zugriff

Mit der \_\_getitem\_\_(self, name) ist es möglich, dass ein Zugriff wie bei einer Liste oder einem Dict erfolgt.
Es gibt dazu eigentlich nicht viel zu sagen. Man umgeht die gesamte '.attr' / \_\_getattribute\_\_ machinery und kommt direkt in die \_\_getitem\_\_ Methode. Wenn man eine Klasse hat, die eine gewisse Datenstruktur abbildet kann dies sicherlich sinnvoll sein.

```py
instanz[attr_name] # -> __getitem__(self, name)
```

<br/>

#### 1.3.3 Descriptor Zugriff

Ein Descriptor ist eine Klasse, welche den Zugriff auf ein Attribut spezialisiert. Auch dazu gibt es später ein eigenes Kapitel. Aber dennoch muss man wissen, an welche Stelle des Attributzugriffs der Descriptor angesprochen wird.

Die Descriptor Methode \_\_get\_\_ wird durch die default Implementation der \_\_getattribute\_\_ mit berücksichtig. Das heißt, selbst wenn ein Attribut als Descriptor beschrieben ist, läuft der Prozess vollständig über \_\_getattribute\_\_ hoch in die default Implementation und dort wird überprüft, ob es sich bei dem Attribut um einen Descriptor handelt. Wenn ja, wird dieser ausgeführt.

[Python 3 Docs: Descriptor HowTo Guid -> invocation from an intsnace](https://docs.python.org/3/howto/descriptor.html#invocation-from-an-instance)

[Stackoverflow: Attribute-Lookup-Tree](https://stackoverflow.com/a/55345947)

<br/>

#### 1.3.4 Zusammenfassung

Zusammengefasst sollte man über den Attributszugriff folgendes behalten:

1. Bei einem Zugriff wird die \_\_getattribute\_\_ bis hoch zur default Implementation durchgefahren. (Sofern eine Klasse auf dem Weg dies nicht Abfängt)
2. Dort wird dann überprüft, ob es sich bei dem Attribut um einen Descriptor handelt.
3. Handelt es sich um ein Descriptor?
   - Wenn ja, dann benutze \_\_get\_\_ des Descriptors.
   - Wenn nein, dann schaue nach, ob das Attribut im instanz.\_\_dict\_\_ vorhanden ist.
4. Wenn es nicht im instanz.\_\_dict\_\_ zu finden ist, dann wird ein AttributError erhoben. Der AttributError triggert in diesem Fall dann eine Suche nach der Fallbackmethode \_\_getattr\_\_.
5. Existiert eine \_\_getattr\_\_-Alternative?
   - Wenn ja, führe sie aus
   - Wenn nein, Script wird mit dem AttributError beendet

Das ganze gilt auch für \_\_setattr\_\_, \_\_setitem\_\_ und \_\_set\_\_. Alles analog zu diesem hier.

Es gibt keine \_\_setattribute\_\_, da beim Schreiben autoamtisch ein neues Attribut erstellt wird, falls es dies noch nicht gibt. Wenn man das Abfangen möchte -> Metaklassen oder in der \_\_setattr\_\_ ein Abfrage implementieren. Gibt ein paar Möglichkeiten.
