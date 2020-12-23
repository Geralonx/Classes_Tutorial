from functools import wraps
from datetime import datetime


# Funktiosndekorator der in diesem Beispiel als Helper verwendet wird
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


# --- Klassendekorator am Kopf der Klasse --- #
@debug_all_cls_methods
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    # Normale Methode die dekoriert wird
    def but_can_it_run_crysis(self, answer):
        if answer:
            print("Yes, it can!")
        else:
            print("No it can't.")

    # Normale Methode die dekoriert wird
    def power(self, voltage, ampere):
        print(f'I consume {voltage*ampere} W right now.')


# ---  Instanziierung und Aufrufen der Methoden --- #
pc_instanz = PC('Ryzen 7', 'RTXSuper2070')

pc_instanz.but_can_it_run_crysis(False)
pc_instanz.power(ampere=2, voltage=230)