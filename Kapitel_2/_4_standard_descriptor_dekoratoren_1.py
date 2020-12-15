# --- Deklaration einer Klasse mit Konstruktor und @property Methodoverloading eines Attributs --- #
class PC:
    #  --- Hier wird bereits auf den @gpu.setter zugegriffen --- #
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    # --- Standard Descriptor für das Attribut 'gpu' --- #
    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self, value):
        self._gpu = value

    @gpu.deleter
    def gpu(self):
        del self._gpu

# --- Instanziierung der Klasse. --- #
#  Ausgabe des gpu Attributs, da im __init__ bereist mit dem @gpu.setter gearbeitet wird
pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070')


print(pc_instanz.gpu)         # Lesezuegriff, @property-Method wird aufgerufen
pc_instanz.gpu = 'RTX3090'    # Schreibzugriff, @gpu.setter-Method wird aufgerufen
del pc_instanz.gpu            # Löschen des Attributs, @gpu.deleter-Method wird aufgerufen
