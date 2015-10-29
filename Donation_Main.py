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

    else:
        import Donation_Location as loc
        print_separator_line()
        print("Welcome in Donation event registration application!")
