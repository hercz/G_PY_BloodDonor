import Menu
import csv
import os

__author__ = 'Stark Industries'


def print_separator_line():
    print("-" * 32)


def print_one_location(line):
    city_to_print = line[5]
    date_of_event_to_print = line[1]
    for char in date_of_event_to_print:
        date_of_event_corrected = date_of_event_to_print.replace("-", ".")
    address_to_print = line[6]
    print('-' * 36)
    print("""{0},{1},{2}
            """.format(city_to_print, date_of_event_corrected, address_to_print))


def print_one_donor(line, counter):
    first_name_to_print = line[0]
    last_name_to_print = line[1]
    weight_to_print = line[8]
    birth_date_to_print = line[6].replace("-", ".")
    age_to_print = line[7]
    email_to_print = line[4]
    print('-' * 36)
    print("""{0}.\t{1}, {2}\n\t{3} kg\n\t{4} - {5} years old\n\t{6}
    """.format(
        counter,
        first_name_to_print,
        last_name_to_print,
        weight_to_print,
        birth_date_to_print,
        age_to_print,
        email_to_print))


def search_app():
    os.system("cls")
    print_separator_line()
    print("Welcome to Search")
    print()
    print_separator_line()
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
        keyword = input("Please enter keyword to search for: ").lower()
        with open("./Data/Donor_Data.csv", "r") as TextFile:
            csv_text = csv.reader(TextFile)
            counter = 0
            page_size = 3
            record_list = list(csv_text)
            for line in record_list[1:]:
                for char in line:
                    if keyword in char.lower():
                        counter += 1
                        print_one_donor(line, counter)
                        if counter % page_size == 0:
                            next_page = input("For next page press: N ")
                            if next_page.lower() == "n":
                                os.system("cls")
                        break
            if counter == 0:
                print("The '{0}' term is not found".format(keyword))

    elif search_number == '2':
        keyword = input("Please enter keyword to search for: ").lower()
        with open("./Data/Location_Data.csv", "r") as TextFile:
            csv_text = csv.reader(TextFile)
            counter = 0
            page_size = 3
            record_list = list(csv_text)
            for line in record_list[1:]:
                for char in line:
                    if keyword in char.lower():
                        counter += 1
                        print_one_location(line)
                        if counter % page_size == 0:
                            next_page = input("For next page press: N ")
                            if next_page.lower() == "n":
                                os.system("cls")
                        break
            if counter == 0:
                print("The '{0}' term is not found".format(keyword))
    print()
    print("Thank for using our Search Engine")
    Menu.ask_answer()


if __name__ == "__main__":
    search_app()
