class Car:
    wheels = 4                               #Class(Static) Variable, If changed affects all objects

    def __init__(self):
        self.mil = 10                        #Instance Variable, If changed only affects the object it is changed for
        self.com = 'BMW'                     #Instance Variable, If changed only affects the object it is changed for


c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheels = 5
print(c1.mil, c1.com, Car.wheels)
print(c2.mil, c2.com, Car.wheels)