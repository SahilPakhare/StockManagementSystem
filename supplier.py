from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Stock Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        #===all variables

        self.var_searchBy=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
                                                    #self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()


                                                    #self.var_doj=StringVar()

                                                    #self.var_email=StringVar()
                                                    #self.var_dob=StringVar()
                                                    #self.var_pass=StringVar()
                                                    #self.var_utype=StringVar()
                                                    #self.var_salary=StringVar()

        #===self.root
        #self.root=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        #self.root.place(x=250,y=20,width=600,height=70) 

        #===options
        lbl_search=Label(self.root,text="Invoice no.",font=("goudy old style",15),bg="white") 
        lbl_search.place(x=700,y=80)  #,width=180
        #cmb_search.current(0)


        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("Georgia",12,"bold"),bg="green",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)
        
        #===title

        title=Label(self.root,text="Supplier Details",font=("Georgia",18,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)




        #===content
        #===row1

        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=80)
        #lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        #lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=180)
        #cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","other"),state='readonly',justify=CENTER,font=("goudy old style",15)) 
        #cmb_gender.place(x=500,y=150,width=180)
        #cmb_gender.current(0)

        #txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

        #===row2

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        #lbl_dob=Label(self.root,text="DOB",font=("goudy old style",15),bg="white").place(x=350,y=190)
        #lbl_doj=Label(self.root,text="DOJ",font=("goudy old style",15),bg="white").place(x=750,y=190)



        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=120,width=180)
        #txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        #txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)


        #===row3

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        #lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        #lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=160,width=180)
        #txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        #cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15)) 
        #cmb_utype.place(x=850,y=230,width=180)
        #cmb_utype.current(0)



        #===row4

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
        #lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)

        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=200,width=470,height=120)
        #txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
 
        #===Buttons

        btn_add=Button(self.root,text="Save",command=self.add,font=("Georgia",12,"bold"),bg="brown",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Georgia",12,"bold"),bg="blue",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Georgia",12,"bold"),bg="green",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Georgia",12,"bold"),bg="maroon",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

        #===Employee Details

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=140,width=380,height=350)


        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)


        self.supplierTable.heading("invoice",text="Invoice No")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        #self.supplierTable.heading("contact",text="Contact")
        #self.supplierTable.heading("dob",text="DOB")
        #self.supplierTable.heading("doj",text="DOJ")
        #self.supplierTable.heading("pass",text="Password")
        #self.supplierTable.heading("utype",text="User Type")
        #self.supplierTable.heading("address",text="Address")
        #self.supplierTable.heading("salary",text="Salary")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100) 
        self.supplierTable.column("desc",width=100) 
        #self.supplierTable.column("contact",width=100) 
        #self.supplierTable.column("dob",width=100) 
        #self.supplierTable.column("doj",width=100) 
        #self.supplierTable.column("pass",width=100) 
        #self.supplierTable.column("utype",width=100) 
        #self.supplierTable.column("address",width=100) 
        #self.supplierTable.column("salary",width=100) 
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        #===button working
    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:

            if self.var_sup_invoice.get()=="": #or self.var_name.get()=="":
                messagebox.showerror("Error","Invoice must be requrired",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","Invoice no. already assigned,try different",parent=self.root)

                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?) ",(
                                            self.var_sup_invoice.get(),
                                            self.var_name.get(),
                                            self.var_contact.get(),
                                            #self.var_desc.get(),
                                            #self.var_contact.get(),

                                            #self.var_dob.get(),
                                            #self.var_doj.get(),
                                            
                                            #self.var_pass.get(),
                                            #self.var_utype.get(),
                                            self.txt_desc.get('1.0',END),
                                            #self.var_salary.get()
                     ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)




        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
         f=self.supplierTable.focus()
         content=(self.supplierTable.item(f))
         row=content['values']
        #print (row)
         self.var_sup_invoice.set(row[0])    #index starting from zero
         self.var_name.set(row[1])
         #self.var_email.set(row[2])
         #self.var_gender.set(row[3])
         self.var_contact.set(row[4])
         #self.var_dob.set(row[5])
         #self.var_doj.set(row[6])
         #self.var_pass.set(row[7])
         #self.var_utype.set(row[8])
         self.txt_desc.delete('1.0',END)
         self.txt_desc.insert(END,row[9])
         #self.var_salary.set(row[10])


    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(
                                   
                                        
                                        
                                        self.var_name.get(),
                                        #self.var_email.get(),
                                        #self.var_gender.get(),
                                        self.var_contact.get(),
                                        
                                        #self.var_dob.get(),
                                        #self.var_doj.get(),
                                        
                                        #self.var_pass.get(),
                                        #self.var_utype.get(),
                                        self.txt_desc.get('1.0',END),
                                        #self.var_salary.get(),
                                        self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice no.",parent=self.root)
                else:
                    cr=messagebox.askyesno("Conform","Do you really want to delete?",parent=self.root)
                    if cr==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.show()





        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    
    def clear(self):
         self.var_sup_invoice.set("")
         self.var_name.set("")
         #self.var_email.set("")
         #self.var_gender.set("Select")
         self.var_contact.set("")
         #self.var_dob.set("")
         #self.var_doj.set("")
         #self.var_pass.set("")
         #self.var_utype.set("Admin")
         self.txt_desc.delete('1.0',END)
         #self.var_salary.set("")
         self.var_searchtxt.set("")
         #self.var_searchBy.set("select")
         self.show()



    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            #if self.var_searchBy.get()=="Select":
                #messagebox.showerror("Error","Select Search by option",parent=self.root)
            if self.var_searchtxt.get()=="":
                 messagebox.showerror("Error","Invoice no. should be required",parent=self.root)

            else:
                 cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    #for row in rows:
                    self.supplierTable.insert('',END,values=row)
                 else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            self.var_sup_invoice.set("")




if __name__==" __main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()
