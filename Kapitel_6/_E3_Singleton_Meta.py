"""
Eine Klasse, welche die 'SingletonMeta' Klasse als Metaklasse verwendet,
kann nur eine einzige Instanz erzeugen. Die Metaklasse ist so designed worden,
dass sie die mehrere Instanzen von verschiedenen Klassen halten kann, aber niemals
mehr als eine Instanz pro Klasse.
"""

# --- Metaklasse --- #
class SingletonMeta(type):
    # Um die SingletonMeta-Klasse auf mehrere Subklasse anenweden zu können muss
    # eine Weg gewählt werden, wodurch mehrere Referenzen abgespeichert werden
    # können. Würde man statt einem Dict ein normales Attribut genutzt würden,
    # dann könnte nur eine einzige Klasse als SingletonMeta verwendet werden.
    # Würde eine zweite Klasse verwendet werden, würde die Referenz der ersten
    # Instanz verloren gehen.
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """ Klassen-Instanz wird im _instance-Attribut der Metaklasse gesucht und 
        zückgegeben falls eine Instanz der verwendeten Klasse bereits existiert.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
        else:
            print("Diese Klasse wurde bereits instanziiert. Rückgabe der einzigartigen Instanz!")
            return cls._instances[cls]

# --- Normale Klasse --- #
class MyClass(metaclass=SingletonMeta):

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

# --- Programmschleife --- #
def main():
    print("Erste Insanziierung")
    instance_1 = MyClass(10, 20)

    print("Wiederholte Intanziierung")
    instance_2 = MyClass(100, 200)

    print(repr(f"Instance 1: {instance_1}"))
    print(repr(f"Instance 2: {instance_2}"))

    print(f"isnatcne_1.arg1: {instance_1.arg1}")
    print(f"isnatcne_2.arg1: {instance_2.arg1}")



if __name__ == '__main__':
    main()
# Output:
# Erste Instanziierung
# Wiederholte Intanziierung
# Diese Klasse wurde bereits instanziiert. Rückgabe der einzigartigen Instanz!
# 'Instance 1: <__main__.MyClass object at 0x000001C6835B7940>'
# 'Instance 2: <__main__.MyClass object at 0x000001C6835B7940>'
# isnatcne_1.arg1: 10
# isnatcne_2.arg1: 10