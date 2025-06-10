# Simple Code to demonstrate polymorphism

'''class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f"Name : {self.name}\nAge = {self.age}"

class Employee(Person) :      # We need to give the parent class as the parameter to the child class
    pass

E1 = Employee("Casey", "27")
print(E1)'''


# Over-ridding the __init__ method and adding method 'details()' to the child class

'''class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person) :      # We need to give the parent class as the parameter to the child class
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def details(self):
        return  f"Name : {self.name}\nPosition : {self.pos}"

        
E1 = Employee("Casey", "AI/ML Intern")
print(E1.details())'''


# Using super() function

'''class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person) :      # We need to give the parent class as the parameter to the child class
    def __init__(self, name, age, pos):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.pos = pos

    def details(self):
        return  f"Name : {self.name}\nAge : {self.age}\nPosition : {self.pos}"

        
E1 = Employee("Casey",27, "AI/ML Intern")
print(E1.details())'''