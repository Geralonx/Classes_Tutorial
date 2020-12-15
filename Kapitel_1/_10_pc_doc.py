# --- Deklarartion einer Klasse mit Konstruktor und Doc-String --- #
class PC:
    '''\nDies ist die Dokumentation der Klasse: PC

    Multiline-Strings sind automatisch mit berücksichtig.
    Es wird sogar mit formatiert. Klasse! Oder?'''

    def __init__(self, cpu, gpu):
        '''Jetzt Dokumentieren wir die __init__ 
        Was eine schöne Funktion.'''
        self.cpu = cpu
        self.gpu = gpu


# --- Deklaration einer normalen Funktion mit Doc-String --- #
def outer_func(arg1):
    '''Das funktioniert auch bei einfachen Funktionen!
    Parameters:
        arg1: any

    Rückgabe: 1'''
    print(arg1)
    return 1


print(PC.__doc__, "\n")
print(PC.__init__.__doc__, "\n")
print(outer_func.__doc__, "\n")