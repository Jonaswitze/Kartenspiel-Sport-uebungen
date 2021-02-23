from tkinter import *
import tkinter.font as font
from _thread import start_new_thread
import settings
import functions
import configparser
import logic

def action_ende():
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    startBT.pack(side=RIGHT, padx=20, pady=20)
    settings.Specs.start = False
    settings.Specs.next = True
    endeBT.pack_forget()

def action_start():
    settings.Specs.start = True
    start_new_thread(run, ())
    nextBT.pack(side=RIGHT, padx=20, pady=20)
    startBT.pack_forget()
    endeBT.pack_forget()

def run():
    cards = logic.cards()
    for i in range(0, cards):
        while True:
            interval = Label(fm3, text=str(logic.interval()) + ' Wiederholung(en) von', font=textFont)
            settings.Specs.next = False
            logic.logic()
            fm3.pack_forget()
            if settings.task1:
                label2.pack_forget()
                label3.pack_forget()
                label4.pack_forget()
                interval.pack()
                label1.pack()
                fm3.pack(expand=True)
            elif settings.task2:
                label1.pack_forget()
                label3.pack_forget()
                label4.pack_forget()
                interval.pack()
                label2.pack()
                fm3.pack(expand=True)
            elif settings.task3:
                label1.pack_forget()
                label2.pack_forget()
                label4.pack_forget()
                interval.pack()
                label3.pack()
                fm3.pack(expand=True)
            elif settings.task4:
                label1.pack_forget()
                label2.pack_forget()
                label3.pack_forget()
                interval.pack()
                label4.pack()
                fm3.pack(expand=True)
            break
        if i != cards:
            while True:
                if settings.Specs.next:
                    interval.destroy()
                    break

    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    startBT.pack_forget()
    nextBT.pack_forget()
    endeBT.pack(side=RIGHT, padx=20, pady=20)


screen = Tk()
screen.title("Ich mache nun was.")
screen.geometry(str(settings.StaticValues.W) + "x" + str(settings.StaticValues.H))

menuleiste = Menu(screen)
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

datei_menu.add_command(label="Settings", command=functions.action_openSettings)
datei_menu.add_command(label="About", command=functions.action_get_info_dialog)
datei_menu.add_separator()
datei_menu.add_command(label="Exit", command=screen.quit)

menuleiste.add_cascade(label="Datei", menu=datei_menu)

screen.config(menu=menuleiste)

fm = Frame(screen)

btFont = font.Font(size=15)

startBT = Button(fm, text='Start', command=action_start, width=15, height=2, bg='#212121', fg='white',
                 activebackground='#484848',
                 activeforeground='White', font=btFont)

nextBT = Button(fm, text='Weiter', command=functions.action_next, width=15, height=2, bg='#212121', fg='white',
                activebackground='#484848',
                activeforeground='White', font=btFont)

endeBT = Button(fm, text='ENDE', command=action_ende, width=15, height=2, bg='#212121', fg='white',
                activebackground='#484848',
                activeforeground='White', font=btFont)


startBT.pack(side=RIGHT, padx=20, pady=20)
fm.pack(side=BOTTOM, fill=X)

fm2 = Frame(screen)
fm3 = Frame(fm2)

textFont = font.Font(size=20, weight="bold")

cfgr = configparser.ConfigParser()
cfgr.read('settings.cfg')

label1 = Label(fm3, text=cfgr.get('Tasks', '1'), font=textFont)
label2 = Label(fm3, text=cfgr.get('Tasks', '2'), font=textFont)
label3 = Label(fm3, text=cfgr.get('Tasks', '3'), font=textFont)
label4 = Label(fm3, text=cfgr.get('Tasks', '4'), font=textFont)


fm2.pack(fill=BOTH, expand=True)

screen.mainloop()
