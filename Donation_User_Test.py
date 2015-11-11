__author__ = 'Gazdik_Zsolt'

import unittest
from Donation_User import UserData


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData()

    def test_get_title_first(self):
        result = self.user.get_title("Y")
        self.assertTrue(result)
        pass



if __name__ == '__main__':
    unittest.main()
