import csv
import os
import Menu

def check_database_is_empty():
    if os.stat("./Data/Donor_Data.csv").st_size == 0:
        print("Your database is empty! Add some donor before you want to delete them!")
        Menu.ask_answer()
        Menu.Main_Menu()
        Menu.Picked_option()
    else:
        pass


def get_id_to_delete():
    id_to_delete = ""
    while id_to_delete == "":
        id_to_delete = input("Please write here the person's ID which you want to delete from the database: ")
        if not id_is_valid(id_to_delete):
            id_to_delete = ""
        else:
            return id_to_delete


def id_is_valid(id_to_delete):
    id_to_delete = id_to_delete.lower()
    if len(id_to_delete) == 0:
        print("This input cannot be empty!")
        return False
    elif len(id_to_delete) != 8:
        print("The ID length is not correct! (8 digit)")
        return False
    elif not id_to_delete[:6].isdigit() and id_to_delete[6:].isalpha() or not id_to_delete[:6].isalpha() and id_to_delete[6:].isdigit():
        print("This ID is wrong, type it again(It must be an ID or Passport number): ")
        return False
    else:
        return True


def delete_id_from_database(id_to_delete):
        donor_data = open("./Data/Donor_Data.csv", "r")
        lines = donor_data.readlines()
        donor_data.close()
        donor_data = open("./Data/Donor_Data.csv", "w")
        for line in lines:
            if id_to_delete not in line:
                donor_data.write(line)
        donor_data.close()
        print("The user with {} Id is deleted".format(id_to_delete))
        Menu.ask_answer()



