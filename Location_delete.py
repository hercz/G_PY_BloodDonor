import csv
import Menu


class DeleteLocation(object):
    id_to_delete = ""

    def __init__(self):
        self.get_delete_id()

    def get_user_input(self):
        user_input = input("Do you want to delete another location from the database? (Y/N)")
        if user_input.lower() == "y":
            return self.get_delete_id()
        elif user_input.lower() == "n":
            Menu.Main_Menu()
            Menu.Picked_option()
        else:
            print("Invalid input!")
            self.get_user_input()

    def delete_id(self):
        location_file = open("./Data/Location_data.csv", "r+")
        read_line = location_file.readlines()
        location_file.seek(0)
        for i in read_line:
            splitted = i.split(",")
            if self.to_delete != splitted[0]:
                location_file.write(i)
        location_file.truncate()
        location_file.close()
        print("the location with {} id was deleted".format(self.to_delete))
        self.get_user_input()

    def get_delete_id(self):
        id_to_delete = ""
        while id_to_delete == "":
            id_to_delete = input("Please write here the location ID which you want to delete from the database: ")
            self.to_delete = id_to_delete
        if id_to_delete == "id":
            print("Invalid ID format!")
            self.get_user_input()
        try:
            with open("./Data/Location_Data.csv", newline="") as file:
                reader = csv.reader(file, delimiter=",")
                ids = []
                for row in reader:
                    ids.append(row[0])
                if id_to_delete in str(ids):
                    self.delete_id()
                else:
                    print("This location ID is not in the database!")
                    self.get_user_input()
        except IndexError:
            print("Your database is empty!")
            print("Register some location before you want to delete them!")
            Menu.Main_Menu()
            Menu.Picked_option()


if __name__ == '__main__':
    DeleteLocation()
