import unittest
from Donation_Location2 import UserData

__author__ = 'Stark_Industries'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData()

    def test_if_date_is_empty(self):
        result = self.user.check_date_of_event("")
        self.assertEqual(False, result)

    def test_if_date_is_empty(self):
        result = self.user.check_date_of_event("")
        self.assertEqual(False, result)



if __name__ == '__main__':
    unittest.main()
