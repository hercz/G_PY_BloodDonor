from tkinter import *
import os


def ask_answer():
    answer = ""
    while answer == "":
        answer = input("Do you want to go back to the Main Menu? Y/N ")
        if answer == "Y" or answer == "y":
            the_menu()
        elif answer == "N" or answer == "n":
            exit()
        else:
            print("You answer must be Y or N ")
            answer = ""

def print_separator_line():
    print("-" * 32)

def option1():


    import Donation_User as user

    print_separator_line()
    print("Welcome in Donor registration application!")
    print()
    person = user.UserData()
    ask_answer()

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Add new donor", command=option1)
filemenu.add_command(label="Add new donation event", command=donothing)
filemenu.add_command(label="Delete a donor", command=donothing)
filemenu.add_command(label="Delete a donation event", command=donothing)
filemenu.add_command(label="List donor or donation events", command=donothing)
filemenu.add_command(label="Search", command=donothing)
filemenu.add_command(label="Exit", command=donothing)


filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Donor", command=donothing)
editmenu.add_command(label="Donation", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()