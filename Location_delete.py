import csv
import os
import Menu

def check_database_is_empty():
    if os.stat("./Data/Location_data.csv").st_size == 0:
        print("Your database is empty! Add some location before you want to delete them!")
        Menu.ask_answer()
        Menu.Main_Menu()
        Menu.Picked_option()
    else:
        pass


def get_id_to_delete():
    id_to_delete = ""
    while id_to_delete == "":
        id_to_delete = input("Please write here the location's ID which you want to delete from the database: ")
        if not id_is_valid(id_to_delete):
            id_to_delete = ""
        else:
            return id_to_delete


def id_is_valid(id_to_delete):
    id_to_delete = id_to_delete.lower()
    if len(id_to_delete) == 0:
        print("This input cannot be empty!")
        return False
    elif not id_to_delete.isdigit():
        print("The ID has to be a number!")
        return False
    else:
        return True


def delete_id_from_database(id_to_delete):
    location_file = open("./Data/Location_data.csv", "r+")
    read_line = location_file.readlines()
    location_file.seek(0)
    for i in read_line:
        splitted = i.split(",")
        if id_to_delete != splitted[0]:
            location_file.write(i)
    location_file.truncate()
    location_file.close()
    print("the location with {} id was deleted".format(id_to_delete))
    Menu.ask_answer()



