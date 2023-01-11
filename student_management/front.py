import back 
import tkinter
from tkinter import *
import tkinter.messagebox


class Student:


    def __init__(self, root):
        self.root = root
        self.root.title("student information management system")
        self.root.geometry(newGeometry="1350x750+0+0")
        self.root.config(bg="sky blue")

        Stdid = StringVar()
        Name = StringVar()
        Gender = StringVar()
        Age = StringVar()
        DoB = StringVar()
        Class = StringVar()
        Enroll = StringVar()

        #####################################functions################################################################
        def iExit():
              iExit=tkinter.messagebox.askyesno("Student information system","confirm if you want to exit")
              if iExit>0:
                     root.destroy()
                     return

        def clearData():
              self.txtStdid.delete(0,END)
              self.txtName.delete(0,END)
              self.txtGender.delete(0,END)
              self.txtAge.delete(0,END)
              self.txtDoB.delete(0,END)
              self.txtClass.delete(0,END)
              self.txtEnroll.delete(0,END)

        back.studentData()
        def addData():
              if(len(Stdid.get())!=0):
                     
                     back.addStdRec(Stdid.get(),Name.get(),Gender.get(),Age.get(),DoB.get(),Class.get(),Enroll.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(Stdid.get(),Name.get(),Gender.get(),Age.get(),DoB.get(),Class.get(),Enroll.get()))

        def DisplayData():
              studentlist.delete(0,END)
              for row in back.viewData():
                  studentlist.insert(END,row)
              
        def searchDatabase():
              studentlist.delete(0,END)
              for rows in back.searchData(Stdid.get(),Name.get(),Gender.get(),Age.get(),DoB.get(),Class.get(),Enroll.get()):
                     studentlist.insert(END,rows,str(""))   

        def StudentRec(Event):
              
              global sd
              
              sd = studentlist.get(studentlist.curselection()[0])
              
              self.txtStdid.delete(0,END)
              self.txtStdid.insert(END,sd[0])
              self.txtName.delete(0,END)
              self.txtName.insert(END,sd[1])
              self.txtGender.delete(0,END)
              self.txtGender.insert(END,sd[2])
              self.txtAge.delete(0,END)
              self.txtAge.insert(END,sd[3])
              self.txtDoB.delete(0,END)
              self.txtDoB.insert(END,sd[4])
              self.txtClass.delete(0,END)
              self.txtClass.insert(END,sd[5])
              self.txtEnroll.delete(0,END)
              self.txtEnroll.insert(END,sd[6])
              

        def DeleteData():
              
              if(len(Stdid.get())!=0):
                     back.deleteRec(Stdid.get())
                     clearData()
                     DisplayData()             
       
        def update():
             
             if(len(Stdid.get())!=0):
                     back.dataUpdate(Stdid.get(),Name.get(),Gender.get(),Age.get(),DoB.get(),Class.get(),Enroll.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(Stdid.get(),Name.get(),Gender.get(),Age.get(),DoB.get(),Class.get(),Enroll.get()))
             
        
        def CountData():
              studentlist.delete(0,END)
              for stats in back.dataStats():
                  studentlist.insert(END,stats)          
        #####################################FRAMES###################################################################
        MainFrame = Frame(self.root, bg="sky blue")
        MainFrame.grid()  # THIS IS MAIN FRAME OUR WINDOW
        TitFrame = Frame(MainFrame, bd=1, padx=54, pady=8, bg="red", relief=RIDGE)
        TitFrame.pack(side=TOP)  # THIS IS TITLE FRAME

        self.lblTit = Label(TitFrame, font=('arial', 35, 'bold'), text="Students information Management System" , bg="red", fg="black")
        self.lblTit.grid()

        self.lblTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Zhejiang university of science and technology", bg="red", fg="black")
        self.lblTit.grid()

        self.lblTit = Label(TitFrame, font=('Lucida Calligraphy', 15, 'bold'), text="developed by Francis", bg="red", fg="black")
        self.lblTit.grid()


        ButtonFrame = Frame(MainFrame, bd=1, width=1000, height=70, padx=18, pady=10, bg="grey", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)  #

        DataFrame = Frame(MainFrame, bd=9, width=1300, height=550, padx=20, pady=20, bg="#555", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)  # THIS IS STI

        DataFrameLeft = LabelFrame(DataFrame, font=('arial', 12, 'bold'), bd=1, width=450, height=600, bg="Ghost White",
                                   relief=RIDGE, text="STUDENT INFO\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, font=('arial', 12, 'bold'), bd=1, width=450, height=400,
                                    bg="Ghost White", relief=RIDGE, text="STUDENT DETAILS\n")
        DataFrameRight.pack(side=RIGHT)
        
#########################################################Lables and entry widget #######################################################################
        self.lblStdid=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="student Id:",bg="ghost white") 
        self.lblStdid.grid(row=0,column=0,sticky=W)
       
        self.txtStdid=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Stdid,bg="ghost white",width=39)
        self.txtStdid.grid(row=0,column=1)#student id

        self.lblName=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Name:",bg="ghost white")
        self.lblName.grid(row=1,column=0,sticky=W)
       
        self.txtName=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Name,bg="ghost white",width=39)
        self.txtName.grid(row=1,column=1)#Name
       

        self.lblGender=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Gender:",bg="ghost white")
        self.lblGender.grid(row=2,column=0,sticky=W)
       
        self.txtGender=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Gender,bg="ghost white",width=39)
        self.txtGender.grid(row=2,column=1)#gender

        self.lblAge=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Age:",bg="ghost white")
        self.lblAge.grid(row=3,column=0,sticky=W)
       
        self.txtAge=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Age,bg="ghost white",width=39)
        self.txtAge.grid(row=3,column=1)#Age
       
        self.lblDoB=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Date of birth:",bg="ghost white")
        self.lblDoB.grid(row=4,column=0,sticky=W)
       
        self.txtDoB=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=DoB,bg="ghost white",width=39)
        self.txtDoB.grid(row=4,column=1)#date of birth 
 
        self.lblClass=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Class:",bg="ghost white")
        self.lblClass.grid(row=5,column=0,sticky=W)
       
        self.txtClass=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Class,bg="ghost white",width=39)
        self.txtClass.grid(row=5,column=1)#class

        self.lblEnroll=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Enrolled Date:",bg="ghost white")
        self.lblEnroll.grid(row=6,column=0,sticky=W)
       
        self.txtEnroll=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Enroll,bg="ghost white",width=39)
        self.txtEnroll.grid(row=6,column=1)#Enroll

        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0 ,column=1,sticky='ns')#scroll bar

        studentlist=Listbox(DataFrameRight,width=68,height=12,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=10)
        scrollbar.config(command= studentlist.yview)

        #######################################Button Widget####################################################
        self.btnAddData=Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=addData)
        self.btnAddData.grid(row=0,column=0)#ADD NEW

        self.btnDisplay=Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayData)
        self.btnDisplay.grid(row=0,column=1)#DISPLAY

        self.btnClear=Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=clearData)
        self.btnClear.grid(row=0,column=2)#CLEAR

        self.btnDelete=Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DeleteData)
        self.btnDelete.grid(row=0,column=3)#DELETE

        self.btnSearch=Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=searchDatabase)
        self.btnSearch.grid(row=0,column=4)#SEARCH

        self.btnUpdate=Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=update)
        self.btnUpdate.grid(row=0,column=5)#UPDATE

        self.btnCount=Button(ButtonFrame,text="Count",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=CountData)
        self.btnCount.grid(row=0,column=6)#Count

        self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555", command=iExit)
        self.btnExit.grid(row=1,column=3)#Exit

if __name__=='__main__':
   root= tkinter.Tk()#CREATE AN OBJECT
   application=Student(root)#PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
   root.mainloop()
