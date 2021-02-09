from settings import StaticValues, Specs
from tkinter import messagebox
from menuSettings import openSettings
import logic
from _thread import start_new_thread



def action_get_info_dialog():
    m_text = "\
************************************************\n\
                              Autoren: \n\
      Jonas-Matthias Witze & Joshua Rahmow\n\n\
                        Date: 05.02.2021\n\
                           Version: 1.27\n\
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

def run():
    while True:
        print('1')
        for i in range(0, logic.cards()):
            while True:
                if Specs.next:
                    Specs.next = False
                    print('Weiter')
                    print(logic.logic())
                    break
                else:
                    continue

def start():
    Specs.next = False
    start_new_thread(run, ())  ## Funkzuniert nicht: schleife wird nicht ausgefürt, thread wird direkt gekillt
