# Inhalt

- [Kapitel 3 Klassenvererbungen](#kapitel-3-klassenvererbung)
  - [3.1 Spezifizieren von Klassen](#31-spezifizieren-von-klassen)
  - [3.2 Komponieren von Klassen](#32-komponieren-von-klassen)
  - [3.3 \_\_mro\_\_ und super()](<#33-__mro__-und-super()>)

<br/>

---

## Kapitel 3: Klassenvererbung

Das Vererben von Klassen verwendet man aus zwei wesentliche Gründen. Der erste Grund, und meiner Meinung nach der häufigere, ist, um eine Klasse zu speifizieren. Der zweite Grund ist, um mehrere Klassen zu einer Gesamtklasse zu komponieren. Dies findet beispielsweise im Fall von _Descriptors_ Anwendung.

---

### 3.1 Allgemein

Wenn eine Klasse vererbt wird hat den Effekt, dass die Kindklasse Zugriff auf alle nicht privaten Attribute und Methoden der Elternklasse(n) bekommt. Vereinfacht gesagt ist eine Kindklasse eine normale Klasse, welche bereits standard Inhalte enthält, ohne dass diese neu in der Kindklasse geschrieben werden müssen. Python hat zudem die Besonderheit, dass die Elternklasse von der Vererbung erfährt und kann damit automatisch im Nachgang der Deklaration einer Kindklasse darauf reagieren kann.

### 3.1.1 \_\_init_subclass\_\_(cls)

Diese 'Dunder'-Method wird immer dann aufgerufen, wenn die Klasse, die diese Methode deklariert, vererbt wird. Nachdem das Objekt der Kindklasse vollständig geformt ist wird in der Elternklasse diese Methode aufgerufen und bekommt die Kindklasse als _cls_ übergeben. Viel mehr kann man dazu nicht sagen. Beispielsweise ist es damit möglich alle definierten Kindklassen einer Baseklasse zu sammeln.

### 3.1 Spezifizieren von Klassen

Um in Python Klassen zu vererben muss bei deklaration der Kindklasse in Klammern die Elternklasse(n) angegeben werden. Im einfachsten Fall hat eine Kindklasse eine einzige Elternklasse, mehrere sind auch möglich.

Ein Beispiel wäre gemeinsame Eigenschaften bestimmten Gruppen zu finden. Ein Student ist eine Person mit einem Namen, Anschrift, Geschlecht, ... etc. Das Gleiche gilt aber auch für einen Arbeitnehmer. Diese Dinge würde man in einer Elternklasse 'Person' zusammenfassen und die speziellen Attribute, welche nur auf eine bestimmte Gruppe zutrifft, durch Vererbung erweitern. Ein Student hat eine Matrikel-Nummer, ein Arbeitnehmer nicht. Umgekehrt verdient ein Arbeitnehmer einen Lohn, ein Student aber nicht. Durch das Vererben und Spezifizieren von Kindklassen spart man sich die wiederholte Definition der gemeinsamen Attribute.

Code: [\_1_person_spezifizieren.py](_1_person_spezifizieren.py)

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
employee = Employee(fname='Maria', lname='Musterfrau', salary=40_000)
```

Für die Instanziierung von Kindklassen kann man verschiedene Ansätze wählen. In dem oben gezeigten Beispiel sind im Student-Konstruktor alle Parameter, welche zum Erzeugen einer Instanz benötigt werde, statisch definiert.

Bei der Employee-Klasse hingegen ist der Ansatz mit \*\*kwargs gewählt worden. Die neuen Attribute der Kindklasse werden einfach in den Konstruktor eingetragen und der Rest wird einfach als \*\*kwargs eingefangen und als Gesamtpaket an die 'nächsthöhere' Klasse weitergeleitet.

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

- Es können belibige Keywords als Argumente übergeben werden und nur die benötigten werden herausgepickt.
- Die Weiterleitung der Argumente ist kürzer.
- Kein Modifizieren der Kindklasse nötig, falls sich etwas in der Elternklasse ändert.

Nachteile:

- Help und inspect Methoden liefern einen nicht spezifizierten Konstruktoaufruf zurück. (In diesem Fall eben \_\_init\_\_(salary, \*\*kwargs))
- Kwargs, welche gar Nicht existieren, werden vom Konstruktor akzeptiert, auch wenn diese nicht verwendet werden. (Diese würden dann auf dort zum Crash führen, wo keine \*\*kwargs mehr akzeptiert werden. In desem Fall in der Elternklasse Person.)
  <br/><br/>

Wofür man sich entscheidet ist sicherliche Anwendungsabhängig. Was habe ich mit der Klasse noch alles vor? Erwarte ich weitere Kindklassen? Werden die Klassen eventuell soagr zusammen vererbt? Dass man für die Help-Methode eine gesamte Darstellung des Konstruktors bevorzugt macht für den späteren Anwender mehr Sinn. Dieses Problem mit dem zweiten Ansatz und der Tatsache, dass die Darstellung \_\_init\_\_(salary, **kwargs) wenig hilfreich ist, ließe sich aber mit Metaklassen kontrollieren. Obwohl **kwargs verwendet wird, würden dann trotzdem alle benötigten Paramerter der Elternklasse(n) mit angezeigt werden. Dadurch verliert man nicht die Dynamik, dass man die Änderungen der Elternklassen mit in die Kindklassen einpfelgen müsste.

---

### 3.2 Komponieren von Klassen / mehrfache Vererbung

Beim Komponieren von Klassen wird eine neue Klasse erzeugt, welche von mehreren Elternklassen erbt. In diesem Beispiel wird der Student mit dem Employee vereint. (Sogesehen eine Stundentische Hilfskraft?) Da die neue Klasse keine neuen Parameter benötigt, muss auch kein neuer \_\_init\_\_-Konstruktor geschrieben werden.

Code: [\_2_person_komponieren.py](_2_person_komponieren.py)

```py
class StudentWorker_V1(Employee, Student):
    pass
```

Die neue Klasse enthält all das, was die beiden Elternklassen und deren Elternklassen enthalten. Die Instanziierung sieht dann folgendermaßen aus.

```py
studentworker1 = StudentWorker_V1(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
```

Man verwendet einfach alle Parameter, die von den Elternklasse(n) benötigt werden und gibt sie als Keywordargumente an. Bezüglich den zwei verschiedenen Ansätzen könnte man aber auf ein Problem stoßen.

Wenn man die Vererbungsreihenfolge von Student und Employee vertauscht, dann landet Student zuerst in der \_\_mro\_\_ Reihenfolge und demenstprechend wird der Konstruktor von dieser Klasse zuerst verwendet.

```py
class StudentWorker_V2(Student, Employee):
    pass
```

```py
studentworker1 = StudentWorker_V2(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
```

<pre>
> Traceback (most recent call last):
>   File "f:/Python-Projects/Projects/Classes_Tutorial/Kapitel_3/vererbung_person.py", line 22, in <module>
>     studentworker1 = StudentWorker(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
> TypeError: __init__() got an unexpected keyword argument 'salary'
</pre>

Durch den gewählten Ansatz 1 bei der Student-Klasse bekommt dieser Konstruktor auch das Keyword 'salary'. Dieser weiß aber nichts damit anzufangen und wirft dementsprechend einen TypeError.

Mit dem Ansatz 2, der bei dem Employee gewählt wurde, passiert dies nicht, da jene Argumente, welche nicht bekannt sind, einfach als kwargs zusammengefasst und weitergeleitet werden. In der obersten Klasse, also die Base Klasse Person, könnte man dort auf \*\*kwargs verzichten, um unbekannte Keywords abzufangen und trotzdem einen Fehler zu schmeißen.

---

### 3.3 \_\_mro\_\_ und super()

Sobald Klassenvererbung ein Thema ist sollte man sich im Klaren sein, wie die 'Built-In'-Methode super() funktioniert. Wie es bereits öfters in diesem Tutorial erwähnt wurde, greift die super()-Methode auf das nächste Element in der \_\_mro\_\_ Liste zu, aber was ist diese mro?

MRO steht für 'Method Resolution Order'. Bei der **Definition** (nicht bei der Instanziierung) einer Klasse wird die \_\_mro\_\_ evaluiert und festgelegt. Dieses Attribut ist Read-Only und existiert auf Klassenebene. Die Evaluation der Reihenfolge erfolgt über die [Wikipedia: C3-Linearization](https://en.wikipedia.org/wiki/C3_linearization). Ich werde hier nicht tiefer darauf eingehen, lediglich darauf verweisen, falls es jemanden ganz genau wissen will.

https://stackoverflow.com/questions/40478154/does-pythons-mro-c3-linearization-work-depth-first-empirically-it-does-not

Fakt ist aber, dass eine Linearisierung standardmäßig stattfindet. Und auch hier sei wieder gesagt, in diesen Prozess lässt sich mittels Metaklassen eingreifen, indem ihr innerhalb der Metaklasse die mro()-Methode neu definiert. Der return dieser Methode wird in dem \_\_mro\_\_ Attribut hinterlegt. Wenn ihr aus irgendeinem Grund eine beispielsweise alphabetisch geordnete MRO benötigt, oder einen anderen Algorythmus zur Linearisierung verwenden möchte, dann ginge das.

<sub>(Randnotiz 1: Obwohl das \_\_mro\_\_ Attribut bei der Definition der Klassen evaluiert wird und das Attribut Read-Only ist lässt sich dieses Attribut später dennoch innerhalb der Laufzeit, bzw nach der Definition der Klasse, verändern. Denn dieses Attribut wird jedes mal neu evaluiert, wenn sich die \_\_bases\_\_ einer Klasse ändern. Und das \_\_bases\_\_-Attribut ist schreibbar. Man kann theoretisch im Programmablauf einfach zu jederzeit die vererbten Klassen einer Klasse ändern. Ob man das tun sollte, wahrscheinlich eher nicht. Erklärt hat dies Mark Smith auf der PyCon 2019. [Youtube:"It's Pythons All The Way Down: Python Types & Metaclasses Made Simple" - Mark Smith (PyCon AU 2019)](https://www.youtube.com/watch?v=ZpV3tel0xtQ))</sub>

<br/>

Wenn man sich mit diesem Wissen nun die \_\_mro\_\_ vom StudentWorker_V2 anguckt, erhält man folgende Reihenfolge.

Code: [\_2_person_komponieren.py](_2_person_komponieren.py)

```py
print(StudentWorker_V2.__mro__)
```

```
> (<class '__main__.StudentWorker'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class '__main__.Person'>, <class 'object'>)
```

Obwohl die Klasse _Student_ und die Klasse _Employee_ beide von der Klasse _Person_ erben, steht die Klasse _Person_ hinter den beiden anderen Klassen in der Reihenfolge.

In der Definition der Klasse _Student_ steht

```py
class Student(Person):  # Ansatz 1
    def __init__(self, mat_nr, fname, lname):
        self.mat_nr = mat_nr
        super().__init__(fname, lname) # -> Zugriff auf Employee.__init__
```

die super()-Methode innerhalb der \_\_init\_\_ und greift im Fall der _StudentWorker_V2_ Klasse **NICHT** auf die vererbte Klasse _Person_ zu, sondern geht laut der \_\_mro\_\_ weiter zur Klasse _Employee_. Würde man natürlich die Klasse Student instanziieren, dann würde die super()-Methode zur Klasse _Person_ weiterleiten, da jede Klassendefinition ihre eigene \_\_mro\_\_ Liste hat.

Dort zeigt sich nocheinmal, wieso man das **Hardcoding** unbedingt vermeiden sollte und wieso man mit \*\*kwargs arbeiten sollte. Je nachdem, wie die Klassen vererbt werden, kann man gar nicht wissen, an welcher Stelle die 'Großeleternklassen' der neuen Klasse stehen. Die übergebenen Parameter _fname_ und _lname_ sind beim Aufruf des Employee-Konstruktor nicht ausreichend, da das _salary_ Argument fehlt.
