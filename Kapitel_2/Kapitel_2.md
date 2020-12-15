# Inhalt

- [Kapitel 2 Spezielle Funktionsdekoratoren für Klassenmethoden](#kapitel-2-spezielle-funktionsdekoratoren-für-klassenmethoden)
  - [2.1 @Classmethod und @Staticmethod](#21-@classmethod-und-@staticmethod)
    - [2.1.1 @Staticmethod](#211-@staticmethod)
    - [2.1.2 @Classmethod](#212-@classmethod)
  - [2.2 Method Overloading](#22-method-overloading)
    - [2.1.1 Optionale Parameter](#211-optionale-parameter)
    - [2.1.2 @property, @fn.setter, @fn.deleter](#212-@property,-@fn.setter,-@fn.deleter)
    - [2.1.3 Weiteres Overloading](#213-weiteres-overloading)

<br/>

---

## Kapitel 2: Spezielle Funktionsdekoratoren für Klassenmethoden

Python bringt standardmäßig einige Dekoratoren mit sich, welche speziell im Klassendesign anwendung finden. Dazu gehören vorallem @classmethod, @staticmethod, @property, @attr.setter und @attr.deleter

---

### 2.1 @Classmethod und @Staticmethod

Jede Methode, welche innerhalb eines 'Class-Body' definiert wird, kann mit diesen Dekoratoren ausgestattet werden. Dadurch verändern sich automatisch die Übergabeparameter und die Verhaltensweise der Methode.

<br/>

#### 2.1.1 @Staticmethod

Die Staticmethod unterscheidet sich in keiner Weise zu ganz normalen Funktionen abgesehen davon, dass sie im Class-Body definiert wird. Anders als die normalen Methoden einer Klasse, hat eine Staticmethod **kein** verpflichtendes _self_-Argument an erster Position. Es kann einfach leer bleiben oder mit belibigen Argumenten definiert werdern.

Code: [\_1_staticmethods.py](_1_staticmethods.py)

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

Die Staticmethod muss nicht mit Inhalten der Klasse interagieren. Es ist eine ganz normale Funktion, die lediglich im Namespace der Klasse liegt und demtentsprechend über diesen Namespace aufgerufen werden muss.

<br/>

#### 2.1.2 @Classmethod

Im Gegensatz zu den Staticmethods verhält es sich mit den Classmethods anders. Meines Wissens nach wird die Classmethod hauptsächlich als Factory-Method verwendet. Eine Factory-Method ist eine Methode, welche die Instanz einer Klasse durch andere Parameter erzeugt, als die Standardparameter der \_\_init\_\_ Methode.

Code: [\_2_classmethods.py](_2_classmethods.py)

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

Anders als bei normalen Methoden ist der erste übergebene Parameter einer Classmethod immer die Klasse selbst. An dieser Stelle könnte man theoretisch auch die Bezeichung _cls_ in Zeile 08 zu _Circle_ umbenennen. Aber da ist wieder das Thema Hardcoding. Würde man eine Klasse Sphere erstellen, welche von _Cricle_ erbt, dann würde bei der Verwendung von _cls_ in Zeile 08 der Sphere Konstruktor aufgerufen werden.

Klassenmethoden sind nicht auf den Aufruf über die Klasse selbst beschränkt. Ebenso wie die Klassenattribute können diese über die Instanz erreicht werden. Das Verhalten ändert sich dadurch aber nicht. Also der erste Attribut bleibt die Klasse selbst.

<sub>(Randnotiz 1: Die Argumente _self_ und _cls_ sind auch nur Conventionen die alle Leute einhalten (sollten). Auch diese beiden Argumente sind vom Bezeichner her frei wählbar, ABER Methoden bekommen automatisch beim Aufruf die Instanz an der ersten Position übergeben, respektive die Klasse für Klassenmethoden. Python IDEs, oder jene die Syntaxhighlighing für Python unterstüzen, haben _meistens_ unterschiedliche Farbkennzeichnungen für _cls_ und _self_ als für belibige Argumente.)</sub>

<sub>(Randnotiz 2: Eine weitere Idee für Klassenmethoden wäre einen Zugang zu Statistiken über den Gebrauch der Klasse zu schaffen. Informationen über alle Instanzen sammeln oder was weiß ich. Über Metaklassen kann man beispielsweise die Verwendung von Instanzen einer Klasse aufzeichnen, ohne dass der Benutzer davon was mitbekommt oder er es selbst implementieren müsste.)</sub>

---

### 2.2 Method Overloading

Method Overloading ist ein Konzept, welches einige von euch wahrscheinlich schon unbewusst angewandt haben. Dieses Konzept besagt, dass eine Methode sich unterschiedlich verhalten kann, abhängig von der Verwendung der Methode. Der einfachste Weg um Method-Overloading in Python zu erreichen sind optionale Parameter.

<br/>

#### 2.1.1 Optionale Parameter

Eine normale Funktion, welche durch optionale Parameter überladen wird, benötigt lediglich default-Werte für mindestens ein Argument. Der Parameter 'debug' ist optional, weil jener in der Funktions-Definition einen default-Wert zugewiesen bekommt.

Code: [\_3_optionale_parameter.py](_3_optionale_parameter.py)

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

<pre>
> Evaluating 100 + 200:
> Result = 300
</pre>

In beiden Fälle gibt die Funktion das Ergebnis zurück, aber durch die Verwendung von dem optionalen Parameter 'debug' ändert sich das Verhalten der Funktion und das, ohne dass der Code verändert werden muss. Das Verhalten lässt sich also durch die übergebenen Argumente direkt steuern. Selbstverstädlich ist diese Art von Overloading auch bei Methoden einer Klasse zulässig.

<br/>

#### 2.1.2 @property, @fn.setter, @fn.deleter

Die genannten Dekoratoren sind besondere, welche man als Descriptor beschreibt. Auch diese werden zum Method-Overloading verwendet, da sie mehrere Methode mit dem gleicher Bezeichnung so ausstatten, dass diese, aufgrund der Art der Verwendung, sich unterschied verhalten. Da es sich um Dekoratoren handelt müssen sie nur vor der Methode angebracht werden, welche den Bezeichner haben, über den sie mit dem '.'-Operator erreicht werden soll.

<sub>(David Beazley spricht in seinem [Tutorial: YouTube: Python 3 Metaprogramming](https://youtu.be/sPiWg5jSoZI) von 'owning the dot'. Klingt eigentlich spannender als es ist, weil er mit Descriptoren den Zugriff auf eine Variable in 100 Wegen überprüft. Dazu später mehr.)</sub>

Code: [\_4_standard_descriptor_dekoratoren_1.py](_4_standard_descriptor_dekoratoren_1.py)

```py
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    @property
    def gpu(self):
        # Beispiel: Zugriffsrechte überprüfen
        return self._gpu

    @gpu.setter
    def gpu(self, value):
        # Beispiel: Type/Value-Cheking
        self._gpu = value

    @gpu.deleter
    def gpu(self):
        # Beispiel: Löschen dokumentieren/aufzeichnen
        del self._gpu


pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070')

pc_instanz.gpu                # Lesezuegriff, @property-Method wird aufgerufen
pc_instanz.gpu = 'RTX3090'    # Schreibzugriff, @gpu.setter-Method wird aufgerufen
del pc_instanz.gpu            # Löschen des Attributs, @gpu.deleter-Method wird aufgerufen
```

Wichtig ist, dass in diesem Fall das eigentliche Attribut nicht den gleichen Namen wie die Methode haben darf, da man sonst in einer Endlosschleife landet. Man kann dies umgehen, indem man direkt auf das Instanz-Dict Zugreift. Das zeige ich später noch. Hier nur das Beipsiel, an was man denken sollte.

```py
@property
def gpu(self):
    return self.gpu
```

Die Zeile 'return self.gpu' würde darin enden, dass durch 'self.gpu' wieder die @property-Methode aufgerufen wird. Das Gleiche gilt für die setter und deleter Methoden. (Endless Recursion... Pythons Default Limit 1000)

<pre>
> Traceback (most recent call last):
>   File "_pydevd_bundle/pydevd_cython.pyx", line 1557, in _pydevd_bundle.pydevd_cython.> ThreadTracer.__call__
> RecursionError: maximum recursion depth exceeded
> Fatal Python error: Cannot recover from stack overflow.
</pre>

Und wozu soll das gut sein? Naja, im Vergleich zu dem normalen Zugriff ist es jetzt möglich beim Schreiben eines Attributs ein Value/Type Checking durchzuführen. Man könnte das Löschen des Attributs loggen, Lesezugriffe beschränken etc. Und das alles würde ganz automatisch im Hintergrund passieren, ohne dass der Zugriff über 'instanz.attribut' sich ändern müsste.

Man kann diese Methode auch damit umsetzten, indem man property() als Funktion aufruft und einem Attribut zuweist. In der property()-Funktion müssen dann die jeweiligen Funktionen für die einzelnen Zugriffe übergeben werden.

Code: [\_5\_\_standard_descriptor_dekoratoren_2.py](_5__standard_descriptor_dekoratoren_2.py)

```py
class PC:
    attr = property(get_func, set_func, delete_func, doc_string)
```

Die übergebenen Funktionen können damit sogar an einem belibgen Orten definiert sein. Die 'Built-In'-Property Methode verknüpfte diese nur an ein Attribut. Das heißt:

- wenn 'pc_instanz.attr' verwendet wird, dann wird die get_func ausgeführt.
- wenn 'pc_instanz.attr =' verwendet wird, dann wird die set_func ausgeführt.
- wenn 'del pc_instanz.attr' verwendet wird, dann wird die delete_func ausgeführt.

Der allgemeine Nachteil ist, dass man die property-Desriptoren nicht wiedervwerdenden kann. Da man im inneren nicht unterscheiden kann, um welches Attribut es sich handelt.

Das Problem lässt sich aber mit eigenen Descriptoren beheben. Descriptoren sind meiner Meinung nach eine coole Sache und für ein fortgeschrittenes Klassendesign können sie sehr hilfreich sein. Deshalb gibt es zu diesen noch ein eigenes Kapitel, wie man eigene Descriptoren erstellt.

<br/>

#### 2.1.3 Weiteres Overloading

Das Standard Package _typing_ enthält einene Dekorator names '@overload', aber damit habe ich micht nicht tiefer beschäftigt. Sollte hier lediglich ein Hinweis sein.

Wenn man mal darüber nachdenkt, dann sind bereits die 'Built-In' Operatoren auch schon überladen. Mit '+' kann ich Floats, Ints, Strings, Lists, ... etc addieren und erhalte trotzdem ein Ergebnis zurück, obwohl sich die Argumente vom Typ her sehr unterschieden können.
