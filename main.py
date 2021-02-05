from tkinter import *
from settings import StaticValues, Specs
import functions

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
#functions.action_openSettings()

screen.mainloop()

