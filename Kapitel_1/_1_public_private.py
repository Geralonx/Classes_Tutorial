# Klassendeklaration mit Konstruktor
class PC:
    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.__ram = ram


# Instanziierung einer Klasse
# Ich bevorzuge die Initialisierung mit den Keywords
pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070Super', ram='GSkill')

# Zugriff auf normale _public_ Attribute
print(pc_instanz.cpu)
print(pc_instanz.gpu)

# Zugriff auf ein _privates_ Attribut
# Auskommentiert, da es einen AttributeError schmeißt.
# print(pc_instanz.__ram)

# Zugriff auf das Instanz-Dictionary, um die Inhalte jener Instanz zu erhalten.
print(pc_instanz.__dict__)

# Zugriff auf das eigentlich _private_ Attribut.
print(pc_instanz._PC__ram)
