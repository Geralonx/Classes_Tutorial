# Helper Klasse um im Beispiel mit Bases arbeiten zu könne.
class Base:
    pass

# # Class-Head
# class MyClass(Base):

#     # Class-Body
#     class_attr = 42

#     def __init__(self, arg1):
#         self.arg1 = arg1

#     def say_hi(self):
#         print("hi")

# Der Class-Header wird in den Namen und die Elternklassen aufgeteilt
clsname = 'MyClass'
bases = (Base,)

# Mittels der type.__prepare__ Methode wird ein leeres Dictionary erzeugt,
# welches als Klassen Dicitonary dienen wird. Mittels Metaklassen lässt sich
# später auch andere Dict-Typen verwenden, warum das mal wichtig war erkläre 
# ich dann.
clsdct = type.__prepare__(clsname, bases)


# Der isolierte Class-Body wird als String behandelt.
# Wichtig ist, dass die Python-Syntax berücksichtig wird.
# Das heißt, dass die Indentation-Blocks im String selbst
# auch vorhanden sind.
clsbody = '''
class_attr = 42

def __init__(self, arg1):
    self.arg1 = arg1


def say_hi(self):
    print(math.pi)
    print("hi")
'''

# Der Class-Body wird in das vorbereitete Class-Dict executiert.
# Für den Fall, dass durch importe im Kopf des Files module verwendet
# werden, müssen diese mittels globals() übergeben werden, ansonsten
# würde bei der Verwendung ein NameError aufkommen, da das Modul
# innerhalb der Klasse unbekannt ist.
exec(clsbody, globals(), clsdct)

# print(clsdct)
# {'class_attr': 42, '__init__': <function __init__ at 0x0000017B69208B80>, 'say_hi': <function say_hi at 0x0000017B69208AF0>}

# Durch die 'type' Methode werden anschließend alle 3 Elemente zu
# einem neuen Klassenobjekt geformt.
MyClass = type(clsname, bases, clsdct)

# print(MyClass.__dict__)
# {'class_attr': 42, '__init__': <function __init__ at 0x0000017B69208B80>, 'say_hi': <function say_hi at 0x0000017B69208AF0>, '__module__': '__main__', '__doc__': None}
