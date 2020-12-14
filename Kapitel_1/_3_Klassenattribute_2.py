# --- Deklaration der Klasse mit einem Klassenattribut und dem Konstruktor --- #
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"

    def __init__(self):
        self.attr1 = self.__class__.klassen_attribut  # Zeile 1
        self.attr2 = type(self).klassen_attribut      # Zeile 2
        self.attr3 = PC.klassen_attribut              # Zeile 3
