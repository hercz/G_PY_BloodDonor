import os
import Donation_User
import Donation_Location
import csv
import User_delete


def print_separator_line():
    print("-" * 32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()


def Main_Menu():
    # print("If you want to use Donor registration application, type in: user")
    print("Main menu")
    print("     1. I want to add a new guy, bro!!")
    print("     2. How about a new donation event? Yeah! That's what i want!")
    print("     3. Genie make a donor disappear!")
    print("     4. Obama destroy event protocol..")
    print("     5. Show me everyone and everything The way I want!")
    print("     6. Search and...? SEARCH")
    print("     7. Exit \n")

    # print("\n Choose what you want: ")
    # print("If you want to use Donation event registration application, type in: loc")


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
        # print()
        # print_separator_line()
        # print("The user main data: ")
        # print()
        # print(person.print_donor_info()['name'], '\n',
        #       str(person.print_donor_info()['weight']), ' kg\n',
        #       person.print_donor_info()['date of birth'], ' - ', person.print_donor_info()['age'], ' years old\n',
        #       person.print_donor_info()['e-mail'])
        # print()
        # print("Thank for your registration (and your blood)!")
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
        import Donor_delete as deleter
        print_separator_line()
        print("Welcome in the donor delete application!")
        print()
        deleter = deleter.DeleteDonor()
        ask_answer()

    elif Picked_option_string == "4":

        ask_answer()
        pass

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

        ask_answer()
        pass

    elif Picked_option_string == "7":
        exit()


def print_one_donor(line):
    first_name_to_print = line[0]
    title_to_print = line[1]
    last_name_to_print = line[2]
    weight_to_print = line[9]
    birth_date_to_print = line[7]
    age_to_print = line[8]
    email_to_print = line[5]
    print_separator_line()
    print("""{0}\n{1} kg\n{2} - {3}\n{4}
            """.format(title_to_print + first_name_to_print + last_name_to_print,
                       weight_to_print,
                       birth_date_to_print,
                       age_to_print,
                       email_to_print))
    print_separator_line()


def print_one_location(line):
    city_to_print = line[5]
    date_of_event_to_print = line[1]
    address_to_print = line[6]
    print_separator_line()
    print("""{0} ,{1} , {2}
            """.format(city_to_print, date_of_event_to_print, address_to_print))


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
