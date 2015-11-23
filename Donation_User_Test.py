__author__ = 'Gazdik_Zsolt'

import unittest
from Donation_User2 import UserData2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData2()
        self.birth_date = "1991.02.12"

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





    # def test_get_weight_with_numberBelow50(self):
    #     result = self.user.valid_weight("6")
    #     self.assertEqual(False, result)

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

    # def test_get_age(self):
    #     result = self.user.valid_age()
    #     self.assertEqual(True, result)

    def test_get_lastDonationDate_with_Number_as_string(self):
        result = self.user.valid_last_donation_date("26")
        self.assertEqual(False, result)

    def test_get_lastDonationDate_with_Alma_as_string(self):
        result = self.user.valid_last_donation_date("Alma")
        self.assertEqual(False, result)

    def test_get_lastDonationDatee_with_WrongYear_as_string(self):
        result = self.user.valid_last_donation_date("199991.05.26")
        self.assertEqual(False, result)

    def test_get_lastDonationDate_with_WrongMonth_as_string(self):
        result = self.user.valid_last_donation_date("1991.13.15")
        self.assertEqual(False, result)

    def test_get_lastDonationDate_with_WrongDay_as_string(self):
        result = self.user.valid_last_donation_date("1991.12.45")
        self.assertEqual(False, result)

    def test_get_lastDonationDate_with_RightDate_as_string(self):
        result = self.user.valid_last_donation_date("2002.12.4")
        self.assertEqual(True, result)




    def test_get_uniqueId_with_lessCharacter(self):
        result = self.user.valid_identifier("123lp")
        self.assertEqual(False, result)

    def test_get_uniqueId_with_onlyDigits(self):
        result = self.user.valid_identifier("1234678")
        self.assertEqual(False, result)

    def test_get_uniqueId_with_onlyLetters(self):
        result = self.user.valid_identifier("asdkloip")
        self.assertEqual(False, result)

    def test_get_uniqueId_with_RightInput_IdentityCard(self):
        result = self.user.valid_identifier("123456lp")
        self.assertEqual(True, result)

    def test_get_uniqueId_with_RightInput_PassportID(self):
        result = self.user.valid_identifier("lpkoji45")
        self.assertEqual(True, result)




    def test_get_ID_expiration_with_number(self):
        result = self.user.valid_id_expiration("26")
        self.assertEqual(False, result)

    def test_get_ID_expiration_with_string_Alma(self):
        result = self.user.valid_id_expiration("Alma")
        self.assertEqual(False, result)

    def test_get_ID_expiration_with_WrongYear(self):
        result = self.user.valid_id_expiration("199991.05.26")
        self.assertEqual(False, result)

    def test_get_ID_expiration_with_WrongMonth(self):
        result = self.user.valid_id_expiration("1991.13.15")
        self.assertEqual(False, result)

    def test_get_ID_expiration_with_WrongDay(self):
        result = self.user.valid_id_expiration("1991.12.45")
        self.assertEqual(False, result)

    def test_get_ID_expiration_with_GoodInputs(self):
        result = self.user.valid_id_expiration("2018.12.4")
        self.assertEqual(True, result)

    # def test_get_ID_expiration_with_WrongInputs(self):
    #     result = self.user.valid_id_expiration("2010.12.4")
    #     self.assertEqual(False, result)


    def test_was_she_he_sick_with_l_StringInput(self):
        result = self.user.valid_was_she_he_sick("l")
        self.assertEqual(False, result)

    def test_was_she_he_sick_with_é_stringInput(self):
        result = self.user.valid_was_she_he_sick("l")
        self.assertEqual(False, result)

    def test_was_she_he_sick_with_Number_as_string_Input(self):
        result = self.user.valid_was_she_he_sick("6")
        self.assertEqual(False, result)

    def test_was_she_he_sick_with_CorrectInputLower(self):
        result = self.user.valid_was_she_he_sick("y")
        self.assertEqual(True, result)

    def test_was_she_he_sick_with_CorrectInputUpper(self):
        result = self.user.valid_was_she_he_sick("N")
        self.assertEqual(True, result)




    def test_get_blood_type_with_Number_as_String(self):
        result = self.user.valid_blood_type("7")
        self.assertEqual(False, result)

    def test_get_blood_type_with_WrongString_Alma(self):
        result = self.user.valid_blood_type("alma")
        self.assertEqual(False, result)

    def test_get_blood_type_with_WrongString_é(self):
        result = self.user.valid_blood_type("é")
        self.assertEqual(False, result)

    def test_get_blood_type_with_WrongString_O(self):
        result = self.user.valid_blood_type("O")
        self.assertEqual(False, result)

    def test_get_blood_type_with_A_as_string(self):
        result = self.user.valid_blood_type("A")
        self.assertEqual(True, result)

    def test_get_blood_type_with_EmptyString(self):
        result = self.user.valid_blood_type("")
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
