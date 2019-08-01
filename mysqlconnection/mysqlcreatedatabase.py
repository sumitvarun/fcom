import mysql.connector
conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='sumit')
mycursor=conn.cursor()
mycursor.execute("show tables")
mycursor.fetchall()
