# File handling is an important part of any webapplications
# Python has several function for creating, reading, updating, and deleting files

# File handling 
# The key function for working with files in python is open()
# The open function takes two parameters file name and mode
# There are four different methods for opening a file
# 'r' Read- default value. opens a file for reading, error if the file does not exist
# 'a' Append- opens a file for appending, create a file if it does not exist
# 'w' Write - opens a file for writing, create a file if it does not exist
# 'x' Create- create a file, returns an error if file exists

# In addition you can specify if the file should be handled as binary or text mode

# 't' -text - default value. text mode
# 'b' -binary - binary mode

# To open a file for reading it is enough to specify the name of the file
f = open('demofile.txt')

f = open('demofile.txt', 'rt')

# Because r for read and t for the text are the default values, you do not need to specifyt them
# Make sure the file exists, or else you will get an error

# Open a file on the server 
# Assume that we have following file, located in the same folder as python

#  To open file use open() function  returns a file object which has a read() method for reading the content
# of file 

f = open('demofile.txt', 'r')
print(f.read())

# Read only parts of the file
# By default the read() method returns the whole text, but you can also specify how many characters you want to
# return
#  Return the first five characters of the file
f = open('demofile.txt', 'r')
print(f.read(5))

#Read lines
# you can return one line by using the readline() method
# read one line of the file 
f = open('demofile.txt', 'r')
print(f.readline())

# By calling readline() you can read the two lines

f = open('demofile.txt')
print(f.readline())
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line
f = open('demofile.txt', 'r')
for x in f:
    print(x)

# It is good practice to always close the file when you are done with it.
f = open('demofile.txt', 'r')
print(f.readline())
f.close()

# you should always close your files, in some cases due to buffering, changes made to file may not 
# show until you close the file

# write to an existing file
# to write to an existing file, you must add parameter to open() function
# 'a' append - will append to the end of the file
# 'w' write - will overwrite any existing content

# Example 
# open the file 'demofile2.txt' and append content to the file

f = open('demofile2.txt', 'a')
f.write('now the file has more content')
f.close()

# open and read the file after appending
f = open('demofile2.txt', 'r')
print(f.read())

# open the 'demofile.txt' and overwrite the content
f = open('demofile3.txt', 'w')
f.write('Woops! I have deleted the content')
f.close()

# open and read the file after the appending
f = open('demofile2.txt', 'r')
print(f.read())

# the 'w' overwrite the entire file


# create a new file in python, use the open() method, with one of the following parameters
# 'x' - Create - create a file will return an error if file does exist
# 'a' -Append- will create a file if the specified file does not exist
# 'w' -write- will create a file if the specified file does not exist

# create a file called 'myfile.txt'
f = open('myfile.txt', 'x')

# create a file if it does not exist
f = open('myfile.txt', 'w')

# Delete file
# To delete a file you must import os module, and run its os.remove() function

import os
os.remove('demofile.txt')

# check if file exist, then delete it 
import os
if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('the file does not exist')

# delete folder
# To delete an entire folder, use os.rmdir() method

# remove the folder myfolder
import os
os.rmdir('myfolder')
# note you can only remove empty folder