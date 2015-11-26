# from msvcrt import getch
# while True:
#    key = ord(getch())
#    print(key)
#
import os
import csv
from Donation_User2 import UserData2
import webbrowser
from datetime import datetime


class Change():
    def change_within(self):
        print('-' * 36)
        print("Change within:")
        print("1, Donors")
        print("2, Donation")
        print()
        answer = ""
        while answer == "":
            answer = input("Pick one of the available: ")
            if answer.lower() == "1":
                self.change_stuff_donor()
            elif answer.lower() == "2":
                self.change_stuff_donation()
            else:
                answer = ""

    def change_stuff_donor(self):
        donor_to_change = ""
        while donor_to_change == "":
            donor_to_change = input("Please type the id of the Donor you want to change: ")
            with open("./Data/Donor_Data.csv", newline="") as file:
                reader = csv.reader(file, delimiter=",")
                ids = []
                for row in reader:
                    ids.append(row[3])


                if donor_to_change in str(ids):
                    with open("./Data/Donor_Data.csv", newline="") as file:
                        reader = csv.reader(file, delimiter=",")
                        items = []

                        for row in reader:
                            if donor_to_change in row:
                                items.append(row)
                                print(items)
                                print(items[0][5])

                    self.Options_for_donor()
                    item_to_change = input("I want to change(1-13):")
                    user_to_change = UserData2()

                    if item_to_change == "1":
                        item = ""
                        while item == "":
                            item = input("Enter the new First Name: ")
                            if user_to_change.valid_first_name(item):
                                items[0][0] = item
                            else:
                                item = ""

                    elif item_to_change == "2":
                        item = ""
                        while item == "":
                            item = input("Enter the new Last Name: ")
                            if user_to_change.valid_last_name(item):
                                items[0][1] = item
                            else:
                                item = ""

                    elif item_to_change == "3":
                        item = ""
                        while item == "":
                            item = input("Enter the new Gender Name: ")
                            if user_to_change.valid_gender(item):
                                items[0][0] = item
                            else:
                                item = ""

                    elif item_to_change == "4":
                        item = ""
                        while item == "":
                            item = input("Enter the new Identifier Name: ")
                            if user_to_change.valid_identifier(item):
                                items[0][3] = item
                            else:
                                item = ""

                    elif item_to_change == "5":
                        item = ""
                        while item == "":
                            item = input("E-mail (abc@xyz.hu/.com): ")
                            email_list = item.split('@')
                            if not user_to_change.valid_email_adress(email_list):
                                print("Please enter your e-mail correctly! (abc@xyz.hu/.com)")
                                item = ""
                            else:
                                items[0][4] = item

                    elif item_to_change == "6":
                        item = ""
                        while item == "":
                            item = input("Enter the new Blood Type Name: ")
                            if user_to_change.valid_blood_type(item):
                                items[0][5] = item
                            else:
                                item = ""

                    elif item_to_change == "7":
                        item = ""
                        while item == "":
                            item = input("Enter the new Birth Date Name: ")
                            if user_to_change.valid_birth_date(item):
                                items[0][6] = item
                            else:
                                item = ""

                    elif item_to_change == "8":
                        item = ""
                        while item == "":
                            item = input("Enter the new Weight(kg): ")
                            if item.isdigit() and int(item) >= 50:
                                items[0][8] = item
                            else:
                                print("Your weight is too low, try this: ")
                                webbrowser.open("https://falatozz.hu/rendeles/Miskolc/")
                                item = ""

                    elif item_to_change == "9":
                        item = ""
                        while item == "":
                            item = input("Enter the new Last Donation Date: ")
                            if user_to_change.valid_last_donation_date(item):
                                last_donation = datetime.strptime(item, "%Y.%m.%d").date()
                                elapsed_months = (datetime.now().date() - last_donation).days // 30
                                if not elapsed_months <= 3:
                                    items[0][9] = item
                                else:
                                    print("You can't add a date within 3 months from now")
                                    item = ""

                    elif item_to_change == "10":
                        item = ""
                        while item == "":
                            item = input("Enter the new Id Expiration date: ")
                            id_expiration = datetime.strptime(item, "%Y.%m.%d").date()
                            if datetime.now().date() < id_expiration:
                                items[0][10] = item
                            else:
                                print("Sorry you can't add that expiration date")
                                item = ""

                    elif item_to_change == "11":
                        item = ""
                        available_answers = ["y", "n"]
                        while item == "":
                            item = input("Enter the new was she/he sick?: ")
                            if item.lower() in available_answers:
                                items[0][12] = item
                            else:
                                item = ""

        pass

    def Options_for_donor(self):
        print('-' * 36)
        print(" 1, First name \n",
              "2, Last name \n",
              "3, Gender \n",
              "4, Identifier \n",
              "5, Email \n",
              "6, Blood Type \n",
              "7, Birth Date \n",
              "8, Weight \n",
              "9, Last Donation Date \n",
              "10, Id Expiration Date \n",
              "11, Was she/he sick? \n")

    def change_stuff_donation(self):
        pass


if __name__ == "__main__":
    Change().change_within()
