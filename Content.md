# Inhalt des Tutorials

- Vorwort
- Vorbereitende Erklärungen
- Kapitel 1 Fortgeschrittenes (Klassen) Design
- Kapitel 2 Klassenvererbungen
- Kapitel 3 Spezielle Funktionsdekoratoren für Klassen
- Kapitel 4 Klassendekoratoren
- Kapitel 5 Metaklassen
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

Um die gezeigten Inhalte zu verstehen solltet ihr bereits die Grundlagen von Python kennen. Dazu gehört allgemein die Syntax, wie man Funktionen und Klassen erstellt und eventuell soagr, dass **alles** in Python Objekte sind. Klassen sind Objekte, Funktionen sind Objekte, selbst eine Variable ist nur ein Objekt einer bestimmten Klasse. Des Weiteren solltet ihr auch ungefähr wissen was Vererbungen/Inheritance sind. Ich werde es nochmal im Detail erklären, dennoch geht es auch bei dem Thema eher um die Tiefe statt die einfache Anwendung. Dictionarys! In Python findet man überall Dictonarys, weswegen es essentiell ist, dass ihr diese im Vorfeld kennt und wisst was man damit machen kann. (dict.keys(), dict.values(), dict.items(), Dicts sind mutable Objekte...) Die letzte Vorraussetzung sind dann noch Closures / Decorators', welche ich bereits in meinem ersten 'Tutorial' erklärt habe (Link im Kommentar).
<br/><br/>

### IDE

Nur zur Information, da es in dem ersten Beitrag auch zur Sprache kam, ich arbeite vollständig mit VSCode und habe mir diese IDE inwzischen schon recht stark Modifiziert. Color Color-Themes, Boilerplates/Snippets, indentation und bracket Colors und ein paar Andere. Für einige ist es sicher zu bunt, mir gefällts halt.
<br/><br/>

### Disclaimer

Jeder macht Fehler. Ich beanspruche keineswegs Vollständig- oder Richtigkeit der hier gezeigten Inhalte. Für weitere Details und noch tiefergehende Informationen empfehle ich grundsätzlich die [Python-Dokumentation](https://docs.python.org/3/).

Ich möchte mit diesem 'Tutorial' einen tieferen Einblick in die elementaren Dinge von Python vermitteln. Auch ich habe währen des Schreibens viel nachlesen und recherchieren müssen. Ich biete hiermit lediglich eine zusammengefasste Form der Informationen an, welche ich auf eine Weise darstellen möchte, wie ich sie mir bei Tutorials von Anderen selbst gewünscht hätte.
<br/><br/>

### Korrektur meiner Aussage im ersten Tutorial
In meinem ersten Tutortial über Closers und Decorators habe ich gesagt, dass man \*args und \*\*kwargs nicht umbenennen sollte und immer als \*args und \*\*kwargs verwenden sollte, auch wenn Python nur auf die Sternchen achtet und die Bezeichner frei wählbar sind. Ich bin bei meinen Recherchen auch darauf gestoßen, dass es sogar von Core-Developern empfohlen wird die Bezeichner umzubennenen, wenn dies das Verständnis vereinfacht. Wenn die \*args für den Input für eine bestimmte Gruppe an Daten verwendet wird und das \* nur dafür genutzt wird, dass man eine belibige Anzahl von Argumenten benutzt, dann kann es ja hilfreich sein, den Bezeichner genau zu bennenen.

Beispiel:
```py
def summe(*args):
    summe = 0
    for zahl in args:
        summe += zahl
        
# Das sollte man ändern zu:
def summe(*zahlen):
    summe = 0
    for zahl in zahlen:
        summe += zahl
        
# Oder
def farbset(*args):
    pass
 
# Das sollte man ändern zu:
def farbset(*farben):
    pass
```
<br/><br/><br/>



## Vorbereitende Erklärungen

Ich werde kurz f-Strings und List-Comprehensions erklären, weil ich diese in den Beispielen regelmäßig verwende, wer das kennt, kann den Teil überspringen. Und direkt mit [Kapitel 1](<##kapitel-1:-fortgeschrittenes-(klassen)-design>) starten.

Dieses Tutorial richtet sich zwar schon an Leute die bereits die Grundlagen von Python kennen und verstehen, aber da ich zwei Dinge in meinen Codebeispielen immer wieder verwende, möchte ich diese zu Anfang einmal kurz erklären. Aufgrund der Kommentare des ersten 'Tutorials' denke ich, dass dies ein paar Leuten weiter helfen kann.

### f-Strings

F-Strings steht für "formatted string literals". Sie kennzeichnen sich dadurch aus, dass vor dem Anführungszeichen des Strings ein f steht. (Klein- oder Großschreibweise spielt dabei keine Rolle, typischerweise verwendet man das kleine f). Innerhalb des Strings dürfen geschweifte Klammern stehen, welche einen Pythonausdruck enthalten. Im einfachsten Fall ist das eine Variable, komplexere Ausdrücke funktionieren aber auch.

Die f-Strings wandeln den Inhalt der geschwiften Klammen während der Laufzeit in einen String um und sind im anschluss ein ganz normaler String. Die Idee dahinter ist, dass man im Code den String vollständig beschreibt und auch ohne die eingefügten Inhalte zu kennen weiß, wie dieser String am Ende aussieht.

```py
mein_name = 'Geralonx'
mein_alter = 30
gruss = f"Grueß dich, mein Name ist {mein_name}, ich bin {mein_alter} Jahre alt."
print(gruss)
```

Ausgabe:

<pre>
> Grueß dich, mein Name ist Geralonx, ich bin 30 Jahre alt.
</pre>

<sub>(Auch wenn es f-Strings bereits Seit Python 3.6 (2016) gibt bin ich erst dieses Jahr vollständig auf die Verwendung von f-Strings umgestiegen. Vorher habe ich immer mit .format() gearbeitet, weil mir diese Darstellung sehr gut gefiel und ich die f-Strings noch nicht im Detail kannte.)</sub>
<br/><br/><br/>

### List-Comprehensions

List-Comprehensions sind präzise Ausdrücke, um eine Liste mit Ergebnissen von einer Operation, welche auf die einzelnen Mitglieder einer Sequenz oder Iterator angewendet werden, zu erzeugen (Frei übersetzt aus der Python-Dokumentation). Bitte was? Im häufigsten Fall ersetzten List-Comprehensions for-Loops, welche eine Liste erzeugen. Die Syntax einer List-Comprehension sieht folgendermaßen aus:

<pre>
> liste = [expression for item in squence [, condition]]
</pre>

Beispiel / Vergleich mit einer for-Loop:

```py
# For Loop um die Quadrate der Zahlen 0-9 zu erzeugen
for_loop_list = []
for i in range(10):
    for_loop_list.append(i*i)

# List-Comprehension um die Quadrahte der Zahlen 0-9 zu erzeugen.
list_comp_list = [i*i for i in range(10)]

# Ausgabe
print("For-Loop-Result:\t", for_loop_list)
print("List-Comp-Result:\t", list_comp_list)
```

Ausgabe:

<pre>
> For-Loop-Result:         [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> List-Comp-Result:        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
</pre>

Die List-Comprehension vereinigt 3 Zeilen Code von einer Empty-List-Initialisierung und das Füllen mit einer for-Loop zu einer einzigen. Es ist auch möglich Bedingungen in die List-Comprehension einzubauen.

<br/>

```py
# List Comprehension mit einer Bedingung, welche nur die geraden Zahlen erfasst.
new_list = [i*i for i in range(10) if i%2 == 0]
print(new_list)

# Das Gleiche Ergebnis ließe sich beispielsweise mit folgendem Code erreichen
new_list = []
for i in range(10):
    if i%2==0:
        new_list.append(i*i)
```

Ausgabe:

<pre>
> [0, 4, 16, 36, 64]
</pre>
List-Comprehensions können die Leserlichkeit verbessern, wenn man sie versteht und lesen kann. Einfache List-Comprehensions schneiden von der Performance meistens auch noch besser ab als die entsprechenden for-Loop Konstrukte. Darauf möchte ich aber nicht tiefer eingehen. Man kann mit List-Comprehension aber auch ganz schönen Unfug treiben und den Scheiß unendlich tief verschachteln oder vieles mehr. Ich werde dazu auch ein File verlinken, wo ich mal solche Konstrukte zeige und umschreibe.
<br/>

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

Funktioniert es? Ja. Ist es einfach zu verstehen? Nein. Zur Übung könnt ihr diese Konstrukte ja mal auseinander nehmen, gerade die Methode 'most_common_tags' ist übel, wenn man noch nicht genau verstanden hat, wie diese aufgebaut sind.
<br/>
<sub>(Hint: Zerlegt die Comprehension von hinten oder von vorne und stoppt immer bei Keywords wie if oder for. Nehmt den Teil bis zu dem Keyword und schmeißt alles bis dahin in eine eigene Zeile. Wenn man von hinten anfängt, dann baut man das Konstrukt von innen nach außen auf, umgekehert wenn man vorne anfängt. Am Ende muss man nur noch die Expression, also den vordersten Teil, in das innere übersetzten. Eine Schritt für Schritt Anleitung ist hier: [GIT-GUB-FILE-REFERENCE]) </sub>
<br/><br/>

## Kapitel 1: Fortgeschrittenes (Klassen) Design
Das Thema von fortgeschrittenem Design hat den wesentlichen Hintergrund des 'Code Reuse', also das Wiederverwenden von bereits geschriebenen 

### 1.0 Style-Guides

Ich möchte am Anfang einmal auf die Style-Guides und ein paar Zitate/Aussagen von Python-Core-Developer hinweisen. Ich möchte bezüglich dem Styling keine Ratschläge geben oder verschiedene Guides vergleichen. Es gibt [PEP8](https://www.python.org/dev/peps/pep-0008/), es gibt eine [Vorlage von Google](https://google.github.io/styleguide/pyguide.html) und sicherlich noch andere, aber selbst Raymond Hettinger sagte in seinem Vortrag:

> "PEP8 is not a weapon for beating other people in the head. It's a stlye
> guide, a guide, not a lawbook." - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

und

> "Isn't it great, when you write code that is PEP8 compliant and out of a room of 500 people one person can figure it out?" - Raymond Hettinger
> [YouTube: Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)

Im Vortrag weist er mit diesen Aussagen darauf hin, dass man die Qualität von Code nicht nach dem Grad der Übereinstimmung von PEP8 bestimmen sollte, sondern ein bisschen weiter denken muss, um den nächsten Lesern das Leben zu vereinfachen. PEP8 hat nicht zu Allem eine Antwort, das wäre unmöglich, deswegen sollte man sich selbst Geanken machen, wie man seinen Stil im Coden so umsetzt, dass dieser am Ende von (im besten Fall) jedem verstanden werden kann.

[The Zen of Python](https://www.python.org/dev/peps/pep-0020/) gefällt mir am besten, wenn ich über die Wege für clean code nachdenke.
<br/><br/>

### 1.1 Klassen Recap

#### 1.1.1 Allgemeines

Wie, wann und wo man Klassen verwenden sollte oder nicht möchte ich gar nicht disskutieren. Ich sebst verwende Klassen auch manchmal, wo der ein oder andere sicherlich sagen würde, dass die dort überflüssig seien. Der Hauptgrund warum ich Klasse überhaupt verwende ist 'Encapsulation'. Das heißt so viel wie, dass die Daten und die Methoden, welche jene Daten modifizieren einfach zusammengepackt werden, damit eine eineindeutiger Zusammenhang besteht.

Die einzige Regel die auch ich grundsätzlich beachte ist aus folgendem Zitat abzuleiten. (Das heißt natürlich nicht, dass man sofort ab 2 zugehörigen Methoden und init eine Klasse schreiben sollte, aber ich denke ihr versteht den Punkt.)

> "The signature of 'this should't be a class' is, that it has two methods one of which is
> init. Any time you see that, you should probably think 'hey, maybe I just need one method'."
> \- Jack Diederich in [YoutTube: Stop Writing Classes](https://youtu.be/o9pEzgHorH0)

<br/>

#### 1.1.2 Public, Private und Protected

Meine beste Sprache ist Python, ich habe C und C++ als erste Sprachen gelernt, aber damit habe ich schon ewig nicht gearbeitet. Weswegen ich hier nicht generell für alle OOP-Sprachen sprechen kann. Mein Verständnis für Public, Private, Protected kommt eben aus C++ und das liegt bei mir schon Jahre zurück. Also verzeiht, wenn ich diesbezüglich nicht alles so genau weiß und hier etwas Erkläre, was selbtsverständlich ist, wenn man sich in der anderen Sprache tief genug auskennt.

**Public**<br/>
Man kann eigentlich sagen, dass **ALLES** innerhalb einer Python Klasse public ist. Es gibt Konzepte und Conventionen, welche die Idee von Private und Proteced nachahmen, aber wenn man sich auskennt, dann kann man auch diese Dinge ohne Aufwand umgehen. (An dieser Stelle fehlt mir die Erfahrung in anderen OOP-Sprachen, um zu wissen, ob dies auch dort einfach zu umgehen ist.)

**Private**<br/>
Wer aus anderen objektorentieren Sprachen kommt wird das Konzept von Public, Proteced und Private kennen. Und direkt mal vorweg, soetwas gibt es in Python nicht. Wer jetzt schonmal die Basics von Klassen in Python kennt wird vielleicht den Finger heben und Fragen: "Was ist denn mit den \_\_vars und \_\_methods()?" (Zwei Unterstriche, falls dies im Text nicht deutlich raus kommt.)

Wenn der Python-Interpreter innerhalb einer Klasse ein Attrribut oder Methode mit zwei führenden Unterstrichen und maximal einem nachfolgenden Unterstrich erkennt führt dieser ein sogenanntes 'Name Mangeling' durch. Das heißt, er bennent die Attribute und die Methode, die dieser Form folgen, für die Außenwelt um.

Hier ein Beispiel:

```py
01  class PC:
02     class_attribute = 'Ich bin ein Klassenattribut'
03
04     def __init__(self, prozessor, grafikkarte, ram):
05         self.prozessor = prozessor
06         self.grafikkarte = grafikkarte
07         self.__ram = ram
08
09  meine_pc_instanz = PC('Ryzen 7', 'RTX2070Super', 'GSkill')
10
11  print(meine_pc_instanz.prozessor)
12  print(meine_pc_instanz.grafikkarte)
13  print(meine_pc_instanz.__ram)
```

Die 3 prints haben folgende Ausgabe:

<pre>
> Ryzen 7
> RTX2070Super
> Traceback (most recent call last):
>   File "f:/Python-Projects/Projects/Classes_Tutorial/name_mangeling.py", line 13, in <module>
>     print(meine_pc_instanz.ram)
> AttributeError: 'PC' object has no attribute '__ram'
</pre>

So gesehen besteht von Außen kein direkter Zugriff auf das Attribut \_\_ram. Der Grund dafür ist, es gibt dieses Attribut gar nicht mehr. Das Attribut \_\_dict\_\_ einer Instanz enthält **alle** instanzspezifischen Attribute, also alles was zu self. zugewiesen wird. Gebe ich dieses \_\_dict\_\_ nun aus sehen wir, was die Instanz wirklich enthält.

```py
print(meine_pc_instanz.__dict__)
```

<pre>
> {'prozessor': 'Ryzen 7', 'grafikkarte': 'RTX2070Super', '_PC__ram': 'GSkill'}
</pre>

Wir sehen, dass prozessor und grafikkarte wie zu erwarten enthalten sind, aber wir sehen auch, dass unser \_\_ram wieder da ist. Das Name Mangeling hat dafür gesorgt, dass der Klassenname mit einem führenden Unterstrich an den Anfang des Attributs gesetzt wurde. Versuche ich folgendes,

```py
print(meine_pc_instanz._PC__ram)
```

<pre>
> GSkill
</pre>

habe ich dennoch Zugang zu den eigentlich 'Privaten' Attributen innerhalb einer Klasse. Die sogesehen privaten Attribute finden dennoch Anwendung. Das Name Mangeling verhindert eben Namespace Kollisionen, wenn die Klasse vererbt wird. Das heißt, wenn ich aus irgendeinem Grund sicherstellen muss, dass ein Attribut oder eine Methode für eine Klasse durch Vererbung nicht verändert werden darf, dann erreiche ich das mit dieser Form.

Ich habe innerhalb der PC Klasse bewusst ein Klassenattribut 'class_attribut' hinzugeführt, um zu zeigen, dass dieses Klassenattribut auch nicht im Dictionary der Instanz auftaucht. Dennoch ist es über den folgenden Aufruf erreichbar.

```py
meine_pc_instanz.class_attribute
```

Es lässt sich sogar verändern ABER, dies geschieht auf der Ebene der Instanz. Wenn ich das class_attribut über obenstehenden Zugriff veränder und auf einen neuen Wert zuweise, dann ist das Klassenattribut innerhalb

<sub>(Randnotiz 1: Natürlich, wenn ihr jetzt verstanden habt wie es geht, dann ist das immernoch möglich, aber es verhindert im ersten Schritt Kollisionen, wenn man über sowas gar nicht nachdenkt. Des Weiteren könnt ihr damit immernoch Attribute vor Anfängern oder unwissenden 'verstecken'.)</sub>

<br/>

**Protected**<br/>
Protected, also das Attribute und Methoden nur von der Klasse und von vererbten Klassen 'gesehen/verwendet' werden können gibt es gar nicht. (Warum auch, nicht einmal ein echtes Private gibt es.)

Unter Python Entwicklern gibt es die Convention, dass 'protected' innerhalb von Klassen mittels einem Unterstrich gekennzeichnet werden. Das ist aber lediglich ein Hinweis für Andere. Python selbst behandelt Attrubute und Methoden mit einem führenden Unterstrich nicht anders als ohne.
<br/><br/>

#### 1.1.3 Klassenattribute

### 1.2 'Dunder'-Methods

Um das Klassendesign im fortgeschrittenen Stil zu verstehen möchte ich bei den
'Dunder'- oder 'Magic'-Methods anfangen. (Dunder steht für 'Double Underscores'). Diese speziellen Methoden erfüllen einzigartige Aufgaben, welche durch die allgemeine Syntax und die 'Built-In' Methods abgerufen/aufgefragt werden können. Ich werde selbstverständlich nicht alle im Detail vopstellen und zeigen, sondern anhand von einzelnen Beispielen die Funktion von 'Dunder'-Methods erklären und auf ein paar besondere hinweisen. Um sie sinnvoll anzuwenden müsste ihr die Dokumentation regeln, da es für manche 'Dunder'-Methods gewisse Regeln gibt, wie beispielsweise, dass die Rückgabe ein bestimmten Datentype hat oder in einem definierten Bereich liegen muss.

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

Ab diesem Punkt sollte klar sein, dass man jede reguläre Klassen-Methode auch über die Bezeichnung der Klasse selbst aufrufen kann, wenn man eine Instanz dieser Klasse an der ersten Position (welches dem self Argument entspricht) übergibt.

<br/><br/>
Beispiel für die Verwendung von 'Dunder'-Methods durch 'Built-In'-Methods:

Die 'Dunder'-Method \_\_len\_\_(self) wird über die 'Built-In' Method
len() aufgerufen. Was diese \_\_len\_\_(self) Methode am Ende durchführt ist
komplett euch überlassen. Die einzige Vorraussetzung ist, dass diese Methode
einen Integer >=0 zurück gibt. Bevor ihr die Vorraussetzung erfüllt, könnt ihr
ausführen, berechnen und hacken was ihr wollt, solange die Vorrausetzung erfüllt wird, ist alles in Ordnung mit der Implementation.

Sobald man aber in dieses Thema des fortgeschrittenen Designs kommt ist man mindestens an einem Punkt, wo man den Code wiederverwenden will, wenn nicht sogar für Andere bereitstellen muss/möchte. Also sollte man sich fragen, was würde jemand anderes bei der Verwendung einer 'Dunder'-Method eigentlich erwarten? Bzw. warum sollte man diese Methode überhaupt auf die Klasse anwenden können?

<sub>(Randnotiz: \_\_len\_\_(self) ist übrigens die Fallback-Methode für \_\_bool\_\_(self). Das heißt, wenn keine Dunder-bool-Method definiert ist wird die Dunder-len-Method verwendet. Alles was >0 ist wird von Python als True interpretiert.)</sub>
<br/>

Für Vergleiche oder arithmetische Operationen gilt das Gleiche.

```py
def __add__(self, other):
# > instance1 + instance2
# > instance1.__add__(instance2)

# gt -> Greater Than
def __gt__(self, other):
# > instance1 > instance2
# > instance1.__gt__(instance2)
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

<sub>(Randnotiz 1: Die Single-Quotes, welche um die '{value}' gepackt sind, sind in diesem Fall hardcoded um alle Argumente. Das funktioniert in diesem Fall nur, weil es bei sich bei Allen um Strings handelt. Man müsste die Dunder-repr-Method noch expliziter gestalten, um verschiedene Datentypen richtig zu unterscheiden. Dieses Beispiel geht lediglich allgemein auf die Dunder-repr-Method ein.)</sub>

<sub>(Randnotiz 2: Wer die join() Method nich kennt sollte sich die anschauen. Sie nimmt eine iteriebares Obejekt and und verknüpft alle Elemente zu einem String, sofern sich die str() Method auf die Inhalte anwenden lässt. Wenn sich die Elemente nicht in einen String umwandeln lassen wird ein TypeError erhoben. Der erste Teil (In diesem Fall ', ') ist der Seperator. Der Seperator wird zwischen die einzelnen Teilelemente gepackt.)</sub>

<sub>(Randnotiz 3: Der repr, also die Represenation eines Objekts, wird von VSCode beispielsweise beim Debuggen verwendet. Wenn man an einem Breakpoint steht, sieht man die Variablen an der Seite. Hinter der Variable steht eben die Representation. Ob und wie es von anderen IDEs verwendet wird weiß ich nicht.)</sub>
<br/><br/><br/>

#### 1.2.3

Das \_\_dict\_\_ einer Instanz enthält **ausschließlich** die Attribute, welche nur innerhallb der Instanz gültig sind. Wohingegen der Aufruf von dir(instance) \_\_dir\_\_ einer Instanz die Attribute **UND** die

<pre>
>
>
>
>
</pre>

### Method Overloading


## Kapitel 2: Klassenvererbungen
Das Vererben von Klassen 
###
