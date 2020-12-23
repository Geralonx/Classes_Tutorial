# ABC Modul um abstracte Methode zu erstellen, welche von den Kindklassen der PCBase
# Klasse nachträglich selbst implementiert werden müssen.

from abc import ABC, abstractmethod

# Base-Klasse, die Methoden als abstracte Methoden kennzeichnet, damit jene von 
# einer vererbten Klasse nachträglich implementiert werden. Nachteil: Die Fehlermeldung
# kommt erst bei der Instanziiierung.

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

# Kindklasse, welche die abstracten Methoden nicht implementiert.
class PC(PCBase):
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

# Bei der Instanziierung wird ein Fehler erzeugt, da die abstracten Methoden nicht
# von der Klasse implementiert worden sind.
pc_instanz = PC('Ryzen 7', 'RTX2070')

        
