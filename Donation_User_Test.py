__author__ = 'Gazdik_Zsolt'

import unittest
from Donation_User2 import UserData2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData2()

    def test_get_title_withEmptyString(self):
        result = self.user.valid_title("")
        self.assertEqual(False, result)

    def test_get_title_with_T_asString(self):
        result = self.user.valid_title("T")
        self.assertEqual(False, result)

    def test_get_title_with_Y_asString(self):
        result = self.user.valid_title("Y")
        self.assertEqual(True, result)

    def test_get_title_with_N_asString(self):
        result = self.user.valid_title("N")
        self.assertEqual(True, result)

    def test_get_title_with_Alma_asString(self):
        result = self.user.valid_title("Alma")
        self.assertEqual(False, result)




    def test_get_first_name_with_6_asString(self):
        result = self.user.valid_first_name("6")
        self.assertEqual(False, result)

    def test_get_first_name_with_125_asString(self):
            result = self.user.valid_first_name("125")
            self.assertEqual(False, result)

    def test_get_first_name_with_Alma_asString(self):
        result = self.user.valid_first_name("Alma")
        self.assertEqual(True, result)

    def test_get_first_name_with_Kovacs_asString(self):
        result = self.user.valid_first_name("Kovacs")
        self.assertEqual(True, result)




if __name__ == '__main__':
    unittest.main()
