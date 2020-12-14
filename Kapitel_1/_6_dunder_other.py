# --- Klassendeklaration mit Konstruktor, 'Dunder'-Add und 'Dunder'-GreaterThan --- #
class Person:
    def __init__(self, vermoegen):
        self.vermoegen = vermoegen

    # self + other
    def __add__(self, other):
        return self.vermoegen + other.vermoegen

    # self > other
    def __gt__(self, other):
        if self.vermoegen > other.vermoegen:
            return True
        else:
            return False

# --- Instanziierung der Person Klasse mit unterschiedlichem Vermoegen --- #
P1 = Person(vermoegen=10_000)
P2 = Person(vermoegen=15_000)

# ---  Addition der Instanzen --- #
print("Gemeinsames Vermoegen:", P1+P2)

# --- Vergleich der Vermoegen --- #
# Da nur __gt__ definiert ist könnte man nicht P1<P2 machen, das würd die __lt__ Aufrufen.
print("P1 hat mehr als P2:", P1>P2)
print("P2 hat mehr als P1:", P2>P1)