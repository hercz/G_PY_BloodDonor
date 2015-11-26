import unittest
from Donation_Location import UserData

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

    def test_if_date_is_correct(self):
        result = self.user.validate_date_of_event("2080.12.18")
        self.assertEqual(True, result)

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

    def test_if_time_is_not_exist(self):
        result = self.user.check_time("87:15")
        self.assertEqual(False, result)

    def test_if_time_is_correct(self):
        result = self.user.check_time("12:23")
        self.assertEqual(True, result)

    def test_if_end_time_stands_before_start_time(self):
        result = self.user.validate_end_time("12:23", "9:00")
        self.assertEqual(False, result)

    def test_if_duration_less_than_30_minutes(self):
        result = self.user.validate_end_time("12:10", "12:20")
        self.assertEqual(False, result)

    def test_if_start_time_and_end_time_are_correct(self):
        result = self.user.validate_end_time("12:35", "18:40")
        self.assertEqual(True, result)

    def test_if_zip_code_is_empty(self):
        result = self.user.validate_zip_code("")
        self.assertEqual(False, result)

    def test_if_zip_code_is_not_4_chars(self):
        result = self.user.validate_zip_code("123")
        self.assertEqual(False, result)

    def test_if_zip_code_starts_with_zero(self):
        result = self.user.validate_zip_code("0123")
        self.assertEqual(False, result)

    def test_if_zip_code_isalpha(self):
        result = self.user.validate_zip_code("abcd")
        self.assertEqual(False, result)

    def test_if_zip_code_is_correct(self):
        result = self.user.validate_zip_code("1234")
        self.assertEqual(True, result)

    def test_if_city_is_empty(self):
        result = self.user.validate_city("")
        self.assertEqual(False, result)

    def test_if_city_is_contains_whitespace(self):
        result = self.user.validate_city("Mi sk ol c")
        self.assertEqual(False, result)

    def test_if_city_is_contains_two_cities(self):
        result = self.user.validate_city("Miskolc Kazincbarcika")
        self.assertEqual(False, result)

    def test_if_city_is_correct(self):
        result = self.user.validate_city("Miskolc")
        self.assertEqual(True, result)

    def test_if_address_is_empty(self):
        result = self.user.validate_address("")
        self.assertEqual(False, result)

    def test_if_address_just_whitespaces(self):
        result = self.user.validate_address("           ")
        self.assertEqual(False, result)

    def test_if_address_contains_commas_and_whitespaces(self):
        result = self.user.validate_address("3535,   Miskolc,   Eper")
        self.assertEqual("3535 Miskolc Eper", result)

    def test_if_address_more_than_25_chars(self):
        result = self.user.validate_address("asdsdgsgdhfjhgjgjfdggfgrrgd")
        self.assertEqual(False, result)

    def test_bed_isEmpty(self):
        result = self.user.validate_available_beds("")
        self.assertEqual(False, result)

    def test_bed_isNumber(self):
        result = self.user.validate_available_beds("asd")
        self.assertEqual(False, result)

    def test_bed_isNegative(self):
        result = self.user.validate_available_beds("-21")
        self.assertEqual(False, result)

    def test_plannedDonor_isEmpty(self):
        result = self.user.validate_planned_donor_number("")
        self.assertEqual(False, result)

    def test_plannedDonor_isNegative(self):
        result = self.user.validate_planned_donor_number("-25")
        self.assertEqual(False, result)

    def test_successDonation_isEmpty(self):
        result = self.user.validate_number_of_successful_donations("")
        self.assertEqual(False, result)

    def test_successDonation_isNegative(self):
        result = self.user.validate_number_of_successful_donations("-89")
        self.assertEqual(False, result)

if __name__ == '__main__':
    unittest.main()
