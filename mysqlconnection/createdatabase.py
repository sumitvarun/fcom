import mysql.connector
#create the connection object
myconn= mysql.connector.connect(host="localhost", user="root", passwd="1234",database ="sumit")

#printing the  connection object
print(myconn)

#creating the cursor object
cur = myconn.cursor()

try:
    dbs = cur.execute("show databases")
except:
    myconn.rollback()
for x in cur:
    print(x)
myconn.close()
    
