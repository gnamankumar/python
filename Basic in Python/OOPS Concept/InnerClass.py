

class Student: # Outer Class

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()


    class Laptop: # Inner Class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 4

        def show(self):
            print(self.brand , self.cpu ,self.ram)



s1 = Student('Naman',2)
s2 = Student('Rahul',5)


s1.show()

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))
