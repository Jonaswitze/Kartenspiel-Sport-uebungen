import settings
from tkinter import messagebox
from menuSettings import openSettings


def action_get_info_dialog():
    m_text = "\
************************************************\n\
                              Autoren: \n\
      Jonas-Matthias Witze & Joshua Rahmow\n\n\
                        Date: 05.02.2021\n\
                         Version: 1.17.36\n\
************************************************"
    messagebox.showinfo(message=m_text, title="About Kartenspiel Übungen")


def action_openSettings():
    openSettings()


def error():
    m_text = "Bitte Nur Zahlen, bei den Runden und \n Maximale zulässige Wiederhoungen"
    messagebox.showinfo(message=m_text, title="ERROR")
    action_openSettings()

def emptySettings():
    m_text = "Die Settings sind noch Leer!"
    messagebox.showinfo(message=m_text, title="Info!")
    action_openSettings()

def restart():
    m_text = "Bitte Programm neu Öffnen"
    messagebox.showinfo(message=m_text, title="Info!")

def action_next():
    settings.Specs.next = True

