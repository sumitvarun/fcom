import random
class Login:
    def Admin(self):
        print("Welcome Admin")
        print("Id")
        for i in range (4):
            value= random.uniform(0,9)
            print(value,end='')
            stdid=float(value)
            f= open((stdid)+".txt","w")
            f.write(stdid)
            f.write("\n")
            a=input("Enter name")
            f.write("ID:")
            f.write(stdid)
            f.write("\n")
            f.write("Name:")
            f.write(a)
            f.write("\n")
            b=(input("Enter Mobile no"))
            f.write("Mobile no:")
            f.write(b)
            f.write("\n")
            
            print("Enter Subject Below")
            c=input("Hindi Marks")
            f.write("Hindi:")
            f.write(c)
            f.write("\n")
            
            d=input("English Marks")
            f.write("English: ")
            f.write(d)
            f.write("\n")
            
            e=input(" MATH Marks")
            f.write("MATH: ")
            f.write(e)
            f.write("\n")
            
            F=input("SCIENCE Marks")
            f.write("SCIENCE: ")
            f.write(F)
            f.write("\n")
            
            g=input("SST Marks")
            f.write("SST: ")
            f.write(g)
            f.write("\n")
            
            
        
            
    def Student(self):
        print("Welcome Student")
        for i in range (4):
            value= random.uniform(0,9)
            print(value,end='')
            Stddata=str(value)
            f= open("Stddata.txt","w")
            f.write(value)
            
            
                   
                   
        
    def __init__(self):
        print("***************************************")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ -_")
        Username= (input('Enter Username'))
        if(Username=="admin"):
            print("Dear admin Enter password        ")
        elif(Username=="student"):
            print("Dear student Enter password      ")
            print("*********************************")
        password= int(input('Enter password'))
        print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
        if(password==123):
            self.Admin()
        elif(password==1234):
            self.Student()
        else:
            print("you enter a wrong password")
r=Login()
