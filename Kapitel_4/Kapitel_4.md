# Inhalt

- [Kapitel 4 Descriptor Protokol](#kapitel-4-Descriptor-protokol)
  - [4.1 Allgemein](#41-anwendung)
    - [4.1.1 Anwendung](#411-allgemein)
    - [4.1.2 Type- und Valuechecking](#412-type--und-valuechecking)
    - [4.1.3 Zusammenfassung](#413-zusammenfassung)

## Kapitel 4 Descriptor Protokol

Descriptoren sind Klassen, welche in den Prozess des Attributszugriff eingreifen und zusätzliche Funkionalität hinzufügen. Der Vorteil von eigenen Discritopren, gegenüber den Descriptoren der standard Libary ([2.1.2 @property, @fn.setter, @fn.deleter](#212-@property,-@fn.setter,-@fn.deleter)), ist, dass das Protokol für alle Instanzen des Descriptors in einer eigene Klasse definiert werden kann. Dadurch lassen sich Descriptoren einfacher warten und erweitern, indem sie in eine neue Klasse vererbt werden und weitere Funktionalität hinzugefügt wird.

[Python Docs: Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)

[Python Docs: Implementing Descriptors](https://docs.python.org/3/reference/datamodel.html?highlight=__get__#implementing-descriptors)

[Stackoverflow: When and why use an Descriptor over property()](https://stackoverflow.com/questions/5842593/when-and-why-might-i-assign-an-instance-of-a-descriptor-class-to-a-class-attribu)

### 4.1 Anwendung

Bei Descriptoren unterscheidet man zwischen 'Data-Descriptor' und 'Non-Data-Descriptor'. 'Non-Data-Descriptors' sind dadurch definiert, dass sie **nur** die \_\_get\_\_-Method enthalten. Für 'Data-Discriptros' muss die \_\_set\_\_ und/oder die \_\_delete\_\_ Method definieren werden. Man unterscheidet aus dem Grund zwischen diesen Typen, da ein 'Non-Data-Descriptor' beispielsweise auch den Zugriff auf eine Methode steuer kann und deswegen nur die \_\_get\_\_-Method benötigt.

Die Descriptor-Klasse wird durch folgende 'Dunder'-Methods beschrieben.

- \_\_get\_\_
- \_\_set\_\_
- \_\_delete\_\_
- \_\_set_name\_\_

<sub>(Randnotiz 1: Es ist natürlich völlig in Ordnung weitere Methoden in der Descriptorklasse zu definieren. Lediglich die oben genannten Methoden machen eine Klasse erst zu einem Descriptor)
</sub>

#### 4.1.1 Allgemein

Ein Attribut, welches mit einem Descriptor arbeiten soll, muss in der Klasse als Klassenattribut deklariert werden. Anschließend kann mit der gleichen Bezeichnung in den Methoden und in den Instanzen weitergearbeitet werden.

Bei der Deklaration, dass ein Attribut ein Descriptor ist, wird automatisch die \_\_set_name\_\_ aufgerufen, sofern diese vorhanden ist. Dies wird häufig dazu verwendet, um die Namen des Attributs für die Zugriffsverarbeitung innerhalb der Descriptorklasse zu haben. Diese Methode ist aber optional.

Code: [\_2_basic_descriptor.py](_2_basic_descriptor.py)

```py
class Descriptor:
    def __set_name__(self, owner_cls, name):
        self.name = name

    def __get__(self, instance, owner_cls=None):
        print(f"Get {self.name!r}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Set {self.name!r} to {value!r}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Delete {self.name!r}")
        del instance.__dict__[self.name]

class MyClass:
    attr = Descriptor()

    def __init__(self, attr):
        self.attr = attr

instanz = MyClass('value_1')
instanz.attr
del instanz.attr
# Set 'attr' to 'value_1' -> Hervorgerufen durch 'self.attr = attr' in der init
# Get 'attr'
# Delete 'attr'

```

Das Attribut 'attr' wird in dieser Klasse als Descriptor erzeugt. Wenn wir zurück an die [1.1.3 Klassenattribute](#113-klassenattribute) denken, dann könnte man meinen, dass der Zugriff doch einfach Umgangen wird, da ein neues Attribut innerhalb der Instanz erzeugt wird, aber dem ist nicht so.

Durch die default Implementation der \_\_getattribute\_\_ Methode wird vor dem Zugriff überprüft, ob das Attribut auf Klassenebene als Descriptor deklariert ist. Wenn ja, dann wird dieser auch verwendet.

#### 4.1.2 Type- und Valuechecking

Aus Descriptoren lässt sich sehr einfach ein allgemeines System zum Type und Valuechecking einführen.

Der nachfolgende Code stammt zum großen Teil aus dem Tutorial von David Beazley [YouTube: Python 3 Metaprogramming](https://youtu.be/sPiWg5jSoZI))

Code: [\_3_typed_descriptor.py](_3_typed_descriptor.py)

```py
class Descriptor:
    def __set_name__(self, owner_cls, name):
        self.name = name

    def __set__(instance, value):
        print(f"Set Attribut {self.name!r} to {value!r}.")
        instance.__dict__[self.name] = value

class Typed(Descriptor):
    dtype = None

    def __set__(self, instance, value):
        # Check Datatype
        assert isinstance(value, self.__class__.dtype), f'Das Attribut {self.name!r} muss vom Datentyp {self.dtype!r} sein!'
        super().__set__(instance, value)

class Integer(Typed):
    dtype = int

class Float(Typed):
    dtype = float

class String(Typed):
    dtype = str

class Positive(Discriptor):
    def __set__(self, instance, value):
        if value >= 0:
            super().__set__(instance, value)
        else:
            raise ValueError("The value for this Attribute needs to be >= 0.")

class PositiveInteger(Integer, Positive):
    pass
```

Man erstellt einen Grunddescriptor, welcher im letzten Schritt den Attributszugriff durchführt. Anschließend wird diese Grundklasse in spezalisierten Klassen erweitert. Auch bei Descriptoren kann man verschiedene Eigenschaften durch das Kombinieren von verschiedenen Descriptoren erhalten. Wie bereits im Kapitel der Klassenvererbung angesprochen ist die Reihenfolge der Vererbung wichtig. Ansonsten könnte es passieren, dass man im Beispiel des PositiveInteger-Descriptor, einen String auf einen Zahlenwert vergleicht, weil der 'Positive' Descriptor vor dem 'Integer' Descriptor in der \_\_mro\_\_ steht.

Weitere Ideen:<br/>
RangedInteger<br/>
EvenIntegers<br/>
OddIntegers<br/>
SizedString<br/>
RegExString<br/>
ODBCDescriptor (Oder Datenbankdescriptor allgemein)<br/>
PostGetDescriptor(?)<br/>
...

Man könnte in den set/get Methoden des Descriptors ja auch Zugriffe über externe Verbindungen durchführen, wieso auch nicht, der einzige Unterschied ist ledgilich, wie jene Methoden aufgerufen werden.

#### 4.1.3 Zusammenfassung

Immer wenn man für Attribute einen besonderen Zugriff benötigt oder eine automatische Weiterleitung in Erwähgung zieht, dann sollte man Descriptoren in Betracht ziehen.
