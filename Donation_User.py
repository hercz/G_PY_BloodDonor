__author__ = 'Gazdik_Zsolt'

class User_Data(object):
    #data from the user
    def __init__(self):
        self.get_title()
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        self.get_weight()
        self.get_gender()
        

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
        pass





    def get_Date_of_Birth(self):
        pass

    def get_Last_Donation_Date(self):
        pass

    def get_was_she_he_sick(self):
        pass

    def get_unique_identifier(self):
        pass

    def get_Blood_Type(self):
        pass

    def get_Expiration_ID(self):
        pass

    def get_Email_Adress(self):
        pass

    def get_Mobil_Number(self):
        pass

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

    def Donor_is_Suitable_or_not(self):
        pass

    def print_donor(self):
        print(self.gender)

if __name__ == "__main__":
    bela = User_Data()
    bela.print_donor()