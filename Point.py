#Using the inheritanc 
class Person:
    #using the init methord to initialize the object 
    #created a construtor the Person object
    def __init__(self, name):
        #self is the reference to the current object 
        self.name = name
    def info(self):
        print(f"Hi, I am {self.name}")
    

class Student(Person): 
    def major(self):
        print("English") 


class Employee(Person):
    def jobTitle(self):
        print("Mathematics")


john = Student("John Smith")
john.info()
john.major()
bob = Person("Bob Smith")
bob.info()