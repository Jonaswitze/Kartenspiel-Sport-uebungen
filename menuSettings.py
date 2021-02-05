from tkinter import *
from settings import StaticValues, Specs
import functions



def open():
    def save():
        print("save")


    settings = Tk()
    settings.title("Settings")
    settings.geometry("470x500")
    settings.resizable(width=0, height=0)

    task1 = Label(settings, text="Übung 1: ")
    task2 = Label(settings, text="Übung 2: ")
    task3 = Label(settings, text="Übung 3: ")
    task4 = Label(settings, text="Übung 4: ")

    space = Label(settings, text=" ")
    space2 = Label(settings, text=" ")

    howManyCards = Label(settings, text="Wie viele Runden:")
    howManyReturns = Label(settings, text="Maximale zulässige \n Wiederhoungen (am stück):")

    error = Label(settings, text="Bitte Nur Zahlen bei den Runden und \n Maximale zulässige Wiederhoungen", fg='RED')


    entry_task1 = Entry(settings, bd=5, width=40)
    entry_task2 = Entry(settings, bd=5, width=40)
    entry_task3 = Entry(settings, bd=5, width=40)
    entry_task4 = Entry(settings, bd=5, width=40)

    entry_howManyCards = Entry(settings, bd=5, width=10)
    entry_howManyReturns = Entry(settings, bd=5, width=10)

    save = Button(settings, text="Speichern", width=20, command=save)


    task1.grid(row=0, column=0)
    task2.grid(row=1, column=0)
    task3.grid(row=2, column=0)
    task4.grid(row=3, column=0)
    space.grid(row=4, column=0)
    howManyCards.grid(row=5, column=0)
    howManyReturns.grid(row=6, column=0)
    space2.grid(row=7, column=0)
    error.grid(row=8, column=0)

    entry_task1.grid(row=0, column=1)
    entry_task2.grid(row=1, column=1)
    entry_task3.grid(row=2, column=1)
    entry_task4.grid(row=3, column=1)
    entry_howManyCards.grid(row=5, column=1)
    entry_howManyReturns.grid(row=6, column=1)
    save.grid(row=8, column=1)

    settings.mainloop()
