__author__ = 'Gazdik_Zsolt'

import unittest
from Donation_User2 import UserData2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = UserData2()

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

    def test_get_blood_type_with_Number_as_String(self):
        result = self.user.valid_blood_type("7")
        self.assertEqual(False, result)

    def test_get_blood_type_with_WrongString_Alma(self):
        result = self.user.valid_blood_type("alma")
        self.assertEqual(False, result)

    def test_get_blood_type_with_WrongString_eekezet(self):
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

    def test_get_mobile_number_06_36_with_10_as_wrong_input(self):
        result = self.user.validate_mobil_number_06_36("10")
        self.assertEqual(False, result)

    def test_get_mobile_number_06_36_with_80_as_wrong_input(self):
        result = self.user.validate_mobil_number_06_36("80")
        self.assertEqual(False, result)

    def test_get_mobile_number_06_36_with_alma_as_wrong_input(self):
        result = self.user.validate_mobil_number_06_36("alma")
        self.assertEqual(False, result)

    def test_get_mobile_number_06_36_with_06_as_Correct_input(self):
        result = self.user.validate_mobil_number_06_36("06")
        self.assertEqual(True, result)

    def test_get_mobile_number_20_30_70_with_10_as_wrong_input(self):
        result = self.user.validate_mobil_number_20_30_70("10")
        self.assertEqual(False, result)

    def test_get_mobile_number_20_30_70_with_80_as_wrong_input(self):
        result = self.user.validate_mobil_number_20_30_70("80")
        self.assertEqual(False, result)

    def test_get_mobile_number_20_30_70_with_alma_as_wrong_input(self):
        result = self.user.validate_mobil_number_20_30_70("alma")
        self.assertEqual(False, result)

    def test_get_mobile_number_20_30_70_with_06_as_Wrong_input(self):
        result = self.user.validate_mobil_number_20_30_70("06")
        self.assertEqual(False, result)

    def test_get_mobile_number_20_30_70_with_30_as_Correct_input(self):
        result = self.user.validate_mobil_number_20_30_70("30")
        self.assertEqual(True, result)

    def test_get_mobile_number_20_30_70_with_70_as_Correct_input(self):
        result = self.user.validate_mobil_number_20_30_70("70")
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
