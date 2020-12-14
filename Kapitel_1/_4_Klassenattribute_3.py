# --- Vererbung von Klassenattributen ---#

# --- Klassendeklaration mit einem Klassenattribut --- #
class PC:
    klassen_attribut = "Ich bin ein Klassenattribut"

# --- Klassendeklaration ohne Inhalt, aber mit Elternklasse --- #
class PC2(PC):
    pass


# --- Instanziierung der beiden Klassen --- #
pc1_instanz = PC()
pc2_instanz = PC2()

# --- Ausgabeblock --- #
print('-'*80)       # Formatting Line
print("Ausgabe der Dicitonarys")

# --- Ausgabe des Dictionarys der Klasse PC und der zugehörigen Instanz --- #
print("PC Klassen Dict:", PC.__dict__)
print("PC Instanz Dict:", pc1_instanz.__dict__)

# --- Ausgabe des Dictionarys der Klasse PC2 und der zugehörigen Instanz --- #
print("PC2 Klassen Dict:", PC2.__dict__)
print("PC2 Instanz Dict:", pc2_instanz.__dict__)
print('-'*80)       # Formatting Line

# --- Ausgabe des Klassenattributs der Elternklasse durch die Instanz der Kindklasse --- #
print("pc2_instanz.klassen_attribut: ---> ", pc2_instanz.klassen_attribut)

# AUSGABE DER PRINTS
# --------------------------------------------------------------------------------
# Ausgabe der Dicitonarys
# PC Klassen Dict: {'__module__': '__main__', 'klassen_attribut': 'Ich bin ein Klassenattribut', '__dict__': <attribute '__dict__' of 'PC' objects>, '__weakref__': <attribute '__weakref__' of 'PC' objects>, '__doc__': None}
# PC Instanz Dict: {}
# PC2 Klassen Dict: {'__module__': '__main__', '__doc__': None}
# PC2 Instanz Dict: {}
# --------------------------------------------------------------------------------
# meine_pc2_instanz.klassen_attribut: ---  Ich bin ein Klassenattribut

# Kommentar ----------------------------------------------------------------------
# Man sieht, dass das Dict der Klasse PC2 und das Dict der Instanz das
# 'klassen_attribut' nicht enhalten und dennoch Zugriff darauf besteht.
