# --- Deklaration der Elternklasse Person --- #
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# --- Deklaration der Kindklasse Student --- #
class Student(Person):
    def __init__(self, mat_nr, fname, lname): # Ansatz 1
        self.mat_nr = mat_nr
        super().__init__(fname, lname)

# --- Deklaration der Kindklasse Employee --- #
class Employee(Person):
    def __init__(self, salary, **kwargs): # Ansatz 2
        self.salary = salary
        super().__init__(**kwargs)
        
# --- Instanziierung mit allen Argumenten als Keywordargumente. --- #
# Diese werden durch die angepassten __init__ Methoden weiter verteilt
student = Student(fname='Max', lname='Mustermann', mat_nr='10142020')
employee = Employee(fname='Maria', lname='Musterfrau', salary=40_000)