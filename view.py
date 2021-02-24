#coded by Shashwat Dhakal

from tkinter import *
from tkinter import ttk, messagebox
from qry import qry
import first

class view:
    def __init__(self) :

        self.root = Tk()
        self.root.title("Paid Workers")
        self.root.geometry("990x800+600+00")

        title = Label(self.root, text="Payment View", bd=10, font=("arial", 40, "bold"),
                      bg="yellow", fg="black")
        title.pack(side=TOP, fill=X)

        self.exe = qry()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        main_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        main_Frame.place(x=10, y=120, width=970, height=700)

        view_Frame = Frame(main_Frame, bd=4, relief=RIDGE, bg="yellow")
        view_Frame.place(x=10, y=10, width=940, height=550)

        scroll_x = Scrollbar(view_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(view_Frame, orient=VERTICAL)
        self.pay_table = ttk.Treeview(view_Frame, columns=(
            "Identity Number", "Name", "Contact","Department", "Payment","Amount","Bonus","Total"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.pay_table.xview)
        scroll_y.config(command=self.pay_table.yview)

        #above_to_here

        self.pay_table.heading("Identity Number", text="Identity Number")
        self.pay_table.heading("Name", text="Name")
        self.pay_table.heading("Contact", text="Contact")
        self.pay_table.heading("Department", text="Department")
        self.pay_table.heading("Payment", text="Payment")
        self.pay_table.heading("Amount", text="Amount")
        self.pay_table.heading("Bonus", text="Bonus")
        self.pay_table.heading("Total", text="Total")

        self.pay_table['show'] = 'headings'

        #adjust_heading_length

        self.pay_table.column("Identity Number", width=150)
        self.pay_table.column("Name", width=250)
        self.pay_table.column("Contact", width=130)
        self.pay_table.column("Department", width=130)
        self.pay_table.column("Payment", width=90)
        self.pay_table.column("Amount", width=90)
        self.pay_table.column("Bonus", width=90)
        self.pay_table.column("Total", width=90)

        self.pay_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        btn_Frame = Frame(main_Frame, bd=0, bg="yellow")
        btn_Frame.place(x=10, y=560, width=900, height=70)

        Button(btn_Frame, text="Exit", font=("arial", 15), width=15, bg="yellow",command=self.exit).grid(row=0, column=1, padx=10, pady=10)
        Button(btn_Frame, text="Back", font=("arial", 15), width=15, bg="yellow",command=self.back).grid(row=0, column=0, padx=10, pady=10)

    def fetch_data(self):
        data = self.exe.fetch_payment()
        self.pay_table.delete(*self.pay_table.get_children())
        for i in data:
            self.pay_table.insert("", "end", text="", values=i)

    def exit(self):
        option=messagebox.askyesno("Exit","Do you really want to exit?")
        if option:
            self.root.destroy()
        else:
            return True

    def back(self):
        ask = messagebox.askyesno("Go Back", "Do you want to get back to management page?")
        if ask > 0:
            self.root.destroy()
            first.Workers()