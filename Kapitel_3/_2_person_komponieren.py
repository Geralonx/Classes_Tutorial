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


# --- Deklaration einer neuen Klasse, welche aus 2 Elternklassen komponiert wird --- #
# Die Reihenfolge der Elternklasse spielt eine wesentliche Rolle.
class StudentWorker_V1(Employee, Student):
    pass

class StudentWorker_V2(Student, Employee):
    pass

# --- Ausgabe des jeweiligen __mro__ Zusammenhangs
print("StudentWorker_V1 -> __mro__")
print(StudentWorker_V1.__mro__)
# StudentWorker_V1 -> __mro__
# (<class '__main__.StudentWorker_V1'>, <class '__main__.Employee'>, <class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
print("") # Leere Zeile für den Abstand

print("StudentWorker_V2 -> __mro__")
print(StudentWorker_V2.__mro__)
# StudentWorker_V2 -> __mro__
# (<class '__main__.StudentWorker_V2'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class '__main__.Person'>, <class 'object'>)

# --- Instanziierung der StudentWorker_V1 --- #
studentworker1 = StudentWorker_V1(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)

# # --- Instanziierung der StudentWorker_V2 --- #
# # Durch die vertauschte Reihenfolge in der __mro__ gibt es einen TypeError, 
# # da ein unbekanntes KeyWord an die __init__ der Student Klasse übergeben wurde.
# studentworker1 = StudentWorker_V2(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
# # Traceback (most recent call last):
# #   File "f:/Python-Projects/Projects/Classes_Tutorial/Kapitel_3/_2_person_componieren.py", line 46, in <module>
# #     studentworker1 = StudentWorker_V2(fname='Max', lname='Mustermann', mat_nr='10142020', salary=450.00)
# # TypeError: __init__() got an unexpected keyword argument 'salary'
