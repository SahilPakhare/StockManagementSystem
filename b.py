from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Stock Management System")
        self.root.config(bg="white")
        self.cart_list=[]

        #===title==
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Stock Management System",image=self.icon_title,compound=LEFT,font=("Georgia",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===BTN_Logout===
        btn_logout=Button(self.root,text="Log out",font=("Georgia",15,"bold"),bg="white",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #===clock==
        self.lbl_clock=Label(self.root,text="Welcome to Stock Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("Georgia",15,"bold"),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===product_Frame===

       
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("Georgia",15,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        #===Product Search  Frame===
        self.var_search=StringVar()
       
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)


        lbl_search=Label(ProductFrame2,text="Search roduct | By Name",font=("Georgia",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_name=Label(ProductFrame2,text="Product Name",font=("Georgia",15,"bold"),bg="white").place(x=5,y=45)

        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("Georgia",15),bg="lightyellow").place(x=160,y=45,width=120,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("Georgia",13,"bold"),bg="blue",fg="white",cursor="hand2").place(x=285,y=45,width=90,height=20)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("Georgia",13,"bold"),bg="black",fg="white",cursor="hand2").place(x=285,y=10,width=90,height=20)

        
        #===Product Details Frame====

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)


        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)


        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="QTY")
        self.product_table.heading("status",text="Status")

        self.product_table["show"]="headings"

        self.product_table.column("pid",width=35)
        self.product_table.column("name",width=80)
        self.product_table.column("price",width=80) 
        self.product_table.column("qty",width=40)
        self.product_table.column("status",width=50) 
 
      
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="NOTE:Enter 0 Quantity to remove product from the Cart",font=("Georgia",9,"bold"),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)


        #====Customer Frame=====

        self.var_cname=StringVar()
        self.var_contact=StringVar()


        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)


        cTitle=Label(CustomerFrame,text="Customer Details",font=("Georgia",15,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("Georgia",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("Georgia",13),bg="lightyellow").place(x=80,y=35,width=150)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("Georgia",15),bg="white").place(x=250,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("Georgia",13),bg="lightyellow").place(x=360,y=35,width=150)
        
         #===Cal cart Frame===
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

         #===Calculator Frame===
        self.var_cal_input=StringVar()
        #self.var_get_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=8,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)


        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=("arial",15,"bold"),command=lambda:self.get_input('7'),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=("arial",15,"bold"),command=lambda:self.get_input('8'),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=("arial",15,"bold"),command=lambda:self.get_input('9'),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=11,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=("arial",15,"bold"),command=lambda:self.get_input('4'),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=("arial",15,"bold"),command=lambda:self.get_input('5'),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=("arial",15,"bold"),command=lambda:self.get_input('6'),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=11,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text='1',font=("arial",15,"bold"),command=lambda:self.get_input('1'),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=("arial",15,"bold"),command=lambda:self.get_input('2'),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=("arial",15,"bold"),command=lambda:self.get_input('3'),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=11,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text='0',font=("arial",15,"bold"),command=lambda:self.get_input('0'),bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='C',font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=1)
        btn_equal=Button(Cal_Frame,text='=',font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=3)


        #===Cart Frame===
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)

        cartTitle=Label(Cart_Frame,text="Cart   Total Product:[0]",font=("Georgia",13,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)

        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)


        self.CartTable.heading("pid",text="P ID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        self.CartTable.heading("status",text="Status")

        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90) 
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=90) 
 
      
        self.CartTable.pack(fill=BOTH,expand=1)


        #===Add Cart Widgets Frame===
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_Cart_WidgetsFrame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Add_Cart_WidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_Cart_WidgetsFrame,text="Product Name",font=("Georgia",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_Cart_WidgetsFrame,textvariable=self.var_pname,font=("Georgia",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_Cart_WidgetsFrame,text="Price Per Qty",font=("Georgia",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_Cart_WidgetsFrame,textvariable=self.var_price,font=("Georgia",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
      
        lbl_p_Qty=Label(Add_Cart_WidgetsFrame,text="Quantity",font=("Georgia",15),bg="white").place(x=390,y=5)
        txt_p_Qty=Entry(Add_Cart_WidgetsFrame,textvariable=self.var_qty,font=("Georgia",15),bg="lightyellow").place(x=390,y=35,width=125,height=22)

        self.lbl_inStock=Label(Add_Cart_WidgetsFrame,text="In Stock ",font=("Georgia",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_Cart_WidgetsFrame,text="Clear",font=("Georgia",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=120,height=30)
        btn_add_cart=Button(Add_Cart_WidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("Georgia",13,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)


    #=====Billing Area=======
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)


        BTitle=Label(billFrame,text="Customer Bill",font=("Georgia",15,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        self.txt_bill_area=Text(billFrame)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)

        scrolly.config(command=self.txt_bill_area.yview)

#==============Billing Buttons==========

        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amount=Label(billMenuFrame,text='Bill Amount',font=("times new roman",15),bg="#3f51b5",fg="white")
        self.lbl_amount.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(billMenuFrame,text='Discount \n[5%]',font=("times new roman",15),bg="#3f51b5",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text='Net Pay \n[0]',font=("times new roman",15),bg="#3f51b5",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=150,height=70)


        btn_print=Button(billMenuFrame,text='Print',cursor="hand2",font=("times new roman",15),bg="#3f51b5",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(billMenuFrame,text='Clear All',cursor="hand2",font=("times new roman",15),bg="#3f51b5",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(billMenuFrame,text='Generate/Save Bill',cursor="hand2",font=("times new roman",15),bg="#3f51b5",fg="white")
        btn_generate.place(x=246,y=80,width=150,height=50)

        #====Footer======

        footer=Label(self.root,text="SMS-Stock Management System",font=("Georgia",15),bg="black",fg="white").pack(side=BOTTOM,fill=X)

        self.show()
#=================All Functions====================

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                 messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                 cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!",parent=self.root)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])  #pid,name,price,qty,status
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")


    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error',"Please select product from the list",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror('Error',"Quantity is requried",parent=self.root)
        else:
            price_cal=(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal=float(price_cal)
            #pid,name,price,qty,status
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get()]
            #print(self.cart_list)
            #=======Update_Cart==========
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present \nDo you want to Update| Removefrom the Cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2]=price_cal     #price
                        self.cart_list[index_][3]=self.var_qty.get()   #qty


                self.cart_list.append(cart_data)





                self.show_cart()
            
    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Bill(root)
    root.mainloop()
    