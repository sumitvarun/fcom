import mysql.connector
#create the connection object
myconn= mysql.connector.connect(host="localhost", user="root", passwd="1234",database ="sumit")

#printing the  connection object
print(myconn)

#creating the cursor object
cur = myconn.cursor()

try:
    #creating a new database
    cur.execute("create database pythondb2")

    #getting the list of all the databases which will now include the new database pythondb2

    dbs = cur.execute("show databases")

except:
    myconn.rollback()
for x in cur:
    print(x)

myconn.close()
    
