import Menu
import os
from msvcrt import getch

def print_separator_line():
    print("-" * 50)


def greetings():
    print_separator_line()
    print("Welcome in the donor delete application!")
    print_separator_line()


def check_database_is_empty():
    if os.stat("./Data/Donor_Data.csv").st_size == 0:
        print("Your database is empty! Add some donor before you want to delete them!")
        Menu.ask_answer()


def id_is_valid(id_to_delete):
    id_to_delete = id_to_delete.lower()
    if len(id_to_delete) == 0:
        print("This input cannot be empty!")
        return False
    elif len(id_to_delete) != 8:
        print("The ID length is not correct! (8 digit)")
        change_purpose()
        return False
    elif not id_to_delete[:6].isdigit() and id_to_delete[6:].isalpha() or not \
            id_to_delete[:6].isalpha() and id_to_delete[6:].isdigit():
        print("This ID is wrong, type it again! (It must be an ID or Passport number)\n>> ")
        change_purpose()
        return False
    else:
        return True

def change_purpose():
    decision = ""
    print("Do you want to delete another donation? (Press Y, or N)")
    while decision == "":
        decision = ord(getch())
        if chr(decision) == "y":
            user_del_app()
        elif chr(decision) == "n":
            Menu.the_menu()
        else:
            os.system("cls")
            print("Please press Y or N")
            decision = ""


def get_id_to_delete():
    id_to_delete = ""
    while id_to_delete == "":
        id_to_delete = input("Please write here the person's ID which you want to delete from the database\n>>")
        if not id_is_valid(id_to_delete):
            id_to_delete = ""
        else:
            return id_to_delete


def delete_id_from_database(id_to_delete):
    donor_data = open("./Data/Donor_Data.csv", "r")
    lines = donor_data.readlines()
    donor_data.close()
    donor_data = open("./Data/Donor_Data.csv", "w")
    line_counter = 0
    for line in lines:
        if id_to_delete not in line:
            line_counter += 1
            donor_data.write(line)
    donor_data.close()
    if line_counter == len(lines):
        print("The user with {} ID is not found".format(id_to_delete))
    else:
        print("The user with {} ID is deleted".format(id_to_delete))


def user_del_app():
    os.system("cls")
    greetings()
    check_database_is_empty()
    id_to_delete = get_id_to_delete()
    delete_id_from_database(id_to_delete)
    change_purpose()

if __name__ == "__main__":
    user_del_app()
