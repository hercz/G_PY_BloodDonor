__author__ = 'Gazdik_Zsolt'
import random
import datetime

class User_Data(object):
    #data from the user

    @staticmethod
    def date_string_is_valid(date_string: str):
        splitted_date = date_string.split(".")
        if not (len(splitted_date) == 3 and splitted_date[0].isdigit() and
            splitted_date[1].isdigit() and splitted_date[2].isdigit()):
            return False
        try:
            datetime.date(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2]))
            return True
        except ValueError as vex:
            print("This date is not correct!")
            return False


    def __init__(self):

        self.available_for_donation()

        self.get_title()
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        self.get_gender()
        self.get_unique_identifier()
        self.get_email_address()
        self.get_blood_type()




    def available_for_donation(self):
        print("We need these data before you can go on!")
        self.get_Date_of_Birth()
        self.donor_age()
        self.get_weight()
        self.get_Last_Donation_Date()
        self.random_hemogoblin_donor_is_suitable_or_not()
        self.get_Expiration_ID()
        self.get_was_she_he_sick()
        print("Congratulations you are available for donation, now we need your other data")

    def get_title(self):
        answer = ""
        while answer == "":
            answer = input("Do you have a title?:  Y/N: ")
            if answer == "Y" or answer == "y":
                self.title = input("In that Case enter your title: ") + " "
            elif answer == "N" or answer == "n":
                print("I see, you dont even have a title, poor boy!")
                self.title = ""
            else:
                answer = ""

    def get_first_name(self):
        first_name = ""
        while first_name == "":
            first_name = input("Please enter your first name: ")
            if not first_name.isalpha():
                print("I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
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
        full_name = self.last_name + ", " + self.first_name + " " + self.title
        self.full_name = full_name

    def get_weight(self):
        weight = ""
        while weight == "":
            weight = input("Please enter your weight in Kg: ")
            if weight.isdigit() and int(weight) >= 50:
                self.weight = int(weight)
            elif weight.isdigit() and int(weight) < 50:
                print("Sorry you are not suitable for donation! ")
                exit()
            else:
                print("You must type in positive integers, above 50Kg ")
                weight = ""

    def get_gender(self):
        gender = ""
        available_genders = ["f", "m"]
        while gender == "":
            gender = input("Please choose your gender F/M")
            if not gender.lower() in available_genders:
                print("You most type in one of the available genders:")
                gender = ""
            else:
                self.gender = gender


    def get_Date_of_Birth(self):
        date = ""
        while date == "":
            date = input("Please enter the Date of Your Birth: YYYY.MM.DD ")
            if User_Data.date_string_is_valid(date) is False:
                print("Please enter a valid Date eg: YYYY.MM.DD, e.g: 1991.05.26 ")
                date = ""
            else:
                self.date_of_birth = date


    def get_Last_Donation_Date(self):
        donation_date = ""
        today = datetime.date.today()
        while donation_date == "":
            donation_date = input("Please enter the date of your last donation: ")
            if User_Data.date_string_is_valid(donation_date) is False:
                print("Please enter a valid Date eg: YYYY.MM.DD, e.g: 1991.05.26 ")
                donation_date = ""
            else:
                donation_date = datetime.datetime.strptime(donation_date, "%Y.%m.%d").date()
                self.donation_date = (today - donation_date).days > 90
            if self.donation_date is False:
                print("You are not suitable because you was on Donation not long ago")
                exit()

    def get_was_she_he_sick(self):
        was_she_he_sick = ""
        available_answers = ["y", "n"]
        while was_she_he_sick == "":
            was_she_he_sick = input("Have you been sick in the last three months? (Y, N)")
            if not was_she_he_sick.lower() in available_answers:
                print("This is an important question! Please write here the TRUTH!")
                was_she_he_sick = ""
            else:
                self.get_was_she_he_sick = was_she_he_sick

    def get_unique_identifier(self):
        identifier = ""
        while identifier == "":
            identifier = input("Please enter your unique identifier aka ID: ")
            if len(identifier) != 8:
                print("Your Identifier length is not enough, type in again: ")
                identifier = ""
            elif identifier[:6].isalpha() and identifier[6:].isdigit():
                print("So that's a Passport ID")
                self.identifier = identifier
            elif identifier[:6].isdigit() and identifier[6:].isalpha():
                print("So it's an Identity Card")
                self.identifier = identifier
            else:
                print("Your ID is wrong, type in again(It must be an ID or Passport number): ")
                identifier = ""


    def get_Expiration_ID(self):
        user_id = ""
        today = datetime.date.today()
        while user_id == "":
            user_id = input("Enter the experiation date of your Unique Identifier: ")
            if User_Data.date_string_is_valid(user_id) is False:
                print("Please enter a valid Date eg: YYYY.MM.DD, e.g: 1991.05.26 ")
                user_id = ""
            else:
                user_id = datetime.datetime.strptime(user_id, "%Y.%m.%d").date()
                self.expiration = today < user_id
            if self.expiration is False:
                print("Sorry you can't donate because your ID is expired")
                exit()


    """
    def get_blood_type(self):
        blood_type = ""
        blood_type = input("Please enter your blood type(eg: A+): ")
        while (blood_type[len(blood_type)-1:] != "+" and\
               blood_type[len(blood_type)-1:] != "-")\
            or (blood_type[:len(blood_type)-1].upper() != "A" and\
                blood_type[:len(blood_type)-1].upper() != "B" and\
                blood_type[:len(blood_type)-1].upper() != "AB"):
            print("Incorrect input!")
            blood_type = input("Please enter your blood type(eg: A+): ")
        self.get_blood_type = blood_type.upper()
    """

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

    def donor_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.date_of_birth,"%Y.%m.%d").date()
        age = (today - birth_date).days // 365
        if age < 18:
            print("Sorry you are too young! ")
            exit()
        else:
            self.age = age

    def random_hemogoblin_donor_is_suitable_or_not(self):
        random_hemogoblin = random.randrange(80,200,1)
        if random_hemogoblin >= 110:
            print("Donor is suitable for donation, your hemogoblin:",random_hemogoblin)
        else:
            print("Sorry you are not suitable for donation, your hemogoblin:",random_hemogoblin)
            exit()

    def data_dictionary(self):
        data = {"name" : self.full_name,
                "weight" : self.weight,
                "date of birt" : self.date_of_birth,
                "age" : self.age,
                "e-mail" : self.email_string}
        return data

    def print_donor(self):
        print(self.age)

if __name__ == "__main__":
    bela = User_Data()
    bela.print_donor()
    print(bela.data_dictionary())