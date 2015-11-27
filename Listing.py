import Menu
import os
import csv
import winsound
from msvcrt import getch

__author__ = 'Vegh Adam'


def print_separator_line():
    print("-" * 50)


def menu_points(number=0):
    space = " " * 5
    before = [space for i in range(3)]
    arrow = "---> "
    before[number] = arrow
    os.system("cls")
    print_separator_line()
    print("Welcome in the listing application!")
    print_separator_line()
    print("Please choose which one you want to list: ")
    print(before[1] + "1. Donors")
    print(before[2] + "2. Donations")
    print()


def menu_donor_order_by(number):
    space = " " * 5
    before = [space for i in range(6)]
    arrow = "---> "
    before[number] = arrow
    print_separator_line()
    print("Please choose a point via arrow keys (UP and DOWN) what the listing will be ordered by: ")
    print(before[1] + "First name")
    print(before[2] + "Last name")
    print(before[3] + "Birth date")
    print(before[4] + "Age")
    print(before[5] + "Weight")
    print()


dict_order_by_to_list = {1: 0, 2: 1, 3: 6, 4: 7, 5: 8}


def menu_location_order_by(number):
    space = " " * 5
    before = [space for i in range(13)]
    arrow = "---> "
    before[number] = arrow
    print_separator_line()
    print("Please choose a point via arrow keys (UP and DOWN) what the listing will be ordered by: ")
    print(before[1] + "ID")
    print(before[2] + "Date of event")
    print(before[3] + "Start time")
    print(before[4] + "End time")
    print(before[5] + "Zip code")
    print(before[6] + "City")
    print(before[7] + "Address")
    print(before[8] + "Available beds")
    print(before[9] + "Planned donor number")
    print(before[10] + "Number of successful donation")
    print(before[11] + "Duration in minutes")
    print(before[12] + "Maximum donor number")
    print()


def check_database_is_empty():
    if os.stat("./Data/Donor_Data.csv").st_size == 0:
        print("Your database is empty! Add some donor before you want to delete them!")
        Menu.ask_answer()


def print_one_donor(line):
    first_name_to_print = line[0]
    last_name_to_print = line[1]
    weight_to_print = line[8]
    birth_date_to_print = line[6].replace('-', '.')
    age_to_print = line[7]
    email_to_print = line[4]
    print_separator_line()
    print("""{0}\n{1} kg\n{2} - {3} years old\n{4}
            """.format(first_name_to_print + ", " + last_name_to_print,
                       weight_to_print,
                       birth_date_to_print,
                       age_to_print,
                       email_to_print))


def print_one_location(line):
    city_to_print = line[5]
    date_of_event_to_print = line[1]
    date_of_event_corrected = date_of_event_to_print.replace("-", ".")
    address_to_print = line[6]
    print_separator_line()
    print("""{0},{1},{2}
            """.format(city_to_print, date_of_event_corrected, address_to_print))


def listing():
    menu_points()
    print("Please choose from the list above. Press '1' or '2'.")
    list_options = ""
    while list_options == "":
        list_options = ord(getch())

        if chr(list_options) == "1":
            menu_points(1)
            order_chooser = 1
            menu_donor_order_by(order_chooser)
            while True:
                key = ord(getch())
                if key == 72 and order_chooser > 1:
                    order_chooser -= 1
                    menu_points(1)
                    menu_donor_order_by(order_chooser)
                elif key == 80 and order_chooser < 5:
                    order_chooser += 1
                    menu_points(1)
                    menu_donor_order_by(order_chooser)
                elif key == 13:
                    os.system("cls")
                    break
            with open("./Data/Donor_Data.csv", "r") as TextFile:
                csv_text = csv.reader(TextFile)
                counter = 0
                page_size = 3
                record_list = list(csv_text)
                rec_list_without_header = record_list[1:]
                rec_list_without_header.sort(key=lambda x: x[dict_order_by_to_list[order_chooser]])
                for line in rec_list_without_header:
                    counter += 1
                    print_one_donor(line)
                    if counter % page_size == 0:
                        print("Press a button to next page")
                        key = ord(getch())
                        if key == 27:
                            Menu.ask_answer()
                        else:
                            menu_points(1)
                Menu.ask_answer()

        elif chr(list_options) == "2":
            menu_points(2)
            order_chooser = 1
            menu_location_order_by(order_chooser)
            while True:
                key = ord(getch())
                if key == 72 and order_chooser > 1:
                    order_chooser -= 1
                    menu_points(2)
                    menu_location_order_by(order_chooser)
                elif key == 80 and order_chooser < 12:
                    order_chooser += 1
                    menu_points(2)
                    menu_location_order_by(order_chooser)
                elif key == 13:
                    os.system("cls")
                    break
            with open("./Data/Location_Data.csv", "r") as TextFile:
                csv_text = csv.reader(TextFile)
                counter = 0
                page_size = 3
                record_list = list(csv_text)
                rec_list_without_header = record_list[1:]
                rec_list_without_header.sort(key=lambda x: x[order_chooser])
                for line in rec_list_without_header:
                    counter += 1
                    print_one_location(line)
                    if counter % page_size == 0:
                        print("Press a button to next page")
                        key = ord(getch())
                        if key == 27:
                            Menu.ask_answer()
                        else:
                            menu_points(2)
                Menu.ask_answer()
        else:
            menu_points()
            print("Press '1' or '2'!")
            winsound.Beep(1000, 200)
            list_options = ""

if __name__ == "__main__":
    listing()
