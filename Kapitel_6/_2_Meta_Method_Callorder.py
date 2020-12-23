""" Dieses File soll zum Erkunden einer Metaklasse sein. Es soll dazu dienen, ein
Verständnis dafür schaffen, welche Abläufe mit welchen Argumenten wann gestartet werden.

Als ersten Schritt empfehle ich: Startet das Skript einmal ohne euch den Code anzusehen
und seht euch zu erst an, was der Output ist. Ich habe hier einmal die 4 wesentlichen
'Dunder'-Methods einer Metaklasse verwendet, um zu zeigen in welcher Reihenfolge
diese angewendet werden. Zusätzlich enthält die Ausgabe die Input- und Outputargumente.

Wenn man weiß, in welchem Schritt der Klassenerstellung welche Argumente zur
Verfügung stehen, dann kann man genau an jenen Stellen eingreifen und die Argumente
überprüfen und/oder modifizieren.
"""
print("\n\n")


class MyMeta(type):
    
    @classmethod
    def __prepare__(metacls, clsname, bases, **meta_kwargs):
        retval = super().__prepare__(clsname, bases)
        print("*"*80)
        print("> Metaclass-Method-Call: __prepare__")
        print("\nInput-Arguments")
        print(f"> metacls: {metacls}")
        print(f"> clsname: {clsname}")
        print(f"> bases:   {bases}")
        print(f"> Optional **meta_kwargs:")
        print(f"{meta_kwargs}\n")
        print(f"> Return Value: {retval!r}")
        print("*"*80)
        return retval

    def __new__(metacls, clsname, bases, clsdct, **meta_kwargs):
        retval = super().__new__(metacls, clsname, bases, clsdct)
        print("*"*80)
        print("> Metaclass-Method-Call: __new__")
        print("\nInput-Arguments")
        print(f"> metacls: {metacls}")
        print(f"> clsname: {clsname}")
        print(f"> bases:   {bases}")
        print(f"> clsdct:  {clsdct}")
        print(f"> Optional **meta_kwargs:")
        print(f"{meta_kwargs}\n")
        print(f"> Return Value: {retval!r}")
        print("*"*80)
        return retval

    def __init__(cls, clsname, bases, clsdct, **meta_kwargs):
        retval = super().__init__(clsname, bases, clsdct)
        print("*"*80)
        print("> Metaclass-Method-Call: __init__")
        print("\nInput-Arguments")
        print(f"> cls: {cls}")
        print(f"> clsname: {clsname}")
        print(f"> bases:   {bases}")
        print(f"> clsdct:  {clsdct}")
        print(f"> Optional **meta_kwargs:")
        print(f"{meta_kwargs}\n")
        print(f"> Return Value: {retval!r}")
        print("*"*80)
        return retval

    def __call__(cls, *args, **kwargs):
        retval = super().__call__(*args, **kwargs)
        print("*"*80)
        print("> Metaclass-Method-Call: __call__")
        print("\nInput-Arguments")
        print(f"> cls: {cls}\n")
        print(f"> *args:")
        print(f"{args}\n")
        print(f"> **kwargs:")
        print(f"{kwargs}\n")
        print(f"> Return Value: {retval!r}")
        print("*"*80)
        return retval

#------------------------------------------------------------------------------#
print("Start: Definition der neuen Klasse.")
# metakey1 und metakey2 (und weitere) kommen ins **kwargs vom __prepare__, __new__, __init__
class MyClass(metaclass=MyMeta, metakey1=1, metakey2=2):
    cls_attr = 10
    def __init__(self, arg1, arg2, kw1):
        self.arg1 = arg1
        self.arg2 = arg2
        self.kw1 = kw1
print("Ende: Definition der neuen Klasse.\n\n\n")

#------------------------------------------------------------------------------#
print("Instanziierung der neuen Klasse.")
myInstance = MyClass(1, 2, kw1='kwarg1')

#------------------------------------------------------------------------------#
print("\n\n\nStart: Definition einer Kindklasse")
class ChildKlass(MyClass):
    die_antwort = 42
print("Ende: Definition einer Kindklasse")