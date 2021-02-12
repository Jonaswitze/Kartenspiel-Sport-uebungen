from settings import StaticValues, Specs
import settings
from tkinter import messagebox
from menuSettings import openSettings
import logic



def action_get_info_dialog():
    m_text = "\
************************************************\n\
                              Autoren: \n\
      Jonas-Matthias Witze & Joshua Rahmow\n\n\
                        Date: 05.02.2021\n\
                           Version: 1.28\n\
************************************************"
    messagebox.showinfo(message=m_text, title="Infos")


def action_openSettings():
    openSettings()


def error():
    m_text = "Bitte Nur Zahlen, bei den Runden und \n Maximale zulässige Wiederhoungen"
    messagebox.showinfo(message=m_text, title="ERROR")
    action_openSettings()


def action_next():
    Specs.next = True
    print(Specs.next)

def run():

    print(logic.cards())
    for i in range(0, logic.cards()):
        while True:
            if Specs.next:
                Specs.next = False
                if logic.logic() == 'A':
                    settings.currentTask = 'A'
                    #print(settings.currentTask)
                elif logic.logic() == 'B':
                    settings.currentTask = 'B'
                    #print(settings.currentTask)
                elif logic.logic() == 'C':
                    settings.currentTask = 'C'
                    #print(settings.currentTask)
                elif logic.logic() == 'D':
                    settings.currentTask = 'D'
                    #print(settings.currentTask)
                break



