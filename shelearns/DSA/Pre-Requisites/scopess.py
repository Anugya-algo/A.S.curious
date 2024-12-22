# Local scope: Variables declared inside a function. They can only be accessed within that function.
# Enclosing scope: Variables declared in any enclosing function, i.e., within a function that is nested inside another function.
# Global scope: Variables declared outside of any function. They are accessible anywhere in the program.
# Built-in scope: Variables that are part of the Python standard library and are always accessible.

x=10

def local():
    x=34 #local scope
    print("local inside function : ",x)

def globally():
    print("the x printed here is under global scope ",x)

local()
globally()
 
 #use "global 'variable '" within function to modify global 
def modify_global():
    global x
    x=78

modify_global()
print("this is globally defined value and modified",x)

#variable in enclosing :nested functions ..ek function ka variale dusre func me modify krna

def h():
    x=90

    def inner():
        nonlocal x
        x=66

    inner()
    print(x)
h()