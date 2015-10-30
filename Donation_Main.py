def print_separator_line():
    print("-"*32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print("Please choose an application which you want to use!")
    print_separator_line()


def print_apps():
    print("If you want to use Donor registration application, type in: user")
    print("If you want to use Donation event registration application, type in: loc")


if __name__ == "__main__":
    print_separator_line()
    greetings()
    apps_alias_str = ""
    while apps_alias_str == "":
        print_apps()
        apps_alias_str = input("> ")
        if not (apps_alias_str == "user" or apps_alias_str == "loc"):
            print("Invalid input!")
            apps_alias_str = ""
    if apps_alias_str == "user":
        import Donation_User as user
        print_separator_line()
        print("Welcome in Donor registration application!")
        print()
        person = user.User_Data()
        print()
        print_separator_line()
        print("The user main data: ")
        print()
        print(person.data_dictionary()['name'], '\n',
              str(person.data_dictionary()['weight']), ' kg\n',
              person.data_dictionary()['date of birth'], ' - ', person.data_dictionary()['age'], ' years old\n',
              person.data_dictionary()['e-mail'])
        print()
        print("Thank for your registration (and your blood)!")

    else:
        import Donation_Location as loc
        print_separator_line()
        print("Welcome in Donation event registration application!")
        print()
        location = loc.User_Data()
        print()
        print("Thank for your registration (and your blood)!")
        