from tkinter import*
#pip install pillow
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title=root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")


        self.otp=''
        #=========Images========
        self.phone_image=ImageTk.PhotoImage(file='images/phone.png')
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #=================Login_Frame========================
        self.employee_id=StringVar()
        self.password=StringVar()
       
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="black").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="black").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Gergoia",15,"bold"),bg="#00B0F0",activebackground="#00B0F0",fg="black",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        or_=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("Andalus",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("Andalus",13,"bold"),bg='white',fg="black",bd=0,activebackground="white",activeforeground="black").place(x=100,y=390)

        #================Frame2==================

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Stock Management System",font=("Gergoia",15,"bold"),bg="white").place(x=0,y=20,relwidth=1)
        #btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,activebackground="white",activeforeground="black").place(x=200,y=15)

        #============== Animation Images ==========================
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()
        
      #================== All Functions ============================
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3

        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        

    def login(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showinfo('Error',"All fields are required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showinfo('Error',"Invalid Username/Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                         self.root.destroy()
                         os.system("python billing.py")
                    


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       

    def forget_window(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":  
                messagebox.showinfo('Error',"Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get()))
                email=cur.fetchone()
                if email==None:
                    messagebox.showinfo('Error',"Invalid Employee ID,try again",parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_confirm_pass=StringVar()
                    #call send email function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                            messagebox.showerror("Error","Connection Error,try again",parent=self.root)
                    else:
                        
                        self.forget_win=Tk()
                        self.forget_win.title('Reset Password')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()


                        title=Label(self.forget_win,text='Reset Password',font=('Gergoia',15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text='Enter OTP sent on register Email',font=('Gergoia',15,"bold")).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=('Gergoia',15,"bold"),bg="lightyellow").place(x=20,y=100,width=250,height=30)

                        self.btn_reset=Button(self.forget_win,text="Submit",command=self.validate_otp,font=('Gergoia',15,"bold"),bg="lightyellow")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        lbl_new_pass=Label(self.forget_win,text='New Password',font=('Gergoia',15,"bold")).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=('Gergoia',15,"bold"),bg="lightyellow").place(x=20,y=190,width=250,height=30)

                        lbl_c_pass=Label(self.forget_win,text='Confirm Password',font=('Gergoia',15,"bold")).place(x=20,y=225)
                        txt_c_pass=Entry(self.forget_win,textvariable=self.var_confirm_pass,font=('Gergoia',15,"bold"),bg="lightyellow").place(x=20,y=255,width=250,height=30)

                        self.btn_update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=('Gergoia',15,"bold"),bg="lightyellow")
                        self.btn_update.place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def update_password(self):
        if input("enter your new password :") != input("confirm your pass :"):
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        #elif self.var_new_pass.get()== self.var_confirm_pass.get():
         #   messagebox.showerror("Error","New Password & confirm Password should be same",parent=self.forget_win)

        else:
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee SET pass=? where eid=?",(input("enter your new password :"),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated successfully",parent=self.forget_win)
                self.forget_win.destroy()

            
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         
             
        


    def validate_otp(self):
        try:
            otp = self.otp
            var_otp =input("enter the otp you received :")
            if otp.isdigit() and var_otp.isdigit():
                if int(otp) == int(var_otp):
                    self.btn_update.config(state=NORMAL)
                    self.btn_reset.config(state=DISABLED)
                else:
                    messagebox.showerror("Error", "Invalid OTP, Try again", parent=self.forget_win)
            else:
                messagebox.showerror("Error", "Invalid OTP, Try again", parent=self.forget_win)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=str(time.strftime("%H%M")) #self.otp=str(time.strftime("%H%S%M"))+str(time.strftime("%S"))  #
        print(self.otp)
        

        subj='Stock Management System - Reset Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nSMS Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 'p'
        else:
            return 'f'





root=Tk()
obj=Login_system(root)
root.mainloop()