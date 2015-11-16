import random
from datetime import datetime

__author__ = 'Stark_Industries'


class UserData(object):

    def __init__(self   ):

        self.available_for_donation()

        self.print_separator_line()

        self.get_title()
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        self.get_gender()
        self.get_unique_identifier()
        self.get_email_address()
        self.get_mobil_number()
        self.get_blood_type()
        self.make_data_into_one_string()
        self.data_to_file()

        self.print_separator_line()

        self.print_donor_info()

    def available_for_donation(self):
        print("First we need some data from you to decide if you are suitable for donation.")
        self.get_birth_date_and_calculate_age()
        self.get_weight()
        self.get_last_donation_date()
        self.random_hemoglobin_donor_is_suitable_or_not()
        self.get_id_expiration()
        self.get_was_she_he_sick()
        print("Congratulations you are available for donation!")
        print("Now we need further more data from you to complete your registration.")

    def print_separator_line(self):
        print("-" * 50)

    def get_title(self):
        answer = ""
        while answer == "":
            answer = input("Do you have a title? (Y/N): ")
            if answer == "Y" or answer == "y":
                self.title = input("In that Case enter your title: ") + " "
            elif answer == "N" or answer == "n":
                self.title = ""
            else:
                answer = ""

    def get_first_name(self):
        first_name = ""
        while first_name == "":
            first_name = input("Please enter your first name: ")
            if not first_name.isalpha():
                print(
                    "I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
                first_name = ""
            else:
                self.first_name = first_name

    def get_last_name(self):
        last_name = ""
        while last_name == "":
            last_name = input("Please enter your last name: ")
            if not last_name.isalpha():
                last_name = ""
            else:
                self.last_name = last_name

    def get_full_name(self):
        full_name = self.first_name + "," + self.title + " " + self.last_name
        self.full_name = full_name
        full_name_without_title = self.first_name + "," + self.last_name
        self.name_without_title = full_name_without_title

    def get_weight(self):
        weight = ""
        while weight == "":
            weight = input("Please enter your weight in kg: ")
            if weight.isdigit() and int(weight) >= 50:
                self.weight = int(weight)
            elif weight.isdigit() and int(weight) < 50:
                print("Sorry you are not suitable for donation! You are below 50 kg.")
                exit()
            else:
                print("You must enter a positive integer! ")
                weight = ""

    def get_gender(self):
        gender = ""
        available_genders = ["f", "m"]
        while gender == "":
            gender = input("Please choose your gender F/M: ")
            if not gender.lower() in available_genders:
                print("You most type in one of the available genders:")
                gender = ""
            else:
                self.gender = gender

    def get_birth_date_and_calculate_age(self):
        birth_date = ""
        age = ""
        while True:
            date = input("Please enter the date of your birth (YYYY.MM.DD): ")
            try:
                birth_date = datetime.strptime(date, "%Y.%m.%d").date()
                age = (datetime.now().date() - birth_date).days // 365
                if age > 18:
                    break
                else:
                    print("Sorry, you are too young for blood donation!")
                    exit()
            except ValueError:
                print("Please enter a valid date!")
        self.birth_date = birth_date
        self.age = age

    def get_last_donation_date(self):
        last_donation_date = ""
        while True:
            date = input("Please enter the date of your last donation: ")
            try:
                last_donation_date = datetime.strptime(date, "%Y.%m.%d").date()
                elapsed_months = (datetime.now().date() - last_donation_date).days // 30
                if elapsed_months >= 3:
                    break
                else:
                    print("You are not suitable because you was on donation not long ago.")
                    exit()
            except ValueError:
                print("Please enter a valid date!")
        self.last_donation_date = last_donation_date

    def get_was_she_he_sick(self):
        was_she_he_sick = ""
        available_answers = ["y", "n"]
        while was_she_he_sick == "":
            was_she_he_sick = input("Have you been sick in the last three months? (Y, N): ")
            if not was_she_he_sick.lower() in available_answers:
                print("This is an important question! Please write here the TRUTH!")
                was_she_he_sick = ""
            else:
                self.was_she_he_sick = was_she_he_sick

    def get_unique_identifier(self):
        identifier = ""
        while identifier == "":
            identifier = input("Please enter your unique identifier aka ID: ")
            if len(identifier) != 8:
                print("Your Identifier length is not enough, type in again: ")
                identifier = ""
            elif identifier[:6].isalpha() and identifier[6:].isdigit():
                print("So that's a Passport ID.")
                self.identifier = identifier
            elif identifier[:6].isdigit() and identifier[6:].isalpha():
                print("So it's an Identity Card.")
                self.identifier = identifier
            else:
                print("Your ID is wrong, type in again(It must be an ID or Passport number): ")
                identifier = ""

    def get_id_expiration(self):
        id_expiration = ""
        while True:
            date = input("Enter the expiration date of your unique identifier: ")
            try:
                id_expiration = datetime.strptime(date, "%Y.%m.%d").date()
                if datetime.now().date() < id_expiration:
                    break
                else:
                    print("Sorry you can't donate because your ID is expired.")
                    exit()
            except ValueError:
                print("You have entered a wrong date type! It should be YYYY.MM.DD!")
        self.id_expiration = id_expiration


    def get_blood_type(self):
        blood_types = ('a', 'b', 'ab', '0')
        blood_type = ""
        while blood_type == "":
            blood_type = input("Please enter your blood type: ")
            if blood_type.lower() not in blood_types:
                print("Blood type can be only A, B, AB or 0 !")
                blood_type = ""
            else:
                self.blood_type = blood_type

    def get_email_address(self):
        email_string = ""
        while email_string == "":
            email_string = input("E-mail (abc@xyz.hu/.com): ")
            email_list = email_string.split('@')
            if len(email_list) == 2 and (email_list[1].endswith(".hu") or email_list[1].endswith(".com")):
                self.email_string = email_string
                return
            else:
                print("Please enter your e-mail correctly! (abc@xyz.hu/.com)")
                email_string = ""

    def get_mobil_number(self):
        mobil_3606_string = ""
        while mobil_3606_string == "":
            mobil_3606_string = input("Your mobile number starts with (+36 or 06): ")
            if not (mobil_3606_string == '+36' or mobil_3606_string == '06'):
                print("Invalid format!")
                mobil_3606_string = ""

        mobil_203060_string = ""
        while mobil_203060_string == "":
            mobil_203060_string = input("Your mobile provide identifier (20, 30 or 70): ")
            if not (mobil_203060_string == '20' or mobil_203060_string == '30' or mobil_203060_string == '70'):
                print("Invalid format!")
                mobil_203060_string = ""

        mobil_num_str = ""
        while mobil_num_str == "":
            mobil_num_str = input("Enter your mobil number (7 digits): ")
            if not (len(mobil_num_str) == 7 and mobil_num_str.isdigit()):
                print("Invalid format!")
                mobil_num_str = ""

        mobil_string = mobil_3606_string + mobil_203060_string + mobil_num_str
        self.mobil_string = mobil_string

    def random_hemoglobin_donor_is_suitable_or_not(self):
        random_hemoglobin = random.randrange(80, 200, 1)
        self.hemoglobin= random_hemoglobin
        if random_hemoglobin >= 110:
            print("You are suitable for donation, your hemoglobin level is:", random_hemoglobin)
        else:
            print("Sorry you are not suitable for donation, your hemoglobin level is:", random_hemoglobin)
            exit()

    def print_donor_info(self):
        print("""Name:       {0}\nWeight:     {1} kg\nBirth date: {2}\nAge:        {3} years old\nEmail:      {4}
        """.format(self.full_name,
                   self.weight,
                   self.birth_date,
                   self.age,
                   self.email_string))

    def make_data_into_one_string(self):
        full_data = str(self.name_without_title) + "," + str(self.gender) + "," + str(self.identifier) + "," + \
                    str(self.email_string) + "," + str(self.blood_type) + "," + str(self.birth_date) + "," + \
                    str(self.age) + "," + str(self.weight) + "," + str(self.last_donation_date) + "," + \
                    str(self.id_expiration) + "," + str(self.hemoglobin) + "," + str(self.was_she_he_sick)

        self.full_data_string = full_data

    def data_to_file(self):
        with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
            Donor_Text_File.write(self.full_data_string + "\n")

if __name__ == '__main__':
    UserData()