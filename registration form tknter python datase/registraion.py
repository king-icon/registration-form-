from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("regisration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #====bgimage=====#
        self.bg=ImageTk.PhotoImage(file="imgs/back.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #====leftimage=====#
        self.left=ImageTk.PhotoImage(file="imgs/logo.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=300,height=500)


        #=======registeframe=====#
        frame1=Frame(self.root,bg="white")
        frame1.place(x=380,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="#39c43e").place(x=50,y=30)

        #=======entry fields=======#

        #==row1
        
        fname=Label(frame1,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        lname=Label(frame1,text="LAST NAME",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #====row2
        contact=Label(frame1,text="CONTACT NO.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="EMAIL",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #==row3
        question=Label(frame1,text="SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("select","your first pet name","your birth place","you best friend name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0) #select wala show ho shuru me isliye index define kiya ha

        answer=Label(frame1,text="ANSWER",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #=======row4
        password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="CONFIRM PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #======terms 
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text=" agee the terms and conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        #====register btn
        self.btn_img=ImageTk.PhotoImage(file="imgs/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        #===signin btn=====#
        btn_login=Button(self.root,text="SIGN IN",font=("times new roman",20),bd=0,cursor="hand2",bg="black",fg="white",activebackground="white").place(x=140,y=460,width=180)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="select" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_answer.get()=="":

            messagebox.showerror("error","all fileds are required",parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("error","password does not match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("error","please agree our terms and conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="form")
                cur=con.cursor()        #query ko excte krne k liye
                cur.execute("select * from form1 where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("error","user alrady exist, pleae try with another email",parent=self.root)
                else:
                    cur.execute("insert into form1 (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                )) 
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","register succesfull",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("error",f"error due to {es}",parent=self.root)
root = Tk()
obj=register(root)
root.mainloop()

