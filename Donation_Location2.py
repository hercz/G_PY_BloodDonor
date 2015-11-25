from datetime import datetime
import csv
import random

__author__ = 'Stark_Industries'


class UserData(object):
    def parse_time(self, time_str):
        return datetime.strptime(time_str, '%H:%M')

    def check_date_of_event(self, date_str):
        date_list = date_str.split(".")
        if date_str == "":
            print("Date of event can not be empty!")
            return False
        elif len(date_list) != 3:
            print("Bad date format! It should be 'YYYY.MM.DD' (e.g. 2015.12.26.)!")
            return False
        else:
            for date in date_list:
                if not date.isdigit():
                    print("Date should only contain numbers!")
                    return False
        try:
            return datetime.strptime(date_str, "%Y.%m.%d").date()
        except AttributeError and ValueError:
            print("This date does not exist!")
            return False

    def check_time(self, time_str):
        time_list = time_str.split(":")
        if len(time_list) != 2:
            print("Bad time format! You must fill the time correctly! It should be HH:MM (e.g. 15:46)!")
            return False
        else:
            for time in time_list:
                if not time.isdigit():
                    print("Time must be a number!")
                    return False
        try:
            self.parse_time(time_str)
            return True
        except ValueError:
            print("This time doesn't exist!")
            return False

    def validate_date_of_event(self, date_of_event_str):
        weekday = self.check_date_of_event(date_of_event_str).isoweekday()
        days_left = (self.check_date_of_event(date_of_event_str) - datetime.now().date()).days
        if weekday <= 5 and days_left >= 10:
            return True
        else:
            print("Blood donations should be only on weekdays and at least 10 days from the current date.")
            return False

    def validate_end_time(self, start_time_str, end_time_str):
        preparation_time = 30
        if ((self.parse_time(end_time_str) - self.parse_time(start_time_str)).total_seconds() / 60) < 0:
            print("The end time must be later than start time! "
                  "(I think you don't want to stay for the following day... idiot!)")
            return False
        elif ((self.parse_time(end_time_str) - self.parse_time(start_time_str))
                .total_seconds() / 60) <= preparation_time:
            print("The duration of event must be more than 30 minutes!")
            return False
        return True

    def validate_zip_code(self, zip_code):
        if zip_code == "":
            print("ZIP code can not be empty!")
            return False
        elif len(zip_code) != 4:
            print("You must enter a valid ZIP code! ")
            return False
        elif zip_code[0] == '0':
            print("Your first character can't be Zero! ")
            return False
        elif not zip_code.isdigit():
            print("You must enter positive numbers! ")
            return False
        elif len(zip_code) == 4:
            return True

    def validate_city(self, city):
        city_names = ["miskolc", "kazincbarcika", "szerencs", "sarospatak"]
        if city.lower() not in city_names:
            print("You must fill this and city names must be: Miskolc, Kazincbarcika, Szerencs, Sarospatak")
            return False
        else:
            return True

    def validate_address(self, address):
        if address == "":
            print("Address can not be empty!")
            return False
        if address.isspace():
            print("Address must contains alphanumerical characters!")
            return False
        if not len(address) > 25:
            address_without_comma = address.replace(",", " ")
            for char in address_without_comma:
                if char == " ":
                    address_without_comma = address_without_comma.replace("  ", " ")
            return address_without_comma
        else:
            print("Address should be less then 25 characters!")
            return False

    def validate_available_beds(self, beds):
        if beds == "":
            print("Number of beds can not be empty!")
            return False
        elif not (beds.isdigit() and beds.isdigit() > 0):
            print("Please enter a positive integer!")
            return False
        else:
            return True

    def validate_planned_donor_number(self, planned_donor_number):
        if planned_donor_number == "":
            print("Number of planned donors can not be empty!")
            return False
        elif not (planned_donor_number.isdigit() and planned_donor_number.isdigit() > 0):
            print("Please enter a positive integer!")
            return False
        return True

    def validate_number_of_successful_donations(self, number_of_successful_donations):
        if number_of_successful_donations == "":
            print("Number of successful donations can not be empty!")
            return False
        elif not (number_of_successful_donations.isdigit() and number_of_successful_donations.isdigit() > 0):
            print("Please enter a positive integer!")
            return False
        return True

    def get_date_of_event(self):
        date_of_event = ""
        while date_of_event == "":
            date_of_event = input("Please enter the date of the donation (YYYY.MM.DD): ")
            if not self.check_date_of_event(date_of_event):
                date_of_event = ""
            elif not self.validate_date_of_event(date_of_event):
                date_of_event = ""
        self.date_of_event = date_of_event

    def get_start_time(self):
        start_time = ""
        while start_time == "":
            start_time = input("Start time (HH:MM): ")
            if not self.check_time(start_time):
                start_time = ""
            self.start_time = start_time

    def get_end_time(self):
        end_time = ""
        while end_time == "":
            end_time = input("End time (HH:MM): ")
            if not (self.check_time(end_time) and self.validate_end_time(self.start_time, end_time)):
                end_time = ""
            self.end_time = end_time

    def get_zip_code(self):
        zip_code = ""
        while zip_code == "":
            zip_code = input("Please enter your ZIP code: ")
            if not self.validate_zip_code(zip_code):
                zip_code = ""
            self.zip_code = zip_code

    def get_city(self):
        city = ""
        while city == "":
            city = input("Please enter your city name: ")
            if not self.validate_city(city):
                city = ""
        self.city = city.lower()

    def get_address(self):
        address = ""
        while address == "":
            address = input("Please enter your address: ")
            if not self.validate_address(address):
                address = ""
            else:
                self.address = self.validate_address(address)

    def get_available_beds(self):
        available_beds = ""
        while available_beds == "":
            available_beds = input("Please enter the number of available beds: ")
            if not self.validate_available_beds(available_beds):
                available_beds = ""
        self.available_beds = int(available_beds)

    def get_planned_donor_number(self):
        planned_donor_number = ""
        while planned_donor_number == "":
            planned_donor_number = input("Please enter the planned donor number: ")
            if not self.validate_planned_donor_number(planned_donor_number):
                planned_donor_number = ""
        self.planned_donor_number = int(planned_donor_number)

    def get_number_of_successful_donations(self):
        number_of_successful_donations = ""
        while number_of_successful_donations == "":
            number_of_successful_donations = input("Please enter the number of the successful donations here: ")
            if not self.validate_number_of_successful_donations(number_of_successful_donations):
                number_of_successful_donations = ""
        self.number_of_successful_donations = int(number_of_successful_donations)

    def calculate_duration_in_minutes(self):
        duration_in_minutes = (self.parse_time(self.end_time) - self.parse_time(self.start_time)).total_seconds() / 60
        self.duration_in_minutes = duration_in_minutes

    def calculate_max_donor_number(self):
        preparation_time = 30
        donation_time = 30

        max_donor_number = ((self.duration_in_minutes - preparation_time) / donation_time) * self.available_beds
        self.maximum_donor_number = max_donor_number

    def calculate_result_of_donation_by_percentage(self):
        result_of_donation_by_percentage = int(100 * self.number_of_successful_donations / self.maximum_donor_number)
        print("This is %d%% of the planned number of donors." % result_of_donation_by_percentage)
        if result_of_donation_by_percentage < 20:
            print("This donation was unsuccessful, not worth to organise there again.")
        elif 20 <= result_of_donation_by_percentage < 75:
            print("This donation was a normal event.")
        elif 75 <= result_of_donation_by_percentage < 110:
            print("This donation was successful!")
        elif 75 <= result_of_donation_by_percentage:
            print("This donation was outstanding!")

    def print_location_info(self):
        print("""Host city: {0}\nAddress: {1}\nZip code: {2}\nDate: {3}\nSuccessful donations: {4}
        """.format(self.city[0].upper() + self.city[1:],
                   self.address,
                   self.zip_code,
                   self.date_of_event,
                   self.number_of_successful_donations))

    def make_data_into_string(self):
        with open("./Data/Location_Data.csv", "r") as TextFile:
            csv_text = csv.reader(TextFile, delimiter=",")
            location_id = random.randint(0, 5000)
            location_ids = []
            for line in csv_text:
                location_ids.append(line[0])
                if not str(location_id) in str(location_ids):
                    location_id = location_id
                else:
                    location_id = random.randint(0, 5000)
        full_data = str(location_id) + ", " + str(self.date_of_event) + ", " + \
                    self.start_time + ", " + self.end_time + ", " + \
                    str(self.zip_code) + ", " + str(self.city) + ", " + str(self.address) + ", " + \
                    str(self.available_beds) + ", " + str(self.planned_donor_number) + ", " + \
                    str(self.number_of_successful_donations) + ", " + str(self.duration_in_minutes) + ", " + \
                    str(self.maximum_donor_number)

        self.full_data_string = full_data

    def data_to_file(self):
        with open("./Data/Location_Data.csv", "a") as Location_Text_File:
            Location_Text_File.write(self.full_data_string + "\n")

    def get_user(self):
        self.get_date_of_event()
        self.get_start_time()
        self.get_end_time()
        self.calculate_duration_in_minutes()
        self.get_available_beds()
        self.calculate_max_donor_number()
        self.get_zip_code()
        self.get_city()
        self.get_address()
        self.get_planned_donor_number()
        self.get_number_of_successful_donations()
        self.calculate_result_of_donation_by_percentage()
        self.print_location_info()
        self.make_data_into_string()
        self.data_to_file()

if __name__ == "__main__":
    ocelot = UserData().get_user()

