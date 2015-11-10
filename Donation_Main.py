def print_separator_line():
    print("-" * 32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()


def Main_Menu():
    #print("If you want to use Donor registration application, type in: user")
    print("Main menu")
    print("     1. I want to add a new guy, bro!!")
    print("     2. How about a new donation event? Yeah! That's what i want!")
    print("     3. Genie make a donor disappear!")
    print("     4. Obama destroy event protocol..")
    print("     5. Show me everyone and everything The way I want!")
    print("     6. Search and...? SEARCH")
    print("     7. Exit \n")

    #print("\n Choose what you want: ")
    #print("If you want to use Donation event registration application, type in: loc")

def Picked_Option():
    Picked_option_string = ""
    while Picked_option_string == "":
        Picked_option_string = input("Pick an option: ")
        if not (Picked_option_string == "1" or Picked_option_string == "2" or Picked_option_string == "3" or \
                Picked_option_string == "4" or Picked_option_string == "5" or Picked_option_string == "6" or \
                Picked_option_string == "7"):
            print("Your input is invalid, choose from the available menus!")
            Picked_option_string = ""
    return Picked_option_string

if __name__ == "__main__":
    print_separator_line()
    greetings()
    Main_Menu()

    if Picked_Option() == "1":
        import Donation_User as user
        print_separator_line()
        print("Welcome in Donor registration application!")
        print()
        person = user.UserData()
        print()
        print_separator_line()
        print("The user main data: ")
        print()
        print(person.print_donor_info()['name'], '\n',
              str(person.print_donor_info()['weight']), ' kg\n',
              person.print_donor_info()['date of birth'], ' - ', person.print_donor_info()['age'], ' years old\n',
              person.print_donor_info()['e-mail'])
        print()
        print("Thank for your registration (and your blood)!")

    elif Picked_Option() == "2":
        import Donation_Location as location
        print_separator_line()
        print("Welcome in Donation event registration application!")
        print()
        location = location.UserData()
        print()
        print("Thank for your registration (and your blood)!")

    if Picked_Option() == "3":
        pass

    if Picked_Option() == "4":
        pass

    if Picked_Option() == "5":
        pass

    if Picked_Option() == "6":
        pass

    if Picked_Option() == "7":
        exit()
