# --- Definition von eigenen Getter/Setter/Deleter Methoden --- #
def my_getter(self):
    print("my_getter-Call")
    return self._gpu

def my_setter(self, value):
    print("my_setter-Call")
    self._gpu = value

def my_deleter(self):
    print("my_deleter-Call")
    del self._gpu

# --- Deklaration der Klasse --- #
class PC:
    # Zuweisung der Portperty-Funktionen auf ein Attribut
    gpu = property(my_getter, my_setter, my_deleter, None)
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

# --- Instanziierung, __init__ verwendet bereits den zugewiesenen setter --- #
pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070')
# my_setter-Call


pc_instanz.gpu                # Lesezuegriff, my_getter wird aufgerufen
# my_getter-Call

pc_instanz.gpu = 'RTX3090'    # Schreibzugriff, my_setter werden aufgerufen
# my_setter-Call

del pc_instanz.gpu            # Löschen des Attributs, my_deleter wird aufgerufen
# my_deleter-Call