class MyMeta(type):
    """ Diese Metaklasse soll die Conventionen der Libary überwachen.
    
    Conventionen: Alle Methoden und Attribute müssen klein geschrieben sein"""
    def __new__(metacls, clsname, bases, clsdict):
        # Regel 1: Alle Methoden sollen klein geschrieben sein
        methods = [method for method in clsdict.keys() if not method.startswith('__') and not method.endswith('__')]
        # Keine if-Abfrage nötig. Wenn eine List-Comprehension keine Werte zurückliefert ist die Liste leer. 
        # Leere Liste -> for-Loop wird übersprungen.
        for method in methods:
            # Wenn der Name der Methode ungleich der Name der Method in kleinen Buchstaben ist.
            if method != method.lower():
                raise TypeError(f"Alle Methoden der klasse muessen kleingeschrieben sein. Methods: {methods}.")

        return super().__new__(metacls, clsname, bases, clsdict)

# Klasse die gegen die Conventionen verstößt.
class MyClass(metaclass=MyMeta):
    def __init__(self, arg1):
        self.Arg1 = arg1

    def GetArg1(self):
        return self.Arg1

    def getPowerAct(self):
        pass

mc = MyClass(1)


print(mc.__class__.__mro__)

