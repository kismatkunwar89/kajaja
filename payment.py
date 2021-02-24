#coded by Shashwat Dhakal

from tkinter import *
from tkinter import ttk, messagebox
from view import view
from qry import qry

class payment:
    def __init__(self,Idno,name,contact,department,payment):

        self.root = Tk()
        self.root.title("Easy Payment System")
        self.root.geometry("770x880+600+70")

        title = Label(self.root, text="Payment", bd=10, font=("arial", 40, "bold"),
                      bg="yellow", fg="black")
        title.pack(side=TOP, fill=X)
        self.exe = qry()

        #frame

        frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        frame.place(x=80, y=120, width=600, height=730)

        #lbl_idno

        lbl_idno = Label(frame, text="ID No", bg="yellow", fg="black", font=("arial", 15))
        lbl_idno.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txt_idno = Entry(frame, bg="yellow", fg="black",
                              font=("arial", 15), relief=GROOVE)
        self.txt_idno.grid(row=1, column=0, pady=10, padx=180, sticky="w")

        #lbl_name

        lbl_name = Label(frame, text="Name", bg="yellow", fg="black", font=("arial", 15))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(frame, bg="yellow", fg="black",
                              font=("arial", 15), relief=GROOVE)
        self.txt_name.grid(row=2, column=0, pady=10, padx=180, sticky="w")

        #lbl_contact

        lbl_contact = Label(frame, text="Contact No", bg="yellow", fg="black",
                            font=("arial", 15))
        lbl_contact.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(frame, bg="yellow", fg="black", font=("arial", 15), relief=GROOVE)
        self.txt_contact.grid(row=3, column=0, pady=10, padx=180, sticky="w")

        #lbl_department

        lbl_department = Label(frame, text="Department", bg="yellow", fg="black",
                               font=("arial", 15))
        lbl_department.grid(row=4, column=0, pady=10, padx=20, sticky="w")


        self.txt_department= Entry(frame, bg="yellow", fg="black", font=("arial", 15), relief=GROOVE)
        self.txt_department.grid(row=4, column=0, pady=10, padx=180, sticky="w")

        #lbl_payment

        lbl_payment = Label(frame, text="Payment", bg="yellow", fg="black", font=("arial", 15))
        lbl_payment.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.combo_payment = Entry(frame, bg="yellow", fg="black", font=("arial", 15), relief=GROOVE)
        self.combo_payment.grid(row=5, column=0, pady=10, padx=180, sticky="w")

        #lbl_amount

        lbl_amount= Label(frame, text="Amount", bg="yellow", fg="black", font=("arial", 15))
        lbl_amount.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        self.amount= Entry(frame, bg="white", fg="black", font=("arial", 15), relief=GROOVE)
        self.amount.grid(row=6, column=0, pady=10, padx=180, sticky="w")
        #self.amount.insert(0)

        #lbl_bonus

        lbl_bonus = Label(frame, text="Bonus", bg="yellow", fg="black",
                               font=("arial", 15))
        lbl_bonus.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_bonus = ttk.Combobox(frame, font=("arial", 15),
                                           state='readonly')
        self.txt_bonus['values'] = (
         "5%", "10%", "15%", "20%", "25%", "30%","50%")
        self.txt_bonus.grid(row=7, column=0, padx=180, pady=10)

        btn_Frame = Frame(frame, bd=0, bg="yellow")
        btn_Frame.place(x=10, y=500, width=500, height=200)
        Button(btn_Frame, text="Pay", font=("arial", 15), width=15, bg="yellow",command=self.paybox).grid(row=0, column=0, padx=10, pady=30)

        Button(btn_Frame, text="View All Payments", font=("arial", 15), width=15, bg="yellow",command=self.view).grid(row=1, column=0, padx=10, pady=10)
        Button(btn_Frame, text="Back", font=("arial", 15), width=15, bg="yellow",command=self.back).grid(row=1, column=1, padx=10, pady=10)




    #insert from first.py

        self.txt_idno.insert(0, Idno)
        self.txt_idno["state"]=DISABLED
        self.txt_name.insert(0, name)
        self.txt_name["state"] = DISABLED
        self.txt_contact.insert(0,contact)
        self.txt_contact["state"] = DISABLED
        self.txt_department.insert(0,department)
        self.txt_department["state"] = DISABLED
        self.combo_payment.insert(0,payment)
        self.combo_payment["state"] = DISABLED

    def paybox(self):
        option=messagebox.askyesno("Payment","Confirm Payment?")
        if option:
            self.payment_add()
        else:
            return

    def payment_add(self):
        self.exe.add_payment(self.txt_idno.get(), self.txt_name.get(), self.txt_contact.get(),self.txt_department.get(), self.combo_payment.get(),self.amount.get(),self.txt_bonus.get())
        self.fetch()



    def fetch(self):
        self.exe.fetch_payment()



    def view(self):
        ask = messagebox.askyesno("View", "Confirm?")
        if ask > 0:
            self.root.destroy()
            view()



    def back(self):
        ask = messagebox.askyesno("Go Back", "Confirm?")
        if ask > 0:
            self.root.destroy()
            import first
            first.Workers()