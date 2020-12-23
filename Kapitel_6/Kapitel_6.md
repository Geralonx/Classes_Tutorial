# Inhalt

- [Kapitel 6 Metaklassen](#kapitel-6-metaklassen)

  - [6.1 Pythons Weg der Klassenerzeugung](#61-pythons-weg-der-klassenerzeugung)

    - [6.1.1 Durchführung](#611-durchführung)
    - [6.1.2 Erläuterung der Ausführlichkeit](#612-erläuterung-der-ausführlichkeit)

  - [6.2 Metaklasse Basics](#62-metaklasse-basics)

    - [6.2.1 Überprüfung der Instanzargumente](#621-überprüfung-der-instanzargumente)

  - [Und weiter?](#und-weiter?)
    <br/>

---

## Kapitel 6 Metaklassen

Fucking finally sind wir endlich im Kapitel der Metaklasse. Man war das ein Weg. Nunja, wie soll ich sagen, ich habe keine Ahnung. Sry. ...

Ich persönlich empfand es am schwierigsten zu verstehen, dass eine Klasse selbst nur eine Instanz einer anderen Klasse ist. Im Standardfall einer Klassendefinition ist sie die Instanz der Klasse 'type'. Mit einer Metaklasse schiebt man dort noch einmal eine Ebene zwischen, wodurch man in den Prozess der Klassenerzeugung eingreifen kann.

### 6.1 Pythons Weg der Klassenerzeugung

Um zu verstehen, in welche Prozesse eine Metaklasse eingreifen kann sollte man erst einmal wissen, wie Python selbst eine Klasse erzeugt. Im wesentlichen passiert das in 4 einfachen Schritten.

#### 6.1.1 Durchführung

1. Der Kopf der Klasse, also 'class MyClass(Bases):', wird vom Body der Klasse getrennt.
2. Es wird mittels der 'Built-In' Funktion/Klasse type ein Class-Dictionary gebildet.
3. Das Class-Body wird in dieses Class-Dictionary executiert.
4. Mittels der 'Built-In' Funktion type wird ein neues Klassenobjekt erzeugt.

Folgender Code wird von Python impliziet durch die beschriebenen 4 Schritte ausgeführt.

Code: [\_1_pythons_weg.py](_1_pythons_weg.py)

```py
# Helper-Class um bases (Vererbung) mit einzubeziehen
class Base:
    pass

# Class-Head
class MyClass(Base):

    # Class-Body
    class_attr = 42

    def __init__(self, arg1):
        self.arg1 = arg1

    def say_hi(self):
        print("hi")
```

Schritt 1: Aufteilung des Class-Header und des Class-Body

```py
clsname = 'MyClass'
bases = (Base,)

clsbody = '''
# Class-Body
class_attr = 42

def __init__(self, arg1):
    self.arg1 = arg1

def say_hi(self):
    print("hi")
'''
```

Schritt 2: Vorbereiten des Klassen-Dictionary

```py
clsdct = type.__prepare__(clsname, bases)
```

Schritt 3: Executieren des Class-Body in das Klassen-Dictionary.

```py
exec(clsbody, globals(), clsdct)

print(clsdct)
```

<pre>
> {'class_attr': 42, '__init__': >function __init__ at 0x000001BEDAE58AF0<, 'say_hi': >function say_hi at 0x000001BEDAE58CA0<}
</pre>

Wie bereits ganz am Anfang erklärt muss man sich nur das Klassen-Dictionary angucken, um zu sehen, was in jener Klasse enthalten ist. Nach der Exec-Funktion enthält das clsdict die Klassenspezifischen Inhalte, die im Body einer Klasse definiert sind. Durch das Erzeugen im letzten Schritt werden noch einige Standard-Attribute in diesem Klassen-Dictionary hinzugefügt und ein Klassenobjekt wird erzeugt.

Schritt 4: Erzeugung einer neuen Klasse

```py
MyClass = type(clsname, bases, clsdct)

print(MyClass.__dict__)
```

<pre>
{'class_attr': 42, '__init__': >function __init__ at 0x000001BEDAE58AF0<, 'say_hi': >function say_hi at 0x000001BEDAE58CA0<, '__module__': '__main__', '__doc__': None}
</pre>

Nach dem Schritt 4 entspricht 'MyClass' exakt dem Gleichen was wir oben vorher durch 'class MyClass(Base):' definiert haben. Es besteht zwischen diesen beiden Objekten / Weisen kein Unterschied im Ergebnis.

<sub>(Randnotiz 1: Wer mal genau hinschaut wird sehen, dass die Methoden der ausgegebenen Dictionarys an den selben Adressen existieren.)</sub>

#### 6.1.2 Erläuterung der Ausführlichkeit

Warum habe ich den Scheiß jetzt so in der Tiefe erklärt? Soetwas macht doch kein Mensch von Hand, bist du nicht ganz sauber?

Eine Metaklasse ist immer eine Kindklasse von der 'type'-Klasse und verwendet mittels super() call auch jene Methoden, um das Dict oder das Objekt zu erzeugen. Lediglich kann man mittels einer Metaklasse in diesen Prozess einfacher eingreifen, als würde man diese Schritte von Hand durchführen. Außerdem verbreitet sich das Verhalten einer Metaklasse über Vererbung, wodurch man wieder Gewinn in der Code-Wiederverwendung entsteht. Am Ende des Tages bleibt aber der implizite Python Weg, um die neue Klasse an sich zu erzeugen. Ich denke man sollte den kennen, um zu verstehen, wann man in welche Prozesse eingreift.

### 6.2 Metaklasse Basics

Eine Metaklasse wird normal wie jede andere Klasse geschrieben. Lediglich verwendet man bei Metaklassen besondere 'Dunder'-Methoden, die man bei normalen Klassen nicht verwendet. Dazu gehören

- \_\_prepare\_\_
- \_\_new\_\_

außerdem verwendet man manchmal die \_\_init\_\_ und die \_\_call\_\_ Methode.

Wie im ersten Teil bereits erwähnt muss die \_\_prepare\_\_-Methode ein Mapping- oder Dictionaryobjekt zurückgeben. Wenn man daran keine beasonderen Anforderungen hat, kann man diese Methode einfach weglassen. Im Gegensatz zu der prepare-Method wird man bei der Verwendung einer Metaklasse immer mindestens eine der \_\_new\_\_, \_\_init\_\_ oder \_\_call\_\_ Methoden benötigen. Damit man nun weiß, wann man welche verwenden sollte empfehle ich euch, mit diesem py-File etwas herumzuspielen.

Code: [\_2_Meta_Method_Callorder.py](_2_Meta_Method_Callorder.py)

Ich habe dort die vier Methoden einmal mit einem größeren Printblock versehen, damit ihr seht, in welcher Reinehnfolge und mit welchen Argumenten die jeweilige Methode aufgerufen wird. Ich würde euch empfehlen, einfach mal das Skript zu starten, en Output zu lesen und anschließend reinzuschauen was dort geschrieben steht. Als zweiten Schritt könnt ihr im unteren Teil einfach mal eine eigene Klasse schreiben und mit der Metaklasse ausstatten. Einfach um ein gefühl dafür zu bekommen, wie eine normale Klasse in der Metaklasse zerlegt und zusammengebaut wird.

#### 6.2.1 Überprüfung der Instanzargumente

Wenn man die Reihenfolge in der eine Metaklasse arbeitet einmal verstanden hat ist es auch keine weitere Magie. Das Schwierige meiner Meinung nach ist konkrete Anwendungsfälle zu zeigen.

Folgender Code zeigt eine Metaklasse, die überprüft, ob alle Attribute in der \_\_init\_\_ kleingeschrieben sind.

Code: [\_3_check_instance_args.py](_3_check_instance_args.py)

```py
import inspect

# --- Metaklasse mit den 'Regeln' für die Klassenerstellung --- #
class CheckInstanceArgs(type):

    def __new__(metacls, clsname, bases, clsdct, **kwargs):
        """ New Method durchsucht das Klassen-Dict nach der __init__ Methode und
        überprüft die gesetzten Argumente nach der Schreibweise. Wenn sie nicht
        klein geschrieben sind, dann wird en NameError erhoben.
        """
        if '__init__' in clsdct:
            init_code = inspect.getsource(clsdct['__init__'])
            init_code = metacls.check_init_code(init_code)
        return super().__new__(metacls, clsname, bases, clsdct)

    @staticmethod
    def check_init_code(init_source):
        """ Diese Methode durchsucht den übergebenen source_code nach 'self.' und
        überprüft, ob das Argument / Methode kleingeschrieben ist.

        Wenn dem nicht der Fall ist wird ein TypeError erhoben.
        """

        # Zerlegung des Init-Codes in die einzelnen Zeilen
        lines = init_source.strip().split("\n")
        search_pat = 'self.'

        for line in lines:
            if search_pat not in line:
                continue
            # Stringaufteilung in das Argument nach dem 'self.' Teil.
            temp_line = line.strip()
            temp_line = temp_line.split('=')[0].strip()
            argument = temp_line.split(search_pat)[1]

            # Wenn sich das Argument nach der Wandulung in lowercase von sich
            # selbst unterscheidet, dann enthält es uppercases.
            if argument.lower() != argument:
                raise NameError("Deine Instanzattribute dürfen ausschließlich aus [a-z][0-9][_] bestehen.")


# --- Normale Klassen --- #
class MyClass(metaclass=CheckInstanceArgs):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.Arg2 = arg2
        self.arG3_ = arg3

    def arg1_add_arg2(self):
        print(self.arg1 + self.Arg2)
```

<pre>
> ...
> NameError: Deine Instanzattribute dürfen ausschließlich aus [a-z][0-9][_] bestehen.
</pre>

Selbstverständlich ist dies nur ein Beispiel. Argumente in anderen Methoden werden nicht überprüft und auch nachträgliche Änderung im Instanz-Dict werden so nicht überprüft. Es soll lediglich die Idee vermitteln, in welchen Prozess hier eingegriffen wird. Denn bereits vor der Instanziierung wird die Klasse überprüft.

### 6.3 Abstract Base Class / Meta

In der standard Libary von Python ist ein ABC-Module vorhanden, welches dazu dienen soll, ein eigene Klassentemplate zu erstellen. Ich möchte nicht ins Detail gehen, was man mit diesem Modul alles machen kann, aber es ist interesannt zu wissen. Persönlich finde ich die 'abstract'-Dekorator man nützlichsten.

#### 6.3.1 'Abstract'-Dekorator

Wenn eine Klasse die _ABC_-Klasse als Elternklasse oder die _ABCMeta_ als Metaklasse hat, dann kann man mit diesen Dekoratoren vorschreiben, welche Methoden und Propertys in der Kindklasse verpflichtend mit implementiert werden müssen.

Code: [\_4_abc_example.py](_4_abc_example.py)

```py
from abc import ABC, abstractmethod

class PCBase(ABC):

    @abstractmethod
    def overclock(oc_in_percent):
        pass

    @classmethod
    @abstractmethod
    def get_total_power(cls):
        pass

    @staticmethod
    @abstractmethod
    def mir_faellt_nichts_mehr_ein():
        pass

class PC(PCBase):
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

pc_instanz = PC('Ryzen 7', 'RTX2070')
```

<pre>
> Traceback (most recent call last):
>   File "f:/Python-Projects/Projects/Classes_Tutorial/Kapitel_6/_4_abc_example.py", line 25, in <module>
    pc_instanz = PC('Ryzen 7', 'RTX2070')
> TypeError: Can't instantiate abstract class PC with abstract methods get_total_power, mir_faellt_nichts_mehr_ein, overclock
</pre>

Die Grundklasse ABC hat selbst die Metaklasse ABCMeta. Sobald man eine Klasse mit nicht definierten abstractmethods versucht zu instnziieren, wird der Fehler ausgegeben.

<sub>(Randnotiz 1: Ich verstehe nicht, wieso das nicht bereits durch die Metaklasse bei der Klassendefinition der PC Klasse überprüft wird. Ich habe mich aber auch nicht so in der Tiefe mit dem ABC Modul befasst.)
</sub>

[Python Docs: abc - Abstract Base Classes](https://docs.python.org/3/library/abc.html)

### Und weiter?

An dieser Stelle besteht gerade für mich die Schwierigkeit euch weiteres im Detail zu erklären, denn im wesentlichen ist die Metaklasse nichts anderes als eine Python-Klasse, welche mit den Daten der Klassendefinition arbeitet. Man muss sich an dieser Stelle ja selbst überlegen, brauche ich eine Metaklasse? Was möchte ich machen? Welche Prozesse will ich steuern/überwachen/eingreifen?
