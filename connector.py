#coded by Shashwat Dhakal

import mysql.connector
class connection:
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',
                                                 database='softwarica',
                                                 user='root',
                                                 password='unostamsik')
        self.my_cursor = self.conn.cursor()

    def iud(self,qry,values):
        try:
            self.my_cursor.execute(qry, values)
            self.conn.commit()
            return 1
        except Exception:
            return 0

    def show(self,qry):
        self.my_cursor.execute(qry)
        return self.my_cursor.fetchall()

    def search(self,qry):
        self.my_cursor.execute(qry)
        return self.my_cursor.fetchall()

    def pay(self,qry,values):
        self.my_cursor.execute(qry,values)
        self.conn.commit()
        return 1

    def binary_search_1(self, key):
        self.my_cursor.execute(key)
        data = self.my_cursor.fetchall()
        start=0
        end=len(data)-1
        print(data)
        while start <= end:
            mid_value=(start+end)//2
            if data[mid_value][1].lower()==key.lower():
                return data[mid_value]
            elif data[mid_value][1].lower()>key.lower():
                end = mid_value-1
            else:
                end= mid_value + 1
        return False

obj = connection()