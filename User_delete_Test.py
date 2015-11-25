import unittest
from User_delete import *

class Test_User_delete(unittest.TestCase):

    def test_input_is_empty(self):
        self.assertEqual(id_is_valid(""), False)

    def test_inputs_are_not_correct(self):
        self.assertEqual(id_is_valid("1"), False)
        self.assertEqual(id_is_valid("unique_id"), False) #isalpha
        self.assertEqual(id_is_valid("12345678"), False) #justletters
        self.assertEqual(id_is_valid("MA1234FG"), False) #upper letters


    def test_inputs_are_correct(self):
        self.assertEqual(id_is_valid("123456tz"), True) #simple id
        self.assertEqual(id_is_valid("qwertz56"), True) #simple passport
        self.assertEqual(id_is_valid("QWERTZ56"), True) #upper letters


    def test_is_it_delete_file(self):
        pass #if we have time...




if __name__ == '__main__':
    unittest.main()
