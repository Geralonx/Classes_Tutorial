class PC:
    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.__ram = ram


# Instanziierung einer Klasse
# Ich bevorzuge die Initialisierung mit den Keywords
meine_pc_instanz = PC(cpu='Ryzen 7', gpu='RTX2070Super', ram='GSkill')


# Zugriff auf normale _public_ Attribute
print(meine_pc_instanz.prozessor)
print(meine_pc_instanz.grafikkarte)

# Zugriff auf ein _privates_ Attribut
# print(meine_pc_instanz.__ram)

# Zugriff auf das Instanz-Dictionary, um die Inhalte jener Instanz zu erhalten.
print(meine_pc_instanz.__dict__)

# Zugriff auf das eigentlich _priuvate_ Attribut.
print(meine_pc_instanz.__ram)
