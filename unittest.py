#coded by Shashwat Dhakal

import unittest
from qry import qry

def TestCase():

    class testing(unittest.TestCase):
        obj = qry()

    def test_add(self):
        actual_result = self.obj.add_workers(800,"textname","teststatus","testemail","testgender","testcontact","testdob","testaddress","testdepartment","testpayment")
        answer = 1
        self.assertEqual(actual_result,answer)


    def test_delete(self):
        actual_result = self.obj.delete_workers(800)
        answer= 1
        self.assertEqual(actual_result,answer)

    def test_update(self):
        actual_result = self.obj.update_workers(800)
        answer= 1
        self.assertEqual(actual_result,answer)

    def test_add_payment(self):
        actual_result = self.obj.add_payment(800, "textname", "testcontact", "testdepartment", "testpayment", 800,
                                             "15%")
        answer = 1
        self.assertEqual(actual_result, answer)