# --- Definition einer normale Funktion --- # 
def func(x):
    return x+1

print(type(func))
# <class 'function'>


# --- Definition einer Funktion mittels Klasse --- #
class func_class:
    def __call__(self, x):
        return x+1

instanz = func_class()

print(instanz(1))