# --- Klassendeklaration mit Konstruktor und 'Dunder'-str-Method --- #
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    # __str__(self) -> Rückgabe muss ein String sein
    def __str__(self):
        msg = ""
        msg += f"\nDiese Instanz ist von der Klasse: {self.__class__.__name__}"
        msg += "\nSie hat folgende Attribute:"
        for key, value in self.__dict__.items():
            msg += f"\n\t{key}: \t{value!r} \t| ({type(value)})"
        return msg

# --- Instanziierung der PC Klasse --- #
pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070Super')

# --- print wendet str() auf das übergeben Objekt an. str() greift auf die __str__-Methode zu --- #
print(pc_instanz)
