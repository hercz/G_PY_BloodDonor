__author__ = 'Gazdik_Zsolt'

class User_Data(object):
    #data from the user
    def __init__(self):
        self.get_title()
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        

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
        self.first_name = ""
        while self.first_name == "":
            self.first_name = input("Please enter your first name: ")
            if not self.first_name.isalpha():
                print("I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
                self.first_name = ""

    def get_last_name(self):
        self.last_name = ""
        while self.last_name == "":
            self.last_name = input("Please enter your last name: ")
            if not self.last_name.isalpha():
                self.last_name = ""

    def get_full_name(self):
        self.full_name = self.title + self.first_name + " " + self.last_name





    def get_weight(self):
        pass

    def get_gender(self):
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
        print(self.full_name)


if __name__ == "__main__":
    bela = User_Data()
    bela.print_donor()