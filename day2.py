#Slicing 
a=”Hello”
a[0:2] -- ‘He’
a[1:] -- ‘ello’
a[:-1] -- ‘Hell’

L={10,20,30,40,50,60}
print(L[1:5])  -- 20,30,40,50
print(L[::2]) -- 10,30,50
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[1:]) 
print(my_tuple[:2]) 
print(my_tuple[1:3])




#Exception handling
A)
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"

B)
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print "Error: can\'t find file or read data"
   
   


    
 #Regular expressions
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
OUTPUT-  YES! We have a match!
This is used to check if the string starts with The and ends with Spain. 

The findall() function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
OUTPUT- ['ai', 'ai']

The search() function searches the string for a match, and returns a Match object if there is a match.

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
OUTPUT- The first white-space character is located in position: 3

The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
OUTPUT- ['The', 'rain', 'in', 'Spain']




#Indexing 
a=”Hello”
print(a[0]) -- H
print(a[2]) --l 

a={‘apple”,”banana”,”lichi”}
print(a[0]) -- apple
print(a[2]) -- lichi
print(a[3]) -- Error out of bound
a=(1,2,3,4,5,6)
print(a[2]) -- 3
