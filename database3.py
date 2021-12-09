#Changing and manipulating records
import sqlite3

conn = sqlite3.connect('customersinfo')
c = conn.cursor()

"""Updating records"""
c.execute("""UPDATE customersinfo SET first_name = 'Sally'
        WHERE rowid = 4 """)
#You want to specify the row you're trying to update
#Note that Primary keys start from 1

"""Deleting records"""
c.execute("DELETE FROM customersinfo WHERE rowid = 5")
#Will delete all from row 5, row 5 has been 'dropped' permanently

"""Ordering Database"""
#By default order is ASCending, let's make it DESCending:
c.execute("SELECT rowid, * FROM customersinfo ORDER BY rowid DESC")

#Order by last name alphabetical
c.execute("SELECT rowid, * FROM customersinfo ORDER BY last_name")

#Or DESCending alphabetically z - a
c.execute("SELECT rowid, * FROM customersinfo ORDER BY last_name DESC")

""" AND OR """
c.execute("SELECT rowid, * FROM customersinfo WHERE last_name LIKE 'Ta%' AND WHERE ROWID = 3")
#Looking for two conditions where it returns a result if our statement is True
#OR can also be used instead of AND 
#OR and AND can be reiterated as many times as you want, depending on what you're looking for

"""Limiting"""
#When dealing with Large data and want to limit the number of rows returns: 
c.execute("SELECT rowid, * FROM customersinfo LIMIT 2") #Will return first 2 rows

#to return last 3 for example:
c.execute("SELECT rowid, * FROM customersinfo ORDER BY rowid DESC LIMIT 3")

"""Dropping a table """

#Deleting a whole table 
c.execute("DROP TABLE customersinfo")
conn.commit()
