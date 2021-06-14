#################################### DATA HANDLING ###########################################

import pandas as pd

x=(1,2,3,4)
myval=pd.Series(x)
print(myval)

x=[(1,2),('a','b')]
myval=pd.Series(x)
print(myval)  #print values in pair
print(myval[1])

x=[(1,2),('a','b')]
myval=pd.Series(x, index=('numbers','alphabets'))  #giving our own labels
print(myval)
print(myval[1])   
print(myval['numbers'])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)    #keys becomes indexes
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])  #Creat a Series using only data from "day1" and "day2"
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df) 
print(df.loc[1])  #returns a pandas Series
print(df.loc[[1,2]])  #When using [], the result is a Pandas DataFrame


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=("day1", "day2", "day3"))  #giving our own labels
print(df) 
print(df.loc['day1'])  
print(df.loc[['day1','day2']]) 


##################################################### FILE HANDLING ########################################################

#1) Count the number of lines in a file

def count():
    f=open('file.txt')
    c=0
    for i in f:
        c+=1
    print("The number of lines in the file are:",c)
    f.close()

#2) Count the number of characters in a file

def count():
    f=open('file.txt')
    c=0
    for i in f:
        for x in i:
            c+=1
    print("The number of characters in the file are:",c)
    f.close()
#3) Replace the content of one file with the other

def copy():
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file before update:",data)
    f1=open('file.txt','w')
    f2=open('file2.txt')
    data=f2.read()
    f1.write(data)
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file after update:",data)
    f1.close()
    f2.close()

#4) Find the sum of the space separated numbers entered in a file
def findsum():
    f1=open('file3.txt')
    data = f1.read()
    x=data.split()
    i = list(map(int, x))
    print('Sum of values is:',sum(i))
    f1.close()

#5) Append the content of one file in another
def copy():
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file before update:",data)
    f1=open('file.txt','a')
    f2=open('file2.txt')
    data=f2.read()
    f1.write(data)
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file after update:",data)
    f1.close()
    f2.close()
    

########################################## Database Connectivity #######################################

import mysql.connector

mydb=mysql.connector.connect(       #connecting to server
    host="localhost",
    user="root",
    password="nancy@123"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE database students")

#connecting to db
mydb=mysql.connector.connect( 
    host="localhost",
    user="root",
    password="nancy@123",
    database="students"
)
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)

#creating table
mycursor.execute('SHOW Tables')
for x in mycursor:
    print(x)

mycursor.execute("CREATE TABLE stud (id Int, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("ALTER TABLE stud MODIFY id INT AUTO_INCREMENT PRIMARY KEY")   #field modified
#adding one record
sql = "INSERT INTO stud (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql,val)
mydb.commit()
print('Number of rows added:',mycursor.rowcount)
print('Last added row id:',mycursor.lastrowid)

#adding multiple records
sql = "INSERT INTO stud (name, address) VALUES (%s,%s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql,val)
mydb.commit()
print('Number of rows added:',mycursor.rowcount)
print('Last added row id:',mycursor.lastrowid)

#retrieving all the records from db
mycursor.execute("SELECT * FROM stud")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#retrieving selected columns from db
mycursor.execute("SELECT id,name FROM stud")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#retrieving only one record from db
mycursor.execute("SELECT * FROM stud")
myresult = mycursor.fetchone()
print(myresult)

#retrieving only one record from db
mycursor.execute("SELECT id, name FROM stud")
myresult = mycursor.fetchone()
print(myresult)

#using WHERE
mycursor.execute("SELECT * FROM stud WHERE address ='Park Lane 38'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#using placeholder to prevent injection
sql="SELECT * FROM stud WHERE address =%s"
val=('Park Lane 38',)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#using WHERE
mycursor.execute("SELECT * FROM stud WHERE name LIKE '%na%'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#using ORDER BY and DESC
mycursor.execute("SELECT * FROM stud ORDER BY name DESC")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Using DELETE
sql = "DELETE FROM stud WHERE name = %s"
val=("Michael" ,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted!")

#UPDATE table
sql = "UPDATE stud SET address = %s WHERE address = %s"
val = ("Valley 345", "Park Lane 38")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#LIMIT AND OFFSET
mycursor.execute("SELECT * FROM stud LIMIT 5 OFFSET 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#DROP TABLE
sql = "DROP TABLE IF EXISTS stud"
mycursor.execute(sql)
