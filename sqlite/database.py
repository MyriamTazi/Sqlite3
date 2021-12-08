import sqlite3

"""conn = sqlite3.connect(':memory:') #this code would if you don't want to save the database"""
conn = sqlite3.connect('customersinfo.db') #Customer is the name of the database, db is for database

#create a cursor 'c'
c = conn.cursor()  #cursor is what tells the database what u want to do 

#Make a table and assign the attributes you want while specifying the datatype of each 
c.execute(''' CREATE TABLE customersinfo  
        (first_name TEXT,     
        last_name TEXT,       
        num INT,           
        email TEXT)''')

"""the following code takes a list of various tuples to add to the table, the order of the attributes must match that of the columns """
other_info = [
('Ken', 'wyne', 55594566, 'kw@gmail.com'),
('king', 'horese', 676658, 'tg@gmail.com'),
('bla', 'quaa', 667789, 'gg@gmail.com'),
('after', 'whatever', 675567, 'at@gmail.com')
]
"""The following is as it implies, the ??? are place holders for the info """
conn.executemany("INSERT INTO customersinfo VALUES(?, ?, ?, ?)", other_info)

conn.execute("SELECT * FROM customersinfo") #* means all

print(conn.fetchall()) #As the name implies
print(conn.fetchone()) #Will return the first result
print(conn.fetchone()[0]) #Will return the first item in the tuple, same can be done with others
print(conn.fetchmany(3)) #Will return the specified number, in this case the first 3


databases = conn.fetchall() #Can also be set as a variable to use in a loop

for i in databases:    #Loop to get all items at index[0] in each tuple
	item = i
	print(f"{item[0]} + is an item in the database")
#Will print: ken, king, bla, after from other_info


#These 2 commands to commit and close, logging the new details 
conn.commit()  

conn.close() 
