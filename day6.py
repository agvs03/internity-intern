# Day-6 Task

# 1.Intro to NumPy:

# What is NumPy: NumPy stands for Numerical Python.NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# Why NumPy: In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.	

# Limitation of NumPy: 
# A)Using “nan” in Numpy: “Nan” stands for “not a number”. It was designed to address the problem of missing values. NumPy itself supports “nan” but lack of cross-platform support within Python makes it difficult for the user. That’s why we may face problems when comparing values within the Python interpreter.
# B)Require a contiguous allocation of memory: Insertion and deletion operations become costly as data is stored in contiguous memory locations as shifting it requires shifting.
# Installation: Install it using this command:
# C:\Users\Your Name>pip install numpy
# Once NumPy is installed, import it in your applications by adding the import keyword:
# import numpy as np

# 2.NumPy ndarray objects: NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.
# Example: 

A)
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


B)As tuples-
import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)

3.
NumPy Array Indexing:Array indexing is the same as accessing an array element.
You can access an array element by referring to its index number.
Example:
A)
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])		#---6

B)Negative Indexing-
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])	#---Last element from 2nd dim: 10


NumPy Array Slicing: Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
Example: 
A)
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])		#---[1 2 3 4]

B)
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])		#---[3 8]



4.Memory layout: 
The following attributes contain information about the memory layout of the array:
ndarray.flags- Information about the memory layout of the array.
ndarray.shape- Tuple of array dimensions.
ndarray.strides- Tuple of bytes to step in each dimension when traversing an array.
ndarray.ndim-	Number of array dimensions.
ndarray.data-	Python buffer object pointing to the start of the array’s data.
ndarray.size-	Number of elements in the array.
ndarray.itemsize-	Length of one array element in bytes.
ndarray.nbytes-	Total bytes consumed by the elements of the array.
ndarray.base-	Base object if memory is from some other object.

Example: 
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)		#---None
print(y.base)		#---[1 2 3 4 5]
5.Copy and Views: The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

Example:
A)Copy-
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)		#---[42 2 3 4 5]
print(x)		#---[1 2 3 4 5]

B)View-
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)	#---[31 2 3 4 5]
print(x)	#---[31 2 3 4 5]

6.Creating arrays: 
We can create any dimension arrays- 0-D, 1-D, 2-D, 3-D etc.

NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

Example:
A)Using ndim-
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)		#---0
print(b.ndim)		#---1
print(c.ndim)		#---2
print(d.ndim)		#---3

B)Higher Dimensional Array- Using ndim argument
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)					#---[[[[[1 2 3 4]]]]]
print('number of dimensions :', arr.ndim)	#---number of dimension : 5

7.Array Data Types: 
list of all data types in NumPy and the characters used to represent them.
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

Example:
A)The NumPy array object has a property called dtype that returns the data type of the array:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)		#---int64
B)
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)			#---[b‘1’ b‘2’ b‘3’ b‘4’]
print(arr.dtype)		#---S1

C)int to boolean using astype()
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)			#---[ True False True ]
print(newarr.dtype)		#---bool
