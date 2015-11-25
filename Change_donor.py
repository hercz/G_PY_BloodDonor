# from msvcrt import getch
# while True:
#    key = ord(getch())
#    print(key)


class Change():

    def change_within(self):
        print('-' * 36)
        print("Change within:")
        print("1, Donors")
        print("2, Donation")
        print()
        answer = ""
        while answer == "":
            answer = input("Are You sure in your selection?: ")
            if answer.lower() == "1":
                self.change_stuff_donor()
            elif answer.lower() == "2":


            else:
                answer = ""
        pass

    def change_stuff_donor(self):
        donor_to_change = input("Please type the id of the Donor you want to change: ")



        pass