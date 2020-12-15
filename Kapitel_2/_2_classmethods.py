# --- Deklaration einer Klasse mit Konstruktor und Factory/Class-Method als alternative Instanziierungsmöglichkeit --- #
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # --- Facorymethod, um eine Instanz der 'Cricle' Klasse mittels dem Durchmesse zu erstellen --- #
    @classmethod
    def from_diameter(cls, diameter):
        calculated_radius = diameter/2
        return cls(radius=calculated_radius)

# --- Instanziierung über den Standardkonstruktor --- #
c1 = Circle(10)

# --- Instanziierung über die Factorymethod --- #
c2 = Circle.from_diameter(40)


print(c1.radius)
print(c2.radius)

# 10
# 20