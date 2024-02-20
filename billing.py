from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile


class bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Stock Management System")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0

        #===title==
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Stock Management System",image=self.icon_title,compound=LEFT,font=("Georgia",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===BTN_Logout===
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("Georgia",15,"bold"),bg="white",cursor="hand2").place(x=1350,y=10,height=50,width=150)
        #===clock==
        self.lbl_clock=Label(self.root,text="Welcome to Stock Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("Georgia",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===product_Frame===

        self.var_search=StringVar()
       
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=450,height=650)

        pTitle=Label(ProductFrame1,text="All Products",font=("Georgia",15,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        #===Product Search  Frame===
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=430,height=90)


        lbl_search=Label(ProductFrame2,text="Search roduct | By Name",font=("Georgia",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_name=Label(ProductFrame2,text="Product Name",font=("Georgia",15,"bold"),bg="white").place(x=5,y=45)

        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("Georgia",15),bg="lightyellow").place(x=160,y=45,width=120,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("Georgia",13,"bold"),bg="blue",fg="white",cursor="hand2").place(x=285,y=45,width=90,height=20)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("Georgia",13,"bold"),bg="black",fg="white",cursor="hand2").place(x=285,y=10,width=90,height=20)

        
        #===Product Details Frame====

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=430,height=475)


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

        self.product_table.column("pid",width=40)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100) 
        self.product_table.column("qty",width=40)
        self.product_table.column("status",width=90) 
 
      
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="NOTE:Enter 0 Quantity to remove product from the Cart",font=("Georgia",9,"bold"),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)


        #====Customer Frame=====

        self.var_cname=StringVar()
        self.var_contact=StringVar()


        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=460,y=110,width=530,height=80)


        cTitle=Label(CustomerFrame,text="Customer Details",font=("Georgia",15,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("Georgia",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("Georgia",13),bg="lightyellow").place(x=80,y=35,width=150)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("Georgia",15),bg="white").place(x=250,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("Georgia",13),bg="lightyellow").place(x=360,y=35,width=150)
        
         #===Cal cart Frame===
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=460,y=190,width=530,height=425)

        
        self.im8=ImageTk.PhotoImage(file="images/im8.jpg")
        self.im4=ImageTk.PhotoImage(file="images/im4.jpg")
        self.im7=ImageTk.PhotoImage(file="images/cat.jpg")
        
        
        

        

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=467,y=198,width=268,height=417)

        self.animate()
       

        #===Cart Frame===
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=4,width=245,height=417)

        self.cartTitle=Label(Cart_Frame,text="Cart  Total Product:[0]",font=("Georgia",13,"bold"),bg="black",fg="white")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)


        self.CartTable.heading("pid",text="P ID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        

        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90) 
        self.CartTable.column("qty",width=40)
        
 
      
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)


        #===Add Cart Widgets Frame===
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_Cart_WidgetsFrame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Add_Cart_WidgetsFrame.place(x=460,y=620,width=530,height=140)

        lbl_p_name=Label(Add_Cart_WidgetsFrame,text="Product Name",font=("Georgia",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_Cart_WidgetsFrame,textvariable=self.var_pname,font=("Georgia",15),bg="lightyellow",state='readonly').place(x=5,y=40,width=190,height=25)

        lbl_p_price=Label(Add_Cart_WidgetsFrame,text="Price Per Qty",font=("Georgia",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_Cart_WidgetsFrame,textvariable=self.var_price,font=("Georgia",15),bg="lightyellow",state='readonly').place(x=230,y=40,width=150,height=25)
      
        lbl_p_Qty=Label(Add_Cart_WidgetsFrame,text="Quantity",font=("Georgia",15),bg="white").place(x=390,y=5)
        txt_p_Qty=Entry(Add_Cart_WidgetsFrame,textvariable=self.var_qty,font=("Georgia",15),bg="lightyellow").place(x=390,y=40,width=125,height=25)

        self.lbl_inStock=Label(Add_Cart_WidgetsFrame,text="In Stock",font=("Georgia",15),bg="white")
        self.lbl_inStock.place(x=5,y=90)

        btn_clear_cart=Button(Add_Cart_WidgetsFrame,text="Clear",command=self.clear_cart,font=("Georgia",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=90,width=120,height=30)
        btn_add_cart=Button(Add_Cart_WidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("Georgia",13,"bold"),bg="orange",cursor="hand2").place(x=340,y=90,width=180,height=30)


#=======================billing area========


        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=1000,y=110,width=530,height=510)

        bTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="black",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)


 #===========================Billing buttons=======

        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=1000,y=620,width=530,height=140)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount \n[0]",font=("goudy old style",17,"bold"),bg="#3f51b5",fg="black")
        self.lbl_amnt.place(x=2,y=5,width=150,height=70)
       
        self.lbl_discount=Label(billMenuFrame,text="Discount \n[5%]",font=("goudy old style",17,"bold"),bg="#8bc34a",fg="black")
        self.lbl_discount.place(x=165,y=5,width=150,height=70)
       
        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay \n[0]",font=("goudy old style",17,"bold"),bg="#607d8b",fg="black")
        self.lbl_net_pay.place(x=325,y=5,width=200,height=70)
       

        btn_print=Button(billMenuFrame,text="Print",command=self.print_bill,cursor="hand2",font=("goudy old style",17,"bold"),bg="lightgreen",fg="black")
        btn_print.place(x=2,y=80,width=150,height=50)
       
        btn_clear_all=Button(billMenuFrame,text="Clear All",command=self.clear_all,cursor="hand2",font=("goudy old style",17,"bold"),bg="gray",fg="black")
        btn_clear_all.place(x=165,y=80,width=150,height=50)
       
        btn_generate=Button(billMenuFrame,text="Generate Bill/Save Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",14,"bold"),bg="#009688",fg="black")
        btn_generate.place(x=325,y=80,width=200,height=50)

        #-------------------------footer------------

        footer=Label(self.root,text="Stock Management System",font=("times new roman",11),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)
       
        self.show()
       #self.bill_top()
        self.update_date_time()

#==========================All Functions==========

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))


    def animate(self):
        self.im=self.im4
        self.im4=self.im8
        self.im8=self.im7

        self.im7=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


#==============================


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
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
                 cur.execute("select * from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
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
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        
    


    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please select product from the list",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is Requried",parent=self.root)
        elif  int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
    
        else:
            #price_cal=int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            
            
            #==========update cart==========

            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes' :
                op=messagebox.askyesno('confirm',"Product already present\nDo you want to Update | Remove from the Cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()


            else:
                self.cart_list.append(cart_data)

            
            
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))


        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount

        self.lbl_amnt.config(text=f'Bill Amnt\n {str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n {str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product:[{str(len(self.cart_list))}]")




    def show_cart(self):
        
        try:
           
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)




        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)

        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add product to the cart",parent=self.root)

        else:
            #===Bill top==
            self.bill_top()
            #===Bill mid==
            self.bill_middle()
            #===Bill bottom==
            self.bill_bottom()
            

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Bill has been generated/Save in Backend",parent=self.root)
            self.chk_print=1
        
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\t\tStock Management System\t\t
\t\t Phone No. 9623922598,mumbai-40001
{str("="*63)}
Customer Name: {self.var_cname.get()}
Ph no. :{self.var_contact.get()}
Bill no. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%y"))}
{str("="*63)}
Product Name\t\t\tQTY\tPrice
{str("="*63)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)


    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*63)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*63)}\n

        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)


    def bill_middle(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        
        try:

            for row in self.cart_list:
                
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'

                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\t"+price)

#==================update qty in product table
                cur.execute("Update product set qty=?,status=? where pid=?",(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock [0]")
        self.var_stock.set('')
        

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product:[0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0

    def update_date_time(self):
        time_=time.strftime('%I:%M:%S')
        date_=time.strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f"Welcome to Stock Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print','Please wait while printing',parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print','Please Generate Bill',parent=self.root)
            
    def logout(self):
            self.root.destroy()
            os.system("python login.py")



if __name__=="__main__":
    root=Tk()
    obj=bill(root)
    root.mainloop()
     
       # btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=200,y=18)