from tkinter import *
import tkinter.font as font


from settings import StaticValues, Specs
import functions
import logic

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
start = Button(fm, text='Start', command=functions.start, width=15, height=2, bg='#212121', fg='white', activebackground='#484848',
               activeforeground='White', font=myFont)

next = Button(fm, text='Weiter', command=functions.start, width=15, height=2, bg='#212121', fg='white', activebackground='#484848',
              activeforeground='White', font=myFont)

start.pack(side=RIGHT, padx=20, pady=20)
next.pack(side=RIGHT)

fm.pack(side=BOTTOM, fill=X)

screen.mainloop()







