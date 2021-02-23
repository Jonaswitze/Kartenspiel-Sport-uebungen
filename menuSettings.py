from tkinter import *
import configparser
import functions
from settings import Specs
from os import path


def openSettings():
    cfg = configparser.ConfigParser()
    cfgr = configparser.ConfigParser()
    cfgr.read('settings.cfg')
    if path.exists("settings.cfg"):
        try:
            cfgr.get('Tasks', '1')
            Specs.settingsnew = False
        except:
            Specs.settingsnew = True

    else:
        Specs.settingsnew = True

    def save():
        file = open('settings.cfg', 'w')
        cfg.add_section('Tasks')
        cfg.add_section('Other')
        cfg.set('Tasks', '1', entry_task1.get())
        cfg.set('Tasks', '2', entry_task2.get())
        cfg.set('Tasks', '3', entry_task3.get())
        cfg.set('Tasks', '4', entry_task4.get())

        cards = str(entry_howManyCards.get())
        returns = str(entry_howManyReturns.get())

        try:
            test1 = int(cards)
            cfg.set('Other', 'howManyCards', entry_howManyCards.get())
        except:
            try:
                test2 = int(returns)
                cfg.set('Other', 'howManyReturns', entry_howManyReturns.get())
            except:
                cfg.set('Other', 'howManyReturns', 'ERROR')
                cfg.write(file)
                file.close()
                settings.destroy()
                functions.error()
            cfg.set('Other', 'howManyCards', 'ERROR')
            cfg.write(file)
            file.close()
            settings.destroy()
            functions.error()
        try:
            test2 = int(returns)
            cfg.set('Other', 'howManyReturns', entry_howManyReturns.get())
        except:
            cfg.write(file)
            file.close()
            settings.destroy()
            functions.error()

        cfg.write(file)
        file.close()
        settings.destroy()
        functions.restart()
        sys.exit()

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

    entry_task1 = Entry(settings, bd=5, width=40)
    entry_task2 = Entry(settings, bd=5, width=40)
    entry_task3 = Entry(settings, bd=5, width=40)
    entry_task4 = Entry(settings, bd=5, width=40)

    entry_howManyCards = Entry(settings, bd=5, width=10)
    entry_howManyReturns = Entry(settings, bd=5, width=10)

    save = Button(settings, text="Speichern", width=20, command=save, bg='#212121', fg='white', activebackground='#484848', activeforeground='White')

    task1.grid(row=0, column=0)
    task2.grid(row=1, column=0)
    task3.grid(row=2, column=0)
    task4.grid(row=3, column=0)
    space.grid(row=4, column=0)
    howManyCards.grid(row=5, column=0)
    howManyReturns.grid(row=6, column=0)
    space2.grid(row=7, column=0)

    entry_task1.grid(row=0, column=1)
    entry_task2.grid(row=1, column=1)
    entry_task3.grid(row=2, column=1)
    entry_task4.grid(row=3, column=1)
    entry_howManyCards.grid(row=5, column=1)
    entry_howManyReturns.grid(row=6, column=1)
    save.grid(row=8, column=1)

    if not Specs.settingsnew:
        entry_task1.insert(0, cfgr.get('Tasks', '1'))
        entry_task2.insert(0, cfgr.get('Tasks', '2'))
        entry_task3.insert(0, cfgr.get('Tasks', '3'))
        entry_task4.insert(0, cfgr.get('Tasks', '4'))

        entry_howManyReturns.insert(0, cfgr.get('Other', 'howManyReturns'))
        entry_howManyCards.insert(0, cfgr.get('Other', 'howManyCards'))

    settings.mainloop()
