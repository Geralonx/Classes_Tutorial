# --- Deklaration einer Klasse mit einer Staticmethod --- #
class PC:
    @staticmethod
    def add_2_to_3():
        return 3+2

# --- Aufruf der Staticmethod, keine Argumente erforderlich ---#
print(PC.add_2_to_3())