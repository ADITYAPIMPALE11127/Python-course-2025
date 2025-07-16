'''
Rules 
1. Name assignment will create or change local names by default.
2. Name references search four scopes at most: Local, Enclosing, Global, Built-in (LEGB).

Scopes:
1. Local: Names assigned in any way within a function (and not declared global).
2. Enclosing: Names in the local scope of any and all enclosing functions.
3. Global (Module): Names assigned at the top level of a module file, or declared global inside a def.
4. Built-in: Names pre-assigned in the built-in names module (e.g., range, enumerate, len).
'''

# Local example
def local():
    y = 20  # local scope 
    return y

print("Local scope example:", local())

# Enclosing example
def Outer():
    a = 23  # enclosing scope
    def inner():
        print("Enclosing scope example:", a)
    inner()

Outer()

# Global example
x = 50  # global scope

def use_global():
    print("Global scope example:", x)

use_global()

# modifying global variable
def modify_global():
    global x
    x = 100  # modifying the global variable
    print("Modified global variable:", x)

modify_global()
use_global()  # check the new value of x

# Built-in example
def built_in_example():
    my_list = [1, 2, 3]
    print("Built-in scope example (using len):", len(my_list))  # len is a built-in function

built_in_example()
