import unittest
import unittests #module name that you're testing

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(unittests.add(10, 5), 15)
        self.assertEqual(unittests.add(-1, 1), 0)
        self.assertEqual(unittests.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(unittests.subtract(10, 5), 5)
        self.assertEqual(unittests.subtract(-1, 1), -2)
        self.assertEqual(unittests.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(unittests.multiply(10, 5), 50)
        self.assertEqual(unittests.multiply(-1, 1), -1)
        self.assertEqual(unittests.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(unittests.divide(10, 5), 2)
        self.assertEqual(unittests.divide(-1, 1), -1)
        self.assertEqual(unittests.divide(-1, -1), 1)
        self.assertEqual(unittests.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, unittests.divide, 10, 0)

        with self.assertRaises(ValueError):
            unittests.divide(10, 0)


if __name__ == "__main__": unittest.main()