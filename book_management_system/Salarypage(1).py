from tkinter import *
import time
import random
import datetime
import tkinter.messagebox
import database(1)

payroll = Tk()
payroll.geometry("1000x650")
payroll.title("Salary Management Systems")
payroll.resizable(0, 0)

# ==============================================FRAMES=======================================

Tops = Frame(payroll, width=1000, height=15)
Tops.pack(side=TOP)

BF = Frame(payroll, width=15, height=30)
BF.pack(side=LEFT)
BF.pack(side=BOTTOM)

LF = Frame(payroll, width=700, height=600, bd=12)
LF.pack(side=LEFT)

RF = Frame(payroll, width=825, height=600, bd=1)
RF.pack (side=RIGHT)

# ==================

lblTitle = Label(Tops, font=('arial', 30, 'bold'), text="BOOK INFORMATION MANAGEMENT SYSTEM", fg="Steel blue", bd=1, anchor="w")
lblTitle.grid(row=0, column=0)

# ==================




# ==================


#  ===========================================FUNCTIONS ===========================

def emprec(event):
    global ed
    searchrec = emplist.curselection()[0]
    ed = emplist.get(searchrec)

    txtbkid.delete(0, END)
    txtbkid.insert(END, ed[1])
    txtbkname.delete(0, END)
    txtbkname.insert(END, ed[2])
    txtisbn.delete(0, END)
    txtisbn.insert(END, ed[3])
    txtauth.delete(0, END)
    txtauth.insert(END, ed[4])
    txtPrice.delete(0, END)
    txtPrice.insert(END, ed[5])
    txtPress.delete(0, END)
    txtPress.insert(END, ed[6])
    txtdate.delete(0, END)
    txtdate.insert(END, ed[7])








def iExit():
    iExit = tkinter.messagebox.askyesno("Book Information management System", "Confirm you want to exit")
    if iExit > 0:
        payroll.destroy()
        return


def addData():
    if len(bookname.get()) != 0:
        database.addbkrec(bookid.get(), bookname.get(), ISBN.get(), price.get(), press.get(), date.get() )
        emplist.delete(0, END)
        emplist.insert(END, (bookid.get(), bookname.get(), ISBN.get(), price.get(), press.get(), date.get()))


def Disdata():
    emplist.delete(0, END)
    for row in database.viewdata():
        emplist.insert(END, row, str(""))


def deletedata():
    if (len(bookname.get()) != 0):
        database.Delete(ed[0])
        reset()
        Disdata()


def SearchData():
    emplist.delete(0, END)
    for row in database.Searchrec(bookid.get(), bookname.get(), ISBN.get(), price.get(), press.get(), date.get()):
        emplist.insert(END, row, str(""))


def update():

    if (len(bookid.get()) != 0):
        database.Delete(ed[0])
    if (len(bookid.get()) != 0):
        database.addbkrec(bookid.get(), bookname.get(), ISBN.get(), price.get(), press.get(), date.get())


        emplist.delete(0, END)

        emplist.insert(END,bookid.get(), bookname.get(), ISBN.get(), price.get(), press.get(), date.get())


def reset():
    bookid .set("")
    bookname.set("")
    ISBN .set("")
    price .set("")
    author .set("")
    press.set("")
    date.set("")

    bookname.set("")





#  ===========================================LISTBOX AND SCROLLBAR ===========================
Scrollbar = Scrollbar(BF)
Scrollbar.grid(row=0, column=1, sticky='ns')

emplist = Listbox(BF, width=100, height=13, font=('arial', 12, 'bold'), yscrollcommand=Scrollbar.set)
emplist.bind('<<ListboxSelect>>', emprec)
emplist.grid(row=0, column=0, padx=8)
Scrollbar.config(command=emplist.yview())

bookid = StringVar()
bookname = StringVar()
author = StringVar()
ISBN = StringVar()
author= StringVar()
price = StringVar()
press = StringVar()
date = StringVar()



# ==================Left Side

lblbkid = Label(LF, font=('arial', 12, 'bold'), text="Book ID", fg="Steel blue", bd=10, anchor="w")
lblbkid.grid(row=0, column=0)
txtbkid = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                   textvariable=bookid, relief="solid")
txtbkid.grid(row=0, column=1)

lblbkname = Label(LF, font=('arial', 12, 'bold'), text="Book Name", fg="Steel blue", bd=10, anchor="w")
lblbkname.grid(row=1, column=0)
txtbkname = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                        textvariable=bookname, relief="solid")
txtbkname.grid(row=1, column=1)

lblisbn = Label(LF, font=('arial', 12, 'bold'), text="ISBN", fg="Steel blue", bd=10, anchor="w")
lblisbn .grid(row=2, column=0)
txtisbn  = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                     textvariable=ISBN, relief="solid")
txtisbn .grid(row=2, column=1)

lblauth = Label(LF, font=('arial', 12, 'bold'), text="Author", fg="Steel blue", bd=10, anchor="w")
lblauth.grid(row=3, column=0)
txtauth = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                 textvariable= author , relief="solid")
txtauth.grid(row=3, column=1)


lblPrice = Label(LF, font=('arial', 12, 'bold'), text="Price", fg="Steel blue", bd=10, anchor="w")
lblPrice.grid(row=4, column=0)
txtPrice = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                textvariable=price, relief="solid")
txtPrice.grid(row=4, column=1)


lblPress = Label(LF, font=('arial', 12, 'bold'), text="Press", fg="Steel blue", bd=10, anchor="w")
lblPress.grid(row=5, column=0)
txtPress = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                    textvariable=press, relief="solid")
txtPress.grid(row=5, column=1)

lbldate = Label(LF, font=('arial', 12, 'bold'), text="Date", fg="Steel blue", bd=10, anchor="w")
lbldate.grid(row=6, column=0)
txtdate = Entry(LF, font=('arial', 12, 'bold'), bd=1, width=54, bg="powder blue", justify="left",
                 textvariable=date, relief="solid")
txtdate.grid(row=6, column=1)




# ----------------------
btnSalaryPayment = Button(RF, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=20,
                          text="Salary Paymant", bg="sky blue", command=addData).grid(row=0, column=0)

btnReset = Button(RF, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=20,
                  text="Reset System", bg="sky blue", command=reset).grid(row=1, column=0)

btnDisplay = Button(RF, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=20,
                    text="Display", bg="sky blue", command=Disdata).grid(row=2, column=0)

btnUpdate = Button(RF, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=20,
                   text="Update", bg="sky blue", command=update).grid(row=3, column=0)

btnDelete = Button(RF, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=20,
                   text="Delete", bg="sky blue", command=deletedata).grid(row=4, column=0)

btnExit = Button(RF, padx=8, pady=8, fg="black", font=('arial', 12, 'bold'), width=20,
                 text="Exit", bg="sky blue", command=iExit).grid(row=4, column=0)

payroll.mainloop()
