__author__ = 'Gazdik_Zsolt'

class User_Data(object):

    def __init__(self):
        self.get_Zip_Code()
        self.get_City()




    #Inputs, gets

    def get_Date_of_Event(self):
        pass

    def get_Start_Time(self):
        pass

    def get_End_Time(self):
        pass

    def get_Zip_Code(self):
        zip_code = ""
        while zip_code == "":
            zip_code = input("Please enter your ZIP code ")
            if len(zip_code) != 4:
                print("You must enter a valid ZIP code")
                zip_code = ""
            elif zip_code[0] == '0':
                print("Your first character can't be Zero")
                zip_code = ""
            elif not zip_code.isdigit():
                print("You must enter positive numbers ")
                zip_code = ""
            elif len(zip_code) == 4:
                self.zip_code = zip_code

    def get_City(self):
        city = ""
        city_names = ("miskolc", "kazincbarcika", "szerencs", "sarospatak")
        while city == "":
            city = input("Please enter your city name: ")
            if city.lower() not in city_names:
                print("You must fill this and city names must be: Miskolc, Kazincbarcika, Szerencs, Sarospatak")
                city = ""
        self.city = city.lower()


    def get_Adress(self):
        pass

    def get_Beds_Available(self):
        pass

    def get_Planned_Donor_Number(self):
        pass

    # FUNCTIONS

    def Registration_ten_days_before_date(self):
        pass

    def Datetime_Only_on_Weekdays(self):
        pass

    def Adress_Validation(self):
        pass

    def Calculate_Duration_in_Minutes(self):
        pass

    def Maximum_Donor_Number(self):
        pass

    def print_donor(self):
        print(self.zip_code)

if __name__ == "__main__":
    gaspar = User_Data()
    gaspar.print_donor()