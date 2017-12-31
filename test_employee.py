import unittest
from employee import Employee

#tests never run in order

class TestEmployee(unittest.TestCase):

    #runs at the start of the test    
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
    
    #runs at the end of the test        
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # -----------------------------------

    #runs before every single test
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("John", "Smith", 50000)
        self.emp_2 = Employee("Susie", "Gray", 60000)

    #runs at the end of every single test
    def tearDown(self):
        print("tearDown\n")
        pass


    # -----------------------------------
        

    def test_email(self):
        print("test_email")        
        self.assertEqual(self.emp_1.email, "John.Smith@email.com")
        self.assertEqual(self.emp_2.email, "Susie.Gray@email.com")

        self.emp_1.first = "Ben"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "Ben.Smith@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Gray@email.com")

    def test_fullname(self):
        print("test_fullname")        
        self.assertEqual(self.emp_1.fullname, "John Smith")        
        self.assertEqual(self.emp_2.fullname, "Susie Gray")

        self.emp_1.first = "Ben"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "Ben Smith")
        self.assertEqual(self.emp_2.fullname, "Jane Gray")

    def test_apply_raise(self):
        print("test_apply_raise")                
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == "__main__": unittest.main()