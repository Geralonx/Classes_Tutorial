# Inhalt des Tutorials

- [Vorwort](#vorwort)
- [Vorbereitende Erklärungen](#vorbereitende-erklärungen)
  - [F-Strings](#f-strings)
  - [List-Comprehensions](#list-comprehensions)
- [Kapitel 1 Fortgeschrittenes Klassen Design](#kapitel-1-fortgeschrittenes-klassen-design)

  - [1.0 Style-Guides](#10-Style-Guides)
  - [1.1 Klassen Recap](#11-klassen-recap)
    - [1.1.1 Allgemein](#111-allgemein)
    - [1.1.2 Public, Private und Protected](#112-public,-private-und-protected)
    - [1.1.3 Klassenattribute](#113-klassenattribute)
  - [1.2 'Dunder'-Methods](#12-'dunder'-methods)
    - [1.2.1 Allgemein](#121-allgemein)
    - [1.2.2 \_\_repr\_\_() oder \_\_str\_\_()](#122-__repr__-oder-__str__)
    - [1.2.3 \_\_enter\_\_ und \_\_exit\_\_](#123-__enter__-und-__exit__)
    - [1.2.4 \_\_doc\_\_ Attribut](#124-__doc__-attribut)
    - [1.2.5 \_\_call\_\_ Method](#125-__call__-method)
    - [1.2.6 Weitere 'Dunder'-Methods](#126-weitere-'dunder'-methods)
    - [1.2.7 Attribut Zugriff](#127-attribut-zugriff)

- [Kapitel 2 Spezielle Funktionsdekoratoren für Klassenmethoden](#kapitel-2-spezielle-funktionsdekoratoren-für-klassenmethoden)
  - [2.1 @Classmethod und @Staticmethod](#21-@classmethod-und-@staticmethod)
    - [2.1.1 @Staticmethod](#211-@staticmethod)
    - [2.1.2 @Classmethod](#212-@classmethod)
  - [2.2 Method Overloading](#22-method-overloading)
    - [2.1.1 Optionale Parameter](#211-optionale-parameter)
    - [2.1.2 @property, @fn.setter, @fn.deleter](#212-@property,-@fn.setter,-@fn.deleter)
    - [2.1.3 Weiteres Overloading](#213-weiteres-overloading)
- [Kapitel 3 Klassenvererbungen](#kapitel-3-klassenvererbung)
  - [3.1 Spezifizieren von Klassen](#31-spezifizieren-von-klassen)
  - [3.2 Komponieren von Klassen](#32-komponieren-von-klassen)
  - [3.3 \_\_mro\_\_ und super()](<#33-__mro__-und-super()>)
- [Kapitel 4 Discriptor Protokol](#kapitel-4-discriptor-protokol)
  - [4.1 Allgemein](#41-allgemein)
- [Kapitel 5 Klassendekoratoren](#kapitel-5-klassendekoratoren)
- [Kapitel 6 Metaklassen](#kepitel-6-metaklassen)
  <br/><br/>

## Vorwort

### Allgemein

So Leude, mein letztes Python-Tutorial ist schon 5 Monate her und inzwischen habe ich einerseits Lust ein neues zu machen und andererseits auch wieder einige Dinge gelernt, welche ich euch überhaupt zeigen könnte.

Warum mach ich das überhaupt? Ehrlich gesagt mache ich das weniger fürs Andere, als für mich selbst. Ich bin der Meinung, wenn man Anderen etwas richtig erklären kann, dann hat man es auch wirklich verstanden. Die Zeit, die ich hier rein investiere, ist in erster Line für mich selbst, um einerseits neue Dinge zu lernen und die Dinge anschließend zu festigen. Die Informationen, die ich für dieses Tutorial zusammentrage, stammen aus vielen Quellen und beispielsweise auch Videomaterial, welches mehrere Stunden beinhaltet. Ich fasse diese Informationen in einer Form zusammen, wie ich sie für sinnvoll und zusammenhängend halte. Für mich entsteht in diesem Prozess ein Dokument, welches alles zu dem Thema beinhaltet, um die gezeigten Inhalte zu verstehen und dies anschließend auf die nicht gezeigten Inhalte übertragen kann.

Andere Leute machen auch Tutorials und wahrscheinlich sogar deutlich besser als ich. Wer mit der Einstellung, "Warum sollte ich mir **DEIN** Tutorial durchlesen, wenn es andere/bessere gibt?", hierher kommt sollte einfach wieder gehen und sich eben die besseren Tutorials durchlesen und mich nicht mit sowas nerven. Für alle Anderen, die ernsthaft interessiert sind und mein erstes Tutorial sogar ganz gut fanden, stelle ich diese Tutorial Repo gerne zur Verfügung und bin im Anschluss auch für weitere Fragen/Disskussionen gerne da.

Bitte den [Disclaimer](#disclaimer) beachten.
<br/><br/>

---

### Für wen ist dieses Tutorial geeignet?

Dieses Tutorial geht schnell über Python-Grundlagen hinaus und befasst sich im Kern mit Klassen und deren speziellen Methoden ('Dunder'-Methods), welche bei der Verwendung von der 'Built-In' Methoden und Syntax verwendet werden. Wenn du nur wissen willst, wie man allgemein Klassen in Python schreibt und verwendet, dann solltest du woanders nachschlagen.

David Beazley hat vor vielen jahren ein Tutorial über Metaprogrammierung gegeben, an welchem ich mich auch Teilweise bediene (wird aber alles auch referenziert), in dem er in 3 Stunden vorführt, wie man mit diesem Programmierstil über die Grenzen der normalen Vernwendung von Python hinaus geht.

<sub>(Am Ende 'hackt' er den import, sodass er Sourcecode über ein XML File direkt importieren kann. Ich müsste es noch 10 Mal anschauen, um exakt zu verstehen, wie das dann geht.)</sub>

> "It's basicly walking trough a class and it's like doing brain surgery on it. It's probably a really bad idea." \- David Beazley in [YouTube: Python 3 Metaprogramming](https://youtu.be/sPiWg5jSoZI)

<br/>

Wenn man einmal versteht, was bei den Prozessen der Erstellung, Initialisierung, Zugriff, Vererbung, etc. von Klassen stattfindet, dann kann man auch exakt an diesen Stellen seinen eigenen Eingriff vornehmen. Da im Wesentlichen **alles** in Python ein Objekt ist, ist es möglich jedes Objekt so anzupassen, wie man es benötigt. Und das ganze auf einer Ebene, wo der Benutzer der Klassen gar nicht mehr mitbekommtn, was im Hintergrund alles passiert.

Metaklassen sind eigentlich für 99% der Nutzer von Python unrelevant. Das benötigen hauptsächlich Framework/Libary Entwickler. Aber bis zu dem Kapitel soll dieses Tutorial allgemein die fortgeschrittene Vernwednung von Klassen beschreiben. Und das ist bestimmt für mehr als 1% der Leute interesannt.
<br/><br/>

---

### Kritik

Zuerst sei gesagt, ich habe die Kritikpunkte unter dem letzten Tutorial alle
gelesen und ich möchte mich auch daran halten. Ersteinmal habe ich in diesem Post auf die Farben verzichtet. Als zweites habe ich das ganze Tutorial auf GitHub gepackt, mit Code, mit Kommentaren und weiteren Texten, welche detaillierter auf die Inhalte eingehen.

Insagesamt wird dieses Tutorial auf mehrere Beiträge gesplitted, einfach weil
das Thema zu groß ist, ja, sogar wenn ich die maximale Größe eines Bildes hier
ausnutzen würde, würde ein Beitrag nicht reichen. Außerdem möchte ich die
einzelnen Beiträge kürzer halten.
<br/><br/>

---

### Hater

Für die, die sagten pr0 sei nicht die Plattform für sowas, bitte Minus geben und weiterziehn.
<br/><br/>

---

### Prerequisites / Vorraussetzungen

Um die gezeigten Inhalte zu verstehen solltet ihr bereits die Grundlagen von Python kennen. Dazu gehört allgemein die Syntax, wie man Funktionen und Klassen erstellt und eventuell soagr, dass **alles** in Python Objekte sind. Klassen sind Objekte, Funktionen sind Objekte, selbst eine Variable ist nur ein Objekt einer bestimmten Klasse. Des Weiteren solltet ihr auch ungefähr wissen was Vererbungen/Inheritance sind. Ich werde es nochmal im Detail erklären, dennoch geht es auch bei dem Thema eher um die Tiefe statt die einfache Anwendung. Dictionarys! In Python findet man überall Dictonarys, weswegen es essentiell ist, dass ihr diese im Vorfeld kennt und wisst was man damit machen kann. (dict.keys(), dict.values(), dict.items(), Dicts sind mutable Objekte...) Die letzte Vorraussetzung sind dann noch 'Closures / Decorators', welche ich bereits in meinem ersten 'Tutorial' erklärt habe (Link im Kommentar).
<br/><br/>

---

### IDE

Da es in dem ersten Beitrag auch zur Sprache kam erwähne ich es hier nochmal explizit, ich arbeite vollständig mit VSCode und habe mir diese IDE inwzischen schon recht stark Modifiziert. Color-Themes, Boilerplates/Snippets, indentation und bracket Colors, Autoformatting und ein paar Andere. Für einige ist es sicher zu bunt, mir gefällts halt.
<br/><br/>

---

### Disclaimer

Jeder macht Fehler. Ich beanspruche keineswegs Vollständig- oder Richtigkeit der hier gezeigten Inhalte. Für weitere Details und noch tiefergehende Informationen empfehle ich grundsätzlich die [Python-Dokumentation](https://docs.python.org/3/).

Ich möchte mit diesem 'Tutorial' einen tieferen Einblick in die elementaren Dinge von Python vermitteln. Auch ich habe währen des Schreibens viel nachlesen und recherchieren müssen. Ich biete hiermit lediglich eine zusammengefasste Form der Informationen an, welche ich auf eine Weise darstellen möchte, wie ich sie für logisch und verständlich halte.

Diese Zusammenfassung/Tutorial soll eigenständig sein. Ich habe Informationen auch für gleiche Themen aus verschiedenen Quellen zusammengetragen, wodurch dieses gesamte Tutorial sehr groß geworden ist. Vielleicht bin ich auch einfach zu doof, um Kurzfassungen zu verstehen, aber dieses Tutorial ist in einer Form wo ich denke, dass dies alles enthält, ohne dass man in 10 verschiedene Quellen gucken muss, um eine einzige Sache zu verstehen.
<br/><br/>

---

### Korrektur meiner Aussage im ersten Tutorial zu 'Clouseres / Decorators'

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

<br/>

---

## Vorbereitende Erklärungen

Dieses Tutorial richtet sich zwar schon an Leute die bereits die Grundlagen von Python kennen und verstehen, aber ich werde kurz f-Strings und List-Comprehensions erklären, weil ich diese Konzepte in den Codebeispielen regelmäßig verwende, wer das kennt, kann diesen Teil überspringen. Und direkt mit [Kapitel 1](<#kapitel-1:-fortgeschrittenes-(klassen)-design>) starten.

---

### f-Strings

F-Strings steht für "formatted string literals". Sie kennzeichnen sich dadurch aus, dass vor dem Anführungszeichen des Strings ein f steht. (Klein- oder Großschreibweise spielt dabei keine Rolle, typischerweise verwendet man das kleine f). Innerhalb des Strings dürfen geschweifte Klammern stehen, welche einen Pythonausdruck enthalten. Im einfachsten Fall ist das eine Variable, komplexere Ausdrücke funktionieren aber auch.

Die f-Strings wandeln den Ausdruck der geschwiften Klammen in einen String um und werden im Anschluss ein ganz normaler String behandelt. Die Idee dahinter ist, dass man im Code den String vollständig beschreibt und auch ohne die eingefügten Inhalte zu kennen weiß, wie dieser String am Ende aussieht.

```py
mein_name = 'Geralonx'
mein_alter = 30
gruss = f"Grueß dich, mein Name ist {mein_name}, ich bin {mein_alter} Jahre alt."
print(gruss)


# Vorgänger Methode
gruss_alt = "Grueß dich, mein Name is {}, ich bin {} Jahre alt.".format(mein_name, mein _alter)
```

<pre>
> Grueß dich, mein Name ist Geralonx, ich bin 30 Jahre alt.
</pre>

Mit der alten Methode reißt es einem beim Lesen des Codes aus dem Fluss. Man muss in die Format-Methode am Ende reingucken und sich dann selbst noch die übergeben Attribute in den String denken. F-Strings sollen es halt einfacher machen.

<sub>(Randnotiz 1: Auch wenn es f-Strings bereits Seit Python 3.6 (2016) gibt bin ich erst dieses Jahr vollständig auf die Verwendung von f-Strings umgestiegen. Vorher habe ich immer mit .format() gearbeitet, weil mir diese Darstellung sehr gut gefiel und ich die es deshlab nicht für nötig hielt mir die f-Strings anzugucken.</sub>

<sub>(Randnotiz 2: Ja, die gezeigte .format() Methode ist in dieser Form die einfachste Version. Man konnte dort auch schon mit Keywords innerhalb der geschweiften Klammern arbeiten, um einen 'Lesefluss' zu erzeuge, aber es bleibt dabei, dass man am Ende die Zuweisung erst im .format() erkennt und nich direkt im String selber.)
</sub>

<br/>

---

### List-Comprehensions

List-Comprehensions sind präzise Ausdrücke, um eine Liste mit Ergebnissen von einer Operation, welche auf die einzelnen Mitglieder einer Sequenz oder Iterator angewendet werden, zu erzeugen (Frei übersetzt aus der Python-Dokumentation). Bitte was? Im häufigsten Fall ersetzten List-Comprehensions for-Loops, welche eine Liste oder ein Dict erzeugen. Die Syntax einer List-Comprehension sieht folgendermaßen aus:

<pre>
> liste = [expression for item in sequence [, condition]]
</pre>

Beispiel / Vergleich mit einer for-Loop:

```py
# For-Loop um die Quadrate der Zahlen 0-9 zu erzeugen
for_loop_list = []
for i in range(10):
    for_loop_list.append(i*i)

# List-Comprehension um die Quadrahte der Zahlen 0-9 zu erzeugen.
list_comp_list = [i*i for i in range(10)]

# expression : i*i
# item : i
# sequence: range(10)


# Ausgabe
print("For-Loop-Result:\t", for_loop_list)
print("List-Comp-Result:\t", list_comp_list)
```

<pre>
> For-Loop-Result:         [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> List-Comp-Result:        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
</pre>

Die List-Comprehension vereinigt 3 Zeilen Code von einer Empty-List-Initialisierung und das Füllen mit einer for-Loop zu einer einzigen. Es ist auch möglich Bedingungen in die List-Comprehension einzubauen.

```py
# List Comprehension mit einer Bedingung, welche nur die geraden Zahlen quadriert.
new_list = [i*i for i in range(10) if i%2 == 0]
print(new_list)

# Das Gleiche Ergebnis ließe sich beispielsweise mit folgendem Code erreichen
new_list = []
for i in range(10):
    if i%2 == 0:
        new_list.append(i*i)
```

<pre>
> [0, 4, 16, 36, 64]
</pre>

List-Comprehensions können die Leserlichkeit verbessern, wenn man sie versteht und lesen kann. Einfache List-Comprehensions schneiden von der Performance meistens auch noch besser ab als die entsprechenden for-Loop Konstrukte. Darauf möchte ich aber nicht tiefer eingehen.

Man kann mit List-Comprehension aber auch ganz schönen Unfug treiben und den Scheiß unendlich tief verschachteln oder vieles mehr. Ich werde dazu auch ein File verlinken, wo ich mal solche Konstrukte zeige und umschreibe.

Hier sind mal ein paar Methoden aus einer Klasse, welche ich zum WebScrapen der Steam-Angebote verwendet habe. Dort habe ich völlig übertrieben, um die List-Comps zu verstehen, aber das geht definitiv zu weit, wenn es um einfach zu verstehenden Code geht.

```py
def filter_games_by_tags(self, tag):
    filtered_list = [game for game in self.steam_discount_list if(game['tag_list'] is not None and set(tag).issubset(game['tag_list']))]
    return filtered_list

def filter_games_by_price(self, max_price, min_price=0.00):
    filtered_list = [game for game in self.steam_discount_list if(min_price < game['actual_price'] <= max_price)]
    return filtered_list

def most_common_tags(self):
    all_tags_flat = [tag for game in self.steam_discount_list if game['tag_list'] is not None for tag in game['tag_list']]
    occur = [[tag, all_tags_flat.count(tag)] for tag in set(all_tags_flat)]
    self.most_common_tags = sorted(occur, key = lambda x: x[1], reverse=True)
```

Funktioniert es? Ja. Ist es einfach zu verstehen? Nein. Zur Übung oder aus Langeweile könnt ihr diese Konstrukte ja mal auseinander nehmen, gerade die Methode 'most_common_tags' ist übel, wenn man noch nicht genau verstanden hat, wie diese aufgebaut sind.
<br/>

<sub>(Hint: Zerlegt die Comprehension von hinten oder von vorne und stoppt immer bei Keywords wie if oder for. Nehmt den Teil bis zu dem Keyword und schmeißt alles bis dahin in eine eigene Zeile. Wenn man von hinten anfängt, dann baut man das Konstrukt von innen nach außen auf, umgekehert wenn man vorne anfängt. Am Ende muss man nur noch die Expression, also den vordersten Teil, in das innere übersetzten. Eine Schritt für Schritt Anleitung ist hier: [Loesung List-Comprehension](https://github.com/Geralonx/Classes_Tutorial/blob/master/Vorbereitende_Erklaerungen/_2_list_comp_loesung.py)) </sub>

<sub>(Randnotiz 1: Es gibt das gleiche auch für Dicts, also Dict-Comprehensions. Die Syntax ist 1:1 wie ber für die List. Das einzige was sich ändert ist, dass man die Comprehensions mit {} statt [] schreibt und sicherstellen muss, dass die Expression ein Key-Value-Pair ist.)</sub>
<br/><br/>

---

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
<br/><br/>

---

### 1.1 Klassen Recap

#### 1.1.1 Allgemein

Wie, wann und wo man Klassen verwenden sollte oder nicht möchte ich gar nicht disskutieren. Ich sebst verwende Klassen auch manchmal dort, wo der ein oder andere sicherlich sagen würde, dass sie dort überflüssig seien. Der Hauptgrund warum ich Klasse überhaupt verwende ist 'Encapsulation'. Das heißt so viel wie, dass die Daten und die Methoden, welche jene Daten modifizieren, einfach zusammengepackt werden, damit ein eineindeutiger Zusammenhang besteht.

Die einzige Regel die auch ich grundsätzlich beachte ist aus folgendem Zitat abzuleiten. (Das heißt natürlich nicht, dass man sofort ab 2 zugehörigen Methoden und init eine Klasse schreiben sollte, aber ich denke ihr versteht den Punkt.)

> "The signature of 'this should't be a class' is, that it has two methods one of which is
> init. Any time you see that, you should probably think 'hey, maybe I just need one method'."
> \- Jack Diederich in [YoutTube: Stop Writing Classes](https://youtu.be/o9pEzgHorH0)

<br/>

---

#### 1.1.2 Public, Private und Protected

Meine beste Sprache ist Python, ich habe C und C++ als erste Sprachen gelernt, aber damit habe ich schon ewig nicht gearbeitet. Weswegen ich hier nicht generell für alle OOP-Sprachen sprechen kann. Mein Verständnis für Public, Private, Protected kommt eben aus C++ und das liegt bei mir schon Jahre zurück. Also verzeiht, wenn ich diesbezüglich nicht alles so genau weiß und hier etwas Erkläre, was selbtsverständlich ist, wenn man sich in der anderen Sprache tief genug auskennt.

**Public**<br/>
Man kann eigentlich sagen, dass **ALLES** innerhalb einer Python Klasse public ist. Es gibt Konzepte und Conventionen, welche die Idee von Private und Proteced nachahmen sollen, aber wenn man sich auskennt, dann kann man auch diese Dinge ohne Aufwand umgehen. (An dieser Stelle fehlt mir die Erfahrung in anderen OOP-Sprachen, um zu wissen, ob dies auch dort einfach zu umgehen ist.)

**Private**<br/>
Wer aus anderen objektorentieren Sprachen kommt wird das Konzept von Public, Proteced und Private kennen. Soetwas gibt es in Python nicht. Wer jetzt schonmal die Basics von Klassen in Python kennt wird vielleicht den Finger heben und Fragen: "Was ist denn mit den \_\_vars und \_\_methods()?" (Zwei Unterstriche, falls dies im Text nicht deutlich raus kommt.)

Wenn der Python-Interpreter innerhalb einer Klasse ein Attrribut oder Methode mit zwei führenden Unterstrichen und maximal einem nachfolgenden Unterstrich erkennt, führt dieser ein sogenanntes 'Name Mangling' durch. Das heißt, er bennent die Attribute und die Methoden, die dieser Form folgen, schlicht und ergreifend einfach um.

Beispiel:

```py
01  class PC:
02     def __init__(self, cpu, gpu, ram):
03         self.cpu = cpu
04         self.gpu = gpu
05         self.__ram = ram
06
07  meine_pc_instanz = PC('Ryzen 7', 'RTX2070Super', 'GSkill')
08
09  print(meine_pc_instanz.cpu)
10  print(meine_pc_instanz.gpu)
11  print(meine_pc_instanz.__ram)
```

Die 3 Prints haben folgende Ausgabe:

<pre>
> Ryzen 7
> RTX2070Super
> Traceback (most recent call last):
>   File "f:/Python-Projects/Projects/Classes_Tutorial/name_mangeling.py", line 11, in <module>
>     print(meine_pc_instanz.ram)
> AttributeError: 'PC' object has no attribute '__ram'
</pre>

So gesehen besteht von Außen kein direkter Zugriff auf das Attribut \_\_ram. Der Grund dafür ist, es gibt dieses Attribut gar nicht mehr. Wenn man wissen will, was in einem Obejkt enthalten ist, dann muss man sich das \_\_dict\_\_ Attribut einer Instanz anschauen. Es enthält **alle** instanzspezifischen Attribute, also alles was zu self zugewiesen wird. Gebe ich dieses \_\_dict\_\_ nun aus sehen wir, was die Instanz wirklich enthält.

```py
print(meine_pc_instanz.__dict__)
```

<pre>
> {'cpu': 'Ryzen 7', 'gpu': 'RTX2070Super', '_PC__ram': 'GSkill'}
</pre>

Wir sehen, dass _cpu_ und _gpu_ wie zu erwarten enthalten sind, aber wir sehen auch, dass unser _\_\_ram_ wieder da ist. Das Name Mangling hat dafür gesorgt, dass der Klassenname mit einem führenden Unterstrich an den Anfang des Attributs gesetzt wurde.

Versuche ich folgendes

```py
print(meine_pc_instanz._PC__ram)
```

<pre>
> GSkill
</pre>

habe ich dennoch Zugang zu den eigentlich 'privaten' Attributen innerhalb einer Klasse. Dennoch findet diese Form Anwendung. Das Name Mangling verhindert eben Namespace Kollisionen, wenn die Klasse vererbt wird. Das heißt, wenn ich aus irgendeinem Grund sicherstellen muss, dass ein Attribut oder eine Methode für eine Klasse durch Vererbung nicht verändert werden darf, dann erreiche ich das mit dieser Form. Denn würde ich ein weiteres \_\_ram Attribut in einer vererbten Klasse erstellen, dann würde dies durch das Name Mangling den Namen der vererbten Klasse vorgestellt bekommen.

<sub>(Randnotiz 1: Warum kann ich innerhalb von Klassen dann mit self.\_\_ram an das Attribut kommen? Ganz einfach, der Interpretert bennent innerhalb einer Klasse ALLE vorkommenden Attribute und Methoden mit 2 führenden Untersichten mittels Name Mangling um. Außerhalb von Klassen eben nicht.)
</sub>

<br/>

**Protected**<br/>
Protected, also das Attribute und Methoden nur von der Klasse und von vererbten Klassen 'gesehen/verwendet' werden können gibt es gar nicht. (Warum auch, nicht einmal ein echtes Private gibt es.)

Unter Python Entwicklern gibt es die Convention, dass 'protected' innerhalb von Klassen mittels einem führenden Unterstrich gekennzeichnet werden. Das ist aber lediglich ein Hinweis für Andere. Der Python-Interpreter selbst behandelt Attribute und Methoden mit einem führenden Unterstrich nicht anders als ohne.
<br/><br/>

---

#### 1.1.3 Klassenattribute

Klassenattribute sind Attribute, welche nicht im Instanz-Dict erstellt werden, sondern bereits vor der Instanziierung auf Klassenebene existieren.

Klassenattribute existieren **nur** auf Klassenebene. Wenn man über eine Instanz auf ein Klassenattribut zugreift ist das möglich, weil Python, sobald das Attribut auf Instanzebene nicht zu finden ist, in der Klasse weiter sucht. Dies Zieht sich auch durch Vererbungen durch.

```py
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"

meine_pc_instanz = PC()

print("Instanz Dict: ", meine_pc_instanz.__dict__)
print("Klassen Dict: ", PC.__dict__)
print("Zugriff über Instanz: ", meine_pc_instanz.klassen_attribut)
```

<pre>
> Instanz Dict: {}
> Klassen Dict: { ..., 'klassen_attribut': 'Ich bin ein Klassenattribut', ...}
> Zugriff über Instanz: Ich bin ein Klassenattribut
</pre>

Wenn man weiß, dass man das Klassenattribut über das Instanz-Objekt lesen kann, dann stell ich mir die Frage, was passiert, wenn man es über die Instanz versucht zu schreiben.

```py
meine_pc_instanz.klassen_attribut = "Neuer Wert"
print(meine_pc_instanz.klassen_attribut)
```

<pre>
> Neuer Wert
</pre>

Super, das funktioniert auch, aber was ist jetzt passiert? Um wirklich zu wissen, welche Daten zu welcher Instanz/Klasse gehören müssen wir ja nur das \_\_dict\_\_ ausgeben.

```py
print("Instanz Dict: ", meine_pc_instanz.__dict__)
print("Klassen Dict: ", PC.__dict__)
```

<pre>
> Instanz Dict:  {'klassen_attribut': 'Neuer Wert'}
> Klassen Dict:  {..., 'klassen_attribut': 'Ich bin ein Klassenattribut', ...}
</pre>

Die leere Instanz hat nun ein eigenes Attribut mit dem Bezeichner 'klassen_attribut' bekommen und das echte Klassenattribut blieb unverändert. Der richtige Weg mit Klassenattributen umzugehen ist immer, dass man über die Instanz auf die Klasse zugreift und anschließend auf das Attribut. Das sieht dann folgendermaßen aus:

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
<br/><br/>

**Vererbung von Klassenattirbuten**<br/>

Durch Vererbung von 'Klasse 1' (Elternklasse) auf 'Klasse 2' (Kindklasse) ist das Klassenattribut auch dort verfügbar, **aber** es wird nicht im \_\_dict\_\_ der 'Klasse 2' aufgeführt. Erstellt ihr eine Instanz von 'Klasse 2' habt ihr mit einem Klassenattribut innerhalb 'Klasse 1' Zugriff auf ein Attribut, welches ihr weder im Instanz-Dict der erstellen Klasse, noch im Klassen-Dict der verwendeten Klasse seht. Das ist meiner Meinung nach... Naja beschissen, zumal ein Klassenattribut der 'Klasse 1' durch die Instanzen von Klasse 1 verändert werden könnten, welche sich anschließend auch in den Instanzen der Kindklassen wiederspiegeln. Seid einfach Vorsichtigt, wenn ihr Klassenattribute aus Elternklassen verwendet.

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

<sub>(Randnotiz 1: Ich habe bisher nicht sehr viel mit Klassenattributen gearbeitet, lediglich habe ich sie als 'Konstanten' verwendet. Ich denke aber ich würde sie einfach immer 'privat' machen, einfach um nicht ausversehen aus vererbten Klassen auf etwas zugreifen zu können, was ich erstmal ewig suchen müsste. Ob man das so macht weiß ich nicht.)</sub>

<sub>(Randnotiz 2: Natürlich, wenn ihr jetzt verstanden habt wie es geht, dann ist der Zugriff immernoch möglich, aber es verhindert im ersten Schritt Kollisionen, wenn man über sowas gar nicht nachdenkt. (Beispielsweise könnte man ja alle Elternklassen auslesen und anschließend das Dict jener und mit dem Namen der Klasse nach Allem suchen was dem Muster f"\_{parent_class}\_\_" folgt.) Des Weiteren könnt ihr damit immernoch Attribute vor Anfängern oder unwissenden 'verstecken', denen beispielsweise nur die Kindklassen zur Verfügung stehen.)</sub>
<br/><br/>

---

### 1.2 'Dunder'-Methods

Um das Klassendesign im fortgeschrittenen Stil zu verstehen und anwenden zu können muss man die Idee hinter den 'Dunder'-Methods kennen (Dunder steht für 'Double Underscores'). Diese speziellen Methoden erfüllen einzigartige Aufgaben, welche durch die allgemeine Syntax und die 'Built-In' Methoden von Python aufgerufen/abgefragt werden. Ich werde selbstverständlich nicht alle im Detail vorstellen und zeigen, sondern anhand von einzelnen Beispielen die Funktion von 'Dunder'-Methods erklären und auf ein paar besondere hinweisen. Um sie sinnvoll anzuwenden zu können müsst ihr sowieso die Dokumentation lesen, da es für manche 'Dunder'-Methods gewisse Regeln gibt, wie beispielsweise, dass die Rückgabe ein nur bestimmten Datentyp sein darf oder in einem definierten Bereich liegen muss.
<br/>

---

#### 1.2.1 Allgemein

Jeder der in Python bereits eine Klasse geschrieben hat wird mindestens die

```py
def __init__(self, arg1, arg2, ...)
```

verwendet haben. 'Dunder'-Methods sind Methoden, welche im allgemeinen Fall **nicht** direkt über ihre Bezeichnung aufgerufen, sondern über die Syntax oder andere 'Built-In' Methods von Python. Sie **können** zwar über die Bezeichnung der 'Dunder'-Methods direkt aufgerufen werden, aber es widerspricht ihrem Sinn. (Ausgenommen innerhalb der Klassendefinition selbst, dazu später mehr.)
<br/>
<sub>(Ich kenne ehrlich gesagt keinen Fall indem man außerhalb der Klassendefinition die 'Dunder'-Methods über ihre Bezeichnung verwenden sollte.)</sub>

```py
# 'Falscher' Weg (Funktioniert, aber man macht es nicht)
# __new__ erstellt eine leere Instanz einer Klasse
my_class_instance = MyClass.__new__(MyClass)
# __init__ initialisiert die übergebene Instanz
MyClass.__init__(my_class_instance, arg1, arg2, ...)


# Richtiger Weg
# Beim Instanziieren einer Klasse über den richtigen Konstrukor werden die
# __new__ (und __prepare__) Methoden automatisch vor der Initialisierung durchgeführt.
my_class_instance = MyClass(arg1, arg2, ...)
```

Dieses Beispiels sollte verdeutlichen, dass man zum einen jede 'Dunder'-Method über ihre Bezeichung aufrufen kann. Außerdem sollte auch klar sein, dass jede Methode einer Klasse direkt über die Klasse selbst aufgerufen werden kann, wenn man an der ersten Stelle die Instanz als das _self_-Argument übergibt.

<br/>
Beispiel für die Verwendung von 'Dunder'-Methods durch 'Built-In'-Methods:

Die 'Dunder'-Method \_\_len\_\_(self) wird über die 'Built-In' Method
len() aufgerufen. Was diese \_\_len\_\_(self) Methode am Ende durchführt ist
komplett euch überlassen. Die einzige Vorraussetzung ist, dass diese Methode
einen Integer >=0 zurück gibt. Bevor ihr die Vorraussetzung erfüllt, könnt ihr
ausführen, berechnen und hacken was ihr wollt, solange die Vorrausetzung erfüllt wird, ist alles in Ordnung mit der Implementation einer 'Dunder'-Method.

Sobald man aber in dieses Thema des fortgeschrittenen Designs kommt ist man mindestens an einem Punkt, wo man den Code wiederverwenden will, wenn nicht sogar für Andere bereitstellen muss/möchte. Also sollte man sich fragen, was würde jemand anderes bei der Verwendung einer 'Dunder'-Method eigentlich erwarten? Bzw. warum sollte man diese Methode überhaupt auf die Instanz einer Klasse anwenden können?

Will ich die Instanz meiner Klasse mittels for-Loop durchlaufen, dann benötige ich die 'Dunder'-Methods \_\_iter\_\_ und \_\_next\_\_. Will ich zwei Instanzen miteinander verrechnen oder vergleichen können, dann benötige ich die 'Dunder'-Methods \_\_add\_\_, \_\_sub\_\_, \_\_gt\_\_, ... usw.

<sub>(Randnotiz: \_\_len\_\_(self) ist übrigens die Fallback-Methode für \_\_bool\_\_(self). Das heißt, wenn keine Dunder-bool-Method definiert ist wird die Dunder-len-Method verwendet. Alles was >0 ist wird von Python als True interpretiert.)</sub>
<br/><br/>

Für Vergleiche oder arithmetische Operationen gilt das Gleiche. Will ich die Instanzen meiner Klasse miteinander addieren können, dann brauche ich die \_\_add\_\_ Method usw.

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

<sub>(Randnotiz 1: Das _other_ Argument in den Vergleichs- und Rechenoperationen kann **alles** sein, was auf der rechten Seite des '+' steht. Behaltet es im Hinterkopf, an solchen stellen evnetuell ein instance/type Checking durchzuführen, damit ihr das abfangt, falls nötig. [_5_dunder_other.py]) </sub>

<sub>(Hint: Die standard Libary functools bietet einen Classdecorator (@total_ordering), welcher einen Shortcut für die Vergleichsoperationen liefert. Das heißt, statt alle Dunder-Methoden für '>', '<', '==', '!=', '>=', '<=' selbst zu implementieren müsstet ihr nur '==' und eine der größer oder kleiner als Methode implementieren und hättet dennoch alle Verglichsoperationen zur verfügung.)</sub>

<br/>

Ich selbst hatte keine Idee, wie man eine allgemeine Zusammenfassung für die 'Dunder'-Methods formulieren könnte. Das hat jemand anderes aber sehr gut hinbekommen.

> A dunder method is an implicit function, that is being called behind the
> scenes of an explicit operation or a function. \- Iakshayarora7 (https://www.djangospin.com/python-dunder-methods-attributes/)

<br/>

Python-Dokumentation über (alle?) Special 'Dunder' Methods: https://docs.python.org/3/reference/datamodel.html#special-method-names

<br/>

---

#### 1.2.2 \_\_repr\_\_ oder \_\_str\_\_

Wenn man gute und ausgereifte Klassen designen will, dann sollte man auf diese beiden 'Dunder'-Methods nicht verzichten. Sie können in jeder Klasse ihren Platz finden, da sie lediglich Informationen enthalten, welche die Klasse und ihren Inhalt beschreiben sollen.

<sub>(Randnotiz 1: Die \_\_repr\_\_ Method ist die Fallback-Methode für den Fall dass str() auf ein Objekt angewendet wird und keine \_\_str\_\_ Method definiert ist. Umgekehert ist dies nicht der Fall. Wendet man repr() auf ein Obejkt an wird **nicht** die \_\_str\_\_ Method als Alternative verwendet, falls es keine \_\_repr\_\_ Method gibt.)</sub>

<br/>
__str__(self)

Die Dunder-str-Method ist dazu gedacht, eine Darstellung des Objekts zurückzugeben, welche für den Benutzer einfach zu lesen und zu verstehen ist. Sie **muss** einen String zurückgeben. Was ihr am Ende für einen String durch die Dunder-str-Methode zurück gibt ist euch überlassen. Der Sinn sollte am folgenden Beispiel klar werden.

Kleines Beispiel:

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
            msg += f"\n\t{key}: \t{value} \t| ({type(value)})"

        return msg

meine_pc_instanz = PC('Ryzen 7', 'RTX2070Super')
print(meine_pc_instanz)
```

Ausgabe, hervorgerufen durch print(meine_pc_instanz):

<pre>
> Diese Instanz ist von der Klasse: PC
> Sie hat folgende Attribute:
>        cpu:      Ryzen 7         | (class 'str')
>        gpu:      RTX2070Super    | (class 'str')
</pre>

<sub>(Randnotiz 2: Eigentlich wird die der Type mit den <> dargestellt (<class 'str'>). Aufgrund der verwendeten Markuplanguage (.md) funktioniert das da nicht.)</sub>

<sub>(Randnotiz 3: Warum sollte ich die Klasse der Attribute ausgeben, ist das nicht eindeutig? Für die 'Built-In' Klassen wie str, int, list, ... scheint es überflüssig zu sein. Angenommen ihr verwendet eigene Klassen, die die Funktionalität der Grundklassen erweitern. Eine eigene Klasse z.b. <class '\_\_main\_\_.SizedStr'>, welche das Attribut auf eine maximale Länge limitiert, würde dem Benutzer eine Erklärung geben, was dort eigentlich hintersteckt, statt dass dieses Attribut ein normaler String wäre, wie es im ersten Augenblick erscheint.)
</sub>

<br/>
__repr__(self)

Repr ist die Kurzform für 'Representation'. Die Dunder-repr-Method wird durch die 'Built-In' Methoden repr() aufgerufen. Der Rückgabewert der Dunder-repr-Method muss ebenfalls ein String sein. Und laut Python Dokumentation soll dieser String der Pythonausdruck sein, um jene Instanz zu erzeugen. Wenn das nicht möglich ist soll eine 'sinnvolle Beschreibung' zurückgegeben werden.

Was heißt das nun, 'der Pythonausdruck, um jene Instanz zu erzeugen'?

PC Beispiel:

```py
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def __repr__(self):
        argument_string_list = [f"{key}='{value}'" for key, value in self.__dict__.items()]
        init_string = ', '.join(argument_string_list)
        return f'{self.__class__.__name__}({init_string})'

meine_pc_instanz = PC('Ryzen 7', 'RTX2070Super')

print(repr(meine_pc_instanz))
```

Was zu folgender Ausgabe führen wird:

<pre>
> PC(cpu='Ryzen 7', gpu='RTX2070Super')
</pre>

<sub>(Randnotiz 1: Die Single-Quotes, welche um die '{value}' gepackt sind, sind in diesem Fall hardcoded um alle Argumente. Das funktioniert in diesem Fall nur, weil es bei sich bei Allen um Strings handelt. Man müsste die Dunder-repr-Method noch expliziter gestalten, um verschiedene Datentypen richtig zu unterscheiden. Dieses Beispiel geht lediglich allgemein auf die Dunder-repr-Method ein.)</sub>

<sub>(Randnotiz 2: Wer die join() Method nich kennt sollte sich die anschauen. Sie nimmt eine iteriebares Obejekt and und verknüpft alle Elemente zu einem String, sofern sich die str() Method auf die Elemente anwenden lässt. Wenn sich die Elemente nicht in einen String umwandeln lassen wird ein TypeError erhoben. Der erste Teil (In diesem Fall ', ') ist der Seperator. Der Seperator wird zwischen die einzelnen Teilelemente gepackt.)</sub>

<sub>(Randnotiz 3: Der repr, also die Represenation eines Objekts, wird von VSCode beispielsweise beim Debuggen verwendet. Wenn man an einem Breakpoint steht, sieht man die Variablen an der Seite. Hinter der Variable steht eben die Representation. Ob und wie es von anderen IDEs verwendet wird weiß ich nicht. Ohne \_\_repr\_\_-Method würde dort allgemein (\_\_main\_\_.\_\_class_name\_\_ at 0x....) stehen, also Classe XY aus dem Main-File an Memoryposition 0x....)</sub>
<br/><br/><br/>

---

#### 1.2.3 \_\_enter\_\_ und \_\_exit\_\_

Enter und Exit werden von den sogeannten 'Contextmanagern' verwendet. Im Wesentlichen kommt dies zur Anwendung, wenn man vor der durchzuführenden Aufgabe etwas vorbereiten muss und nach erledigen der Aufgabe etwas nachbearbeiten (oder Aufräumen muss). Einige von euch werden es sicherlich schonmal von der 'Built-In' Methode _open()_ Gebrauch gemacht haben. Sie öffnet eine Datei und lädt sie in eine Variable. Wenn man eine Datei öffnet, dann sollte man sie auch wieder schließen. Die _open()_ Methode führt das Schließen mittels der \_\_exit\_\_ aus, wenn ein Contextmanager verwendet wird. Der Contextmanager wird mit dem Keyword _with_ verwendet. Ein anderes Beispiel sind Frameworks die eine Verbindung irgendwohin erstellen (Server, Datenbank, ...). Im Enter werden diese Verbindugen aufgebaut und im Exit wird diese Verbindung eben geschlossen. Schaut euch dazu einfach weitere Beispiele an, falls ihr das benötigt.

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

---

### 1.2.4 \_\_doc\_\_ Attribut

Dokumentiert eure Sachen. Muss man das noch sagen? In Python kann man die Dokumentation einer Klasse oder Funktion als _doc_-String hinterlegen. Der String wird in 3 Anführungszeichen (es gehen doppelte \" und einfache \', aber typischerweise werden doppelte verwendet. [PEP 257 - Docstrings](https://www.python.org/dev/peps/pep-0257/)) am Kopf der Funktion oder Klasse geschrieben.

Das \_\_doc\_\_ Attribut ist in jedem Objekt vorhanden, auch wenn keiner gesetzt wird. Falls keiner vom Author geschrieben wird, ist der Wert None.

Lest euch die Style-Guides zu dem Doc-Attribut durch. Dort gibt es schöne Anregungen, wie man eine Klasse oder Funktion ordentlich dokumentiert.

```py
class PC:
    """Dies ist die Dokumentation der Klasse: PC

    Multiline-Strings sind automatisch mit berücksichtig.
    Es wird sogar mit formatiert. Klasse! Oder?"""

    def __init__(self, prozessor, grafikkarte):
        """Jetzt Dokumentieren wir die __init__
        Was eine schöne Funktion."""
        self.prozessor = prozessor
        self.grafikkarte = grafikkarte

def outer_func(arg1):
    """Das funktioniert auch bei einfachen Funktionen!"""
    print(arg1)


print(PC.__doc__, "\n")
print(PC.__init__.__doc__, "\n")
print(outer_func.__doc__, "\n")
```

Ausgabe:

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
</pre>

Bei komplexeren Methoden werden häufig Input- und Outputargumente erklärt. Welcher Datentyp sie haben, was passiert, welche restricstions gelten. Also alles weis irgendwie hilfreich ist, um den Teil eben zu verwenden.

---

#### 1.2.5 \_\_call\_\_ Method

Mittels der call 'Duner'-Method kann man die Instanzen einer Klasse aufrufbar machen. Wer sich mit Funktionen und deren Implementation schon tiefer auskennt wird auch wissen, dass Funktionen in Python genau so impementiert sind.

```py
def func(x):
    return x+1

print(type(func))
```

<pre>
> >class 'function'<
</pre>

Dies lässt sich auch 1 zu 1 so implementieren:

```py
class func_class:
    def __call__(self, x):
        return x+1

my_instance = func_class()

print(my_instance(1))
```

<pre>
> 2
</pre>

---

#### 1.2.6 Weitere 'Dunder'-Methods

Während den Recherchen habe ich diese Seite gefunden, welche nochmal einen detaillierteren Überblick über viele 'Dunder'-Methods präsentiert. Wer noch mehr wissen will, einfach reinschauen. https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15

Allgemeine Zusammenfassung ist, wenn ihr mit eurer Klasse irgendeine Standardoperation (+, -, <, >, aufruf, len(), bool(), str(), dir(), ...) verwenden wollte, dann schaut einfach nach der speziellen 'Dunder'-Method dafür nach und ihr könnt das sauber dafür implementieren, statt euch irgendwelche Adapter workarounds zu basteln.

---

#### 1.2.7 Attribut Zugriff

Der Attributzugriff in einer Python-Klasse lässt sich über verschiedene Wege erreichen.

<br/><br/><br/>

---

## Kapitel 2: Spezielle Funktionsdekoratoren für Klassenmethoden

Python bringt standardmäßig einige Dekoratoren mit sich, welche speziell im Klassendesign anwendung finden. Dazu gehören vorallem @classmethod, @staticmethod, @property, @attr.setter und @attr.deleter

### 2.1 @Classmethod und @Staticmethod

Jede Methode, welche innerhalb eines 'Class-Body' definiert wird, kann mit diesen Dekoratoren ausgestattet werden. Dadurch verändern sich automatisch die Übergabeparameter und die Verhaltensweise der Methode.

#### 2.1.1 @Staticmethod

Die Staticmethod unterscheidet sich in keiner Weise zu ganz normalen Funktionen abgesehen davon, dass sie im Class-Body definiert wird. Anders als die normalen Methoden einer Klasse, hat eine Staticmethod **kein** verpflichtendes self-Argument an erster Position. Es kann einfach leer bleiben oder mit belibigen Argumenten definiert werdern.

```py
class PC:
    @staticmethod
    def add_2_to_3():
        return 3+2

print(PC.add_2_to_3())
```

<pre>
> 5
</pre>

Die Staticmethod muss nichts mit Inhalten der Klasse interagieren. Es ist eine ganz normale Funktion, die lediglich im Namespace der Klasse liegt und demtentsprechend über diesen Namespace aufgerufen werden muss.

#### 2.1.2 @Classmethod

Im Gegensatz zu den Staticmethods verhält es sich mit den Classmethods anders. Meines Wissens nach wird die Classmethod hauptsächlich als Factory-Method verwendet. Eine Factory-Method ist eine Methode, welche die Instanz einer Klasse durch andere Parameter erzeugt, als die Standardparameter der \_\_init\_\_ Methode.
Beispiel:

```py
01 class Circle:
02     def __init__(self, radius):
03         self.radius = radius
04
05     @classmethod
06     def from_diameter(cls, diameter):
07         calculated_radius = diameter/2
08         return cls(radius=calculated_radius)
09
10 c1 = Circle(10)
11 c2 = Circle.from_diameter(40)
12
13 print(c1.radius)
14 print(c2.radius)
```

<pre>
> 10
> 20
</pre>

Anders als bei normalen Methoden ist der erste übergebene Parameter einer Classmethod immer die Klasse selbst. An dieser Stelle könnte man theoretisch auch die Bezeichung _cls_ in Zeile 08 zu _Circle_ umbenennen. Aber da ist wieder das Thema Hardcoding. Würde man eine Klasse Spehre erstellen, welche von _Cricle_ erbt, dann würde bei der Verwendung von _cls_ in Zeile 08 der Spehre Konstruktor aufgerufen werden, welcher sich unter Umständen von dem Konstruktor der _Circle_ Klasse unterscheiden kann.

Klassenmethoden sind nicht auf den Aufruf über die Klasse selbst beschränkt. Ebenso wie die Klassenattribute können diese über die Instanz erreicht werden. Das Verhalten ändert sich dadurch aber nicht. Also der erste Attribut bleibt die Klasse selbst.

<sub>(Randnotiz 1: Die Argumente _self_ und _cls_ sind auch nur Conventionen die alle Leute einhalten (sollten). Auch diese beiden Argumente sind vom Bezeichner her frei wählbar, ABER Methoden bekommen automatisch beim Aufruf die Instanz an der ersten Position übergeben, respektive die Klasse für Klassenmethoden. Python IDEs, oder jene die Syntaxhighlighing für Python unterstüzen, haben _meistens_ unterschiedliche Farbkennzeichnungen für _cls_ und _self_ als für belibige Argumente.)</sub>

<sub>(Randnotiz 2: Eine weitere Idee für Klassenmethoden wäre einen Zugang zu Statistiken über den Gebrauch der Klasse zu schaffen. Informationen über alle Instanzen sammeln oder was weiß ich. Über Metaklassen kann man beispielsweise die Verwendung von Instanzen einer Klasse aufzeichnen, ohne dass der Benutzer davon was mitbekommt ode res selbst implementieren müsste.)</sub>

### 2.2 Method Overloading

Method Overloading ist ein Konzept, welches einige von euch wahrscheinlich schon unbewusst angewandt haben. Dieses Konzept besagt, dass eine Methode oder Funktion sich unterschiedlich verhalten kann, abhängig von der Verwendung der Methode. Der einfachste Weg um Method-Overloading in Python zu erreichen sind optionale Parameter.
<br/><br/>

#### 2.1.1 Optionale Parameter

Eine normale Funktion, welche durch optionale Parameter überladen wird, benötigt lediglich default-Werte für mindestens ein Argument. Der Parameter 'debug' ist optional, weil jener in der Funktions-Definition einen default-Wert zugewiesen bekommt.

```py
def adder(x, y, debug=False):
    if debug:
        print(f"Evaluating {x} + {y}:")
        result = x + y
        print(f"Result: {result}")
        return result
    return x + y

retval = adder(10, 20)

retval = adder(100, 200, debug=True)
```

Ausgabe:

<pre>
> Evaluating 100 + 200:
> Result = 300
</pre>

In beiden Fälle gibt die Funktion das Ergebnis zurück, aber durch die Verwendung von dem optionalen Parameter 'debug' ändert sich das Verhalten der Funktion. Und das ohne, dass der Code verändert werden muss. Das Verhalten lässt sich also durch die übergebenen Argumente direkt steuern. Selbstverstädlich ist diese Art von Overloading auch bei Methoden einer Klasse zulässig.
<br/><br/>

#### 2.1.2 @property, @fn.setter, @fn.deleter

Die genannten Dekoratoren sind besondere, welche man als Descriptor beschreibt. Auch diese werden zum Method-Overloading verwendet, da sie mehrere Methode mit dem gleicher Bezeichnung so ausstatten, dass diese, aufgrund der Art der Verwendung, sich unterschied verhalten. Da es sich um Dewkoratoren handel müssen sie nur vor der Methode angebracht werden, welche den Bezeichner hat, über den sie mit dem '.'-Operator erreicht werden soll.

<sub>(David Beazley spricht in seinem [Tutorial: YouTube: Python 3 Metaprogramming](https://youtu.be/sPiWg5jSoZI) von 'owning the dot'. Klingt eigentlich spannender als es ist, weil er mit Discriptoren den Zugriff auf eine Variable in 100 Wegen überprüft. Dazu später mehr.)</sub>

Beispiel:

```py
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    @property
    def gpu(self):
        # if user.acceslevel > x:
        return self._gpu

    @gpu.setter
    def gpu(self, value):
        # Type/Value-Cheking
        self._gpu = value

    @gpu.deleter
    def gpu(self):
        # log(f"Gelöscht am: {date} von {user}")
        del self._gpu


meine_pc_isntanz = PC(cpu='Ryzen 7', gpu='RTX2070')

meine_pc_isntanz.gpu                # Lesezuegriff, @property wird aufgerufen
meine_pc_isntanz.gpu = 'RTX3090'    # Schreibzugriff, @gpu.setter wird aufgerufen
del meine_pc_isntanz.gpu            # Löschen des Attributs, @gpu.deleter wird aufgerufen
```

Wichtig ist, dass das eigentliche Attribut nicht den gleichen Namen wie die Methode haben darf, da man sonst in einer Endlosschleife landet.

```py
@property
def gpu(self):
    return self.gpu
```

Die Zeile 'return self.gpu' würde darin enden, dass durch self.gpu wieder die @property-Methode aufgerufen wird. Das Gleiche gilt für die setter und deleter Methoden. (Endless Rekursion... Pythons Default Limit 1000)

<pre>
> Traceback (most recent call last):
>   File "_pydevd_bundle/pydevd_cython.pyx", line 1557, in _pydevd_bundle.pydevd_cython.> ThreadTracer.__call__
> RecursionError: maximum recursion depth exceeded
> Fatal Python error: Cannot recover from stack overflow.
</pre>

Und wozu soll das gut sein? Naja, im Vergleich zu dem normalen Zugriff ist es jetzt möglich beim Schreiben eines Attributs ein Value/Type Checking durchzuführen. Man könnte das Löschen des Attributs loggen, Lesezugriffe beschränken etc. Und das alles würde ganz automatisch im Hintergrund passieren, ohne dass der Zugriff über 'instanz.attribut' sich ändern müsste.

Eine weitere Möglichkei, um die Discriptoren der standard Libary zu verwenden ist, dass man sich die Methoden für get, set und delete selbst definiert und dann mit folgender Zeile an das Attribut übergibt.

```py
class PC:
    attr = property(get_func, set_func, delete_func, doc_string)
```

Die übergebenen Funktionen können belibig definiert sein und können auch machen was sie wollen. Die 'Built-In'-Property Methode verknüpfte diese nur an ein Attribut. Das heißt:

- wenn pc_instance.attr verwendet wird, dann wird die get_func ausgeführt.
- wenn pc_instance.attr = verwendet wird, dann wird die set_func ausgeführt.
- wenn del pc_instance.attr verwendet wird, dann wird die delete_func ausgeführt.

Was diese Funktionen machen ist euch überlassen. Mit diesem Ansatz kann man die Zugangsmethoden einmalig definieren und sie einfach als property an ein Attribut setzten.

Da Discriptoren meiner Meinung nach eine coole Sache sind und für ein fortgeschrittenes Klassendesign sehr hilfreich sein können, gibt es zu diesen noch ein eigenes Kapitel, wie man eigene Discriptoren erstellt.

<sub>(Randnotiz 1: Auch bei der Zuweisung in der \_\_init\_\_ wird die @attr.setter Method durchgeführt, da der Attributzugriff über self.attr innerhalb einer Klasse keinen Unterschied zu dem Zugriff instance.attr außerhalb einer Klasse darstellt.)</sub>
<br/><br/><br/>

#### 2.1.3 Weiteres Overloading

Das Standard Package _typing_ enthält einene Dekorator names '@overload', aber damit habe ich micht nicht tiefer beschäftigt.

Wenn man mal darüber nachdenkt, dann sind bereits die 'Built-In' Operatoren auch schon überladen. Mit '+' kann ich Floats, Ints, Strings, Lists, ... etc addieren und erhalte trotzdem ein Ergebnis zurück.

<br/><br/><br/>

## Kapitel 3: Klassenvererbung

Das Vererben von Klassen kann man in zwei wesentliche Kategorien unterteilen. Der erste Grund, und meiner Meinung nach der häufigere, ist, um eine Klasse zu speifizieren. Der zweite Grund ist, um mehrere Klassen zu einer Gesamtklasse zu komponieren. Dies findet beispielsweise im Fall von "Descriptors" Anwendung.

<sub>(Randnotiz 1: Im folgenden Kapitel bauen die Code-Teile aufeinander auf.)</sub>

### 3.1 Spezifizieren von Klassen

Um in Python Klassen zu vererben muss bei deklaration der Kindklasse in Klammern die Elternklasse(n) angegeben werden. Im einfachsten Fall hat eine Kindklasse eine einzige Elternklasse, aber mehrere sind auch möglich.

Im folgenden Beispiel ist die Elternklasse 'Person' und zwei getrennte Kindklassen, welche von 'Person' erben.

<sub>(Auf die super()-Methode gehe ich später noch ein. Aktuell reicht es zu wissen, dass damit auf die Methode der Elternklasse/vorhergehenden Klasse zugegriffen wird.</sub>

```py
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):  # Ansatz 1
    def __init__(self, mat_nr, fname, lname):
        self.mat_nr = mat_nr
        super().__init__(fname, lname)

class Employee(Person): # Ansatz 2
    def __init__(self, salary, **kwargs):
        self.salary = salary
        super().__init__(**kwargs)

student = Student(fname='Max', lname='Mustermann', mat_nr='10142020')
employee = Employee(fname='Maria', lname='Musterfrau', salary=40000)
```

Für die Instanziierung von Kindklassen kann man verschiedene Ansätze wählen. In dem oben gezeigten Beispiel sind im Student-Konstruktor alle Parameter, welche zum Erzeugen einer Instanz benötigt werde, fix definiert. Anders ist es beim Employee. Dort wird das neue Attribut in den Konstruktor eingetragen und der Rest wird einfach als \*\*kwargs eingefangen und als Gesamtpaket weitergeleitet.

<br/>

**Student**<br/>
Vorteile:

- Explizitere Definition der Klasse
- Help oder inspect Methoden würden den vollständigen Konstruktor zurückgeben (Beispiel: \_\_init\_\_(mat_nr, fname, lname))
- Keine frei wählbaren Keyword-Argumente erlaubt.

Nachteile:

- Wesentlich mehr Schreibarbeit beim weiterleiten der Argumente.
- Wenn sich in der Elternklasse Argumente ändern, dann muss dies auch in der Kindklasse nachgetragen werden.
  <br/><br/>

**Employee**<br/>
Vorteile:

- Es können belibige Keywords als Argumente übergeben werden und nur die 'richtigen' werden herausgepickt.
- Die Weiterleitung der Argumente ist kürzer.
- Kein Modifizieren der Kindklasse nötig, falls sich etwas in der Elternklasse ändert.

Nachteile:

- Help und inspect Methoden liefern einen nicht spezifizierten Konstruktoaufruf zurück. (In diesem Fall eben \_\_init\_\_(salary, \*\*kwargs))
- Kwargs, welche gar Nicht existieren, werden vom Konstruktor akzeptiert, auch wenn diese nicht verwendet werden.
  <br/><br/>

Wofür man sich entscheidet ist sicherliche Anwendungsabhängig. Was habe ich mit der Klasse noch alles vor? Erwarte ich weitere Kindklassen? Dass man für die Help-Methode eine gesamte Darstellung des Konstruktors bevorzugt macht für den späteren Anwender mehr Sinn. Dieses Problem mit dem zweiten Ansatz und der Tatsache, dass die Darstellung \_\_init\_\_(salary, **kwargs) wenig hilfreich ist, ließe sich aber mit Metaklassen kontrollieren. Obwohl **kwargs verwendet wird, würden dann trotzdem alle benötigten Paramerter der Elternklasse(n) mit angezeigt werden.

### 3.2 Komponieren von Klassen

Beim Komponieren von Klassen wird eine neue Klasse erzeugt, welche von mehreren Elternklassen erbt. In diesem Beispiel wird der Student mit dem Employee vereint. (Sogesehen eine Stundentische Hilfskraft?) Da die neue Klasse keine neuen Parameter benötigt, muss auch keine init geschrieben werden.

```py
class StudentWorker(Student, Employee):
    pass
```

Die neue Klasse enthält all das, was die beiden Elternklassen enthalten. Die Instanziierung sieht dann folgendermaßen aus.

```py
studentworker1 = StudentWorker(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
```

<pre>
> Traceback (most recent call last):
>   File "f:/Python-Projects/Projects/Classes_Tutorial/Kapitel_3/vererbung_person.py", line 22, in <module>
>     sw1 = StudentWorker(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
> TypeError: __init__() got an unexpected keyword argument 'salary'
</pre>

BONK. Problem. Durch den gewählten Ansatz 1 bei der Student Klasse stoßen wir auf ein weiteres Problem mit der Verwendung der einzelnen Keyword-Argumente. Bei der Instanziierung der StundentWorker Klasse wird der Konstruktor des Students zuerst verwendet. Der kennt aber das 'salary' Keyword nicht und schmeißt dementsprechend einen Error. Mit dem Ansatz 2, der bei dem Employee gewähtl wurde, wäre dies nicht passiert, da jene Argumente, welche nicht bekannt sind einfach als kwargs zusammengefasst und weitergeleitet werden. In der obersten Klasse könnte man dort auf \*\*kwargs verzichten, um unbekannte Keywords abzufangen und trotzdem einen Fehler zu schmeißen.

### 3.3 \_\_mro\_\_ und super()

Sobald Klassenvererbung ein Thema ist sollte man sich im Klaren sein, wie die 'Built-In'-Methode super() funktioniert. Einfach gesagt, die super()-Methode greift auf das nächste Element in der \_\_mro\_\_ Liste zu. MRO steht für 'Method Resolution Order'.

Python ist eine Interpreter-Sprache. Das heißt, ein Skript wird von oben nach unten durchgearbeitet und erst bei erreichen der Zeile evaluiert, was dort passiert. Auch Ausdrücke, welche innerhalb des Class-Bodys definiert sind werden stumpf ausgeführt.

Bei der **Definition** (nicht bei der Instanziierung) einer Klasse wird die \_\_mro\_\_ evaluiert und festgelegt. Dieses Attribut ist Read-Only und existiert auf Klassenebene. Die Evlauation erfolgt über die [Wikipedia: C3-Linearization](https://en.wikipedia.org/wiki/C3_linearization). Ich werde hier nicht tiefer darauf eingehen, lediglich darauf verweisen, falls es jemanden ganz genau wissen will.

https://stackoverflow.com/questions/40478154/does-pythons-mro-c3-linearization-work-depth-first-empirically-it-does-not

Fakt ist aber, dass eine Linearisierung stattfindet. Und auch hier sei wieder gesagt, auch in diesen Prozess lässt sich mittels Metaklassen eingreifen. Wenn ihr aus irgendeinem Grund eine beispielsweise alphabetisch geordnete MRO benötigt, dann ginge das.

<sub>(Randnotiz 1: Obwohl das \_\_mro\_\_ Attribut bei der Definition der Klassen evaluiert wird und das Attribut Read-Only ist lässt sich dieses Attribut später dennoch verändern. Denn es wird jedes mal neu evalusiert, wenn sich die \_\_bases\_\_ einer Klasse ändern. Und dieses Attribut ist schreibbar. Man kann theoretisch im Programmablauf einfach zu jederzeit die vererbten Klassen einer Klasse ändern. Ob man das tun sollte, wahrscheinlich eher nicht. Erklärt hat dies Mark Smith auf der PyCon 2019. [Youtube:"It's Pythons All The Way Down: Python Types & Metaclasses Made Simple" - Mark Smith (PyCon AU 2019)](https://www.youtube.com/watch?v=ZpV3tel0xtQ))</sub>

Wenn man sich mit diesem Wissen nun die mro vom StudentWorker anguckt erhält man folgende Reihenfolge.

```py
print(StudentWorker.__mro__)
```

```
> (<class '__main__.StudentWorker'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class '__main__.Person'>, <class 'object'>)
```

Obwohl die Klasse _Student_ und die Klasse _Employee_ beide von der Klasse _Person_ erben, steht die Klasse _Person_ hinter den beiden Anderen Klassen in der Reihenfolge.

In der Definition der Klasse _Student_ steht

```py
class Student(Person):  # Ansatz 1
    def __init__(self, mat_nr, fname, lname):
        self.mat_nr = mat_nr
        super().__init__(fname, lname)
```

die super()-Methode innerhalb der \_\_init\_\_ und greift im Fall der _StudentWorker_ Klasse **NICHT** auf die vererbte Klasse _Person_ zu, sondern geht laut der \_\_mro\_\_ weiter zur Klasse _Employee_. Würde man natürlich die Klasse Student instanziieren, dann würde die super()-Methode zur Klasse _Person_ weiterleiten. Dort zeigt sich nocheinmal, wieso man das **Hardcoding** unbedingt vermeiden sollte und außerdem wieso man mit \*\*kwargs arbeiten sollte. Je nachdem, wie die Klassen vererbt werden, kann man gar nicht wissen, an welcher Stelle die Elternklasse der neuen Klasse stehen. Die übergebenen Parameter _fname_ und _lname_ machen im Aufruf des Employee-Konstruktor überhaupt keinen Sinn und würeden dementsprechend einen Fehler generieren.

## Kapitel 4 Discriptor Protokol

Discriptoren sind Klassen, welche in den Prozess des Attributszugriff eingreifen und zusätzliche Aufgaben durchführen können. Der Vorteil von eigenen Discritopren, gegenüber den Discriptoren der standard Libary ([2.1.2](#212-@property,-@fn.setter,-@fn.deleter)), ist, dass das Protokol für alle Attribute in einer eigene Klasse definiert wird. Dadurch lassen sich Discriptoren einfach warten und erweitern, indem sie in eine neue Klasse vererbt werden und weitere Funktionalität hinzugefügt wird.

[Python Docs: Discriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)

[Python Docs: Implementing Discriptors](https://docs.python.org/3/reference/datamodel.html?highlight=__get__#implementing-descriptors)

[Stackoverflow: When and why use an discriptor over property()](https://stackoverflow.com/questions/5842593/when-and-why-might-i-assign-an-instance-of-a-descriptor-class-to-a-class-attribu)

### 4.1 Allgemein

Bei Discriptoren unterscheidet man zwischen 'Data-Discriptor' und 'Non-Data-Discrptor'. 'Non-Data-Discriptors' sind dadurch definiert, dass sie **nur** die \_\_get\_\_-Method enthalten. Für 'Data-Discriptros' müssen die \_\_set\_\_ und optional die \_\_delete\_\_ Methods definieren werden. Man unterscheidet aus dem Grund zwischen diesen Typen, da ein 'Non-Data-Discriptor' beispielsweise auch den Zugriff auf eine Methode steuer kann und deswegen nur die \_\_get\_\_-Method benötigt.

Die Discriptor-Klasse wird durch folgende 'Dunder'-Methods beschrieben.

- \_\_get\_\_
- \_\_set\_\_
- \_\_delete\_\_
- \_\_set_name\_\_

Selbstverstädnlich darf eine Discriptorklasse auch andere Methoden haben

## Kapitel 5 Klassendekoratoren

Klassendekoratoren sind der erste Schritt zur Metaklasse. Viele Dinge, die man mit Metaklassen realisieren kann, könnte man auch mit Klassendekoratoren erreichen. Die Frage wozu man Metklassen dann überhaupt lässt sich mit den zwei wesentlichen Unterschieden beantworten.

1. Klassendekoratoren werden **NACH** der Erzeugung der Klassendefinition angewandt. Metaklassen werden **VOR** der Erzeugung der Klassendefinition durchgeführt.
2. Metaklassen werden durch Vererbung weitergeleitet. Ein Klassendekorator wirkt nur auf die Klasse, die damit dekoriert wird.

### 5.1 Allgemein

Klassendekoratoren unterscheiden sich von Funktionsdekoratoren nur in der Weise, dass sie, statt der Funktion, eine Klasse als Inputargument haben und eine Klasse zurückgeben. Da die Klassendekoratoren nach der Erzeugung der Klasse aufgerufen werden hat die Klasse bereits ein vollständig gefülltes Dict, welches alle Inhalte des Class-Bodys enthält.

#### 5.1.1 Klassendekorator XXXXXXX

```py
from datetime import datetime

def debugger(func):
    def wrapper(*args, **kwargs):
        print(f"\nFunktionsaufruf am {datetime.now()}: Übergabeparameter: {args}, {kwargs}.")
        return func(*args, **kwargs)
    return wrapper

def debug_all_cls_methods(cls):
    # Alle Elemente des Klassendicts durchsuchen
    for key, element in cls.__dict__.items():
        # Filtern nach den Aufrufbaren elementen (Klassenattribute werden herausgefiltert)
        if callable(element):
            # Rausfiltern der 'Dunder'-Methods (Wenn man möchte)
            if not key.startswith('__') :
                # Anbringen des 'debug'-Dekorator und zurück ins Klassendictionary schreiben
                setattr(cls, key, debugger(element))
    # Rückgabe der modifizierten Klassen
    return cls

@debug_all_cls_methods
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def but_can_it_run_crysis(self, answer):
        if answer:
            print("Yes, it can!")
        else:
            print("No it can't.")

    def power(self, voltage, ampere):
        print(f'I consume {voltage*ampere} W right now.')

meine_pc_instanz = PC('Ryzen 7', 'RTXSuper2070')

meine_pc_instanz.but_can_it_run_crysis(False)
meine_pc_instanz.power(ampere=2, voltage=230)
```

<pre>
> Funktionsaufruf am 2020-12-07 19:11:46.998121: Übergabeparameter: (<__main__.PC object at 0x0000019368148880>, False), {}.
> No it can't.
>
> Funktionsaufruf am 2020-12-07 19:11:47.155469: Übergabeparameter: (<__main__.PC object at 0x0000019368148880>,), {'ampere': 2, 'voltage': 230}.
> I consume 460 W right now.
</pre>

Das \_\_main\_\_.PC Object (Welches die Instanz der Klasse ist) ist in diesem Fall das _self_-Argument, welches automatisch bei dem Aufruf übergeben wird. Wir sehen aber, dass **ALLE** Methoden der Klasse mittels des Debug-Dekorator erweitert wurden. Würde man nur auf Funktionsdekoratoren zurückgreifen, dann müsste man jede Methode einzeln mit einem Ausstatten.

<sub>(Kleine Denkaufgabe: Warum kann ich im Klassdekorator die 'Dunder'-Methods nur anhand der vorhergehenden Unterstriche identifizieren und muss nicht noch nach den nachfolgenden Unterstrichen suchen, um sicherzustellen, dass es sich um kein privates Attribut/Methode handelt?)</sub>
<br/><br/>

Wer in [1.2.5 \_\_call\_\_ Method](#125-__call__-method) aufgepasst hat wird wissen, dass man eine Funktion auch als Klasse darstellen kann. Man kann damit also eine Klasse mit einer aufrufbaren Klasse dekorieren.

## Kapitel 6 Metaklassen
