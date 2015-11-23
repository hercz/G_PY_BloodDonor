__author__ = 'Gazdik_Zsolt'

import unittest
from Donation_User2 import UserData2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData2()

    # def test_get_title_withEmptyString(self):
    #     result = self.user.valid_title("")
    #     self.assertEqual(False, result)
    #
    # def test_get_title_with_T_asString(self):
    #     result = self.user.valid_title("T")
    #     self.assertEqual(False, result)
    #
    # def test_get_title_with_Y_asString(self):
    #     result = self.user.valid_title("Y")
    #     self.assertEqual(True, result)
    #
    # def test_get_title_with_N_asString(self):
    #     result = self.user.valid_title("N")
    #     self.assertEqual(True, result)
    #
    # def test_get_title_with_Alma_asString(self):
    #     result = self.user.valid_title("Alma")
    #     self.assertEqual(False, result)

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

    def test_get_first_name_with_string_whitespace(self):
        result = self.user.valid_first_name(" ")
        self.assertEqual(False, result)





    def test_get_last_name_with_Number6(self):
        result = self.user.valid_last_name("6")
        self.assertEqual(False, result)

    def test_get_last_name_with_Number125(self):
            result = self.user.valid_last_name("125")
            self.assertEqual(False, result)

    def test_get_last_name_with_stringAlma(self):
        result = self.user.valid_last_name("Alma")
        self.assertEqual(True, result)

    def test_get_last_name_with_stringKovacs(self):
        result = self.user.valid_last_name("Kovacs")
        self.assertEqual(True, result)

    def test_get_last_name_with_string_whitespace(self):
        result = self.user.valid_last_name(" ")
        self.assertEqual(False, result)





    def test_get_weight_with_numberBelow50(self):
        result = self.user.valid_weight("6")
        self.assertEqual(False, result)

    def test_get_weight_with_numberOver50(self):
            result = self.user.valid_weight("125")
            self.assertEqual(True, result)

    def test_get_weight_with_string_Alma(self):
        result = self.user.valid_weight("Alma")
        self.assertEqual(False, result)

    def test_get_weight_with_string_Kovacs(self):
        result = self.user.valid_weight("Kovacs")
        self.assertEqual(False, result)

    def test_get_weight_with_string_whitespace(self):
        result = self.user.valid_weight(" ")
        self.assertEqual(False, result)





    def test_get_gender_with_String_P(self):
        result = self.user.valid_gender("P")
        self.assertEqual(False, result)

    def test_get_gender_with_String_Dot(self):
        result = self.user.valid_gender(".")
        self.assertEqual(False, result)

    def test_get_gender_with_String_Whitespace(self):
        result = self.user.valid_gender(" ")
        self.assertEqual(False, result)

    def test_get_gender_with_String_M(self):
        result = self.user.valid_gender("M")
        self.assertEqual(True, result)

    def test_get_gender_with_String_m(self):
        result = self.user.valid_gender("m")
        self.assertEqual(True, result)

    def test_get_gender_with_String_F(self):
        result = self.user.valid_gender("F")
        self.assertEqual(True, result)




    def test_get_birthDate_with_Number_as_string(self):
        result = self.user.valid_birth_date("26")
        self.assertEqual(False, result)

    def test_get_birthDate_with_Alma_as_string(self):
        result = self.user.valid_birth_date("Alma")
        self.assertEqual(False, result)

    def test_get_birthDate_with_WrongYear_as_string(self):
        result = self.user.valid_birth_date("199991.05.26")
        self.assertEqual(False, result)

    def test_get_birthDate_with_WrongMonth_as_string(self):
        result = self.user.valid_birth_date("1991.13.15")
        self.assertEqual(False, result)

    def test_get_birthDate_with_WrongDay_as_string(self):
        result = self.user.valid_birth_date("1991.12.45")
        self.assertEqual(False, result)

    def test_get_birthDate_with_RightDate_as_string(self):
        result = self.user.valid_birth_date("1991.12.4")
        self.assertEqual(True, result)







if __name__ == '__main__':
    unittest.main()
