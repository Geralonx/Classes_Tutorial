# --- Deklaration der Klasse mit einem Konstruktor und der 'Dunder'-rpr-Method --- #
class PC:
    def __init__(self, cpu, gpu):
        self.cpu = cpu
        self.gpu = gpu

    def __repr__(self):
        argument_string_list = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        init_string = ', '.join(argument_string_list)
        return f'{self.__class__.__name__}({init_string})'

# --- Instanziierung der PC Klasse --- #
pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070Super')

# --- Die repr() Funktion greift auf die __repr__() Methode des übergebene Objekts zu --- #
# Da diese auch einen String zurück gibt kann der direkt auch geprinted werden
print(repr(pc_instanz))
