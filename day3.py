# simple python code to check whether a number is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print ("even")
	else:
		print ("odd")


# Driver code to call the function
if __name__=="__main__":
  a = int(input("Enter a number"))
  evenOdd(a)
  
 # importing sqrt() and factorial from the
# module math
from math import sqrt, factorial
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))


#List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.

def listcomp(str):
  List = []
  for character in str:
    List.append(character)
  print(List)
if __name__=="__main__":
  str = input("What do you want to add in list")
  listcomp(str)
  
  
#iterators
def itera(val):
    iter_obj = iter(val)
    while True:
        try:
            item = next(iter_obj)
            print(item)
        except StopIteration:
            break
    
if __name__=="__main__":
    val = input("enter the data you want to iterate\n")
    itera(val)
    
#generators
"""Generator-Function : A generator-function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword 
rather than return. If the body of a def contains yield, the function 
automatically becomes a generator function."""
def nextsquare():
    i=1;
    while True:
        yield i*i
        i+=1

if __name__=="__main__":
    it = int(input("Enter a number upto what number you need squares"))
    for num in nextsquare():
        if num>it:
            break
        print(num)
    
