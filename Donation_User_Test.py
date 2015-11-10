__author__ = 'Gazdik_Zsolt'

import unittest
from Donation_User import User_Data
#felesleges comment
class MyTestCase(unittest.TestCase):
    def test_get_title_return_false_with_numbers(self):
        person1 = User_Data()
        self.assertEqual("", person1.get_title("p"))

    def test_get_title_return_false_with_numberss(self):
        pass

if __name__ == '__main__':
    unittest.main()
