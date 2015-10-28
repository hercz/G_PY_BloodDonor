__author__ = 'Gazdik_Zsolt'

class User_Data(object):
    #data from the user
    @staticmethod


    def get_name():
        entered_data_is_valid = False
        name = ""
        answer = ""
        while answer == "":
            answer = input("Do you have a title?:  Y/N: ")
            if answer == "Y" or answer == "y":
                title =input("In that Case enter your title: ") + " "
            elif answer == "N" or answer == "n":
                print("I see, you dont even have a title, poor boy!")
                title = ""
            else:
                answer = ""

        first_name = ""
        while first_name == "":
            first_name = input("Please enter your first name: ")
            if not first_name.isalpha():
                print("I really hope your name does not contain numbers or special characters or whitespace, check before you enter!")
                first_name = ""

        last_name = ""
        while last_name == "":
            last_name = input("Please enter your last name: ")
            if not last_name.isalpha():
                last_name = ""

        name = title + first_name + " " + last_name
        return name




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

if __name__ == "__main__":
    Donor1 = User_Data
    print(Donor1.get_name())