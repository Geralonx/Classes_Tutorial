class Discriptor:
    # owner_cls ist das Klassenobejkt, indem der Descriptor verwendet wird
    def __set_name__(self, owner_cls, name):
        pass

    def __get__(self, instance, owner_cls=None):
        pass

    def __set__(self, instace, value):
        pass

    def __delete__(self, instance):
        pass