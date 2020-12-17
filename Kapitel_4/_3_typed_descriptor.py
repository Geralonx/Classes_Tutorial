class Discriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, cls=None):
        print(f"Get {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Set {self.name} to {value!r}")
        instance.__dict__[self.name] = value

        print(f"Delete {self.name}")
        del instance.__dict__[self.name]

class Typed(Discriptor):
    dtype = None

    def __set__(self, instance, value):
        if type(value) != self.__class__.dtype:
            raise TypeError(f"{self.name!r} Attribut needs to be from Type: {self.__class__.dtype!r}.")
        super().__set__(instance, value)

class String(Typed):
    dtype = str

class Integer(Typed):
    dtype = int

class Float(Typed):
    dtype : float

class Positiv(Discriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name!r} Attribut needs to be >= 0.")
        super().__set__(instance, value)

class PositivInteger(Integer, Positiv):
    pass

#------------------------------------------------------------------------------#

class PC:
    cpu = String()
    gpu = String()
    clock_speed = PositivInteger()


    def __init__(self, cpu, gpu, clock_speed):
        self.cpu = cpu
        self.gpu = gpu
        self.clock_speed = clock_speed

pc_instanz = PC('Ryzen 7', 'RTX2070', 4500)

print(pc_instanz.gpu)
