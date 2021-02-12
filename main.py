from tkinter import *
import tkinter.font as font
from _thread import start_new_thread
from settings import StaticValues, Specs
import functions

def action_start():
    start_new_thread(functions.run, ())
    nextBT.pack(side=RIGHT)

screen = Tk()
screen.title("Ich mache nun was.")
screen.geometry(str(StaticValues.W) + "x" + str(StaticValues.H))

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

myFont = font.Font(size=15)
startBT = Button(fm, text='Start', command=action_start, width=15, height=2, bg='#212121', fg='white', activebackground='#484848',
               activeforeground='White', font=myFont)

nextBT = Button(fm, text='Weiter', command=functions.action_next, width=15, height=2, bg='#212121', fg='white', activebackground='#484848',
              activeforeground='White', font=myFont)

startBT.pack(side=RIGHT, padx=20, pady=20)

fm.pack(side=BOTTOM, fill=X)

screen.mainloop()







