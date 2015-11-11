import csv
import Menu

class DeleteDonor(object):

    id_to_delete = ""

    def __init__(self):
        self.get_delete_id()

    def get_user_input(self):
        user_input = input(print("Are you sure you want to delete another donor from the database? (Y/N)"))
        if user_input == "Y":
            return self.get_delete_id()
        elif user_input == "N":
             Menu.Main_Menu()
             Menu.Picked_option()
        else:
            print("Invalid input!")
            self.get_user_input()


    def delete_id(self):
        print(self.to_delete)



    def get_delete_id(self):
        id_to_delete = ""
        while id_to_delete == "":
            id_to_delete = input("Please write here the person's ID which you want to delete from the database: ")
            self.to_delete = id_to_delete
            try:
                with open("./Data/Donor_Data.csv", newline="") as file:
                    reader = csv.reader(file, delimiter=",")
                    ids = []
                    for row in reader:
                        ids.append(row[3])
                    if id_to_delete in str(ids):
                        self.delete_id()
                    else:
                        print("This ID is not in the database!")
                        self.get_user_input()
            except IndexError:
                print("Your database is empty!")
                print("Register some donor before you want to delete them!")
                Menu.Main_Menu()
                Menu.Picked_option()




if __name__ == '__main__':
    DeleteDonor()

