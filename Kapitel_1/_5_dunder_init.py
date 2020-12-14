# --- Klassendeklaration mit Konstruktor --- #
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

# --- Instanziierung über die 'Dunder'-Methods --- #
# 'Falscher' Weg (Funktioniert, aber man macht es nicht)
# __new__ erstellt eins leers Objekt einer Klasse
instanz1 = MyClass.__new__(MyClass)
# __init__ initialisiert die übergebene Instanz
MyClass.__init__(instanz1, 'weird_arg1', 'weird_arg2')
print("Instanz1: ", instanz1.__dict__)

# --- Instanziierung der Klasse über den normalen Weg des Konstruktors --- #
# Beim Instanziieren einer Klasse über den richtigen Konstrukor werden die
# __new__ (und __prepare__) Methoden automatisch implizit vor der Initialisierung durchgeführt.
instanz2 = MyClass('arg1', 'arg2')
print("Instanz2: ", instanz2.__dict__)