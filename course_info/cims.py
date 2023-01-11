from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import mysql.connector


class Course:
    def __init__(self, root):
        self.root = root
        self.root.title("Course information management system")
        self.root.geometry(newGeometry="1350x750+0+0")
        self.root.config(bg="maroon")
      
        TitFrame = Frame(self.root, bd=1, bg="olive", relief=RIDGE)
        TitFrame.pack(side=TOP,fill=X)  # THIS IS TITLE FRAME
        ### variables
        self.course_id_var = StringVar()
        self.course_code_var = StringVar()
        self.course_name_var = StringVar()
        self.credit_var = StringVar()
        self.semester_id_var = StringVar()
        self.semester_var = StringVar()
        self.time_var = StringVar()
      
        #
        self.Title=Label(TitFrame,text="Course information management system",font=("Script MT Bold",40,"bold"),fg="black",bg="olive")
        self.Title.pack(side=TOP,fill=X)  


        
        self.lblTit = Label(TitFrame, font=('Lucida Calligraphy', 20, 'bold'), text="Zhejiang university of science and technology", bg="olive", fg="black")
        self.lblTit.pack()

        self.lblTit = Label(TitFrame, font=('Lucida Calligraphy', 15, 'bold'), text="(computer science department first year)", bg="olive", fg="black")
        self.lblTit.pack()

        ButtonFrame = Frame(self.root, bd=4, bg="olive", relief=RIDGE)
        ButtonFrame.place(width=500, height=570, x=10, y=160)  

        detailsFrame = Frame(self.root, bd=4, bg="olive", relief=RIDGE)
        detailsFrame.place(width=820, height=570, x=520, y=160)

        m_detailslbl = Label(ButtonFrame,text="manage courses", bd=4,fg="ghost white", bg="olive", font=('arial', 20,'bold'))
        m_detailslbl.grid(row=0,columnspan=2,pady=10)

       # lbl_id = Label(ButtonFrame,text="Course Id.",fg="ghost white", bg="olive", font=('arial', 15,'bold'))
       # lbl_id.grid(row=1,column=0,padx=10,pady=10)

       # txt_id = Entry(ButtonFrame,textvariable=self.course_id_var, bd=4,bg="ghost white", font=('arial', 15,'bold'),relief=GROOVE)
       # txt_id.grid(row=1,column=1,padx=10,pady=10,sticky="W")

        lbl_ccode = Label(ButtonFrame,text="Course Code",fg="ghost white", bg="olive", font=('arial', 15,'bold'))
        lbl_ccode.grid(row=1,column=0,padx=10,pady=10)

        txt_ccode = Entry(ButtonFrame,textvariable=self.course_code_var, bd=4,bg="ghost white", font=('arial', 15,'bold'),relief=GROOVE)
        txt_ccode.grid(row=1,column=1,padx=10,pady=10,sticky="W") 
        
        lbl_cname = Label(ButtonFrame,text="Course Name",fg="ghost white", bg="olive", font=('arial', 15,'bold'))
        lbl_cname.grid(row=2,column=0,padx=10,pady=10)

        txt_cname = Entry(ButtonFrame,textvariable= self.course_name_var, bd=4,bg="ghost white", font=('arial', 15,'bold'),relief=GROOVE)
        txt_cname.grid(row=2,column=1,padx=10,pady=10,sticky="W")

        lbl_ccredit = Label(ButtonFrame,text="Credit",fg="ghost white", bg="olive", font=('arial', 15,'bold'))
        lbl_ccredit.grid(row=3,column=0,padx=10,pady=10)

        combo_credit = ttk.Combobox(ButtonFrame,textvariable=self.credit_var,font=('arial', 13,'bold'),state='readonly')
        combo_credit['values']=(1,2,3,4,5,6)
        combo_credit.grid(row=3,column=1,padx=10,pady=10)
        
        lbl_semester = Label(ButtonFrame,text="Semester",fg="ghost white", bg="olive", font=('arial', 15,'bold'))
        lbl_semester.grid(row=4,column=0,padx=10,pady=10)

        combo_semester = ttk.Combobox(ButtonFrame,textvariable=self.semester_var,font=('arial', 13,'bold'),state='readonly')
        combo_semester['values']=("first","second")
        combo_semester.grid(row=4,column=1,padx=10,pady=10)

        lbl_time = Label(ButtonFrame,text="Time",fg="ghost white", bg="olive", font=('arial', 15,'bold'))
        lbl_time.grid(row=5,column=0,padx=10,pady=10)

        txt_time = Entry(ButtonFrame,textvariable=self.time_var, bd=4,bg="ghost white", font=('arial', 15,'bold'),relief=GROOVE)
        txt_time.grid(row=5,column=1,padx=10,pady=10,sticky="W")

        ButFrame = Frame(ButtonFrame, bd=4, bg="olive", relief=RIDGE)
        ButFrame.place(x=10,y=450, width=480)

        btnAdd=Button(ButFrame,text="Add",font=('arial',15,'bold'),width=8,fg="#555",command=self.addcourse).grid(row=0,column=0,padx=5,pady=5)
        btnModify=Button(ButFrame,text="Modify",font=('arial',15,'bold'),width=8,fg="#555",command=self.updatedata).grid(row=0,column=1,padx=5,pady=5)
        btnDelete=Button(ButFrame,text="Delete",font=('arial',15,'bold'),width=8,fg="#555",command=self.deletedata).grid(row=0,column=2,padx=5,pady=5)
        btnClear=Button(ButFrame,text="Clear",font=('arial',15,'bold'),width=8,fg="#555",command=self.clearData).grid(row=0,column=3,padx=5,pady=5)
        btnsearch=Button(detailsFrame,text="Search",font=('arial',15,'bold'),width=10,fg="#555",command=self.searchdata).grid(row=0,column=0,padx=5,pady=5)
        btncount=Button(detailsFrame,text="Count",font=('arial',15,'bold'),width=10,fg="#555",command=self.countdata).grid(row=0,column=1,padx=5,pady=5)
        btnshow=Button(detailsFrame,text="Show All",font=('arial',15,'bold'),width=10,fg="#555",command=self.fetchdata).grid(row=0,column=2,padx=5,pady=5)

        tableFrame = Frame(detailsFrame, bd=10, bg="white", relief=RIDGE)
        tableFrame.place(width=780, height=480, x=10, y=70) 

        scrollx=Scrollbar(tableFrame,orient=HORIZONTAL)
        scrolly=Scrollbar(tableFrame,orient=VERTICAL)
        self.Course_table=ttk.Treeview(tableFrame,columns=("ccode","cname","ccredit","semester","time"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Course_table.xview)
        scrolly.config(command=self.Course_table.yview)

        #Course_table.heading("id",text="Course Id.")
        self.Course_table.heading("ccode",text="Course Code")
        self.Course_table.heading("cname",text="Course Name")
        self.Course_table.heading("ccredit",text="Credit")
        self.Course_table.heading("semester",text="Semester")
        self.Course_table.heading("time",text="Time")
        self.Course_table['show']='headings'
       # Course_table.column("id",width=100)
        self.Course_table.column("ccode",width=100)
        self.Course_table.column("cname",width=100)
        self.Course_table.column("ccredit",width=100)
        self.Course_table.column("semester",width=100)
        self.Course_table.column("time",width=100)
        self.Course_table.pack(fill=BOTH,expand=1)
        self.fetchdata()
        self.Course_table.bind("<ButtonRelease-1>",self.get_cursor)

    def addcourse(self):
           con = mysql.connector.connect(host="localhost", user="root", password="", database="course_management")
           cur = con.cursor()
           
           cur.execute("insert into course_info values(%s,%s,%s,%s,%s)",(self.course_code_var.get(),
                                                                        self.course_name_var.get(),
                                                                        self.credit_var.get(),
                                                                        self.semester_var.get(),
                                                                        self.time_var.get()
                                                                      ))  

          
           con.commit()
           self.fetchdata()
           self.clearData()
           con.close()

    def fetchdata(self):
           con = mysql.connector.connect(host="localhost", user="root", password="", database="course_management")
           cur = con.cursor()
           cur.execute("select * from course_info")                  
           rows = cur.fetchall()
           if len(rows)!=0:
               self.Course_table.delete(*self.Course_table.get_children())
               for row in rows:
                     self.Course_table.insert('',END,values=row)
                   
               con.commit()
           con.close()   

    def clearData(self):
        self.course_code_var.set("")
        self.course_name_var.set("")
        self.credit_var.set("")
        self.semester_var.set("")
        self.time_var.set("")

    def get_cursor(self,ev):    
        cursor_row=self.Course_table.focus()
        contents=self.Course_table.item(cursor_row)
        row=contents['values']
        self.course_code_var.set(row[0])
        self.course_name_var.set(row[1])
        self.credit_var.set(row[2])
        self.semester_var.set(row[3])
        self.time_var.set(row[4])

    def updatedata(self):
           con = mysql.connector.connect(host="localhost", user="root", password="", database="course_management")
           cur = con.cursor()
           cur.execute("UPDATE course_info set course_name=%s,credit=%s,semester=%s,time=%s WHERE \
               course_code=%s",(self.course_name_var.get(),self.credit_var.get(),self.semester_var.get(),self.time_var.get(),self.course_code_var.get()))  
                                                                                                                                                                                                                                                                            
           con.commit()
           self.fetchdata()
           self.clearData()
           con.close()   

    def deletedata(self):
           con = mysql.connector.connect(host="localhost", user="root", password="", database="course_management")
           cur = con.cursor()
           cur.execute("""DELETE FROM course_info WHERE course_code= %s""", (self.course_code_var.get(),))
                                                                                                                                                                                                                                                                            
           con.commit()
           con.close()  
           self.fetchdata()
           self.clearData()     


    def searchdata(self):
           con = mysql.connector.connect(host="localhost", user="root", password="", database="course_management")
           cur = con.cursor()
           cur.execute("SELECT * FROM course_info WHERE course_code=%s OR course_name=%s OR credit=%s OR semester=%s OR time=%s",(self.course_code_var.get(),
                                                                        self.course_name_var.get(),
                                                                        self.credit_var.get(),
                                                                        self.semester_var.get(),
                                                                        self.time_var.get()
                                                                      ))                  
           rows = cur.fetchall()
           if len(rows)!=0:
               self.Course_table.delete(*self.Course_table.get_children())
               for row in rows:
                     self.Course_table.insert('',END,values=row)
                   
               con.commit()
           con.close()   
    
    def countdata(self):
           con = mysql.connector.connect(host="localhost", user="root", password="", database="course_management")
           cur = con.cursor()
           cur.execute("SELECT credit,COUNT(*) as count FROM course_info  WHERE credit <4 GROUP BY credit")
           rows = cur.fetchall()
           if len(rows)!=0:
               self.Course_table.delete(*self.Course_table.get_children())
               for row in rows:
                     self.Course_table.insert('',END,values=row)
                   
               con.commit()
           con.close()  

if __name__=='__main__':
   root= tkinter.Tk()#CREATE AN OBJECT
   ob=Course(root)#PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
   root.mainloop()
