import mysql.connector
import random
#create the connection object
myconn= mysql.connector.connect(host="localhost", user="root", passwd="1234",database ="pythondb2")

#printing the  connection object
print(myconn)

#creating the cursor object
cur = myconn.cursor()
sql= "insert into employee(name, id, salary, dept_id, branch_name)values(%s,%s,%s,%s,%s)"


#The row values are provided in the form of tuple
#val= ("sumit", 110, 25000.00, 201, "newyork")
print("welcome Admin")
print("ID")
for i in range(4):
    value= random.uniform(0,9)
    print(value,end='')
    stdid=str(value)
    f=open((stdid)+".txt","w")
    f.write(stdid)
    f.write("\n")
    
    f.write("ID:")
    f.write(stdid)
    f.write("\n")
    
    a= input("Enter the name")
    f.write("name")
    f.write(a)
    f.write("\n")

    
    id =(input("ENTER THE ID"))
    f.write("id")
    f.write(id)
    f.write("\n")

    
    salary= (input("Enter Employee Salary"))
    f.write("salary")
    f.write(salary)
    f.write("\n")

    dept_id= (input("Enter department id"))
    f.write("dept_id")
    f.write(dept_id)
    f.write("\n")

    branch_name= input("Enter Branch name")
    f.write("branch_name")
    f.write(branch_name)
    f.write("\n")

    print(a,id,salary,dept_id,branch_name)
    

try:
    #inserting the values into the tables
    cur.execute(sql,a,id,salary,dept_id,branch_name)

   #commit the transaction
    myconn.commit()
except:
    myconn.rollback()

print(cur.rowcount,"record inserted!")
myconn.close


