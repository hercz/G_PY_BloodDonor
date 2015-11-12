__author__ = 'Vegh Adam'

class Search():
    @staticmethod
    def separator_line():
        print("-" * 32)

    def __init__(self):
        self.get_search()

    def get_search(self):
        Search.separator_line()
        print("Search within:")
        print("1, Donors")
        print("2, Donation")
        print()
        search_number = ""
        while search_number == "":
            search_number = input("Please choose from the list above: ")
            if not (search_number == '1' or search_number == '2'):
                search_number = ""
        if search_number == '1':
            pass
        elif search_number == '2':
            pass
if __name__ == "__main__":
    Search()