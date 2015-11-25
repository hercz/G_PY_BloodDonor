import unittest
from Donation_Location2 import UserData

__author__ = 'Stark_Industries'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData()

    def test_if_date_is_Empty(self):
        result = self.user.check_date_of_event("")
        self.assertEqual(False, result)

    def test_if_date_not_3Parts(self):
        result = self.user.check_date_of_event("2015.1118")
        self.assertEqual(False, result)

    def test_if_date_is_not_digit(self):
        result = self.user.check_date_of_event("2015.11.a8")
        self.assertEqual(False, result)

    def test_if_date_not_exist(self):
        result = self.user.check_date_of_event("2015.11.40")
        self.assertEqual(False, result)

    def test_if_date_is_out_of_10_day(self):
        result = self.user.validate_date_of_event("2015.11.20")
        self.assertEqual(False, result)

    def test_if_date_is_on_weekdays(self):
        result = self.user.validate_date_of_event("2015.12.19")
        self.assertEqual(False, result)

    def test_if_time_is_empty(self):
       result = self.user.check_time("")
       self.assertEqual(False, result)

    def test_if_time_is_a_whitespace(self):
       result = self.user.check_time(" : ")
       self.assertEqual(False, result)
    
    def test_if_time_is_alphabet(self):
       result = self.user.check_time("aa:ss")
       self.assertEqual(False, result)

    def test_if_time_is_not_2Parts(self):
       result = self.user.check_time("15:45:45")
       self.assertEqual(False, result)

    def test_if_time_is_exist(self):
       result = self.user.check_time("87:15")
       self.assertEqual(False, result)

    def test_if_zip_code_is_empty(self):
       result = self.user.validate_zip_code("")
       self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
