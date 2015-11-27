import os
import csv
from Donation_User import UserData2
import webbrowser
from datetime import datetime
import Menu
from Donation_Location import LocationData




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
            File = open("./Data/Donor_Data.csv", newline="")
            reader = csv.reader(File, delimiter=",")

            ids = []
            for row in reader:
                ids.append(row[3])
            if not donor_to_change in ids:
                print("The id you entered is not valid")
                donor_to_change = ""
            else:
                items = []
                i = -1
                File = open("./Data/Donor_Data.csv", newline="")
                reader = csv.reader(File, delimiter=",")
                for row in reader:
                    i += 1
                    if donor_to_change in row:
                        items.append(row)
                os.system("cls")
                self.Options_for_donor()
                item_to_change = input("I want to change(1-11):")
                user_to_change = UserData2()

                if item_to_change == "1":
                    item = ""
                    while item == "":
                        item = input("Enter the new First Name: ")
                        self.print_old_items(items)
                        if user_to_change.valid_first_name(item):
                            items[0][0] = item
                        else:
                            item = ""

                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()


                elif item_to_change == "2":
                    item = ""
                    while item == "":
                        item = input("Enter the new Last Name: ")
                        self.print_old_items(items)
                        if user_to_change.valid_last_name(item):
                            items[0][1] = item
                        else:
                            item = ""
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "3":
                    item = ""
                    while item == "":
                        item = input("Enter the new Gender: ")
                        if user_to_change.valid_gender(item):
                            self.print_old_items(items)
                            items[0][2] = item
                        else:
                            item = ""
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "4":
                    item = ""
                    while item == "":
                        item = input("Enter the new Identifier: ")
                        if item in ids:
                            print("The ID your entered is not Unique")
                            item = ""
                        elif user_to_change.valid_identifier(item):
                            self.print_old_items(items)
                            items[0][3] = item

                        else:
                            item = ""

                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "5":
                    item = ""
                    while item == "":
                        item = input("E-mail (abc@xyz.hu/.com): ")
                        email_list = item.split('@')
                        if not user_to_change.valid_email_adress(email_list):
                            print("Please enter your e-mail correctly! (abc@xyz.hu/.com)")
                            item = ""
                        else:
                            self.print_old_items(items)
                            items[0][4] = item
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "6":
                    item = ""
                    while item == "":
                        item = input("Enter the new Blood Type: ")
                        if user_to_change.valid_blood_type(item):
                            self.print_old_items(items)
                            items[0][5] = item
                        else:
                            item = ""
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "7":
                    item = ""
                    while item == "":
                        item = input("Enter the new Birth Date: ")
                        if user_to_change.valid_birth_date(item):
                            self.print_old_items(items)
                            items[0][6] = item
                        else:
                            item = ""

                        birth_date = datetime.strptime(item, "%Y.%m.%d").date()
                        calculated_age = (datetime.now().date() - birth_date).days // 365
                        if calculated_age < 18:
                            print("Sorry you are too young to donate")
                            item = ""
                        else:
                            print(type(calculated_age))
                            items[0][7] = calculated_age
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "8":
                    item = ""
                    while item == "":
                        item = input("Enter the new Weight(kg): ")
                        if item.isdigit() and int(item) >= 50:
                            self.print_old_items(items)
                            items[0][8] = item
                        else:
                            print("Your weight is too low, try this: ")
                            webbrowser.open("https://falatozz.hu/rendeles/Miskolc/")
                            item = ""
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "9":
                    item = ""
                    while item == "":
                        item = input("Enter the new Last Donation Date: ")
                        if user_to_change.valid_last_donation_date(item):
                            last_donation = datetime.strptime(item, "%Y.%m.%d").date()
                            elapsed_months = (datetime.now().date() - last_donation).days // 30
                            if not elapsed_months <= 3:
                                self.print_old_items(items)
                                items[0][9] = item
                            else:
                                print("You can't add a date within 3 months from now")
                                item = ""

                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "10":
                    item = ""
                    while item == "":
                        item = input("Enter the new Id Expiration date: ")
                        id_expiration = datetime.strptime(item, "%Y.%m.%d").date()
                        if datetime.now().date() < id_expiration:
                            self.print_old_items(items)
                            items[0][10] = item
                        else:
                            print("Sorry you can't add that expiration date")
                            item = ""
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "11":
                    item = ""
                    available_answers = ["y", "n"]
                    while item == "":
                        item = input("Enter the new was she/he sick?: ")
                        if item.lower() in available_answers:
                            self.print_old_items(items)
                            items[0][12] = item
                        else:
                            item = ""
                    list_of_items = self.convert_list_into_string(items)
                    self.print_new_items(items)
                    self.delete_id_from_database(donor_to_change)
                    with open("./Data/Donor_Data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

    def print_new_items(self, items):
        print("New items: ", end="")
        print(items, "\n")

    def print_old_items(self, items):
        print("Old items: ", end="")
        print(items)

    def change_stuff_donation(self):
        location_to_change = ""
        while location_to_change == "":
            location_to_change = input("Please type the id of the Location you want to change: ")
            File = open("./Data/Location_data.csv", newline="")
            reader = csv.reader(File, delimiter=",")

            ids = []
            for row in reader:
                ids.append(row[0])
            if not location_to_change in ids:
                location_to_change = ""
            else:
                items = []
                i = -1
                File = open("./Data/Location_data.csv", newline="")
                reader = csv.reader(File, delimiter=",")
                for row in reader:
                    i += 1
                    if location_to_change in row:
                        items.append(row)
                os.system("cls")
                self.Options_for_donation()
                item_to_change = input("I want to change(1-9):")
                loc_to_change = LocationData()

                if item_to_change == "1":
                    item = ""
                    while item == "":
                        item = input("Enter the new Location ID: ")
                        if not item in ids and not item == "":
                            self.print_old_items(items)
                            items[0][0] = item
                        else:
                            print("Your ID is not Unique: ")
                            item = ""
                        list_of_items = self.convert_list_into_string(items)
                        self.print_new_items(items)
                        self.delete_location_from_database(location_to_change)
                        with open("./Data/Location_Data.csv", "a") as Donor_Text_File:
                            Donor_Text_File.write(list_of_items + "\n")
                        print("Task Completed!")
                        Menu.ask_answer()

                elif item_to_change == "2":
                    item = loc_to_change.get_date_of_event()
                    items[0][1] = item
                    list_of_items = self.convert_list_into_string(items)
                    print(list_of_items)
                    self.delete_location_from_database(location_to_change)
                    with open("./Data/Location_data.csv", "a") as Donor_Text_File:
                        Donor_Text_File.write(list_of_items + "\n")
                    print("Task Completed!")
                    Menu.ask_answer()

                elif item_to_change == "3":
                    item = ""
                    while item == "":
                        item = input("Start time (HH:MM): ")
                        if not loc_to_change.check_time(item):
                            item = ""
                        else:
                            items[0][2] = item
                            item2 = items[0][3]
                            duration_in_minutes = (loc_to_change.parse_time(item2) - loc_to_change.parse_time(item)).total_seconds() /60
                            items[0][10] = duration_in_minutes
                            int_duration = int(duration_in_minutes)
                            preparation_time = 30
                            donation_time = 30
                            available_beds = items[0][7]
                            max_donor_number = ((int_duration - preparation_time) / donation_time) * int(available_beds)
                            items[0][11] = max_donor_number
                            list_of_items = self.convert_list_into_string(items)
                            self.delete_location_from_database(location_to_change)
                            with open("./Data/Location_data.csv", "a") as Donor_Text_File:
                                Donor_Text_File.write(list_of_items + "\n")
                            print("Task Completed!")
                            Menu.ask_answer()


                elif item_to_change == "4":
                    item2 = items[0][2]
                    item = ""
                    while item == "":
                        item = input("End time (HH:MM): ")
                        if not loc_to_change.check_time(item):
                            item = ""
                        elif item < item2:
                            print("You can't save End time before the Start time..")
                            item = ""
                        else:
                            items[0][3] = item
                            item2 = items[0][2]
                            duration_in_minutes = (loc_to_change.parse_time(item) - loc_to_change.parse_time(item2)).total_seconds() /60
                            items[0][10] = duration_in_minutes
                            int_duration = int(duration_in_minutes)
                            preparation_time = 30
                            donation_time = 30
                            available_beds = items[0][7]
                            max_donor_number = ((int_duration - preparation_time) / donation_time) * int(available_beds)
                            items[0][11] = max_donor_number
                            list_of_items = self.convert_list_into_string(items)
                            self.delete_location_from_database(location_to_change)
                            with open("./Data/Location_data.csv", "a") as Donor_Text_File:
                                Donor_Text_File.write(list_of_items + "\n")
                            print("Task Completed!")
                            Menu.ask_answer()

                elif item_to_change == "5":
                    item = ""
                    while item == "":
                        item = input("Enter the new Zip Code ")
                        if not loc_to_change.validate_zip_code(item):
                            self.print_old_items(items)
                            items[0][4] = item
                        else:
                            item = ""

                        list_of_items = self.convert_list_into_string(items)
                        self.print_new_items(items)
                        self.delete_location_from_database(location_to_change)
                        with open("./Data/Location_Data.csv", "a") as Donor_Text_File:
                            Donor_Text_File.write(list_of_items + "\n")
                        print("Task Completed!")
                        Menu.ask_answer()





        pass

    def convert_list_into_string(self, items):
        list_of_items = items
        list_of_items = str(list_of_items).strip('[]')
        list_of_items = list_of_items.replace("'", "")
        list_of_items = list_of_items.replace(" ", "")
        return list_of_items

    def delete_id_from_database(self, donor_to_change):
        donor_data = open("./Data/Donor_Data.csv", "r")
        lines = donor_data.readlines()
        donor_data.close()
        donor_data = open("./Data/Donor_Data.csv", "w")
        line_counter = 0
        for line in lines:
            if donor_to_change not in line:
                line_counter += 1
                donor_data.write(line)
        donor_data.close()

    def delete_location_from_database(self, item):
        location_file = open("./Data/Location_data.csv", "r+")
        read_line = location_file.readlines()
        location_file.seek(0)
        line_counter = 0
        for line in read_line:
            splitted = line.split(",")
            if item != splitted[0]:
                line_counter += 1
                location_file.write(line)
        location_file.truncate()
        location_file.close()

    def Options_for_donation(self):
        print('-' * 36)
        print(" 1, ID \n",
              "2, Date of Event \n",
              "3, Start time \n",
              "4, End Time \n",
              "5, Zip Code \n",
              "6, City \n",
              "7, Available beds \n"
              " 8, Planned Donor Number \n"
              " 9, Numbber of succesfull donations \n")

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


if __name__ == "__main__":
    Change().change_within()
