import csv
import Menu


reload_list = []

location_id_to_delete = ""
while location_id_to_delete == "":
        location_id_to_delete = input("Please enter the line ID to delete: ")
        if not location_id_to_delete.isdigit():
            print("Your input must be a Number")
            location_id_to_delete = ""

with open("./Data/Location_Data.csv", "r") as TextIn:
    csv_text = csv.reader(TextIn)
    record_list = list(csv_text)
    for line in record_list:
        if not location_id_to_delete == line[0]:
            reload_list.append(line)
    for i in range(len(reload_list)):
        if not i == 0:
            reload_list[i][0] = i



with open("./Data/Location_Data.csv", "w") as NewTextData:
     writer = csv.writer(NewTextData)
     writer.writerows(reload_list)

Menu.ask_answer()
