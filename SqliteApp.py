import sqlite3
#Connect to database
conn = sqlite3.connect('customersinfo')
    #create a cursor
c = conn.cursor()


""" First function to return all items in table customersinfo """
def return_all():
    #Ask database
    c.execute("SELECT rowid, * FROM customersinfo")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit ()
    conn.close()


""" Second function: call when wanting to add a record to the database """
def add_record(first, last, email):
    c.execute("INSERT INTO customersinfo VALUES (?, ?, ?), (first, last, email)")
    conn.commit()
    conn.close()
    
    
"""Third function: call when wanting to delete a record from the database"""
def delete_record(id):
    c.execute("DELETE FROM customersinfo WHERE rowid = (?), id") #? is a placeholder 
    conn.commit()
    conn.close()
#BEWARE! argument passed must be is string format(ex:'3') 

"""Fourth function: Create many records"""
def many_records(list):
    c.executemany("INSERT INTO customersinfo VALUES (?, ?, ?), list")
    conn.commit()
    conn.close()
#To call this function, the argument can be preset to a list of tuples, for example:
# lst = [('name', 'second name', 'email'), ('name', 'second name', 'email'), ('name', 'second name', 'email') ]
# SqliteApp.many_records(lst)


"""Fifth function: search and pull where records are"""
def where_is(email):
    c.executemany("SELECT rowid, * customersinfo WHERE email = (?), email")
    #Loop to return records with the passed email
    items = c.fetchall()
    for item in items:
        print(item)
        
    conn.commit ()
    conn.close()
#Keep in mind that due to several different ways you might want to find and return 
#stuff, this function would not really be viable to make in a 'real-life' situation


"""Calling all functions:"""

"""First function: """ 
import SqliteApp
SqliteApp.return_all()

"""Second function: """
import SqliteApp
SqliteApp.add_record('john', 'LaFoe', 'Jolf@gmail.com')

"""Third function: """
import SqliteApp
SqliteApp.delete_record('5')

"""Fourth function: """
import SqliteApp
lst = [('name', 'second name', 'email'), ('name', 'second name', 'email'), ('name', 'second name', 'email') ]
SqliteApp.many_records(lst)

"""Fifth function: """
import SqliteApp
SqliteApp.where_is('Jolf@gmail.com')