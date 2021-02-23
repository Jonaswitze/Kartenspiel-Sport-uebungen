import settings
from tkinter import messagebox
from menuSettings import openSettings
import os, sys

def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def action_get_info_dialog():
    m_text = "\
************************************************\n\
                              Autoren: \n\
      Jonas-Matthias Witze & Joshua Rahmow\n\n\
                        Date: 05.02.2021\n\
                         Version: 1.18.37\n\
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

