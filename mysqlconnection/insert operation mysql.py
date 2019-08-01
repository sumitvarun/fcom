import mysql.connector
#create the connection object
myconn= mysql.connector.connect(host="localhost", user="root", passwd="1234",database ="pythondb2")

#printing the  connection object
print(myconn)

#creating the cursor object
cur = myconn.cursor()
sql= "insert into employee(name, id, salary, dept_id, branch_name)values(%s,%s,%s,%s,%s)"


#The row values are provided in the form of tuple
val= ("sumit", 110, 25000.00, 201, "newyork")


try:
    #inserting the values into the tables
    cur.execute(sql,val)
    print(val)

   #commit the transaction
    myconn.commit()
except:
    myconn.rollback()

print(cur.rowcount,"record inserted!")
myconn.close
