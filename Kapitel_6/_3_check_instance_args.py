""" Diese Metaklasse solle überprüfen, ob die Argumente, welche bei der 
Instanziierung einer Instanz verwedet werden, ALLE kleingeschrieben sind.
"""

import inspect

# --- Metaklasse mit den 'Regeln' für die Klassenerstellung --- #
class CheckInstanceArgs(type):

    def __new__(metacls, clsname, bases, clsdct, **kwargs):
        """ New Method durchsucht das Klassen-Dict nach der __init__ Methode und
        überprüft die gesetzten Argumente nach der Schreibweise. Wenn sie nicht
        klein geschrieben sind, dann wird en NameError erhoben.
        """
        if '__init__' in clsdct:
            init_code = inspect.getsource(clsdct['__init__'])
            init_code = metacls.check_init_code(init_code)
        return super().__new__(metacls, clsname, bases, clsdct)

    @staticmethod
    def check_init_code(init_source):
        """ Diese Methode durchsucht den übergebenen source_code nach 'self.' und
        überprüft, ob das Argument / Methode kleingeschrieben ist.

        Wenn dem nicht der Fall ist wird ein TypeError erhoben.
        """

        # Zerlegung des Init-Codes in die einzelnen Zeilen
        lines = init_source.strip().split("\n")
        search_pat = 'self.'

        for line in lines:
            if search_pat not in line:
                continue
            # Stringaufteilung in das Argument nach dem 'self.' Teil.
            temp_line = line.strip()
            temp_line = temp_line.split('=')[0].strip()
            argument = temp_line.split(search_pat)[1]

            # Wenn sich das Argument nach der Wandulung in lowercase von sich 
            # selbst unterscheidet, dann enthält es uppercases.
            if argument.lower() != argument:
                raise NameError("Deine Instanzattribute dürfen ausschließlich aus [a-z][0-9][_] bestehen.")


# --- Normale Klassen --- #
class MyClass(metaclass=CheckInstanceArgs):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.Arg2 = arg2
        self.arG3_ = arg3

    def arg1_add_arg2(self):
        print(self.arg1 + self.Arg2)


