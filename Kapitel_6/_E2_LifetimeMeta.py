"""
Eine Klasse, welche die 'LifetimeMeta' Klasse als Metaklasse verwendet, 
startet bei der Instanziierung eines Objekts einen Thread, welcher das Objekt
nach Ablauf der Lebenszeit wieder entfernt. Außerdem stell die Metaklasse 
sicher, dass die benötigten Attribute, in diesem Fall das Klassenattribut 
'_lifetime', von der Klasse bereitgestellt werden muss.
"""

# --- Import Standard-Libary --- #
import time, threading


# --- Metaklasse --- #
class LifetimeMeta(type):
    """ Metaklasse um Instanzen nach einer gegeben Lebenszeit zu löschen."""

#------------------------------------------------------------------------------#
    def __new__(clsmeta, clsname, bases, clsdct):
        """ Sicherstellung der Existenz der benötigten Attribute in der neuen Klasse.

        Das Argument 'clsdct' enthält alle Attribute und Methoden der neuen Klasse.
        Dort wird nach dem benötigten Attribut gesucht und, falls es nicht vorhanden
        ist, ein TypeError erhoben. Dieser gibt den eindeutigen Hinweis, welche
        Attribute in der neuen Klasse definiert sein müssen.
        """

        if '_lifetime' not in clsdct:
            raise AttributeError("Deine Klasse muss ein '_lifetime'-Attribut bereitstellen. (Default-Value: 0 (s) -> Instanz wird niemals gelöscht.)")
        return super().__new__(clsmeta, clsname, bases, clsdct)

#------------------------------------------------------------------------------#
    def __call__(cls, *args, **kwargs):
        """ Nach der Erzeugung einer Instanz wird der 'Lifetimer' jener Instanz gestartet.

        Die __call__ Method wird automatisch durch die Verwendung des Konstruktors 
        aufgerufen, noch bevor die __init__ der verwendeten Klasse aufgerufen wird. 
        Jene wird durch den super()-Aufruf von __call__ eingeleitet und die Rückgabe
        entspricht dem vollständigen Instanzobjekt. Bevor dieses Objekt aber zurück
        nach Außen gegeben wird, wird der 'Lifetimer' gestartet.
        """

        # Erzeugen der echten Instanze, welche am Ende von Außen verwendet wird.
        instance = super().__call__(*args, **kwargs)
        cls.__start_life(instance)
        return instance

#------------------------------------------------------------------------------#
    def __start_life(cls, instance):
        """ Methode um den 'Lifetimer' einer Instanz zu starten.
            
            Das Attribut '_lifetime' wird überprüft und für den Fall dass
            es >0 ist, wird der 'Lifetimer' einer Instanz gestartet. Die Metaklasse
            stellt sicher, dass die Klasse ein '_lifetime' Attribut hat, falls 
            der Autor kein Attirbut in der Instanz bereitstellt. 
        """
        if instance._lifetime > 0:
            print("Instanz erzeugt, Lebenszeit wird gestartet.")
            threading.Timer(instance._lifetime, cls.__end_life, [instance]).start()

#------------------------------------------------------------------------------#
    def __end_life(cls, instance):
        """ Methode um die Instanz nach Ablauf der Lebenszeit zu lösche
            
            Nach Ablauf der Lebenszeit wird im globalen-Dict der Datei nach der
            übergebenen Instanz gesucht. Wenn sie gefunden wird, wird das Key-Value
            Paar aus jenem Dict entfernt. Somit wird die Instanz gelöscht.
        
        TODO: Die Schleife, welche im Globalen-Dict nach der Instanz sucht 
        erzeugt zusätzliche 'Lebenszeit'. Mir ist an dieser Stelle noch kein
        bessere Weg Eingefallen, wie ich an den Key der Instanz komme, ohne 
        durch das Globale-Dict zu laufen und zu suchen.
        Am besten wäre es, wenn die Methode __end_life lediglich 
        > del globals()[instance_key]
        enthalten würde, da diese Methode exakt nach der Lebenszeit aufgerufen 
        wird.
        """

        for key, value in globals().items():
            if value == instance:
                del globals()[key]
                print(f"Die Lebenszeit von {instance} ist vorbei.")
                break


# --- Normale Klasse ---#
class MyClass(metaclass=LifetimeMeta):
    """ Normale Beispielklasse, welche die 'LifetimeMeta'-Klasse als Metaklasse verwendet."""

    # --- Klassen Attribute ---#
    _lifetime = 0 # 0 -> Instance wird nicht gelöscht

    # --- Methoden ---#
    def __init__(self, arg1, lifetime):
        self.arg1 = arg1
        self._lifetime = lifetime


# --- Programmschleife --- #
if __name__ == '__main__':
    lifetime = 3

    # Erzeugen der Instanz impliziert das starten der Lebenszeit.
    outside_instance = MyClass(5, lifetime=lifetime)

    # Zugriff auf die Instanz, während sie noch 'lebt'
    print(outside_instance.arg1)

    # Warten bis die Lebenszeit der Instanz überschritten ist
    time.sleep(lifetime + 1)

    # Zugriff auf die Instanz, nachdem sie gelöscht ist.
    print(outside_instance.arg1)

    # Instanz erzeugt, Lebenszeit wird gestartet.
    # 5
    # Die Lebenszeit von <__main__.MyClass object at 0x000001390DE42250> ist vorbei.
    # Traceback (most recent call last):
    #   File "f:/Python-Projects/Projects/Classes_Tutorial/Kapitel_6/_E2_LifetimeMeta.py", line 112, in <module>
    #     print(outside_instance.arg1)
    # NameError: name 'outside_instance' is not defined


