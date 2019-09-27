# Python variables often used to output variables
# To combine both text and variables python uses the + charcter
x = 'awesome'
print('Python is '+ x)
# You can also use the + character to add a variable to another
x = 'Python is '
y = 'awesome'
print(x + y)

#For numbers + characters works as mathematical operator
x = 5 
y = 10 
print(x+y)


# Global variables
# Variables that are created outside the function is known as global variables
# Global variables can be used by every one, both inside of the function and outside of the function
# create a variable out of the function and use it inside of the function
x = 'awesome'

def myfunc():
    print('Python is ' + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local
# and can only be used inside the function.The global variable with the same name will
# remain as it was global and with the original value

# create a variable inside function with the same name as global variable
x = 'awesome'

def myfunc():
    x = 'fantastic'
    print('python is ' + x)

myfunc()
print('Python is ' + x)

# Normally, when you create a variable inside a function, that variable is local , and can only be
# used inside that function
# To create a global variable inside a function use global keyword

# Example if you use global keyword, the variable belongs to the global scope

def myfunc():
    global x
    x = 'fantastic'

myfunc()
print('python is ' + x)

# Also user global keyword if you want to change a global variable inside a function
x = 'pretty'
def myfunc():
    global x 
    x = 'fantastic'
myfunc()    # changed the global keyword
print('python is ' + x)