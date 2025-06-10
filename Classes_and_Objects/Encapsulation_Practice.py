# By default every attribute and method is public in python

'''class Demo:

    def __init__(self, name):
        self.name = name # Public Attribute

d1 = Demo("ABC")
print(f'The name is {d1.name}')  # Accessed it outside of the class
'''

# Use of Protected attributes/Member

'''class ProtectedDemo:

    def __init__(self):
        self._age = 170         # Using '_' makes the attribute Protected

class ProtectedChild(ProtectedDemo):
    pass

d2 = ProtectedChild()
d2._age = 190                 # Using child class to change the protected attribute
print(f'age = {d2._age}')'''


# Use of Private Attributes/Members


class PrivateDemo:
    def __init__(self):
        self.__age = 17       # Using '__' makes the attribute Private

class PrivateChild(PrivateDemo):
    pass

d3 = PrivateDemo()       
#print(d3.__age)         # Will give error and same error eill be given if we make an object of PrivateChhild()