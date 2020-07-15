


class Car:

    wheels = 4  #Class Variable

    
    def __init__(self):
        self.mil = 10       #Insrance Variable
        self.com = "BMW"    #Insrance Variable


c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.com , c1.mil, c1.wheels)
print(c2.com , c2.mil, c2.wheels)
