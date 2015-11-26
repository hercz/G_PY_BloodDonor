import unittest
from Location_delete import *

class Location_deleteTestCase(unittest.TestCase):


    def test_input_is_empty(self):
        self.assertEqual(id_is_valid(""), False)


    def test_inputs_are_not_isdigit(self):
        self.assertEqual(id_is_valid("dfgdfg"), False)
        self.assertEqual(id_is_valid("egyekettoharOMegy"), False)


    def test_inputs_are_isdigits(self):
        self.assertEqual(id_is_valid("1"), True)
        self.assertEqual(id_is_valid("400"), True)



if __name__ == '__main__':
    unittest.main()
