#coded by Shashwat Dhakal

from connector import connection


class qry:
    def __init__(self):
        self.exe = connection()

    def add_workers(self, Idno, name, status, email, gender, contact, dob, address, department, payment):
        qry = "INSERT INTO workers(Idno,name,status,email,gender,contact,dob,address,department,payment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = Idno, name, status, email, gender, contact, dob, address, department, payment

        return self.exe.iud(qry, values)

    def delete_workers(self, values):
        qry = "DELETE  from workers WHERE Idno =%s"
        values = (values,)
        return self.exe.iud(qry, values)

    def update_workers(self, Idno, name, status, email, gender, contact, dob, address, department, payment):
        qry = "UPDATE workers SET Idno =%s, name = %s, status = %s, email = %s, gender = %s, contact = %s, dob = %s, address = %s, department = %s, payment = %s WHERE Idno =%s "
        values = Idno, name, status, email, gender, contact, dob, address, department, payment, Idno
        return self.exe.iud(qry, values)

    def fetch_workers(self):
        qry = "SELECT * from workers order by Idno"
        return self.exe.show(qry)

    def search_workers(self):
        qry = "SELECT * from workers order by name"
        return self.exe.show(qry)


    def add_payment(self, Idno, name, contact, department, payment, amount, overtime):
        qry = "INSERT INTO payouts(Idno,name,contact,department,payment,amount,overtime,total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (Idno, name, contact, department, payment, amount, overtime,
                  (int(amount) * int(overtime[:-1]) / 100) + int(amount))
        return self.exe.pay(qry, values)
    def ok(self):
        pass

    def fetch_payment(self):
        qry = "SELECT * from payouts"
        return self.exe.show(qry)

obj = qry()