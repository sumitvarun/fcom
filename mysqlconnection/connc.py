Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector

>>> #create the connection object
>>> myconn=mysql.connector.connect(host="localhost", user="root", passwd="1234")
>>> print(myconn)
<mysql.connector.connection.MySQLConnection object at 0x032A9970>
>>> 
