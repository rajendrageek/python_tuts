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

# Numbers
# There are three  numeric types in Python:
# Int
# Float
# complex
# Variables of numeric types are created when you assign a value to them
x = 1 # Int
y = 2.8 # Float
z = 3j  # Complex

# To verify the type of an object use type function
print(type(x))
print(type(y))
print(type(z)) 

# Float can also be scientific numbers with an "e" to indicate the  of 10
x = 35e5

# Type conversion
# you can convert one type to another with the int(), float(), complex methods

x = 1 
y = 2.8
z = 1j

# convert from int to float
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

# Note you can not convert complex numbers to another number type


# Random number 
# Python doesn't have a random() function to make a random number, but python has built in module 
# called random that can be used to make random numbers
# Example
# import random module and print a number between 1 to 9 
import random

x = random.randrange(1, 10)
print(x)



# Casting

# There may be times when you want to specify a type on to a variable
# This can be done with casting. Python is an object oriented language, and as such it uses classes to define
# to define datatypes including its primitive types

# Casting in python is therefore done using constructor function
# int constructs an integer number from integer literal, a float literal or a string literal
# flaot() constructs a float number from an integer literal, a float literal or a string literal
# str constructs a string  from a wide variety of data types, including strings, integer literals and flaot literals

# int
x = int(1)
y = int(2.8)
z = int('3')
print(x, y, z)

# flaot
x = float(1)
y = float(2.8)
z = float('2.8')
w = float('4')

print(x, y, z, w)

# string
x = str('s1')
y = str(2)
z = str(3.0)
w = str('5.8')

print(x, y, z, w)


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

# List is a collection which is ordered and changeable. In python lists are written with square brackets
# Create list 
thislist = ['apple', 'banana', 'cherry']
print(thislist)

# Access items by referring the index number
# print the second item of the list
thislist = ['apple', 'banana', 'cherry']
print(thislist[1]) 

# Negative indexing
# negative indexing means begining from the end, -1 refers to the last item, -2 refers to the second last item etc.
# print last item from the list
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1])

# Range of indexes 
# you can specify range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be newlist with the specified items 

# Return the third fourth and fifth item 
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:5])

# Note the search will start at index 2(included) and end at index 5 (not included)
# Remember the first item has index 0

# Range of negative indexes
# specify negative indexes if you want to start the search from the end of the list
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])

# Change the item value
# To change the value of specified item, refer to the index number
# change the second item 
thislist = ['apple', 'banana', 'cherry']
thislist[1] = 'blackcurrant'
print(thislist)

# Loop thorough a list
# you can loop thorough the list items by using for loop
# print all items in list one by one
thislist = ['apple', 'banana', 'cherry']

for x in thislist:
    print(x)

# Check if item exists 
# To determine if a specified item is present in a list use in keyword

# Check if apple present in the list
thislist = ['apple', 'banana', 'cherry']

if 'apple' in thislist:
    print('yes, apple in the fruits list')

# List length 
# To determine how many items a list has, use the len method
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

# Add items 
# To add an item to the end of the list, use append method
# Using append method to append an item

thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)


# To add an item to the specified index, use the insert method
# Insert an item as the second item

thislist = ['apple', 'banana', 'cherry']
thislist.insert(1, 'orange')
print(thislist)

# remove item 
# There are several methods to remove items from a list
# the remove method removes specified item
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# The pop() method removes specified index, (or the last item if the index is not specified)
thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

# the del keyword removes the specified index

thislist = ['apple', 'banana', 'cherry']
del thislist[1]
print(thislist)


# The del keyword also removes list completely
del thislist

# Clear() method empties the list

thislist = ['apple', 'banana', 'cherry']

# thislist.clear()

print(thislist)


# Copy a list
# you can not copy the list by simply typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2
# there are ways to make a copy, one is to use the built in list method copy()

# Make a copy of the list with the copy method

thislist = ['apple', 'banana', 'cherry']
# mylist = thislist.copy()
# print(mylist) 

# Another way to make a copy is to use the built in method list()
# Use the extend() method, which purpose is to add elements from one list to another list
# Make a copy of the list with list() method

thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)

# Join Two lists 
# there are several ways to join, or concatenate, two or more lists in python 
# one of the easiest ways are by using the + operator

# Join Two list
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one
# Append list2 into list1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

# Or you can use the extend() method, which purpose is to add elements from onelist to another list
# Use the extend() method to add list2 at the end of list1:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# the list() constructor
# It is also possible to use the list() constructor to make a newlist
# Using the list constructor to make a list

thislist = list(('apple', 'banana', 'cherry'))
print(thislist)


# Python List count() method 
# Return the number of times the value occured in list 
fruits = ['apple', 'banana', 'cherry']
x = fruits.count('apple')
print(x)


#Index() method
# Returns the position at the first occurence of the specified value
numbers = [1, 2, 4, 25, 45, 4, 6, 7, 4]
x = numbers.index(4)
print(x) 


# Reverse()
# reverse the order of fruit list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


# sort()
numbers = [1, 7, 9, 4, 5, 6]
numbers.sort()
print(numbers)

# A tuple is a collection which is ordered and unchangeable. In python tuples are written with round brackets
# Create tuple
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

# Access tuple items 
# you can access tuple items by referrring to the index number, inside square brackets
# print the second item in the tuple

thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1])


# negative indexing 
# negative indexing means starting from the end -1, refers to the last item, -2 refers to the second last
# item 
# print the last item of the tuple
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[-1])

# Range of indexes 
# you can specify range of indexes by specifying where to start and where to end range.
# when specifying   a range the return value will be a tuple with the specified items
# Return the third, fourth, fifth items
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[3:6])

# range of negative indexes 
# Specify negative indexes if you want to start the search from end of the tuple
# the below example returns the items from -4 to index -1(excluded)
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1])

# Change tuple values 

# Once the tuple is created, you can not change its values. Tuples are unchangeable, or
# immutable as it also is called

# But there is work around. you can conevert the tuple into list, and convert the list back into a tuple
# convert the tuple into list to be able to change the  values
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)


print(x)

# Loop through a tuple items by using a for loop
# Iterate through the items and print the values 

thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
    print(x)

# check if item exists
# To determine if a specified item is present in A tuple use in keyword
# check if 'apple' is present in the tuple
thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
     print(' Yes, apple is in the fruits tuple')

# To determine how many items a tuple has, use the len() method
# print the number of items in a tuple
thistuple = ('apple', 'banana', 'cherry')
print(len(thistuple))

# Add items 
# Once a tuple is created, you can not add items to it. tuples are unchangeable
# You can not add items to a tuple

'''thistuple = ('apple', 'banana', 'cherry')
thistuple[1] = 'orange' # it will raise the error
print(thistuple)'''

# Create a tuple with one item 
# To create a tuple with one item you have to add a comma after the item, unless python 
# won't recognize the variable as a tuple

# one item tuple remember the comma 
thistuple = ('apple',)
print(type(thistuple))

thistuple = ('apple') # not a tuple
print(type(thistuple))

# Remove items 
# tuples are unchangeable so you can not remove the items from it, but you can delete completely
# The del keyword can delete the tuple completely
thistuple = ('apple', 'banana', 'cherry')
del thistuple
# print(thistuple) # name thistuple is not defined

# join two tuples 
# to join two tuples you can use + operator
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple constrctor
# It is also possible to use tuple() constructor to make a tuple
# using the tuple() method to make the tuple
thistuple = tuple(('apple', 'banana', 'cherry')) # note the double rounded brackets
print(thistuple)

# count()  method
# Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 4, 2, 5, 3, 6, 5)
x = thistuple.count(5)
print(x)

# index() method will return only first occurance of specified value

thistuple = ('apple', 'banana', 'cherry')
x = thistuple.index('apple')
print(x)


# Python sets
# A set is a collection which is unordered and unindexed. In python sets are written in curly braces
# create a set
thisset = {1, 2, 3, 4, 5}
print(thisset)
# Sets are unordered, so you can not be sure in which order items will appear

# Access items 
# you can not access items in a set by an index, since sets are unordered
# the items have no index
# but you can loop through set items using for loop, or ask if a specified value present in a set \
# by using the in keyword

# Loop through the set items and print values
thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

# check if banana present in set
thisset = {'apple', 'banana', 'cherry'}
print('banana' in thisset)

# Once set is created you can not change items, but you can add new items
# Add items
# To add one item to set use add() method 
# To add  more than one item to a set use update() method

# Add an item to a set, using add method
thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)

# Add multiple items to a set
thisset = {'apple', 'banana', 'cherry'}
thisset.update(['orange', 'kiwi', 'mango'])
print(thisset)

# Get the lenght of the set
thisset = {'apple', 'banana', 'cherrry'}
print(len(thisset))

# Remove an item
thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana') # If the item not found remove method raise exception
print(thisset)

# remove banana by usig discard method
thisset = {'apple', 'banana', 'cherry'}
thisset.discard('banana') # if the item to remove does not exist discard method will not raise error
print(thisset)

# You can also use pop method to remove item but this method will remove last item
thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop()
print(x)
# sets are unordered, so when using pop() method, you will not know which item that gets removed
# the return value of pop method() is the removed item

# clear method() empties the set
thisset = {'apple', 'banana', 'cherry'}
thisset.clear()
print(thisset)

# del keyword delete the set completely
thisset = {'apple', 'banana', 'cherry'}
del thisset
# print(thisset) # raise an error as name thisset can not defined

# Join two sets there are several ways to join two or more sets 
# you can use the union method that returns a new set containing all items from both sets,
# or the update() method that inserts all items from both sets 

set1 = {1, 2, 3, 4}
set2 = {'a', 'b', 'c', 1}

set3 = set1.union(set2)
print(set3)

set4 = set1.update(set2)
print(set4)

# Both union and update methods will exclude any duplicate items
# There are other methods to that joins two sets and keeps only the duplicates, or never the duplicates

# set() contructor
# It is also possible to use set constructor to make a set

thisset = set(('apple', 'banana', 'cherry'))

# Copy()
fruits = {'apple', 'banana', 'cherry'}
x = fruits.copy()
print(x)

# The difference method returns a set that contains the difference between two sets
# the returned set contains items that exist only in the first set and not in the both sets
x = {'apple', 'banana', 'cherry'}
y = {'gogle', 'microsoft', 'apple'}
z = y.difference(x)
print(z)


# differnce update
# The difference_update method removes the items that exist in both sets
# The difference_update method is different from difference() method because difference method returns new 
# set, without the unwanted items, and the difference update method removes the unwanted items from the original set

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.difference_update(y)
print(x)


# Intersection()
# Returns a set that contains the similarity between two or more sets
# Meaining: the returned set contains only items that exists in both sets, or in all sets
# if the comparision done with more than two sets

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.intersection(y)
print(z)

# compare three sets, and return a set with items that is present in all 3 sets
x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}

result = x.intersection(y, z)
print(result)

# the intersection_update() method removes the items that is not present in both sets 
# the intersection_update() method is different from the intersection method, because the intersection method
# returns a new set, without the unwanted items, and the intersection_update() method removes the 
# unwanted items from original set
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

x.intersection_update(y)
print(x)

# isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns false
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.isdisjoint(y)
print(z)

# issubset() method returns the True if all items in the set exists in the specified set, otherwise it returns false
x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z = x.issubset(y)
print(z)

# issuperset method returns True if all items present in the specified set that exist in original set 
# Otherwise it returns false
x = {'f', 'e', 'd', 'c', 'b', 'a'}
y = {'a', 'b', 'c'}

z = x.issuperset(y)
print(z)

# the symmetric_difference method 
# symmetric_differece method returns a set that contains all items from both sets, but not the items
# that are present in the both sets  
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)

# the symmetric_difference_update()
# this method return updated set by removing items that are present in both sets, and inserting the other items

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y)
print(x)


# A dictionary is a collection which is unordered, changeable and indexed, in python dictionaries written in curly brackets
# and they have keys and values
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1946
}

print(thisdict)

# you can access the items of a dictionary by referring to its key name, inside square brackets
# Get the value of model key

x = thisdict['model']
print(x)

# there is also method called get that will give you the same result
# Get the value of model key
x = thisdict.get('model')
print(x)

# you can change the value of a specific item by refrring to its key name
# change the year
thisdict['year'] = 2019
print(thisdict)

# you can loop through a dictionary using a for loop
# when looping through a dictionary the return values are keys of the dictionary
# but there are methods to return values of the keys

for x in thisdict:
    print(x) # return all keys 

# print all values in the dictionary one by one
for x in thisdict:
    print(thisdict[x])

# you can also use values function to return values
for x in thisdict.values():
    print(x)

# loop through both keys and  values by using items function
for x, y in thisdict.items():
    print(x, y)
# check if key exists
# To determine if a specified key present in a dictionary use the in keyword

# check if the model present in the dictionary or not 
thisdict = {
    'brand': 'ford',
    'model': 'year',
    'year': 1946
}

if 'model' in thisdict:
    print('yes, model is the one of the keys in thisdict dictionary')

# Dictionary length
# To determine how many items a dictionary has, use the len() method
# print the number of items in a dictionary
print(len(thisdict))

# Adding items to the dictionary is done by using a new key index by assigning a value to it
thisdict = {
    'brand': 'ford', 
    'model': 'mustang',
    'year': 1946
}

thisdict['color'] = 'red'

# Removing items from a dictionary
# there are several methods to remove items from a dictionary 
# the pop() method will remove the item with the specified key name
thisdict = {
    'brand': 'ford',
    'model': 'Mustang',
    'year': 1946
}

# The pop method removes the item with the specified key name

thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

thisdict.pop('model')

print(thisdict)


# The popitem() method removes the last inserted item(in versions before 3.7, a random item is removed instead)
thisdict = {
    'brand': 'Ford',
    'model': 'mustang',
    'year': 1946
}

thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified keyname
thisdict  = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

del thisdict['model']

print(thisdict)

# The del keyword also delete the dictionary completely
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

del thisdict
# print(thisdict) # raise error because thisdict is no longer exists

# The clear() method empties the dictionary
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

thisdict.clear()
print(thisdict)

# Copy the dictionary
# you cannot copy a dictionary simply by typing dict2 = dict1, becuase dict2 only be reference to 
# dict1, and changes made in dict1 will automatically also made in dict2 
# there are ways to make copy, one way is use the built in dictionary method copy()
# Make a copy of a dictionary with copy() method

thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1947
}

mydict = thisdict.copy()
print(mydict)

# another way to make a copy is to use built in dict() method
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

mydict = dict(thisdict)
print(mydict)


# Nested dictionary
# a dictionary can also contain many dictionaries
# this is called nested dictionaries

myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'tobias',
        'year': 2007
    },
    'child3': {
        'name': 'linus',
        'year': 2011
    }
}

# Or if you want to nest three dictionaries that already exists as dictionaries
child1 = {
    'name': 'emil',
    'year': 2004
}

child2 = {
    'name': 'tobias',
    'year': 2007
}

child3 = {
    'name': 'linus',
    'year': 2011
}

myfamily = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(myfamily)

# The dict constructor
# It is also possible to make a dict constructor

thisdict = dict(brand='ford', model='mustang', year=1946)
# note that keywords are not string literals
# note that use of equal rather than colon for assignment


# fromkeys()
# the fromkeys() return a dictionary with the specified keys and values
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)

print(thisdict)

# Python dictionary keys() method 
# the keys() method returns a view object that object . this view object contains the keys of the dictionary
# as a list The view object will reflect any changes done to the dictionary 
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

x = car.keys()
car['color'] = 'white'
print(x)

# The setdefault() method returns the value of the item with the specified key 
# If the key does not exist, insert the key, with the specified value 

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946

}

x = car.setdefault('model', 'bronco')

print(x)

#update()
# the update method inserts the specified items to the dictionary
# the specified items can be a dictionary or an iterable object

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

car.update({'color': 'white'})


# python conditions and if statements
# Python supports the usual logical conditions from mathematics 

# if statement
a = 33
b = 200

if b > a:
    print(' b is greater than a')

# Indentation 
# python relies on indentation to define scope in the code
# other programing languages uses curly brace for the purpose

# the elif keyword is pythons way of saying 'if the previous conditoins were not true,
# then try this condition 
a = 33
b = 33
if b > a:
    print('b is greater than a')
elif a == b: 
    print(' a is equal to b')

# the else statement catches anything which isn't caught by the preceeding conditions
a = 200
b = 33
if b > a:
    print( 'b is greater than a')
elif a == b:
    print('a and b are eqaul')
else:
    print('a is greater than b')


# Shorthand if 
# if you have only one statement to execute, you can put it on the same line as the if statement
# one line if statement
if a > b: print('a is greater than b')

# shorthand if else
a = 2
b = 330
# print('A') if a > b else print('B') #  getting invalid syntax while runnig 

# one line if else statement, with 3 conditions
a = 330
b = 330
# print('A') if a > b else print('=') if a == b else print('B') 

# And keyword is a logical operator and is used to combine conditional statements
# Test if a greater than b, AND if c is greater than a
a = 200
b = 33
c = 500
if a > b and c > a: 
    print('Both conditions are true')

# the or keyword is a logical operator and is used to combine conditional statements
a = 200
b = 33
c = 500

if a > b or a > c:
    print('At least one of the conditions is True')

# Nested if
# You can have if statements inside if statements this  is called nested if statements

x = 41
if x > 10:
    print('Above ten,')
    if x > 20:
        print('and, also above 20')
    else:
        print('but not above 20')

# Python Loops
# Python has two primitive loops 
# while loops 
# For loops


# The while loop we can execute a set statements as long as condition is true
# print i as long as i less than 6

i = 1
while  i < 6:
    print(i)
    i += 1 

# remember to  increament i, or else the loop will continue forever

# The while loop requires relavant variable to be ready, in this example we need to define
# an indexing variable i,, which is set to 1

# the break statement
# with the break statement we can stop the loop even if the while condition is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue statement 
# with the continue we can stop the current iteration and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement we can run a block of code when the conditin is no longer is True
# Continue to the next iteration if i = 3

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

# A for loop is used for iterating over sequence
# this is less like the for keyword in other programing languages, and works more like an iterator 
# method as found in other object oriented programing languages
# with the for loop we can execute a set of statements,once for each item in a list, tuple etc.

fruits = ['apple', 'banana', 'orange']
for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand
# Looping through a string
# Even strings are iterable objects, they contain a sequence of characters

for x in 'banana':
    print(x)

# With break statement we can stop the loop before it has looped through all the items
# exit the loop when x is banana

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# With the continue we can stop the current iteration of the loop, and continue with the next 
# do not print banana

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)


# The Range() function
# TO through a set of code a specified number of times, we can use the range() function
# the range function returns a sequence of numbers starting from 0 by default and increaments by 1
# ends at a specified number

for x in range(6):
    print(x)

# note that range(6) is not the values of 0 to 6 but 0 to 5
# The range function defaults to 0 as a starting value, however it is possible to specify 
# the starting value by adding a parameter:range(2, 6) 
for x in range(2, 6):
    print(x)

# the range() function default to increament the sequence by 1, however it is possible to specify
# the increament value by adding this parameter range(2, 30, 3)
# increament sequence with 3
for x in range(2, 30, 3):
    print(x)

# Else in for loop
# the else keyoword in a for specifies a block of code that execute after for loop is finished
for x in range(6):
    print(x)
else:
    print('finally finished')

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)

# Python functions
# A function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# A function can return data as a result
# In python a function is defined using def keyword

def my_fuction():
    print('hello from a function')

# To call a function, use the function name followed by paranthesis

def my_function():
    print('hello from a function')

# Patameters 
# Information can be passed to functions as parameters 
# Parameters specified after the function name inside the paranthesis. you can add as many parameters
# as you want, just separate them with a commma
# The following example has a function with one parameter, when the function is called, we
# pass along a first name which is used inside the function to print the full name

def my_function(fname):
    print(fname + ' refsnes') 

my_function('Emil')
my_function('Tobias')
my_function('Linus')


# Default parameter value
# The following example shows how to use default parameter value 
# If we call the parameter without parameter, It uses the default value

def my_function(country='norway'):
    print('I am from ' + country)

my_function()
my_function('India')
my_function('brazil')

# passing list as a parameter
# You can send any type of parameter to a function and it will be treated as the same data type inside the function
# If you send list as a parameter, It will still be a list when it reaches the function

def my_function(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'cherry']
my_function(fruits)

# Return value 
# To let a funciton return a value, use the return statement

def my_function(x):
    return x * 5

my_function(3)
my_function(5)
my_function(9)

# Keyword arguments
# you can also send the arguments with the key = value syntax
# this way the order of the arguments does not matter
def my_function(child3, child2, child1):
    print('The youngest child is ' + child3)

my_function(child1 = 'Emil' , child2 = 'Tobias', child3 = 'Linus')

# The phrase Keyword arguments are often shortened to kwargs in python documentations

# Arbitary arguments
# If you do not know how many arguments that will be passed into your function, add a * before
# the parameter name in the functoin definition 
# this way function receives the tuple of arguments, and can access the items accordingly

def my_function(*kids):
    print('The youngest kid is ' + kids[2])

my_function('Emil', 'Tobias', 'Linus')

# Python also accepts the function recursion, which means a defined function can call itself
# This has the benefit of the meaning that you can loop through data to reach a result
# The developer should be very careful with recursion as it can be quite easy slip into writig function
# which never terminates, or one that uses excess amount of memory or processor power
# In this example try_recursion is a function that we can defined to call itself we use k variable as data
# which decreaments everytime we recurse. the recursion ends with when the condition is not greater than 0

def try_recursion(k):
    if k > 0:
        result = k + try_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
try_recursion(6)

# Python Lambda
# A Lambda function is small anonymous function 
# A Lambda can take any number of arguments, but can only have one expression
# The expression is executed and the result is returned

x = lambda a: a + 10  
print(x(5))

x = lambda a ,b: a * b 
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(2, 3, 4))

# Why use lamda functions
# the power of lambda is better shown when you use them as an anonymous function inside another function
# Say you have function definition that takes one argument and that argument will be multiplied with
# an unknown number

def myfunc(n):
    return lambda a: a * n

# Use that function definition to make a function tha always doubles the number that you send in 

def my_func(n):
    return lambda a: a * n

mydoubler = my_func(2) 
print(mydoubler(11))

# Or use the same function definition to make a function that always triples the number you send in

def my_fun(n):
    return lambda a: a * n

mytripler = my_fun(3)
print(mytripler(11))

# Use lambda functions when anonymous function is required for a short period of time


# Python does not have support for arrays, but python lists can be used instead 
# Arrays are used to store multiple values in single varialbe
# Create an array containing car names 

cars = ['Ford', 'Volvo', 'BMW']

# What is an array
# An array is special variable which holds more than one item at a time 
# If you have a list of items, storing the cars in single variable looks like this 
car1 = 'Ford'
car2 = 'Volvo'
car3 = 'BMW'


# Python classes 
# Python is an object oriented programing language
# Almost everything in python is object, with its properties and methods
# A class is like an object constructor, or a blue print for creating objects

# Create a class
# use the keyword class

class MyClass:
    x = 5

# create an object
# now we can use the class named myclass to create objects
# create an object named p1 and print the value of x

p1 = MyClass()
print(p1.x)

# The init function 
# The examples above are classes and objects in their simplest form, and are not really useful in real life
# To uderstand the meaning of classes we have to understand the builtin init function
# all classes have a function called init which is always executed when the class is being initiated
# Use the init function to assign values to object properties or other operations that are neccessary to do
# when the object is being created 
# Create class named person, use the init function to assign values for name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
p1 = Person('John', 36)

print(p1.name)
print(p1.age)

# The init function is called automatically every time class is being used to create new object
# object methods 
# objects can also contain methods. Methods in objects are functions that belong to the object
# Let us create the function in Person class
# Insert a person that prints greeting,and execute it in p1 object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('Hello my name is ' + self.name)


p1 = Person('John', 36)

p1.myfunc()

# NOte that self parameter is reference to the current instance of the class, and is used to access the 
# variables that belongs to the class

# The self parameter is a reference to the current instance of the class and is used to access the
# variables that belongs to the class

# It does not have to be named self, you can call it whatever you like, but it has to be the 
# first parameter of any function in the class

# use the words mysillyobject and abc instead of self

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print('hello my name is ' + abc.name)
p1 = Person('john', 36)
p1.myfunc()

# Modify object properties on objects like this
p1.age = 25


# delete the object property

del p1.age

# delete objects

del p1

# Inheritance allows us to define a class that inherites all the properties and methods
# Parent class is class being inherited from, also called base class
# Child class is class that inherits from another class, also called derived class

# Create a parent class 
# any class can be parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
    

# Use the person class to create an object, and then execite the  printname method
x = Person('john', 'doe')
x.printname()


# Create child class

class Student(Person):
    pass

# Use the pass keyword when you do not want to add  any other properties or methods to class
# Now the student has the same properties and methods as the person class
# use the student class to create object

x = Student('rajendra', 'reddy')
x.printname()


# Add the __init__ function 
# So far we created a child class that inherits the  properties and methods from its parent
# We want to add __init__ funciton to the child class
# The __init__ method called automatically every time the class is being used to create a new object

# Add __init_ function  to the student class
class Student(Person):
    def __init__(self, fname, lname):
        f = fname

# When you add __init__() function, the child class will no longer inherit the parent init
# the childs __init__() function overrides the inheritance of the parents init functionn

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
    
# now we have successfully added the __init__() function, and kept the inheritance of the parent class
# and we are ready to add functionality in the init function 

# Use the super() function 
# python also have a super function that will make the child class inherit all the methods and
# properties from its parent 

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
        
# # add a year parameterm, and pass the correct year when creating objects

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super(Person, self).__init__(fname, lname)
#         self.graduationyear = year

# x = Student('john', 'doe', 2019)


# Add a method called welcome to the student class


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print('welcome' + self.firstname , self.lastname + 'to the class of '+ self.graduationyear)

# If you add a  method in the child class with same name as a function in the parent class
# the inheritance of the parent method will be overriden 

# Iterators 
# Iterator is an object that contains countable number of values 
# An iterator is an object that can be iterated upon, meaning that you can traverse through 
# all the values
# Technically in python iterator is an object which implements iterator protocal, which consists
# of methods __iter__() and __next__()

# Iterator vs iterable
# Lists , tuple , dictionary and sets are iterable objects. They are iterable containers, which you can get iterator from
# All these objects have a  iter() method which is used to get an iterator 
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings also iterable objects, containing a sequence of characters
mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator
# We can also use a for loop to iterate through an iterable object
mytuple = ('apple', 'banana', 'cherry')
for x in mytuple:
    print(x)

# Iterate the charecters of string 

mystr = 'banana'
for z in mystr:
    print(z)

# The for loop actually creates an iterator object and executes the next() method for each loop
# Create an iterator 
# To create an itarator you have to implement the methods __iter__() and __next__()
# to your object
# As you learned in python classes/objects chapter, all classes have a function called __init__()
# which allows you do some initializing when the object is being created 
# the iter() method acts similar, you can do operations, but must alwyas return the iterator object itself

#Create an iterator that returns numbers, starting with 1,and each sequenc increase by 1

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Stop iteration 
# The example above continue forever if you had enough next() statements or if it was used in a
# for loop to prevent the iteration to go on forever, we can use the stop iteration statement
# In the next() method, we can add a terminating condition to raise an error if the iteration done
# a specified number of times

class MyNumber:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 9:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass1 = MyNumber()
myiter1 = iter(myclass1)
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))


# Python generators
# Generator function: A generator is defined like normal function
# But whenever it needs to generate  a value , it does so with the yield keyword rather than 
# return. if the body of def contains yield, thr function automatically generator function

def simple_generaration():
    yield 1
    yield 2
    yield 3

for value in simple_generaration():
    print(value)

# Generator object 
# Generator function return generator object. generator objects are used either by calling the next
# methodon generator object or using the generaotor object in a for loop
def simplegenratorfun():
    yield 1
    yield 2
    yield 3

x = simplegenratorfun()
# print(x.next())

# A simple program for fibonacci series using generator
def fib(limit):

    # initali first two fibonacci numbers
    a, b = 0, 1

    # one by one yield fibonacci numbers

    while a < limit:
        yield a
        a, b = b, a+b

x = fib(5)
#print(x.next())


# iterating over generator object using for

for i in fib(5):
    print(i)


# decorators 
# Following are important facts about functions in python that are useful to understand decorator
# functions 
# In python we can define a function inside a function 
# In python a function can be passed as parameter to another function

# Adds a welcome message to the string
def messagewithwelcome(str):

    #Nsted function
    def welcome():
        return 'welcome to '

    # Return cancatenation of welcome 
    # and str
    return welcome() + str

# to get site name which welcome is added
def site(site_name):
    return site_name

print(messagewithwelcome('geeksforgeeks'))


# function decorator
# A decorator is a function that takes a function as its only parameter and returns a function.
# this is helpful to wrap functionality with the same code over and over again 
# the above code can be written as follow
# we use @func_name to specify decorator to be applied on another function

# Adds welcoome message to the string
# returned by fun(). takes fun() as 
# parameter and returns welcome()
def decorate_message(fun):

    # nested function
    def addWelcome(site_name):
        return 'welcome to' + fun(site_name)

    # Decorator return the function
    return addWelcome

@decorate_message
def site(site_name):
    return site_name

# Driver code 
# this call is equivalent to call to 
# decorate_message () with function
# site('geeksforgeeks) as parameter
print(site('geeks for geeks'))

# Decorator can also be useful to attach data to functions
# A python example to demonstrate that 
# Decorators can be useful to attach data to functions

# data to func
def attach_data(func):
    func.data = 3
    return func

@attach_data
def add(x, y):
    return x + y

print(add(2, 3))

print(add.data)

# # Module
# Consider a module to be the same as code library
# A file containing set of functions you want to include in your application 

# Create module
# To create module just save the code you want in a file with fiel extension .py

# now we can use the module we just created by using import statement
# import the module
import mymodule
mymodule.greeting('rajendra')

# when usig function from module use syntax module.function
# varibles in modules the module can contain functions as already described but also variables of all types

a = mymodule.person1['age']
print(a)

# import only dictionary person1 from the module
from mymodule import person1
print(person1['age'])

# When importing from keyword, do not use the module name when reffering to elements in the module


# Python dates
# A date in python not a data type of its own, but we can import a module named datatime
# to work with dates as date objects
# import the current datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)

# Date output 
# when we exexute the code from the example above the result will be
# the date contains year, month, day, hour, minute, second, and micro second
# The datetime module has many methods to return information about the dateobject 
# here we can see few objects
import datetime 
x = datetime.datetime.now()
print(x.year)

print(x.strftime('%A'))


# Creating date object
# TO create date,, we can use the datetime() class of the datetime module 
# The datetime class require three parameters to create a date: year, month, day

x = datetime.datetime(2020, 5, 12)
print(x)

# The date time class also takes paremeters for time and timezone, but they are optional and 
# has default value of 0 

# The strftime method 
# the datetime object has method for formatting date objects into readable strings
# the method is called strftime, and takes one parameter, format to specify the format of the returned string

# display the name of the string
import datetime
x = datetime.datetime(2018, 5, 19)
print(x.strftime('%B'))


# JSON is storing and exchanging data 
# JSON is text , writen with javascript object notation 
# Python has built in package called json,which can be work with json data
import json

# Parse json convert from json to python
# if you have a JSON string, you can parse it by using the json.loads() method
# The result will be python dictionary

# Convert from JSON to python 
import json

# Some json
x = '{ "name":"john", "age":36, "city":"new york"}'

# Parse x
y = json.loads(x)

# the result is a python dictionary
print(y["age"])


# Convert from python to json
# if you have a python object, you can convert into a JSON string by using the json.dumps()
# method 
# Convert from python to json

import json
# A python object
x = {
    "name": "john",
    "age": 30,
    "city": "new york"
}

# convert into JSON
y = json.dumps(x)

# The result is json string
print(y)

# we can convert the following python objects into json strings

# dict
# list
# tuple
# string
# int
# float
# string
# Flase
# True
# None

# Convert python object into json strings
print(json.dumps({"name": "john", "age": 30 }))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps('helo'))
print(json.dumps(42))
print(json.dumps(37.89))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from python to json, Python object converted into JSON equivalent


# Python                                                JSON
# dict                                                  Object
# list                                                  Array
# tuple                                                 Array
# str                                                   String
# int                                                   Number
# Flaot                                                 Number
# True                                                  true
# False                                                 false
# None                                                  null


# Convert Python object that contain all legal types
import json
x = {
    "name": "john",
    "age": 36,
    "married": True,
    "divorced": False,
    "children" : ("Ann", "Billy"),
    "Pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# Format the result

# The example above prints the json string but its not very easy to read, with no indentions and line breaks
# The json.dumps() method has parameters to make it easier to made the result 
# use the indent parameter to define the numbers of indents 

t = json.dumps(x, indent=4)
print(t)

# you can also define the separators, default value is (",",":") which means using a commma and a
# space to separete each object, and a colon and a space to separate keys from values
# Use the separators to change the default separator

k = json.dumps(x, indent=4, separators = (".", "="))
print(k)


# Order the result
# Json.dumps parameter method has parameters to order the keys in the result

# Use the sort_keys parameter to specify the result should be sorted or not 

l = json.dumps(x, indent=4, sort_keys=True)
print(l)


# Python regex or python regular expression, is a sequence of characters that form a search pattern
# Regex can be used to check if a string contains a specified search pattern
# Regex module 
# Python has builtin module called re, which can be used to work with regular expressions
# Import the re module
import re 
# when you have imported the re module, you can start using regular expressions
# Search the string that starts with The and ends with spain
import re
txt = "The rain in spain"
x = re.search("^The.*spain$", txt)

print(x)

# The findall function 
# The findall function returns list containin all matches 
# print list of all matches
import re
str = "The rain in spain"
x = re.findall('ai', str)
print(x)

# the list contains matches in the order they are found
# If no matches are found an empty list is returned

# return an empty list if no match was found
import re
str = 'The rain in spain'
x = re.findall('portugal', str)
print(x)


#the serch() function
# The search function searches the string for a match and returns a match object
# if there is a match, only the first occurence of the match will be returned

# search for white space character
str = 'The rain in spain'
x = re.search('\s',str)
print('The first white space character is located in position:', x.start())

# The split function
# The split function returns a list where the string has been spllit at each match
# split at each white space character
import re
str = "The rain in spain"
x = re.split('\s', str)
print(x)

# you can control the number of occurences by specifying the maxsplit parameter
# split the string only at the first occurence
import re
str = 'The rain in spain'
x = re.split("\s", str, 1)
print(x)

# The sub() function
# The sub() function replaces the matches with the text of your choice
# Replace every white space character with the number 9
import re
str = 'The rain in spain'
x = re.sub('\s', '9', str)
print(x)

# You can control the number of replacements by specyfying count parameter
# replace the first two occurences
import re 
str1 = 'The rain in spain'
x = re.sub('\s', 9, str1, 2)

# Matc object
# A match object is an object containing information about search and result

# if there is no match none will be returned, instead of match object
# DO a search that will be returned a match object
import re
str = 'The rain in spain'
x = re.search('ai', str)
print(x)

# The match object has properties and methods used to retrieve information about search,and
# the result
# .span() method returns tuple containing start, end positions of the match
# .string() return the string passed into the function
# .group() return the part of the string where there was a match

# print the position of the first match occurence
# The regular expression looks for anywords that starts with uppercase S
import re
str = 'The rain in the spain'
x = re.search(r'\bS\w+', str)
print(x.span())


# print the string passed into the function
str = 'The rain in spain'
x = re.search(r'\bS\w+', str)
print(x.string)

#print the part of a string where there was a match
#The regular expression looks for any words that starts with an upper case "S"

import re
str = 'The rain in the spain'
x = re.search(r'\bS\w+', str)
print(x)

# PIP 
# What is PIP 
# PIP is a package manager for python packages , or modules if you like
# If you have python 3.4 later pip is included by default
# # What is package
# A package contains all the files you need for a module
# modules are code libraries you can include in your project
# check if pip is installed 
# Once package is installed you can use that package in your project


# Python try except finally blocks
# The try block lets you test the block of code for errors
# The except block lets you handle the error
# The finallu block lets you execute the code, regardless of the result of the try and except
# blocks
# Exception handling
# when an error occurs , or an exception as we call it,Python will normally stop and 
# generate an error message These exceptions can handle using the try statement

# The try block generate an exception, because x is not defined
try:
    print(x)
except:
    print('an exception occured')

# Since the try block raises an error, the except block will be executed 
# without the try block, the program will crash and raise an error
# This statement will raise an error, because x is not defined
print(x)

#Many exceptions
# you can define as many exception blocks as you want , if you want special block of code for
# kind of an error 

# print one message if the try block raises a NameError and other block for other errors
try:
    print(x)
except NameError:
    print('variable is not defined')
except:
     print('somethingelse went wrong')


# you can use else keyword to define a block of code to be executed if no errors were raised
# Example
# IN this try block does not generate any error
try:
    print("hello")
except:
    print('something went wrong')
else:
    print('Nothing went wrong')

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not 

try:
    print(x)
except:
    print('something went wrong')
finally:
    print('The try except finished')

# this can be used to close objects and clean up resources
# try to open a file and write to a file that is not writable
try:
    f = open('demofile.txt')
    f.write("Lorum Ipsum")
except:
    print('something went wrong writing to the file')
finally:
    f.close()


# Python command line input
# Python allows for command line input
# that means we are able ask user for input
print('Enter your name:')
x = input()
print('hello', x)

y = input("enter your name:")
print('hello', y)


# new comment