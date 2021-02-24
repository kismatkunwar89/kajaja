#coded by Shashwat Dhakal

from tkinter import *
from tkinter import ttk, messagebox
from qry import qry
import payment

class Workers:
    def __init__(self):

        self.root = Tk()
        self.root.title("Worker Payment System")
        self.root.geometry("1900x1900+0+0")
        #self.pay = payment.payment()

        title = Label(self.root, text="Worker Payment System", bd=10, font=("arial", 40, "bold"),
                      bg="yellow", fg="black")
        title.pack(side=TOP, fill=X)

        self.exe=qry()

        #search_variables

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #manage_frame

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Manage_Frame.place(x=30, y=120, width=530, height=730)

        m_title = Label(Manage_Frame, text="Details", font=("arial", 20), fg="black", bg="yellow")
        m_title.grid(row=0, columnspan=1, pady=1)

        #identity

        lbl_idno = Label(Manage_Frame, text="ID Number", bg="yellow", fg="black", font=("arial", 15))
        lbl_idno.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txt_idno = Entry(Manage_Frame, bg="white", fg="black",
                              font=("arial", 15), relief=GROOVE)
        self.txt_idno.grid(row=1, column=0, pady=10, padx=180, sticky="w")
        
        #name

        lbl_name = Label(Manage_Frame, text="Name", bg="yellow", fg="black", font=("arial", 15))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(Manage_Frame, bg="white", fg="black",
                              font=("arial", 15), relief=GROOVE)
        self.txt_name.grid(row=2, column=0, pady=10, padx=180, sticky="w")
        
        #email

        lbl_email = Label(Manage_Frame, text="Email", bg="yellow", fg="black", font=("arial", 15))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_email = Entry(Manage_Frame, bg="white", fg="black",
                               font=("arial", 15), relief=GROOVE)
        self.txt_email.grid(row=3, column=0, pady=10, padx=180, sticky="w")
        
        #gender

        lbl_gender = Label(Manage_Frame, text="Gender", bg="yellow", fg="black", font=("arial", 15))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.combo_gender = ttk.Combobox(Manage_Frame, font=("arial", 15),
                                         state='readonly')
        self.combo_gender['values'] = ("Male", "Female")
        self.combo_gender.grid(row=4, column=0, padx=180, pady=10)

        #contact

        lbl_contact = Label(Manage_Frame, text="Contact Number", bg="yellow", fg="black",
                            font=("arial", 15))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(Manage_Frame, bg="white", fg="black", font=("arial", 15), relief=GROOVE)
        self.txt_contact.grid(row=5, column=0, pady=10, padx=180, sticky="w")

        #date of birth

        lbl_dob = Label(Manage_Frame, text="DoB", bg="yellow", fg="black", font=("arial", 15))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_dob = Entry(Manage_Frame, bg="white", fg="black", font=("arial", 15), relief=GROOVE)
        self.txt_dob.grid(row=6, column=0, pady=10, padx=180, sticky="w")
        self.txt_dob.insert(0, 'DD/MM/YYYY')

        #address
        
        lbl_address = Label(Manage_Frame, text="Address", bg="yellow", fg="black", font=("arial", 15))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame, bg="white", fg="black", font=("arial", 15), relief=GROOVE,
                                width=20, height=4)
        self.txt_address.grid(row=7, column=0, pady=10, padx=180, sticky="w")

        #department

        lbl_department = Label(Manage_Frame, text="Department", bg="yellow", fg="black",
                               font=("arial", 15))
        lbl_department.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.txt_department = ttk.Combobox(Manage_Frame, font=("arial", 15),
                                           state='readonly')
        self.txt_department['values'] = (
        "x", "Administration", "Management", "Information Technology", "Reception", "Sales", "Marketing",)
        self.txt_department.grid(row=8, column=0, padx=180, pady=10)

        #status

        lbl_status = Label(Manage_Frame, text="Status", bg="yellow", fg="black", font=("arial", 15))
        lbl_status.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.combo_status = ttk.Combobox(Manage_Frame, font=("arial", 15),
                                         state='readonly')
        self.combo_status['values'] = ("Present", "Absent", "Free", "Busy")
        self.combo_status.grid(row=9, column=0, padx=180, pady=10)

        #method_of_payment

        lbl_payment = Label(Manage_Frame, text="Payment", bg="yellow", fg="black", font=("arial", 15))
        lbl_payment.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        self.combo_payment = ttk.Combobox(Manage_Frame, font=("arial", 15),
                                          state='readonly')
        self.combo_payment['values'] = ("Cash", "Bank", "Cheque","E-Sewa","Master Card")
        self.combo_payment.grid(row=10, column=0, padx=180, pady=10)

        #btn_frame

        btn_Frame = Frame(Manage_Frame, bd=4, bg="yellow")
        btn_Frame.place(x=10, y=600, width=450)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_workers).grid(row=0, column=0, padx=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear_workers).grid(row=0, column=2, padx=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=3, padx=10)

        #detail_frame

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Detail_Frame.place(x=600, y=120, width=1280, height=840)

        #lbl_search

        lbl_search = Label(Detail_Frame, text="Search By", bg="yellow", fg="black", font=("arial", 15))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("arial", 15), state='readonly')
        combo_search['values'] = ("x", "Name", "ID Number")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, bg="white",textvariable=self.search_txt, fg="black", font=("arial", 15), relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,command=self.search_data).grid(row=0, column=4, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,command=self.fetch_data).grid(row=0, column=5, padx=10, pady=10)

        #table_frame

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="yellow")
        Table_Frame.place(x=10, y=70, width=1245, height=750)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Workers_table = ttk.Treeview(Table_Frame, columns=(
            "ID Number", "Name", "Email", "Gender", "Contact", "DoB", "Address", "Department", "Status",
            "Payment"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Workers_table.xview)
        scroll_y.config(command=self.Workers_table.yview)
        
        #visible_table

        self.Workers_table.heading("ID Number", text="ID Number")
        self.Workers_table.heading("Name", text="Name")
        self.Workers_table.heading("Gender", text="Gender")
        self.Workers_table.heading("Email", text="Email")
        self.Workers_table.heading("Contact", text="Contact")
        self.Workers_table.heading("Department", text="Department")
        self.Workers_table.heading("DoB", text="Date of birth")
        self.Workers_table.heading("Address", text="Address")
        self.Workers_table.heading("Status", text="Status")
        self.Workers_table.heading("Payment", text="Payment")

        self.Workers_table['show'] = 'headings'

        #adjust_table

        self.Workers_table.column("ID Number", width=150)
        self.Workers_table.column("Name", width=250)
        self.Workers_table.column("Email", width=400)
        self.Workers_table.column("Gender", width=150)
        self.Workers_table.column("Contact", width=250)
        self.Workers_table.column("Department", width=150)
        self.Workers_table.column("DoB", width=180)
        self.Workers_table.column("Address", width=300)
        self.Workers_table.column("Status", width=150)
        self.Workers_table.column("Payment", width=150)

        self.Workers_table.pack(fill=BOTH,
                                 expand=1)
        self.Workers_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        #report_frame

        Button(btn_Frame, text="Payment", font=("arial", 15), width=15, bg="yellow",command=self.payment).grid(
            row=1, column=0, columnspan=2, padx=10, pady=30)

        Button(btn_Frame, text="Logout", font=("arial", 15), width=15, bg="yellow",
                           command=self.logout).grid(row=1, column=2, columnspan=2, padx=10)

    #assigned_functions

    #logout

    def logout(self):
        ask = messagebox.askyesno("Logout", "Proceed to logout?")
        if ask > 0:
            self.root.destroy()
            import Login
            Login.login(self)

    #payment_file_connector

    def payment(self):
        self.root.destroy()
        payment.payment(self.row[0],self.row[1],self.row[4],self.row[7],self.row[9])



    def add_workers(self):

        self.exe.add_workers(self.txt_idno.get(), self.txt_name.get(), self.combo_status.get(), self.txt_email.get(),
                  self.combo_gender.get(), self.txt_contact.get(), self.txt_dob.get(), self.txt_address.get("1.0", END),
                  self.txt_department.get(), self.combo_payment.get())
        self.fetch_data()
        return True

    #fetch_data

    def fetch_data(self):
        data =self.exe.fetch_workers()
        self.Workers_table.delete(*self.Workers_table.get_children())
        for i in data:
            self.Workers_table.insert("", "end", text="", values=i)

    #cursor_movement_among_tables

    def get_cursor(self, ev):
        self.clear_workers()
        cursor_row = self.Workers_table.focus()
        contents = self.Workers_table.item(cursor_row)
        self.row = contents['values']
        self.txt_idno.insert(0,self.row[0])
        self.txt_name.insert(0, self.row[1])
        self.txt_email.insert(0,self.row[2])
        self.combo_gender.set(self.row[3])
        self.txt_contact.insert(0,self.row[4])
        self.txt_dob.insert(0,self.row[5])
        self.txt_address.insert(END, self.row[6])
        self.txt_department.set(self.row[7])
        self.combo_status.set(self.row[8])
        self.combo_payment.set(self.row[9])

    #update_table

    def update_data(self):

        self.exe.update_workers (self.txt_idno.get(), self.txt_name.get(), self.combo_status.get(), self.txt_email.get(),
                  self.combo_gender.get(), self.txt_contact.get(), self.txt_dob.get(), self.txt_address.get("1.0", END),
                  self.txt_department.get(), self.combo_payment.get(),)

        self.fetch_data()
        return True

    #delete_data
    
    def delete_data(self):

        self.exe.delete_workers(self.txt_idno.get())
        self.fetch_data()
        self.clear_workers()
        return True

    #clear

    def clear_workers(self):
        self.txt_idno.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_dob.delete(0, END)
        self.combo_status.set('')
        self.combo_gender.set('')
        self.combo_payment.set('')
        self.txt_address.delete("1.0", END)
        self.txt_department.delete(0, END)

        self.txt_idno.insert(0, '')
        self.txt_name.insert(0, '')
        self.txt_email.insert(0, '')
        self.txt_contact.insert(0, '')
        self.txt_dob.insert(0, '')
        self.txt_department.insert(0, '')

    # search

    def search_data(self):
        data = None
        z = None
        if self.search_by.get() == "ID Number":
            data = self.exe.fetch_workers()
            z = self.binary_search_id(data, int(self.search_txt.get()))
        elif self.search_by.get() == "Name":
            data = self.exe.search_workers()
            z = self.binary_search_name(data, self.search_txt.get())
        else:
            messagebox.showerror('Error', 'Invalid Search!')
        self.Workers_table.delete(*self.Workers_table.get_children())

        self.Workers_table.insert('', END, values=data[z])

    def binary_search_name(self, list, value):
        l = 0
        r = len(list) - 1
        while l <= r:
            mid = int((r + l) // 2)
            if list[mid][1] == value:
                return mid
            elif list[mid][1] > value:
                r = mid - 1
            elif list[mid][1] < value:
                l = mid + 1
            else:
                return False
        return False

    def binary_search_id(self, list, value):
        l = 0
        r = len(list) - 1
        while l <= r:
            mid = int((r + l) // 2)
            if list[mid][0] == value:
                return mid
            elif list[mid][0] > value:
                r = mid - 1
            elif list[mid][0] < value:
                l = mid + 1
            else:
                return False
        return False

obj=Workers()
mainloop()