import webbrowser
import os
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
    print("     7. Change")
    print("     8. Exit \n")

def check_picked_option(input_str: str):
    return input_str.isdigit()

def valid_picked_option(input_str: str):
    return int(input_str) in range(1, 10)

def Picked_option():
    Picked_option_string = ""
    while Picked_option_string == "":
        Picked_option_string = input("Pick an option: ")
        if not check_picked_option(Picked_option_string):
            print("Your input is not a number, choose from the available menus!")
            Picked_option_string = ""
        elif not valid_picked_option(Picked_option_string):
            print("The menu number is not found, choose from the available menus!")
            Picked_option_string = ""

    if Picked_option_string == "1":
        import Donation_User
        Donation_User.donor_app()

    elif Picked_option_string == "2":
        import Donation_Location
        Donation_Location.location_app()

    elif Picked_option_string == "3":
        import User_delete
        User_delete.user_del_app()

    elif Picked_option_string == "4":
        import Location_delete
        Location_delete.loc_del_app()

    elif Picked_option_string == "5":
        import Listing
        Listing.listing()

    elif Picked_option_string == "6":
        import Search as search_option
        os.system("cls")
        print_separator_line()
        print("Welcome to Search")
        print()
        Search.Search()
        print()
        print("Thank for using our Search Engine")

        ask_answer()

    elif Picked_option_string == "7":
        answer = ""
        while answer == "":
            answer = input("Are You sure in your selection?: ")
            if answer.lower() == "y":
                print("Thank for using our Blood Donation Register Software!")
                exit()
            elif answer.lower() == "n":
                the_menu()
            else:
                print("Press 'Y' or 'N'!")
                answer = ""

    elif Picked_option_string == "8":
        pass

    elif Picked_option_string == "9":
        webbrowser.open("https://www.youtube.com/watch?v=_uUBQeJ61nw")

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


def the_menu():
    os.system('cls')
    print_separator_line()
    greetings()
    Main_Menu()
    Picked_option()


def ask_answer():
    answer = ""
    while answer == "":
        answer = input("Do you want to go back to the Main Menu? (Press 'y' or 'n'!) ")
        if answer.lower() == "y":
            the_menu()
        elif answer.lower() == "n":
            exit()
        else:
            print("You answer must be Y or N!")
            answer = ""

if __name__ == "__main__":
    the_menu()