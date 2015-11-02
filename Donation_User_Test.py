__author__ = 'Vegh Adam es Benedek Balazs'

import unittest
from Donation_User import User_Data


class MyTestCase(unittest.TestCase):
    def test_valid_weight_string(self):
        self.assertFalse(User_Data.valid_weight("I don't know"))

    def test_valid_weight_negative(self):
        self.assertFalse(User_Data.valid_weight("-50"))

    def test_get_weight_below_50(self):
        with self.assertRaises(SystemExit):
            User_Data.valid_weight("49")

    def test_get_weight_above_50(self):
        self.assertTrue(User_Data.valid_weight("60"))



    def test_check_date_string_1(self):
        self.assertFalse(User_Data.check_date_string("gsdkjhgs"))

    def test_check_date_string_2(self):
        self.assertFalse(User_Data.check_date_string("2005.02.31"))

    def test_check_date_string_3(self):
        self.assertTrue(User_Data.check_date_string("2005.12.05"))





if __name__ == '__main__':
    unittest.main()
