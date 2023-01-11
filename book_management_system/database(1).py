import sqlite3


def database():
    con = sqlite3.connect("bookinfo.db")
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS bookmanage(ISBN INTEGER NOT NULL PRIMARY KEY, bookname TEXT \
        author	TEXT, price	VARCHAR,press TEXT,date	VARCHAR)")
    con.commit()
    con.close()


def addbkrec(ISBN, bookname, author, price, press, date):
    con = sqlite3.connect("bookinfo.db")
    cur = con.cursor()
    cur.execute("INSERT INTO bookmanage VALUES (?,?,?,?,?,?)", (ISBN, bookname, author, price, press, date))
    con.commit()
    con.close()


def viewdata():
    con = sqlite3.connect("bookinfo.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM bookmanage")
    rows = cur.fetchall()
    con.close()
    return rows


def Delete(ISBN):
    con = sqlite3.connect("bookinfo.db")
    cur = con.cursor()
    cur.execute("DELETE FROM bookmanage WHERE ISBN=?", (ISBN,))
    con.commit()
    con.close()


def Searchrec(ISBN="", bookname="", author="", price="",  press="",  date=""):
    con = sqlite3.connect("bookinfo.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM bookmanage WHERE ISBN=? OR bookname=? OR author=? OR price=? OR  press=? OR\
                 date=?", (ISBN,  bookname, author, price, press, date))
    rows = cur.fetchall()
    con.close()
    return rows


def UpdateData(ISBN, bookname, author, price, press, date):
    con = sqlite3.connect("bookinfo.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE bookmanage SET  bookname=?,author=?, price=? ,  press=?, date=?  WHERE ISBN=?",
        (bookname, author, price, press, date, ISBN))
    con.commit()
    con.close()
