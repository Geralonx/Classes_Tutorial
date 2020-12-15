# --- Diese Klasse soll demonstrieren, dass das 'other'-Arguemnt der 'Dunder'-Methods alles sein darf ---#
class IntStringAdder(int):
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, str):
            try:
                x = int(other)
            except:
                raise ValueError(f"String Value >{other}< cannot be converted to 'int'.")
        else:
            raise TypeError("Wrong datatype, expected a 'str' as 2nd operand.")
        return IntStringAdder(self.number + x)

    def __str__(self):
        return f"My Value is {self.number}"


# --- Instanziierung der Klasse mittels Konstruktor --- #
my_number = IntStringAdder(10)

# --- Addition mittels expliziter Syntax und implizitem Methodenaufruf --- #
# --- Die Rückgabe ist eine neue Instanz der Klasse --- #
my_new_number = my_number + '15'

print(my_new_number)


# --- Wirft einen Error, da sich der str-Wert 'Simon' nicht in einen Integer umwandeln lässt --- #
my_new_number = my_number + 'Simon' 