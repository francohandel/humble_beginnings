import mysql.connector

def studentData():
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="studentinfo")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS Student(Stdid INTEGER PRIMARY KEY, \
        Name text,Gender text,Age text,DoB text,Class text,Enroll text)")
    con.commit()
    con.close()


def addStdRec(Stdid,Name,Gender,Age,DoB,Class,Enroll):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="", database="studentinfo")
    cur = con.cursor()
    cur.execute("INSERT INTO Student VALUES(%s,%s,%s,%s,%s,%s,%s)",(Stdid,Name,Gender,Age,DoB,Class,Enroll))
    con.commit()
    con.close()


def viewData():
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="", database="studentinfo")
    cur = con.cursor()
    cur.execute("select Name,Age from Student")
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(Stdid):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="", database="studentinfo")
    cur = con.cursor()
    cur.execute("DELETE FROM Student WHERE Stdid=%s", (Stdid,))
    con.commit()
    con.close()


def searchData(Stdid,Name,Gender,Age,DoB,Class,Enroll):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="", database="studentinfo")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM Student WHERE Stdid=%s OR Name=%s OR Gender=%s OR Age=%s OR DoB=%s \
         OR Class=%s OR Enroll=%s",
        (Stdid,Name,Gender,Age,DoB,Class,Enroll))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(Stdid,Name,Gender,Age,DoB,Class,Enroll):
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="studentinfo")
    cur = con.cursor()
    cur.execute(
        "UPDATE Student SET Name=%s,Gender=%s,Age=%s,DoB=%s,Class=%s,Enroll=%s WHERE Stdid=%s",(Name,Gender,Age,DoB,Class,Enroll,Stdid))
   
    con.commit()
    con.close()
    

def dataStats():
    con = con = mysql.connector.connect(host="localhost", user="root",passwd="", database="studentinfo")
    cur = con.cursor()
    cur.execute("SELECT Gender,COUNT(*) as count FROM Student GROUP BY Gender")
    stats = cur.fetchall()
    con.close()
    return stats
