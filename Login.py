#coded by Shashwat Dhakal

from tkinter import*
from tkinter import messagebox

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Worker Payment System")
        self.root.geometry("500x360+600+100")

        F1=Frame(self.root,bg="yellow", padx=20)
        F1.place(x=0,y=0,height=360)

        self.user=StringVar()
        self.password=StringVar()


        title=Label(F1,text="Login",font=("arial", 30, "bold"),fg="black",bg="yellow").grid(row=0,columnspan=2,pady=10)

        lblusername=Label(F1,text="Username",font=("arial", 20, "bold"),fg="black",bg="yellow").grid(row=1,column=0,pady=10,padx=10)

        txtuer=Entry(F1,textvariable=self.user,width=25,font=("arial", 15, "bold")).grid(row=1,column=1,padx=10,pady=10)

        lblpass=Label(F1,text="Password",font=("arial", 20, "bold"),fg="black",bg="yellow").grid(row=2,column=0,pady=10,padx=10)

        txtpass=Entry(F1,show="*",textvariable=self.password,width=25,font=("arial", 15, "bold")).grid(row=2,column=1,padx=10,pady=10)

        btnlogin=Button(F1,text="Login",font=("arial", 15, "bold" ),bd=7,width=10,command=self.log_fun).place(x=5,y=270)
        btnreser=Button(F1,text="Reset",font=("arial", 15, "bold" ),bd=7,width=10,command=self.reset).place(x=160,y=270)
        btnexit=Button(F1,text="Exit",font=("arial", 15, "bold" ),bd=7,width=10,command=self.exit_fun).place(x=320,y=270)
    def log_fun(self):
        if self.user.get()=="admin" and self.password.get()=="admin":
            self.root.destroy()
            import first
            first.Workers()
        else:
            messagebox.showerror("Error", "invalid username or password")
    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit_fun(self):
        option=messagebox.askyesno("Exit", "Proceed to exit?")
        if option:
            self.root.destroy()
        else:
            return



root=Tk()
ob=login(root)
root.mainloop()
