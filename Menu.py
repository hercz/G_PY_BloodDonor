import os
import Donation_User
import Donation_Location
import csv
import User_delete
import Search


def print_separator_line():
    print("-" * 32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()


def Main_Menu():
    print("Main menu")
    print("     1. Add new donor")
    print("     2. Add new donation event")
    print("     3. Delete a donor")
    print("     4. Delete a donation event")
    print("     5. List donor or donation events")
    print("     6. Search")
    print("     7. Exit \n")


def Picked_option():
    Picked_option_string = ""
    while Picked_option_string == "":
        Picked_option_string = input("Pick an option: ")
        if not (Picked_option_string == "1" or Picked_option_string == "2" or Picked_option_string == "3" or
                        Picked_option_string == "4" or Picked_option_string == "5" or Picked_option_string == "6" or
                        Picked_option_string == "7"):
            print("Your input is invalid, choose from the available menus! ")
            Picked_option_string = ""

    if Picked_option_string == "1":
        import Donation_User as user

        print_separator_line()
        print("Welcome in Donor registration application!")
        print()
        person = user.UserData()
        ask_answer()


    elif Picked_option_string == "2":
        import Donation_Location as location

        print_separator_line()
        print("Welcome in Donation event registration application!")
        print()
        location = location.UserData()
        print()
        print("Thank for your registration (and your blood)!")
        ask_answer()


    elif Picked_option_string == "3":
        import User_delete as user_deleter
        print_separator_line()
        print("Welcome in the donor delete application!")
        print()
        user_deleter = user_deleter.DeleteDonor()
        ask_answer()

    elif Picked_option_string == "4":
        import Location_delete as location_deleter
        print_separator_line()
        print("Welcome in the location delete application!")
        print()
        user_deleter = location_deleter.DeleteLocation()
        ask_answer()

    elif Picked_option_string == "5":
        list_options = ""
        while list_options == "":
            print("Please choose which one you want to List: ")
            print("     1.Donor")
            print("     2.Donation")
            list_options = input("")
            if list_options == "1":
                with open("./Data/Donor_Data.csv", "r") as TextFile:
                    csv_text = csv.reader(TextFile)
                    counter = 0
                    page_size = 3
                    record_list = list(csv_text)
                    for line in record_list[1:]:
                        counter += 1
                        print_one_donor(line)
                        if counter % page_size == 0 and counter <= len(record_list):
                            next_page = input("For next page press: N ")
                            if next_page.lower() == "n":
                                os.system("cls")

                    ask_answer()

            if list_options == "2":
                with open("./Data/Location_Data.csv", "r") as TextFile:
                    csv_text = csv.reader(TextFile)
                    counter = 0
                    page_size = 3
                    record_list = list(csv_text)
                    for line in record_list[1:]:
                        counter += 1
                        print_one_location(line)
                        if counter % page_size == 0 and counter <= len(record_list):
                            next_page = input("For next page press: N ")
                            if next_page.lower() == "n":
                                os.system("cls")

                    ask_answer()

    elif Picked_option_string == "6":
        import Search as search_option
        os.system("cls")
        print_separator_line()
        print("Welcome to Search")
        print()
        search_option = Search.Search()
        print()
        print("Thank for using our Search Engine")

        ask_answer()
        pass

    elif Picked_option_string == "7":
        exit()


def print_one_donor(line):
    first_name_to_print = line[0]
    last_name_to_print = line[1]
    weight_to_print = line[8]
    birth_date_to_print = line[6]
    age_to_print = line[7]
    email_to_print = line[4]
    print_separator_line()
    print("""{0}\n{1} kg\n{2} - {3} years old\n{4}
            """.format(first_name_to_print + last_name_to_print,
                       weight_to_print,
                       birth_date_to_print,
                       age_to_print,
                       email_to_print))
    print_separator_line()


def print_one_location(line):
    city_to_print = line[5]
    date_of_event_to_print = line[1]
    for char in date_of_event_to_print:
        date_of_event_corrected = date_of_event_to_print.replace("-", ".")

    address_to_print = line[6]
    print_separator_line()
    print("""{0},{1},{2}
            """.format(city_to_print, date_of_event_corrected, address_to_print))


def ask_answer():
    answer = ""
    while answer == "":
        answer = input("Do you want to go back to the Main Menu? Y/N ")
        if answer == "Y" or answer == "y":
            Main_Menu()
            Picked_option()
        elif answer == "N" or answer == "n":
            exit()
        else:
            print("You answer must be Y or N ")
            answer = ""
