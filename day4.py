########################################### CLASSES AND OBJECTS ##################################################
#A class is a user-defined blueprint or prototype from which objects are created. 
"""Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute"""


class temp:
  pass
  
  
  
class student:
  name = input("enter student name")
  id = input("enter student id")

  def fun(self):
    print("my name is "+ self.name)
    print("my id is "+ self.id)
#creating an object for student class
ob1=student()
ob1.fun()



class student:
  def __init__(self,name):
    self.name=name
    print(self.name)
  def fun(self,id):
    self.id=id
    print(self.id)

if __name__=="__main__":
  name = input("enter the student name: ")
  ob1=student(name)
  id = input("enter the student id")
  ob1.fun(id)
  
  
  
##########################################################################

#CLASS INHERITANCE

#single level inheritance

'''In python single inheritance,a derived class is derived only from a single parent
class and allows the class to derive behaviour and properties from a single base class.
This enables code reusability of a parent class
and adding new features to a class makes code more readable, elegant and less redundant.'''

class a:
    def m(self):
        print("hello")   
class b(a):
    def m2(self):
        print("bye")
q=b()
q.m()
q.m2()

#output-- hello bye

#multileval inheritance

'''Multi-Level inheritance is possible in python like other object-oriented languages.
Multi-level inheritance is archived when a derived class inherits another derived class.
There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.'''

class a:
    def m(self):
        print("hii")
class b(a):
    def m2(self):
        print("bye")
class c(b):
    def m3(self):
        print("tata")
q=c()
q.m()
q.m2()
q.m3()

#output-- hii bye tata


#multiple inheritance

'''Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance'''


class parent: 
    def m(self):
        print("my name is")
class parent2:
    def m2(self):
        print("taran")
class child(parent,parent2):
    def m3(self):
        print("hello")
c=child()
c.m()
c.m2()
c.m3()

#output--- my name is taran hello

#hierarchial inheritance

'''Hierarchical Inheritance: When more than one derived classes are created from a single base this type of
inheritance is called hierarchical inheritance.'''

class employe:
    company="data loves"
class system(employe):
    def sa(self):
        print("salary 45")
        print(self.company)
class tutor(employe):
    def re(self):
        print("hii")
class python(tutor):
    def ta(self):
        print("bye")
q=python()
q.ta()
q.re()
w=system()
w.sa()

#output-- hii salary 45 data loves

##########################################################################################################################

#closure in python

'''A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution.
Three characteristics of a Python closure are
it is a nested function. it has access to a free variable in outer scope.'''

#Question 1

class a:
    def fun(x,y):
        if x>=y:
            def msg(x,y):
                print('team win x ',x)
            msg()
        else:
            print('team win y')
    fun(x=input(int('enter team x score')),y=input(int('enter a team y secore')))
a()

#question 2

def hii(x,y):
    def hello(x,y):
        print(x,y)
    hello()
hii(x=5,y=5)

#output-- 5 5

##################################################################################################################

#DECORATORS

#Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
#@ DECORATOR

#Question


class student:
    name="vsics"
    def __init__(self,x,y):
        count=0
        self.name=x
        self.rollno=y
    def display(self):
        print("hello my self is:",self.name)
        print("hello my roll number is:",self.rollno)
    @classmethod
    def getcollegename(cls):
        print("college name is :",cls.name)
     

a=student(x="taran",y="5")

a.display()
a.getcollegename()

#output--hello my self is: taran
#hello my roll number is: 5
#college name is : vsics
#college name is : vsics


#Question 2

class student:
    name="vsics"
    def __init__(self,x,y):
        count=0
        self.name=x
        self.rollno=y
    def display(self):
        print("hello my self is:",self.name)
        print("hello my roll number is:",self.rollno)
    @classmethod
    def getcollegename(cls):
        print("college name is :",cls.name)
    @staticmethod
    def findaverage(x,y):
        print("avg:",(x+y)/2)
     

a=student(x="taran",y="5")

a.display()
a.getcollegename()

student.getcollegename() #second method
student.findaverage(x=5,y=4)



#output--hello my self is: taran
#hello my roll number is: 5
#college name is : vsics
#college name is : vsics
#avg :4.5

#########################################################################################################


#Descriptors

'''Descriptors let objects customize attribute lookup, storage, and deletion.
This guide has four major sections:
The “primer” gives a basic overview,
moving gently from simple examples,
adding one feature at a time. Start here if you’re new to descriptors.
The second section shows a complete,
practical descriptor example.
If you already know the basics, start there.
The third section provides a more technical
tutorial that goes into the detailed mechanics of how descriptors work.
Most people don’t need this level of detail.
The last section has pure Python equivalents for built-in descriptors that are written in C.
Read this if you’re curious about how functions turn
into bound methods or about the implementation of common tools like classmethod(), staticmethod(), property(), and __slots__.'''


#Question

class A:
    x = 5       # Regular class attribute
    y = Ten()    # Descriptor instance

a = A()         # Make an instance of class A
a.x             # Normal attribute lookup
a.y             # Descriptor lookup


#output--5 10


#Question 2


import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute
s = Directory('songs')
g = Directory('games')
s.size                              # The songs directory has twenty files
g.size                              # The games directory has three files
os.remove('games/chess')            # Delete a game
g.size                              # File count is automatically updated



#output--- 20 3 2


#Question 3

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def disp(self):
        pass
class B(A):
    def disp(self):
        print("GOOD MORNING")
a=B()
a.disp()

#output--- GOOD MORNING

#########################################################################################################

#PROPERTIES

'''This class has a single attribute named hidden_name which we do not want people to access directly. Hence,
two methods are defined in the class – a getter called get_name() and a setter called set_name().'''

class Person():
    def __init__(self, value):
        self.hidden_name = value
    
    @property
    def name(self):
        print('Getting name:')
        return self.hidden_name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        self.hidden_name = value
        
    @name.deleter
    def name(self):
        print('Deleting name')
        del self.hidden_name


p = Person('Bob')

# calls the getter
print(p.name)
#OUTPUT-- Prints Getting name: Bob

# calls the setter
p.name = 'Sam'
#OUTPUT-- Setting name to Sam

# calls the deleter
del p.name
#OUTPUT-- Deleting name

  
  
