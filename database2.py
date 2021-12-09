"""ROWID and WHERECLOSE"""
import sqlite3

conn = sqlite3.connect('customersinfo.db') #Customer is the name of the database, db is for database

#create a cursor 'c'
c = conn.cursor()  #cursor is what tells the database what u want to do 
 
c.execute("SELECT * FROM customersinfo")

items = c.fetchall()
for i in items:
        print(i)
#primary key is a unique ID number that each recod in database gets
#each instance that carries attributes is a record (ex: the row that contains all infor pertaining to one person)

#rowid is the primary key  sqlite keeps for each record:
c.execute("SELECT rowid, * FROM customersinfo")#means print the row ID along with other info in database
#therefore when u call a certain primary key(ID), it returns the info attached to it


"""WHERE CLOSE"""
#To look for specific info:
c.execute("SELECT * FROM customersinfo WHERE last_name = 'Tazi' ")
#This code will print info stored to that last name include the last name

c.execute("SELECT * FROM customersinfo WHERE age >= 21")
#Will print everyone over the age of 21

c.execute("SELECT * FROM customersinfo WHERE name LIKE 'Ta%' ")
#This will print everything beginning with Ta, the % is a wild card to say whatever comes after

c.execute("SELECT * FROM customersinfo WHERE email LIKE '%gmail.com' ")
#Returns all emails registered to gmail 

