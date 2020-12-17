import logging

logging.basicConfig(level=logging.INFO)

# Wenn man mit getattr und setattr arbeiten muss/möchte,
# dann benötigt man ein anderen Bezeichner für das Attribut innerhalb
# der Instanz als die Definition in der Klasse. Dieser andere
# Bezeichner wird aber nur Intern verwendet. Der Zugriff selbst
# bleibt bei dem Bezeichner, welchen man auf der Klassenebene definier hat.
# (Durch getattr und dem gleichen Bezeichner würde man wieder in 
# einer Endlosschleife landen.)
class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info(f'Accessing {self.public_name!r}. Retrun: {value!r}.')
        return value

    def __set__(self, obj, value):
        logging.info(f'Updating {self.public_name!r} to {value!r}')
        setattr(obj, self.private_name, value)

class Person:
    name = LoggedAccess()
    age = LoggedAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

p1 = Person('Gera', 32)
# INFO:root:Updating 'name' to 'Gera'
# INFO:root:Updating 'age' to 32

p1.birthday()
# INFO:root:Accessing 'age'. Retrun: 32.
# INFO:root:Updating 'age' to 33