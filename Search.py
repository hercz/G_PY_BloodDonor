__author__ = 'Vegh Adam'
import csv
import os

class Search():
    @staticmethod
    def separator_line():
        print("-" * 32)

    def __init__(self):
        self.get_search()

    @staticmethod
    def print_one_location(line):
        city_to_print = line[5]
        date_of_event_to_print = line[1]
        for char in date_of_event_to_print:
            date_of_event_corrected = date_of_event_to_print.replace("-", ".")

        address_to_print = line[6]

        print("""{0},{1},{2}
                """.format(city_to_print, date_of_event_corrected, address_to_print))
        print("-" * 32)
    @staticmethod
    def print_one_donor(line):
        first_name_to_print = line[0]
        last_name_to_print = line[1]
        weight_to_print = line[8]
        birth_date_to_print = line[6]
        age_to_print = line[7]
        email_to_print = line[4]
        print("""{0}\n{1} kg\n{2} - {3}\n{4}
                """.format(first_name_to_print + last_name_to_print,
                           weight_to_print,
                           birth_date_to_print,
                           age_to_print,
                           email_to_print))
        print("-" * 32)

    def get_search(self):
        Search.separator_line()
        print("Search within:")
        print("1, Donors")
        print("2, Donation")
        print()
        search_number = ""
        while search_number == "":
            search_number = input("Please choose from the list above: ")
            if not (search_number == '1' or search_number == '2'):
                search_number = ""
        if search_number == '1':
            os.system("cls")
            keyword = input("Please enter keyword to search for: ")
            with open("./Data/Donor_Data.csv", "r") as TextFile:
                csv_text = csv.reader(TextFile)
                counter = 0
                page_size = 3
                record_list = list(csv_text)
                for line in record_list[1:]:
                    for char in line:
                        if keyword in char:
                            counter += 1
                            Search.print_one_donor(line)
                            if counter % page_size == 0 and counter <= len(record_list):
                                next_page = input("For next page press: N ")
                                if next_page.lower() == "n":
                                    os.system("cls")

        elif search_number == '2':
            os.system("cls")
            keyword = input("Please enter keyword to search for: ")
            with open("./Data/Location_Data.csv", "r") as TextFile:
                csv_text = csv.reader(TextFile)
                counter = 0
                page_size = 3
                record_list = list(csv_text)
                for line in record_list[1:]:
                    for char in line:
                        if keyword in char:
                            counter += 1
                            Search.print_one_location(line)
                            if counter % page_size == 0 and counter <= len(record_list):
                                next_page = input("For next page press: N ")
                                if next_page.lower() == "n":
                                    os.system("cls")



            pass
if __name__ == "__main__":
    Search()