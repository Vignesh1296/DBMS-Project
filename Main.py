#DBMS PROJECT
#CREATED BY VIGNESH (RA1511003010323)
#15IT302J

from tkinter import *
import sqlite3
import tkinter.ttk as ttk

def Database():
    global cursor, conn
    cursor = sqlite3.connect("dbms.db")
    cursor.commit()

def DatabaseView():


def Main():
    root = Tk()
    w = 450
    h = 300
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Database Mangaement System Project")
    root.mainloop()


Main()
