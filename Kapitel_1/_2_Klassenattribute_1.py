# --- Deklaration der Klasse mit einem Klassenattribut--- #
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"


# --- Instanziierung einer Klasse ohne Konstruktor eigenen Konstruktor --- #
meine_pc_instanz = PC()

# --- Lesen der Dictionarys, um die Inahlte der Obejkte zu bekommen --- #
print("Instanz Dict: ", meine_pc_instanz.__dict__)
print("Klassen Dict: ", PC.__dict__)

# --- Lesen eines Klassenattributs über die Instanz --- #
print("Zugriff über Instanz: ", meine_pc_instanz.klassen_attribut)

# --- Zuweisung des 'Klassenattributs' über eine Instanz (funktioniert nicht) --- #
meine_pc_instanz.klassen_attribut = "Neuer Wert"
print(meine_pc_instanz.klassen_attribut)

# --- Erneute Ausgabe der Dictionarys, um ihre jeweiligen Inhalte zu bekommen --- #
print("Instanz Dict: ", meine_pc_instanz.__dict__)
print("Klassen Dict: ", PC.__dict__)
