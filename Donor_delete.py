import csv

class DeleteDonor(object):

    def __init__(self):
        self.get_delete_id()

    # @staticmethod
    def get_user_input(self):
        user_input = input(print("Are you sure you want to delete donor from the database? (Y/N)"))
        if user_input == "Y":
            return self.get_delete_id()
        elif user_input == "N":
            import Donation_Main as main
            main.Main_Menu()
            main.Picked_Option()
        else:
            print("Invalid input!")
            self.get_user_input()


    def delete_id(self):
        pass


    def get_delete_id(self):
        delete_id = ""
        while delete_id == "":
            delete_id = input("Please write here the person's ID which you want to delete from the database: ")
        with open("./Data/Donor_Data.csv", newline="") as file:
            reader = csv.reader(file, delimiter=",")
            ids = []
            for row in reader:
                ids.append(row[3])
            if delete_id in str(ids):
                self.delete_id()
            else:
                print("This ID is not in the database!")
                self.get_user_input()




if __name__ == '__main__':
    DeleteDonor()

#
# id = "7"
#
# with open("./Data/Donor_Data.csv", newline="") as file:
#     reader = csv.reader(file, delimiter=",")
#     ids = []
#     for row in reader:
#         ids.append(row[3])
#     if id not in str(ids):
#             print("This ID is not in the database!")
#     else:
#         pass
#     print(ids)

#row_print
# with open("./Data/Donor_Data.csv", newline="") as file:
#     Reader = csv.reader(file, delimiter=",")
#     for row in Reader:
#         print(row[3])
#mainbe
     # if Picked_Option() == "3":
     #    import Donor_delete as deleter
     #    print_separator_line()
     #    print("Welcome in the donor delete application!")
     #    print()
     #    deleter = deleter.DeleteDonor()