from datetime import datetime
__author__ = 'Stark_Industries'
Józsibácsi
class UserData(object):

    def __init__(self):
        self.get_date_of_event()
        self.get_start_and_end_time()
        self.calculate_duration_in_minutes()
        self.get_beds_available()
        self.calculate_max_donor_number()
        self.get_zip_code()
        self.get_city()
        self.get_address()
        self.get_planned_donor_number()
        self.get_number_of_successful_donations()
        self.calculate_result_of_donation_by_percentage()

    def get_date_of_event(self):
        date_of_event = ""
        while True:
            date = input("Please enter the date of the donation (YYYY.MM.DD): ")
            try:
                date_of_event = datetime.strptime(date, "%Y.%m.%d").date()
                weekday = date_of_event.isoweekday()
                days_left = (date_of_event - datetime.now().date()).days
                if weekday <= 5 and days_left >= 10:
                    break
                else:
                    print("Blood donations should be only on weekdays and at least 10 days from the current date.")
            except ValueError:
                print("You have entered a wrong date type! It should be YYYY.MM.DD!")
        self.date_of_event = date_of_event

    def get_start_and_end_time(self):
        start_time = ""
        end_time = ""
        while True:
            start = input("Please enter the start time of the donation (HH:MM): ")
            end = input("Please enter the end time of the donation (HH:MM): ")
            try:
                start_time = datetime.strptime(start, "%H:%M")
                end_time = datetime.strptime(end, "%H:%M")
                if start_time < end_time:
                    break
                else:
                    print("Start time can not be later than end time!")
            except ValueError:
                print("You have entered a wrong time type! It should be HH:MM!")
        self.start_time = start_time
        self.end_time = end_time

    def get_zip_code(self):
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

    def get_city(self):
        city = ""
        city_names = ("miskolc", "kazincbarcika", "szerencs", "sarospatak")
        while city == "":
            city = input("Please enter your city name: ")
            if city.lower() not in city_names:
                print("You must fill this and city names must be: Miskolc, Kazincbarcika, Szerencs, Sarospatak")
                city = ""
        self.city = city.lower()

    def get_address(self):
        address = ""
        while address == "":
            address = input("Please enter your address: ")
            if len(address) > 25:
                print("Address should be less then 25 characters!")
                address = ""
        self.address = address

    def get_beds_available(self):
        available_beds = ""
        while available_beds == "":
            available_beds = input("Please enter the number of available beds: ")
            if not available_beds.isdigit():
                print("Please enter a positive integer!")
                available_beds = ""
            if available_beds == "0":
                print("You should enter a positive integer!")
                available_beds = ""
        self.available_beds = int(available_beds)

    def get_planned_donor_number(self):
        planned_donor_number = ""
        while planned_donor_number == "":
            planned_donor_number = input("Please enter the planned donor number: ")
            if not planned_donor_number.isdigit() or planned_donor_number <= "0":
                print("Please enter a positive integer!")
                planned_donor_number = ""
        self.planned_donor_number = planned_donor_number

    def get_number_of_successful_donations(self):
        number_of_successful_donations = ""
        while number_of_successful_donations == "":
            number_of_successful_donations = input("Please enter the number of the successful donations here: ")
            if not number_of_successful_donations.isdigit() or number_of_successful_donations <= "0":
                print("Please enter a positive integer!")
                number_of_successful_donations = ""
        self.number_of_successful_donations = number_of_successful_donations

    def calculate_duration_in_minutes(self):
        duration_in_minutes = (self.end_time - self.start_time).total_seconds() // 60
        self.duration_in_minutes = int(duration_in_minutes)

    def calculate_max_donor_number(self):
        preparation_time = 30
        donation_time = 30

        max_donor_number = ((self.duration_in_minutes - preparation_time) / donation_time) * self.available_beds
        self.maximum_donor_number = max_donor_number

    def calculate_result_of_donation_by_percentage(self):
        result_of_donation_by_percentage = int(100 * int(self.number_of_successful_donations) / int(self.maximum_donor_number))
        print("This is %d%% of the planned number of donors." % result_of_donation_by_percentage)
        if result_of_donation_by_percentage < 20:
            print("This donation was unsuccessful, not worth to organise there again.")
        elif 20 <= result_of_donation_by_percentage < 75:
            print("This donation was a normal event.")
        elif 75 <= result_of_donation_by_percentage < 110:
            print("This donation was successful!")
        elif 75 <= result_of_donation_by_percentage:
            print("This donation was outstanding!")

if __name__ == "__main__":
    UserData()
