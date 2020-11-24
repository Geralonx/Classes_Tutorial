#!F:\Python-Projects\Projects\Classes_Tutorial\env\Scripts\python.exe

# --- Standard Libary Imports --- #
 # import numpy as np
 # import os
 # ...

import abc
class Driveable(abc.ABC):
    @abc.abstractmethod
    def drive(self):
        pass

class Car(Driveable):
    def drive(self):
        print("Look, you've got a drive-Method")




def main():
    car1 = Car()
    car1.drive()

if __name__ == '__main__':
    main()