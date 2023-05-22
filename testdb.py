import sqlite3
from sqlite3 import OperationalError
# connection=sqlite3.connect("hastext.db")
# cur=connection.cursor()
#
# # cur.execute("CREATE TABLE Persons (PersonID int, LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));")
# cur.execute("INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (100,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger');")
# connection.commit()

class database:

    def createdev(self):
        connection = sqlite3.connect("hastext.db")
        cur=connection.cursor()
        cmd="""CREATE TABLE IF NOT EXISTS Authdev (PersonID INTEGER PRIMARY KEY, 
        LastName varchar(255),UserName varchar(255),Phonenumber varchar(255),
        FirstName varchar(255),
        State varchar(40),City varchar(255),
        Password varchar(255),designation varchar(55),Email varchar(255),Pincode varchar(20),Aadharnumber varchar(16))"""
        try:
            cur.execute(cmd)
            connection.close()
            print("table AuthDev created")
            return True
        except:
            return False
    def Adddata(self,LastName,UserName,Phonenumber,FirstName,State, City,Password,designation,Email,Aadharn,Pcode):
            connection = sqlite3.connect("hastext.db")
            cur = connection.cursor()
            cmd=f"""INSERT INTO Authdev (LastName,UserName,Phonenumber, 
            FirstName,State, City,Password,designation,Email,Pincode,Aadharnumber
            ) VALUES ('{LastName}','{UserName}','{Phonenumber}', '{FirstName}','{State}','{City}','{Password}','{designation}','{Email}','{Pcode}','{Aadharn}');"""
            try:
                cur.execute(cmd)
                connection.commit()
                print(OperationalError)

                return True
            except:
                print(OperationalError)
                return False
    def showdata(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        # store=cur.fetchall()
        #show all data
        store=cur.execute("SELECT * from Authdev")

    def showdatacdash(self):
        #show data for client dashboard of saved jobs
            connection = sqlite3.connect("hastext.db")
            cur = connection.cursor()
            # store=cur.fetchall()
            # show all data
            store = cur.execute("SELECT * from job")
            return store


    def delalrecord(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd="DELETE FROM job"
        try:
            cur.execute(cmd)
            connection.close()
            return True
        except:
           return False


    def delrowrecod(self,username):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        del_row=f"delete from job where jobname='{username}';"
        cur.execute(del_row)
        return True
    def deletetable(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        del_table="DROP TABLE job"
        cur.execute(del_table)
        cur.close()
        return True
    def deletecol(self,colname):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"ALTER TABLE Auth2 DROP COLUMN {colname}"
        cur.execute(cmd)
        cur.close()
        return True
    def addcol(self,colname):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"ALTER TABLE job ADD {colname} varchar(150)"
        cur.execute(cmd)
        cur.close()
        return True
    def searchuser(self,uname):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"select Password from Authdev where UserName='{uname}'"
        try:
            t=cur.execute(cmd)

            return t
        except:
            return "False"

    def createjobinfo(self,clname):
        connection = sqlite3.connect("hastext.db")
        cur=connection.cursor()
        cmd=f"""CREATE TABLE IF NOT EXISTS {clname} (JobID INTEGER PRIMARY KEY,
        jobname varchar(40),JobCategory varchar(40),
        Message varchar(500),price integer,fprice integer)"""
        try:
            cur.execute(cmd)
            connection.close()

            print("table job created")
            return True
        except sqlite3.Error as error:
            print(format(error))

            return False
    def Adddatajob(self,jobname,Title,message,price):

            connection = sqlite3.connect("hastext.db")
            cur = connection.cursor()
            cmd=f"""INSERT INTO job (jobname,JobCategory,Message,price) VALUES ('{jobname}','{Title}','{message}','{price}');"""
            try:
                cur.execute(cmd)
                connection.commit()
                print("added")

                return True
            except  sqlite3.Error as error:
                print(format(error))

                return False

    def delbyid(self,jid):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        del_row = f"delete from job where JobID={jid};"
        try:
            cur.execute(del_row)
            connection.commit()
            return True
        except  sqlite3.Error as error:
            print(format(error))

            return False
    def searchbyid(self,jid):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        search_rec = f"select * from job where JobID={jid};"
        try:
            t=cur.execute(search_rec)
            return t
        except  sqlite3.Error as error:
            print(format(error))

            return False
    def searchfrpass(self,uname):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"select Email,Phonenumber from Authdev where UserName='{uname}'"
        try:
            t=cur.execute(cmd)

            return t
        except:
            return False


    def designation(self,username):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd = f"select designation from Authdev where UserName='{username}';"
        # f=cur.execute("select * from  Authdev")
        # for j in f:
        #     print(j)
        try:
            t = cur.execute(cmd)
            for i in t:
                print(i[0])
                return i[0]
        except  sqlite3.Error as error:
            print(format(error))
            return False
    def hitcountertable(self):
        connection = sqlite3.connect("hitcount.db")
        cur = connection.cursor()
        cmd="""CREATE TABLE IF NOT EXISTS hitcounter (hit_ID INTEGER PRIMARY KEY,hitcounts integer)"""
        try:
           cur.execute(cmd)
           return True
        except  sqlite3.Error as error:
                print(format(error))
                return False
    def hitcounter(self,counts):
        if self.hitcountertable():
            connection = sqlite3.connect("hitcount.db")
            cur = connection.cursor()
            cmd1=f"""insert into hitcounter(hitcounts) values({counts})"""
            cmd2 = f"""select hitcounts from hitcounter where hit_ID=1"""
            try:
                checkcounter=cur.execute(cmd2)
                tempnumber=0
                for i in checkcounter:
                    print(i)
                    tempnumber=i[0]
                print(tempnumber)
                if tempnumber >= counts:
                    cmd3=f"""UPDATE hitcounter SET hitcounts = {counts} WHERE hit_ID = 1;"""
                    try:
                        cur.execute(cmd3)
                        print("hitcount Values updated")
                        cur.execute("select * from hitcounter")
                        t = cur.fetchall()
                        for i in t:
                            print(i[1])
                    except  sqlite3.Error as error:
                        print(format(error))
                else:
                    try:
                        cur.execute(cmd1)
                        print("New Hitcount Inserted")
                        cur.execute("select * from hitcounter")
                        t=cur.fetchall()
                        for i in t:
                            print(i[1])
                    except  sqlite3.Error as error:
                        print(format(error))

            except  sqlite3.Error as error:
                print(format(error))


        else:
            print("Table Not created")
    def feedback(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd = """CREATE TABLE IF NOT EXISTS feedback (feedback_ID INTEGER PRIMARY KEY,Person_name varhcar(50),Person_email varhcar(100),Person_message varhcar(1000))"""
        try:
            cur.execute(cmd)
            return True
        except  sqlite3.Error as error:
            print(format(error))
            return False
    def feedbackadd(self,name,emails,mesg):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd=f"insert into feedback (Person_name,Person_email,Person_message) values('{name}','{emails}','{mesg}')"
        try:
            cur.execute(cmd)
            connection.commit()
            return True
        except  sqlite3.Error as error:
            print(format(error))
            return False

    def searchtable(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd =f"""SELECT name FROM sqlite_master WHERE type='table' """
        try:
          cur.execute(cmd)
          t=cur.fetchall()
          j=[]
          for i in t:
              print(i)
              j.append(i)
          return j
        except  sqlite3.Error as error:
            print(format(error))
            return False
    def createclusertable(self,clnames,jobname,Title,message,price):
        try:
            if self.createjobinfo(clnames):
                connection = sqlite3.connect("hastext.db")
                cur = connection.cursor()
                cmd=f"""INSERT INTO {clnames} (jobname,JobCategory,Message,price) VALUES ('{jobname}','{Title}','{message}','{price}');"""
                try:
                    cur.execute(cmd)
                    return True
                except  sqlite3.Error as error:
                    print(format(error))
                    return False
            else:
                return False
        except:
            print("Cannot Create table of the user")
            return False
    def createclaimedtable(self):
        connection = sqlite3.connect("hastext.db")
        cur = connection.cursor()
        cmd="""CREATE TABLE IF NOT EXISTS claimed(claim_ID INTEGER PRIMARY KEY,Person_name varhcar(50),price integer,Person_message varhcar(1000))"""
        flag=False
        try:
            cur.execute(cmd)
            flag=True
            return True
        except  sqlite3.Error as error:
            print(format(error))
            return False
    def insertclaims(self,username,price,message):
        if self.createclaimedtable():
            connection = sqlite3.connect("hastext.db")
            cur = connection.cursor()
            cmd=f"""INSERT INTO claimed (Person_name,price,Person_message) VALUES ('{username}','{price}','{message}');"""
            try:
                cur.execute(cmd)
                connection.commit()
                return True
            except  sqlite3.Error as error:
                print(format(error))
                return False
        else:
            return False
    def showclaims(self):
           connection = sqlite3.connect("hastext.db")
           cur = connection.cursor()
           cmd="""select Person_name,price from claimed"""
           try:
               cur.execute(cmd)
               t=cur.fetchall()
               return t
           except  sqlite3.Error as error:
               print(format(error))
               return False





















if __name__=="__main__":

   point=database()
   t=point.showclaims()
   for i in t:
       print(i)



