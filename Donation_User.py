__author__ = 'Gazdik_Zsolt'
import random


class User_Data(object):
    #data from the user
    def __init__(self):

        self.get_Date_of_Birth()
        self.get_title()
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        self.get_weight()
        self.get_gender()
        self.get_unique_identifier()
        self.get_email_address()
        self.get_was_she_he_sick()
        self.get_blood_type()
        self.random_hemogoblin_donor_is_suitable_or_not()


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
        full_name = self.title + self.first_name + " " + self.last_name
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

    @staticmethod
    def date_verification(date):
        date_parts = date.split(".")
        if len(date_parts) == 3:
            for part in date_parts:
                if not part.isdigit():
                    print("Bad date format ! It should be YYYY.MM.DD !")
                    return False
            return True
        print("Bad date format ! It should be YYYY.MM.DD !")
        return False

    @staticmethod
    def date_string_is_valid(date_string: str):
        splitted_date = date_string.split(".")
        return len(splitted_date) == 3 and \
            splitted_date[0].isdigit() and int(splitted_date[0]) in range(1910,2015) and\
            splitted_date[1].isdigit() and int(splitted_date[1]) in range(1, 13) and \
            splitted_date[2].isdigit() and int(splitted_date[2]) in range(1, 32)


    def get_Date_of_Birth(self):
        date = ""
        while date == "":
            date = input("Please enter the Date of Your Birth: YYYY.MM.DD ")
            if User_Data.date_string_is_valid(date) is False:
                print("Please enter a valid Date eg: YYYY.MM.DD, e.g: 1991.05.26 ")
                date = ""


    def get_Last_Donation_Date(self):


        pass

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
            elif identifier[:2].isalpha() and identifier[2:].isdigit():
                print("So that's a passport ID")
                self.identifier = identifier
            elif identifier[:2].isdigit() and identifier[2:].isalpha():
                print("So it's an Identity Card")
                self.identifier = identifier
            else:
                print("Your ID is wrong, type in again(It must match with the ID or the Passport): ")
                identifier = ""


    def get_Expiration_ID(self):
            user_id = input("Enter the experiation date of your Unique Identifier: ")


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

    # And now functions

    def Suitable_For_donation(self):
        pass

    def Donor_Age(self):
        pass

    def Id_is_not_Expired(self):
        pass

    def Personal_Document(self):
        pass

    def Data_In_Table_Form(self):
        pass

    def Random_Number(self):
        pass

    def random_hemogoblin_donor_is_suitable_or_not(self):
        random_hemogoblin = random.randrange(80,200,1)
        if random_hemogoblin >= 110:
            print("Donor is suitable for donation")
        else:
            print("Sorry you are not suitable for donation!")
            exit()

    def print_donor(self):
        print(self.weight)

if __name__ == "__main__":
    bela = User_Data()
    bela.print_donor()