from settings import StaticValues, Specs
from tkinter import messagebox


def action_get_info_dialog():
    m_text = "\
************************************************\n\
                              Autoren: \n\
      Jonas-Matthias Witze & Joshua Rahmow\n\n\
                        Date: 05.02.2021\n\
                           Version: 1.07\n\
************************************************"
    messagebox.showinfo(message=m_text, title="Infos")

def action_settings():
    print("test")
