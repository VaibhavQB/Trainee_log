# Simple Class-Object demonstration

'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

P1 = Person("Vaibhav", "1700")
print(f"{P1.name} is {P1.age} years old.")'''


# Class Oject represnted as string

'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{P1.name} is {P1.age} years old.")

P1 = Person("Vaibhav", "1700")
print(P1)'''


# Object Method

'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'Hello there, my name is {self.name}')


P1 = Person("Vaibhav", "1700")
P1.greeting()'''


# Modig=fing and deleting Object property

'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{P1.name} is {P1.age} years old.")

P1 = Person("Vaibhav", "1700")

P1.age = 7000   # Changing an Objects property 
print(P1.age)
del P1.age      # Deleting an Objects propetry
#print(P1.age)  # Will return Error if not commented'''

