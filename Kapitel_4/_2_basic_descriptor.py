class Descriptor:
    def __set_name__(self, owner_cls, name):
        self.name = name

    def __get__(self, instance, owner_cls=None):
        print(f"Get {self.name!r}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Set {self.name!r} to {value!r}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Delete {self.name!r}")
        del instance.__dict__[self.name]

class MyClass:
    attr = Descriptor()

    def __init__(self, attr):
        self.attr = attr

instanz = MyClass('value_1')
instanz.attr
del instanz.attr
# Set 'attr' to 'value_1' -> Hervorgerufen durch 'self.attr = attr' in der init
# Get 'attr'
# Delete 'attr'