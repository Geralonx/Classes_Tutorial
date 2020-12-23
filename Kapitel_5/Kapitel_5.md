# Inhalt

- [Kapitel 5 Klassendekoratoren](#kapitel-5-klassendekoratoren)
  - [5.1 Allgemein](#51-allgemein)
    - [5.1.1 Klassendekorator](#511-klassendekorator)
    - [5.1.2 Zusammenfassung](#512-zusammenfassung)

<br/>

---

## Kapitel 5 Klassendekoratoren

Klassendekoratoren sind der erste Schritt zur Metaklasse. Viele Dinge, die man mit Metaklassen realisieren kann, könnte man auch mit Klassendekoratoren erreichen. Die Frage wozu man Metklassen dann überhaupt lässt sich mit den zwei wesentlichen Unterschieden beantworten.

1. Klassendekoratoren werden **NACH** der Erzeugung der Klassendefinition angewandt. Metaklassen werden **VOR** der Erzeugung der Klassendefinition durchgeführt.
2. Metaklassen verbreiten sich durch die Vererbung der Grundklasse fort. Ein Klassendekorator wirkt nur auf die Klasse, die damit dekoriert wird.

---

### 5.1 Allgemein

Klassendekoratoren unterscheiden sich von Funktionsdekoratoren nur in der Weise, dass sie, statt der Funktion, eine Klasse als Inputargument haben und eine Klasse zurückgeben. Da die Klassendekoratoren nach der Erzeugung der Klasse aufgerufen werden hat die Klasse bereits ein vollständig gefülltes Dict, welches alle Inhalte des Class-Bodys enthält. Man kann damit also, nachdem die Klasse erzeugt wurde, in den Inhalten herumdoktorn. Man kann einfach in das Klassen-Dict greifen, eine oder mehrere Funktionen herausnehmen, sie mittels einem Dekorator verändern und anschließend zurück in das Klasse-Dict stecken.

<br/>

#### 5.1.1 Klassendekorator

Mittels diesem Klassendekorator wird, abgesehen von den 'Dunder'-Methods, jeder Methode eine Debug-Print hinzugefügt. Es gibt den Namen der Funktion, das Datum und die übergeben Argumente aus.

```py
from functools import wraps
from datetime import datetime

# Funktionsdekarote der als Helper verwendet wird
def debugger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n{func.__qualname__!r} aufgerufen am {datetime.now()}: Übergabeparameter: {args}, {kwargs}.")
        return func(*args, **kwargs)
    return wrapper


# Klassendekorator
def debug_all_cls_methods(cls):
    # Alle Elemente des Klassendicts durchsuchen
    for key, element in cls.__dict__.items():
        # Filtern nach den Aufrufbaren elementen (Klassenattribute werden herausgefiltert)
        if callable(element):
            # Rausfiltern der 'Dunder'-Methods (Wenn man möchte)
            if not key.startswith('__') :
                # Die orginale Methode der Klasse wird einfach an der gleichen Stelle durch die dekorierte Methode überschrieben
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

pc_instanz = PC('Ryzen 7', 'RTXSuper2070')

pc_instanz.but_can_it_run_crysis(False)
pc_instanz.power(ampere=2, voltage=230)
```

<pre>
> 'PC.but_can_it_run_crysis' aufgerufen am 2020-12-14 19:02:13.323263: Übergabeparameter: (<__main__.PC object at 0x000001F276717940>, False), {}.
> No it can't.

> 'PC.power' aufgerufen am 2020-12-14 19:02:13.336117: Übergabeparameter: (<__main__.PC object at 0x000001F276717940>,), {'ampere': 2, 'voltage': 230}.     
> I consume 460 W right now.
</pre>

Das \_\_main\_\_.PC Object (Die Instanz der Klasse) ist in diesem Fall das _self_-Argument, welches automatisch bei einem Aufruf über eine Instanz übergeben wird. Wir sehen aber, dass **alle** Methoden der Klasse mittels des Debug-Dekorator erweitert wurden. Würde man nur auf Funktionsdekoratoren zurückgreifen, dann müsste man jede Methode einzeln mit einem Ausstatten.

<sub>(Kleine Denkaufgabe: Warum kann ich im Klassdekorator die 'Dunder'-Methods nur anhand der 2 führenden Unterstriche identifizieren und muss nicht noch nach den nachfolgenden Unterstrichen suchen, um sicherzustellen, dass es sich um kein privates Attribut/Methode handelt?)</sub>

## 5.1.2 Zusammenfassung

Wenn man Funktionsdekoratoren, Klassen und das Klassen-Dict verstanden hat, dann sind Klassendekoratoren keine Besonderheit. Man bekommt die Klasse als Input und kann mit der genau die gleichen Dinge anstellen wie außerhalb eines Dekorators. Der einzige Unterschied ist mal wieder, dass dies mit in einem automatischen Prozess im Hintergrund passiert. Wie immer geht es um Code-Reuse und dass die wesentlichen Skripte/Inhalte nicht durch Hintergrunprozesse überladen sind. Kurz ein Dekartor dran und fertig ist das Debuggen/Loggen/Checken, whatever.
