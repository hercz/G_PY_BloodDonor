import csv, os, Menu

__author__ = 'Vegh Adam'

def print_separator_line():
    print("-" * 32)

def print_one_donor(line):
    first_name_to_print = line[0]
    last_name_to_print = line[1]
    weight_to_print = line[8]
    birth_date_to_print = line[6]
    age_to_print = line[7]
    email_to_print = line[4]
    print_separator_line()
    print("""{0}\n{1} kg\n{2} - {3} years old\n{4}
            """.format(first_name_to_print + last_name_to_print,
                       weight_to_print,
                       birth_date_to_print,
                       age_to_print,
                       email_to_print))
    print_separator_line()


def print_one_location(line):
    city_to_print = line[5]
    date_of_event_to_print = line[1]
    for char in date_of_event_to_print:
        date_of_event_corrected = date_of_event_to_print.replace("-", ".")

    address_to_print = line[6]
    print_separator_line()
    print("""{0},{1},{2}
            """.format(city_to_print, date_of_event_corrected, address_to_print))

def listing():
    os.system("cls")
    list_options = ""
    while list_options == "":
        print("Please choose which one you want to List: ")
        print("     1.Donor")
        print("     2.Donation")
        list_options = input("")
        if list_options == "1":
            with open("./Data/Donor_Data.csv", "r") as TextFile:
                csv_text = csv.reader(TextFile)
                counter = 0
                page_size = 3
                record_list = list(csv_text)
                for line in record_list[1:]:
                    counter += 1
                    print_one_donor(line)
                    if counter % page_size == 0 and counter <= len(record_list):
                        next_page = input("For next page press: N ")
                        if next_page.lower() == "n":
                            os.system("cls")
                Menu.ask_answer()

        if list_options == "2":
            with open("./Data/Location_Data.csv", "r") as TextFile:
                csv_text = csv.reader(TextFile)
                counter = 0
                page_size = 3
                record_list = list(csv_text)
                for line in record_list[1:]:
                    counter += 1
                    print_one_location(line)
                    if counter % page_size == 0 and counter <= len(record_list):
                        next_page = input("For next page press: N ")
                        if next_page.lower() == "n":
                            os.system("cls")
                Menu.ask_answer()

if __name__ == "__main__":
    listing()
