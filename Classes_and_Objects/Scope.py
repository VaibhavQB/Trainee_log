# Demonstartion of scope

'''x = 700

def checkx():
    x = 300
    return x

print(f'X in local scope of the defined function {checkx()}')
print(f"X in global scope : {x}")'''


# Use of global keyword

'''x = 300

def changeGlobal():
    global x
    x = 700

print(f"X Before calling the function: {x}")
changeGlobal()
print(f"X After calling the function : {x}")'''


# Use of nonlocal keyword

def myf1(inp = None):
    x = "Hello"
    def myf2():
        nonlocal x
        x = "World"
    
    if inp != None :
        myf2()
        return x
    
    return x

print(f'X without using nonlocal : {myf1()}')
print(f'X with using nonlocal : {myf1(0)}')