from msvcrt import getch
import Menu
import csv
import os
import winsound

__author__ = 'Stark Industries'


def print_separator_line():
    print("-" * 32)


def menu_points(number=0):
    space = " " * 5
    before = [space for i in range(3)]
    arrow = "---> "
    before[number] = arrow
    os.system("cls")
    print_separator_line()
    print("Welcome to Search")
    print_separator_line()
    print("Search within:")
    print(before[1] + "1. Donors")
    print(before[2] + "2. Donations")
    print()
    print("Please choose from the list above. Press '1' or '2'.")


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
    menu_points()
    search_number = ""
    while search_number == "":
        search_number = ord(getch())
        if not (chr(search_number) == '1' or chr(search_number) == '2'):
            menu_points()
            print("Please press 1 or 2!")
            winsound.Beep(1000, 250)
            search_number = ""

    if chr(search_number) == '1':
        menu_points(int(chr(search_number)))
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

    elif chr(search_number) == '2':
        menu_points(int(chr(search_number)))
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
