#single line comment
#string input
name = input("enter your name: ")
print(name)
#integer inputs
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
#python arithmetic operators
add = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
mod = num1%num2
power = num1**num2
print(add)
print(sub)
print(mul)
print(div)
print(mod)
print(power)

#relational operators
print(num1>num2)
print(num1==num2)
print(num1>=num2)
#python functions
print(len(name))
print(name.upper())
num3= -20
print(abs(num3))
s= sum([1,2,3,4,5])
print(s)
#find number divisible by 5 in a list
list=[12,35,67,90,34,70,50,80,10,25,19]
for item in list:
    if(item%5==0):
     print(item)
#tuples
tup1=('python', 'is', 'high','level')
tup2=('programmin','language')
print(tup1+tup2)
#size of a tuple
print("size of tuple1 in bytes: " + str(tup1.__sizeof__()))
print("size of tuple2 in bytes: " + str(tup2.__sizeof__()))

#dictionary
dict1 = {'a':10,'b':20,'c':30}
dict2 = {'d':40,'e':50}
dict3={**dict1,**dict2}
print(dict3)  
#check if 30 present in dict
print(30 in dict3.values())

def returnSum(dict1):
    sum=0
    for i in dict1:
        sum=sum + dict1[i]
        return sum

print("sum: ", returnSum(dict1))   

#strings
string1= "i am learning python strings"
print(string1)
print(string1[4:20])
print(string1[10:-1])
