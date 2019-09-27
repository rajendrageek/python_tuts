message = 'Hello World'
print(message)
print(len(message))

print(message[6:])
print(message[:5])

# count the number of characters in a string
print(message.count('Hello'))
print(message.count('l'))

# find method used to get the starting character in a string
print(message.find('Hello'))
print(message.find('l'))
print(message.find('universe')) # it con't find that so it returns -1 

# Replcing a word in a sentence
new_message = message.replace('world0', 'Universe')
print(new_message)

# String concating
message = 'hello' + ', ' + 'Michael' + '. welcome'
print(message) # this is little bit complicated but for now 
# It is okay but if it is a large then you feel it like complicated track all the variables and 
# symbols

greeting = 'Hello'
name = 'Michael'
message = '{}, {}. welcome'.format(greeting, name)
print(message)

# if you are using python 3.6 or above versions you can use f string

#message = f'{greeting}, {name}. Welcome'
print(message)

# string formatting
person = {'name': 'Rajendra', 'age': 26}
message = 'My name is {} and i am {} years old.'.format(person['name'], person['age'])
print(message)

message = 'iam {1} years old and my name is  {0}'.format(person['name'], person['age'])
print(message)

message = 'My name is {0[name]} and iam {0[age]} years old'.format(person, person)
print(message)
print('rajendra is a good boy')

# Unlike other programing languages python has no command for declaring variables 
# The variable is created the moment you first assign a value to it 
# example 
# variable do not need to be declared with any perticular type and can even change type after they have been set
x = 4 
x = 'new string'

# a variable can have a short name or a descriptive name for python
# rules for python variables 
# A variable name must start with a letter or a underscore character
# A variable cannot start with a number 
# A variable only contains only alphanumeric characters and underscores
# Python allows you to assign values to multiple variables in one line
a , b, c = 'raj', 'anji', 'srinu'
# and you can assign a value for multiple variables
d = e = f = 'Orange'
print(a)
print(b)
print(c)
print(d)
print(e)

for x in range(1, 11):
    print('{:2d} {:3d} {:4d}'.format(x, x*x, x*x*x))

    





# string literals
# String literals in python surrounded by a single quotation marks or double quotation marks
# 'hello' same as "hello"
# you can display a string literal with the print function
print('Hello')
print('hell0')


# Assign a string to a variable is done with variable name followed by an equal sign and the string
a = 'hello'
print(a)

# Multiline string
a = '''rajendra is a good boy,
he is so ambicious and wise
'''

print(a)

# note: in the result, the line breaks are inserted at the same position as in the code
# STRINGS ARE ARRAYs
# Like many other programing languages, strings in Python are arrays of bytes representing unicode
# characters However python does not have a character datatype, a single character is simply a string with a length of 1
# Square brackets can be used to access elements of the string.

# Get the character at position 1
a = 'hello, world!'
print(a[1])

# Slicing
# you can return a range of characters by using the slice syntax
# specifying the start index and end index, separeated by a colon, to return a part of the string

# Get the characters from position 2 to position 5(not included)
b = 'hello, world!'
print(a[2:5])

# negative indexing
# Use the negative index to start slice from the end of the string
# Get the characters from 5 to position 1, starting from end of the string:
b = 'hello, world!'
print(b[-5:-2])

# string length
# To get the length of the string, use the len() function
# The len function returns the length of the string
a = 'hello,, world!'
print(len(a))


# String methods
# Python has a set of built in methods that you can use on strings
# The strip method removes any white space froom begining or the end
a = ' hello, world! '
print(a.strip())
 
# The lower method returns the string in lower case
a = 'Hello, World!'
print(a.lower())

# The upper method returns the string in the upper case
a = 'hello, world!'
print(a.upper())

# replace method replaces a string with another string
a = 'Hello, World'
print(a.replace('H', 'J'))

# Split method splits the string into substrings if it finds instance of separator
a = 'Hello, World!'
print(a.split(','))

# converts the string into lower case
a = 'HELLO WORLD'
#y = a.casefold()
#print(y)

# capitalize() method
# converts the first character to uppercase
a = 'hello, world!'
x = a.capitalize()
print(x)

# encode()
name = 'My name is rajendra'
print(name.encode(encoding='ascii', errors='backslashreplace'))
print(name.encode(encoding='ascii', errors='ignore'))
print(name.encode(encoding='ascii', errors='namereplace'))
print(name.encode(encoding='ascii', errors='strict'))
print(name.encode(encoding='ascii', errors='replace'))
print(name.encode(encoding='ascii', errors='xmlcharrefreplace'))

# center()
# center method will center the string using a specified character(optional)
name = 'rajendra'
modified_name = name.center(10, '*')
print(modified_name)

# endswith()
# returns true if the string endswith specified value
name = 'rajendra'
print(name.endswith('r'))

# expandtabs()
# Sets the tabsize of the string

name = 'rajendra'
txt ='H\te\tl\tl\to'
print(txt.expandtabs())
print(txt)
print(txt.expandtabs(2))
print(txt.expandtabs(4))

#join() 
# join memthod takes all the items in an iterable and joins them into one string
mytuple = ['john', 'peter', 'vicky']
x = '#'.join(mytuple)
print(x)

mydict = {'name': 'john', 'country': 'norway'}
separator = '$'
x = separator.join(mydict)
print(x)

# maketrans()
# maketrans method returns traslation talbe to be used in translations
# find()
# find method returns the first ocuurence of the specified where it was found

x = 'hello, welcome to my world'
y = x.find('welcome')
v = x.find('helo')
print(y)
print(v)

z = 'hello world'
w = z.index('hello')
print(w)

# The partition method searches for specified string, and splits the string into a tuple containing three elements
# the first part before the specified string
# the second element contains specified strig
# the third element contains the part after the specified part

txt = 'i could eat bananas all the day'
x = txt.partition('bananas')
print(x)

# splitlines()
# splitlines method splits a split into a list. The splitting is done at line breaks
txt = 'thank you for the music\n Welcome to the jungle'
x= txt.splitlines(True)
print(x)

txt ='thank you for the music\n Welcome to the jungle'
y = txt.splitlines()
print(y)

# Swapcase()
# swaps cases, lower case becomes upper case and vice versa
a = "Hello"
print(a.swapcase())


# zfill
txt = '50'
x = txt.zfill(10)
print(x)


# Check string
# To Check if a certain phrase or character present in string, we can use the keywords in or not in 

# Check if the phrase 'ain' is present in the following text
txt = 'The rain in the spain stays in the plain'
x = 'ain' in txt
print(x)

# Check the phrase 'ain' is not present in the following text
text = 'The rain in the spain stays in the plain'
x = 'ain' not in text
print(x)

# String concatenation
# To concatenate or to combine to strings you can use + operator
a = 'Hello'
b = 'World'
c = a + b
print(c)

# To add space between them, use ' ' 
a = 'hello'
b = 'world'
c = a +' ' + b
print(c)

# String format
# As we learned in the python variables chapter, we cannot combine like this

age = 36
# txt = 'My name is John, I am ' + age

print(txt)

# But we can combine string and numbers using format() method
# The format method takes the arguments, formats them, and places them in the string
# where the placeholders { }:

age = 26
txt = 'My name is Rajendra, I am {}'
print(txt.format(age))

# The format method takes unlimited arguments, and are placed into respective placeholders
quatity = 3
itemno = 576
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(quatity, itemno, price))

# we can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {2} dollars for {0} pieces of item {1}.'
print(myorder.format(quantity, itemno, price))

# Python operators
# operators are used to perform operations on variables and values
# python devides the operators in the following groups

# Arithematic operators
# Assignment operators
# Comparision operators
# Logical operators
# Identity opearators
# Membership operators
# Bitwise operators

# Python lists
# Python collections(Arrays)
# there are four collection data types in the python programing language
# LIST is a collection which is ordered and changeable. Allows duplicate members.
# TUPLE is a collection which is ordered and unchangeable. Allows duplicate members
# SET is a collection which is unordered and unindexed. No duplicate members
# DICTIONARY is a collection which is unordered, changeable and indexed. no duplicate members

# when choosing collection type it is useful to understand the properties of that type.
# choosing the right type for a perticular data set could mean retension of meaning 
# and it could mean increase the efficiency and security



































# PIP 
# What is PIP 
# PIP is a package manager for python packages , or modules if you like
# If you have python 3.4 later pip is included by default
# # What is package
# A package contains all the files you need for a module
# modules are code libraries you can include in your project
# check if pip is installed 
# Once package is installed you can use that package in your project




# new comment