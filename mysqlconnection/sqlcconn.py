import mysql
connection= mysql.connector.connect(host= 'localhost', user= "root", passwd= "1234", db= "sumit")
mycursor = connection.cursor()
mycursor.execute("""create table detail
(
id int primary key
name varchar (20)
)""")
connection.commit()
connection.close()
