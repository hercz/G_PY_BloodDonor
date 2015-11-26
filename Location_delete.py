import Menu
import os


def print_separator_line():
    print("-" * 50)


def greetings():
    print_separator_line()
    print("Welcome in the location delete application!")
    print_separator_line()


def check_database_is_empty():
    if os.stat("./Data/Location_data.csv").st_size == 0:
        print("Your database is empty! Add some location before you want to delete them!")
        Menu.ask_answer()


def id_is_valid(id_to_delete):
    id_to_delete = id_to_delete.lower()
    if len(id_to_delete) == 0:
        print("This input cannot be empty!")
        return False
    elif not id_to_delete.isdigit():
        print("The ID has to be a number!")
        return False
    return True


def get_id_to_delete():
    id_to_delete = ""
    while id_to_delete == "":
        id_to_delete = input("Please write here the location's ID which you want to delete from the database\n>> ")
        if not id_is_valid(id_to_delete):
            id_to_delete = ""
        else:
            return id_to_delete


def delete_id_from_database(id_to_delete):
    location_file = open("./Data/Location_data.csv", "r+")
    read_line = location_file.readlines()
    location_file.seek(0)
    line_counter = 0
    for line in read_line:
        splitted = line.split(",")
        if id_to_delete != splitted[0]:
            line_counter += 1
            location_file.write(line)
    location_file.truncate()
    location_file.close()
    if line_counter == len(read_line):
        print("The location with {} ID is not found".format(id_to_delete))
    else:
        print("The location with {} ID is deleted".format(id_to_delete))


def loc_del_app():
    os.system("cls")
    greetings()
    check_database_is_empty()
    id_to_delete = get_id_to_delete()
    delete_id_from_database(id_to_delete)
    Menu.ask_answer()

if __name__ == "__main__":
    loc_del_app()
