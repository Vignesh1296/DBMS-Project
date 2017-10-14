#DBMS PROJECT
#CREATED BY VIGNESH (RA1511003010323)
#15IT302J

from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import tkinter.ttk as ttk

def Database():
    global cursor, conn
    cursor = sqlite3.connect("dbms.db")
    cursor.commit()

def DatabaseView():
    None

def b1():
    frame = Toplevel()
    global cursor, conn
    Database()
    def ViewAll():
        None

def b2():
    frame = Toplevel()
    global cursor, conn
    Database()
    def ViewAll():
        None

def b3():
    frame = Toplevel()
    global cursor, conn
    Database()
    def ViewAll():
        None

def b4():
    frame = Toplevel()
    global cursor, conn
    Database()
    def ViewAll():
        None

def b5():
    frame = Toplevel()
    global cursor, conn
    Database()
    def ViewAll():
        None

def About():
    tm.showinfo("About", "DBMS Project v1.0 \nInsert and view records")

def Main():
    root = Tk()
    w = 1024
    h = 720
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("ABC Software Corporation Database Management v1.0")
    root.config(bg="#0700ad")
    l1 = Label(root, text="ABC Software Corporation Database", bg="#ffffff", fg="#000000", bd=3, font=('arial',35))
    l1.pack(fill='x')
    b1=Button(root, text="Developers List Record", command=None, font=('arial', 20), width=19)
    b1.pack(pady=8)
    b2=Button(root, text="Games List Record", command=None, font=('arial', 20), width=19)
    b2.pack(pady=8)
    b3=Button(root, text="HQ List Record", command=None, font=('arial', 20), width=19)
    b3.pack(pady=8)
    b4=Button(root, text="Servers List Record", command=None, font=('arial', 20), width=19)
    b4.pack(pady=8)
    b5=Button(root, text="User Region List Record", command=None, font=('arial', 20), width=19)
    b5.pack(pady=8)
    b8 = Button(root, text="Exit", command=root.quit, font=('arial', 20), width=10)
    b8.pack(side=LEFT, padx=120)
    b7 = Button(root, text="Help", command=None, font=('arial', 20), width=10)
    b7.pack(side=RIGHT, padx=120)
    root.resizable(0, 0)
    root.mainloop()

Main()
