import random
from datetime import datetime
import Menu

__author__ = 'Stark_Industries'


class UserData2(object):
    def print_separator_line(self):
        print("-" * 50)

    def valid_first_name(self, firstName):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for number in numbers:
            if number in firstName:
                print(
                    "I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
                return False
        if firstName.isdigit():
            print(
                "I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
            return False
        elif firstName == " ":
            return False
        else:
            return True

    def get_first_name(self):
        firstName = ""
        while firstName == "":
            firstName = input("Please enter your first name: ")
            if not self.valid_first_name(firstName):
                firstName = ""
            else:
                self.first_name = firstName

    def get_last_name(self):
        lastName = ""
        while lastName == "":
            lastName = input("Please enter your last name: ")
            if not self.valid_last_name(lastName):
                lastName = ""
            else:
                self.last_name = lastName

    def valid_last_name(self, lastName):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for number in numbers:
            if number in lastName:
                print(
                    "I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
                return False
        if lastName.isdigit():
            print(
                "I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
            return False
        elif lastName == " ":
            return False
        elif "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in lastName:
            print(
                "I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
            return False
        else:
            return True

    def get_full_name(self):
        fullName = self.first_name + "," + self.last_name
        self.full_name = fullName

    def get_weight(self):
        weight = ""
        while weight == "":
            weight = input("Please enter your weight in kg: ")
            if not self.valid_weight(weight):
                weight = ""
            else:
                self.weight = weight

    def valid_weight(self, weight):
        if weight.isdigit() and int(weight) >= 50:
            return True
        elif weight.isdigit() and int(weight) < 50:
            print("Your weight is too low to donate")
            Menu.ask_answer()
            return False
        elif weight.isalpha():
            return False
        elif weight == " ":
            return False

    def get_gender(self):
        gender = ""
        while gender == "":
            gender = input("Please choose your gender F/M: ")
            if not self.valid_gender(gender):
                print("You most type in one of the available genders:")
                gender = ""
            else:
                self.gender = gender

    def valid_gender(self, gender):
        available_genders = ["f", "m"]
        if not gender.lower() in available_genders:
            return False
        else:
            return True

    def get_birth_date(self):
        birthDate = ""
        while birthDate == "":
            birthDate = input("Please enter the date of your birth (YYYY.MM.DD): ")
            if not self.valid_birth_date(birthDate):
                birthDate = ""
            else:
                birth_date = datetime.strptime(birthDate, "%Y.%m.%d").date()
                self.birth_date = birth_date

    def valid_birth_date(self, birthDate):
        try:
            birth_date = datetime.strptime(birthDate, "%Y.%m.%d").date()
        except ValueError:
            print("Please enter a valid date!")
            return False
        else:
            return True

    def get_age(self):
        calculated_age = (datetime.now().date() - self.birth_date).days // 365
        return calculated_age

    def valid_age(self):
        if self.get_age() < 18:
            print("Sorry you are too young to donate")
            Menu.ask_answer()
        else:
            return True

    def get_last_donation_date(self):
        lastDonationDate = ""
        while lastDonationDate == "":
            lastDonationDate = input("Please enter the date of your last donation (YYYY.MM.DD): ")
            if not self.valid_birth_date(lastDonationDate):
                lastDonationDate = ""
            else:
                last_donation = datetime.strptime(lastDonationDate, "%Y.%m.%d").date()
                self.last_donation_date = last_donation

    def valid_last_donation_date(self, lastDonationDate):
        try:
            last_donation_d = datetime.strptime(lastDonationDate, "%Y.%m.%d").date()
        except ValueError:
            print("Please enter a valid date!")
            return False
        else:
            return True

    def available_for_donation_last_donation_date(self):
        elapsed_months = (datetime.now().date() - self.last_donation_date).days // 30
        if elapsed_months <= 3:
            print("You are not suitable because you was on donation not long ago.")
            Menu.ask_answer()

    def get_unique_identifier(self):
        unique_id = ""
        while unique_id == "":
            unique_id = input("Please enter your unique identifier aka ID: ")
            if not self.valid_identifier(unique_id):
                unique_id = ""
            else:
                self.identifier = unique_id

    def valid_identifier(self, unique_id):
        if len(unique_id) != 8:
            print("Your Identifier length is not enough, type in again: ")
            return False
        if unique_id[:6].isalpha() and unique_id[6:].isdigit():
            print("So that's a Passport ID.")
            return True
        elif unique_id[:6].isdigit() and unique_id[6:].isalpha():
            print("So it's an Identity Card.")
            return True
        else:
            return False

    def get_id_expiration(self):
        id_expiration = ""
        while id_expiration == "":
            id_expiration = input("Enter the expiration date of your unique identifier: ")
            if not self.valid_id_expiration(id_expiration):
                id_expiration = ""
            else:

                self.id_expiration = id_expiration

    def valid_id_expiration(self, id_expiration):
        try:
            id_expiration = datetime.strptime(id_expiration, "%Y.%m.%d").date()
            if not datetime.now().date() < id_expiration:
                print("Sorry you can't donate because your ID is expired.")
                answer = input("Do you want to go back to the main menu: Y/N")
                Menu.ask_answer()
        except ValueError:
            print("You have entered a wrong date type! It should be YYYY.MM.DD!")
            return False
        else:
            return True

    def get_was_she_he_sick(self):
        was_she_he_sick = ""
        while was_she_he_sick == "":
            was_she_he_sick = input("Have you been sick in the last three months? (Y, N): ")
            if not self.valid_was_she_he_sick(was_she_he_sick):
                print("This is an important question! Please write here the TRUTH!")
                was_she_he_sick = ""
            else:
                self.was_she_he_sick = was_she_he_sick

    def valid_was_she_he_sick(self, was_she_he_sick):
        available_answers = ["y", "n"]
        if not was_she_he_sick.lower() in available_answers:
            print("I hope you understand that we dont want sick donators..")
            Menu.ask_answer()
        else:
            return True

    def get_blood_type(self):
        blood_type = ""
        while blood_type == "":
            blood_type = input("Please enter your blood type: ")
            if not self.valid_blood_type(blood_type):
                print("Blood type can be only A, B, AB or 0 !")
                blood_type = ""
            else:
                self.blood_type = blood_type

    def valid_blood_type(self, blood_type):
        blood_types = ('a', 'b', 'ab', '0')
        if blood_type.lower() not in blood_types:
            return False
        else:
            return True

    def get_email_address(self):
        email_string = ""
        while email_string == "":
            email_string = input("E-mail (abc@xyz.hu/.com): ")
            email_list = email_string.split('@')
            if not self.valid_email_adress(email_list):
                print("Please enter your e-mail correctly! (abc@xyz.hu/.com)")
                email_string = ""
            else:
                self.email_string = email_string

    def valid_email_adress(self, email_list):
        if len(email_list) == 2 and (email_list[1].endswith(".hu") or email_list[1].endswith(".com")):
            return True

    def get_mobil_number_06_36(self):
        mobil_3606_string = ""
        while mobil_3606_string == "":
            mobil_3606_string = input("Your mobile number starts with (+36 or 06): ")
            if not self.validate_mobil_number_06_36(mobil_3606_string):
                print("Invalid format!")
                mobil_3606_string = ""
            else:
                self.mobil_num_06_36 = mobil_3606_string

    def validate_mobil_number_06_36(self, mobil_3606_string):
        if not (mobil_3606_string == '+36' or mobil_3606_string == '06'):
            return False
        else:
            return True

    def get_mobil_number_20_30_70(self):
        mobil_203070_string = ""
        while mobil_203070_string == "":
            mobil_203070_string = input("Your mobile provide identifier (20, 30 or 70): ")
            if not self.validate_mobil_number_20_30_70(mobil_203070_string):
                print("Invalid format!")
                mobil_203070_string = ""
            else:
                self.mobil_num_20_30_70 = mobil_203070_string

    def validate_mobil_number_20_30_70(self, mobil_203070_string):
        if not (mobil_203070_string == '20' or mobil_203070_string == '30' or mobil_203070_string == '70'):
            return False
        else:
            return True

    def get_mobil_number_the_rest(self):
        mobil_num_str = ""
        while mobil_num_str == "":
            mobil_num_str = input("Enter your mobil number (7 digits): ")
            if not self.validate_mobil_number_the_rest_(mobil_num_str):
                print("Invalid format!")
                mobil_num_str = ""
            else:
                self.mobil_num_rest = mobil_num_str

    def validate_mobil_number_the_rest_(self, mobil_num_str):
        if not (len(mobil_num_str) == 7 and mobil_num_str.isdigit()):
            return False
        else:
            return True

    def get_full_phone_number(self):
        mobil_string = self.mobil_num_06_36 + " " + self.mobil_num_20_30_70 + " " + self.mobil_num_rest
        self.phone_number = mobil_string

    def get_random_hemoglobin_donor_is_suitable_or_not(self):
        random_hemoglobin = random.randrange(80, 200, 1)
        self.hemoglobin = random_hemoglobin
        if random_hemoglobin >= 110:
            print("You are suitable for donation, your hemoglobin level is:", random_hemoglobin)
        else:
            print("Sorry you are not suitable for donation, your hemoglobin level is:", random_hemoglobin)
            Menu.ask_answer()

    def make_data_into_one_string(self):
        full_data = str(self.full_name) + "," + str(self.gender) + "," + str(self.identifier) + "," + \
                    str(self.email_string) + "," + str(self.blood_type) + "," + str(self.birth_date) + "," + \
                    str(self.get_age()) + "," + str(self.weight) + "," + str(self.last_donation_date) + "," + \
                    str(self.id_expiration) + "," + str(self.hemoglobin) + "," + str(self.was_she_he_sick)

        self.full_data_string = full_data

    def data_to_file(self):
        with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
            Donor_Text_File.write(self.full_data_string + "\n")

    def get_user(self):
        self.get_random_hemoglobin_donor_is_suitable_or_not()
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        self.get_weight()
        self.get_gender()
        self.get_birth_date()
        self.get_age()
        self.valid_age()
        self.get_last_donation_date()
        self.available_for_donation_last_donation_date()
        self.get_unique_identifier()
        self.get_id_expiration()
        self.valid_id_expiration(self.id_expiration)
        self.get_was_she_he_sick()
        self.get_blood_type()
        self.get_email_address()
        self.get_mobil_number_06_36()
        self.get_mobil_number_20_30_70()
        self.get_mobil_number_the_rest()
        self.get_full_phone_number()
        self.make_data_into_one_string()
        self.data_to_file()

if __name__ == '__main__':
    bela = UserData2().get_user()




