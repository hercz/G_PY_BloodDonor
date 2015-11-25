import unittest
import User_delete

class MyTestCase(unittest.TestCase):

    def test_if_id_equal_empty_string(self):
        result = User_delete.get_id("")
        self.assertEqual(False, result)





if __name__ == '__main__':
    unittest.main()
