import mysql.connector
#create the connection object
myconn= mysql.connector.connect(host="localhost", user="root", passwd="1234",database ="pythondb2")

#printing the  connection object
print(myconn)

#creating the cursor object
cur = myconn.cursor()

try:
    dbs = cur.execute("create table Employee(name varchar(20) not null,id int(20) not null primary key, salary float not null,Dept_id int not null)")
    db = cur.execute("show tables")
except:
    myconn.rollback()

myconn.close()
    
