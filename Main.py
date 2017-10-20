#DBMS PROJECT
#CREATED BY VIGNESH (RA1511003010323)
#15IT302J

from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import tkinter.ttk as ttk


def msg():
    tm.showinfo("Insert", "Record Inserted Successully")

def Size(w, h, master):
    ws = master.winfo_screenwidth()  # width of the screen
    hs = master.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))

def Display(result):
    frame = Toplevel()
    for data in result:
        Label(frame, text=data).pack()


def b1():
    global conn, cursor
    global f1, f2, f3, f4, f5, f6
    conn = sqlite3.connect("dbms.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'DevList'(DevTeam TEXT PRIMARY KEY,Head TEXT,Location TEXT,Region TEXT,Servers TEXT,Type TEXT)")
    conn.commit()
    f1 = StringVar()
    f2 = StringVar()
    f3 = StringVar()
    f4 = StringVar()
    f5 = StringVar()
    f6 = StringVar()
    f7 = StringVar()

    def Insert():
        global f1, f2, f3, f4, f5, f6
        global conn, cursor
        f1.get(), f2.get(), f3.get(), f4.get(), f5.get(), f6.get()
        cursor.execute("INSERT INTO 'DevList'(DevTeam, Head, Location, Region, Servers, Type) VALUES(?,?,?,?,?,?)",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get()), str(f6.get())))
        conn.commit()
        msg()

    def View(result):
        view = Toplevel()
        Size(1024, 300, view)
        scrollbarx = Scrollbar(view, orient=HORIZONTAL)
        scrollbary = Scrollbar(view, orient=VERTICAL)
        tree = ttk.Treeview(view, columns=("Team Name", "Head Developer", "Location", "Region", "Servers", "Type"),
                            selectmode='extended', height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Team Name', text="Team Name", anchor=W), tree.heading('Head Developer', text="Head Developer", anchor=W),
        tree.heading('Location', text="Location", anchor=W), tree.heading('Region', text="Region", anchor=W),
        tree.heading('Servers', text="Servers", anchor=W), tree.heading('Type', text="Type", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120),
        tree.column('#2', stretch=NO, minwidth=0, width=200), tree.column('#3', stretch=NO, minwidth=0, width=120),
        tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        for data in result:
            tree.insert('','end', values=data)
        tree.pack()

    def Select():
        global conn, cursor
        cursor.execute("SELECT * FROM DevList")
        fetch = cursor.fetchall()
        View(fetch)

    def Count():
        global conn, cursor
        cursor.execute("SELECT COUNT(*) FROM DevList")
        fetch = cursor.fetchall()
        Display(fetch)

    def Distinct():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM DevList")
        fetch = cursor.fetchall()
        View(fetch)

    def Update():
        global f1, f2, f3, f4, f5, f6
        global conn, cursor
        cursor.execute("UPDATE DevList SET DevTeam = ?, Head = ?, Location = ?, Region = ?, Servers = ?, Type = ?",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get()), str(f6.get())))
        conn.commit()
        msg()

    def Order():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM DevList ORDER BY Servers DESC")
        fetch = cursor.fetchall()
        View(fetch)

    def Delete1():
        global conn, cursor, delete
        frame = Toplevel()
        delete = StringVar()
        Label(frame, text="Head Name :").pack(side=LEFT)
        e = Entry(frame, textvariable=delete)
        e.pack(side=LEFT)
        Button(frame, text="Delete", command=Delete2).pack(side=LEFT)

    def Delete2():
        global conn, cursor, delete
        cursor.execute("DELETE FROM DevList WHERE Head = ? ", [str(delete.get())])
        conn.commit()


    b1 = Tk()
    b1.title("Developers Record")
    b1.config(bg='#99ff99')
    Size(800, 450, b1)
    middle = Frame(b1, bg='#99ff99')
    middle.grid(row=1, column=0, sticky=W + E + S + N, columnspan=2, padx=30)
    lframe = Frame(b1, bg='#99ff99', bd=1, relief=SOLID)
    lframe.grid(row=0, column=0, sticky=W, pady=20, padx=20)
    rframe = Frame(b1, bg='#99ff99', bd=1, relief=SOLID)
    rframe.grid(row=0, column=1, sticky=E, pady=20, padx=20)
    Label(lframe, text="Team Name", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(lframe , font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(lframe, text="Head Developer", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(lframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(lframe, text="Location", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(lframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(lframe, text="Region", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(lframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(lframe, text="Servers Alotted", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(lframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(lframe, text="Type", bg='#99ff99', font=('arial', 13)).grid(row=6, column=0, sticky=W)
    f6 = Entry(lframe, font=('arial', 13))
    f6.grid(row=6, column=1, padx=10, pady=10)
    Label(rframe, text="Team Name", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(rframe , font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(rframe, text="Head Developer", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(rframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(rframe, text="Location", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(rframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(rframe, text="Region", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(rframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(rframe, text="Servers Alotted", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(rframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(rframe, text="Type", bg='#99ff99', font=('arial', 13)).grid(row=6, column=0, sticky=W)
    f6 = Entry(rframe, font=('arial', 13))
    f6.grid(row=6, column=1, padx=10, pady=10)
    Button(lframe, text="Insert Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(rframe, text="Update Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(middle, text="Exit", command=b1.destroy, font=('arial', 13), width=10).grid(row=0, column=0, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="SELECT *", command=Select, font=('arial', 13), width=10).grid(row=0, column=1, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="COUNT *", command=Count, font=('arial', 13), width=10).grid(row=0, column=2, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DISTINCT *", command=Distinct, font=('arial', 13), width=10).grid(row=0, column=3, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="ORDER BY", command=Order, font=('arial', 13), width=10).grid(row=0, column=4, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DELETE", command=Delete1, font=('arial', 13), width=10).grid(row=0, column=5, sticky=W + E + N + S, pady=7, padx=10)
    b1.resizable(0, 0)

def b2():
    global f1, f2, f3, f4, f5
    global conn, cursor
    conn = sqlite3.connect("dbms.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS 'Games' ( `Game` TEXT, `Platform` TEXT, `Type` TEXT, `Dev` TEXT, `Servers` TEXT )")
    conn.commit()
    f1 = StringVar()
    f2 = StringVar()
    f3 = StringVar()
    f4 = StringVar()
    f5 = StringVar()

    def Insert():
        global f1, f2, f3, f4, f5
        global conn, cursor
        f1.get(), f2.get(), f3.get(), f4.get(), f5.get()
        cursor.execute("INSERT INTO 'Games' (Game, Platform, Type, Dev, Servers) VALUES(?,?,?,?,?)",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get())))
        conn.commit()
        msg()

    def View(fetch):
        global conn, cursor
        view = Toplevel()
        Size(1024, 300, view)
        scrollbarx = Scrollbar(view, orient=HORIZONTAL)
        scrollbary = Scrollbar(view, orient=VERTICAL)
        tree = ttk.Treeview(view, columns=("Game", "Platform", "Type", "Developer", "Servers"),
                            selectmode='extended', height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Game', text="Game", anchor=W), tree.heading('Platform', text="Platform", anchor=W),
        tree.heading('Type', text="Type", anchor=W), tree.heading('Developer', text="Developer", anchor=W),
        tree.heading('Servers', text="Servers", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120),
        tree.column('#2', stretch=NO, minwidth=0, width=200), tree.column('#3', stretch=NO, minwidth=0, width=120),
        tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        cursor.execute("SELECT * FROM Games")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('','end', values=data)
        tree.pack()

    def Select():
        global conn, cursor
        cursor.execute("SELECT * FROM Games")
        fetch = cursor.fetchall()
        View(fetch)

    def Count():
        global conn, cursor
        cursor.execute("SELECT COUNT(*) FROM Games")
        fetch = cursor.fetchall()
        View(fetch)

    def Distinct():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Games")
        fetch = cursor.fetchall()
        View(fetch)

    def Update():
        global conn, cursor
        cursor.execute("UPDATE Games SET Game = ?, Platform = ?, Type = ?, Dev = ?, Servers = ?",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get())))
        conn.commit()

    def Order():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Games ORDER BY Servers DESC")
        fetch = cursor.fetchall()
        View(fetch)

    def Delete1():
        global conn, cursor, delete
        frame = Toplevel()
        delete = StringVar()
        Label(frame, text="Game Name :").pack(side=LEFT)
        e = Entry(frame, textvariable=delete)
        e.pack(side=LEFT)
        Button(frame, text="Delete", command=Delete2).pack(side=LEFT)

    def Delete2():
        global conn, cursor, delete
        cursor.execute("DELETE FROM Games WHERE Game = ? ", [str(delete.get())])
        conn.commit()


    b2 = Tk()
    b2.title("Games")
    b2.config(bg='#99ff99')
    Size(800, 450, b2)
    middle = Frame(b2, bg='#99ff99')
    middle.grid(row=1, column=0, sticky=W + E + S + N, columnspan=2, padx=30)
    lframe = Frame(b2, bg='#99ff99', bd=1, relief=SOLID)
    lframe.grid(row=0, column=0, sticky=W, pady=20, padx=20)
    rframe = Frame(b2, bg='#99ff99', bd=1, relief=SOLID)
    rframe.grid(row=0, column=1, sticky=E, pady=20, padx=20)
    Label(lframe, text="Game", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(lframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(lframe, text="Platform", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(lframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(lframe, text="Type", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(lframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(lframe, text="Developer", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(lframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(lframe, text="Servers", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(lframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(rframe, text="Game", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(rframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(rframe, text="Platform", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(rframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(rframe, text="Type", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(rframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(rframe, text="Developer", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(rframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(rframe, text="Servers", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(rframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Button(lframe, text="Insert Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(rframe, text="Update Record", command=Update, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(middle, text="Exit", command=b2.destroy, font=('arial', 13), width=10).grid(row=0, column=0, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="SELECT *", command=Select, font=('arial', 13), width=10).grid(row=0, column=1, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="COUNT *", command=Count, font=('arial', 13), width=10).grid(row=0, column=2, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DISTINCT *", command=Distinct, font=('arial', 13), width=10).grid(row=0, column=3, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="ORDER BY", command=Order, font=('arial', 13), width=10).grid(row=0, column=4, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DELETE", command=Delete1, font=('arial', 13), width=10).grid(row=0, column=5, sticky=W + E + N + S, pady=7, padx=10)

    b2.resizable(0, 0)

def b3():
    global f1, f2, f3, f4, f5
    global conn, cursor
    conn = sqlite3.connect("dbms.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `Hq` ( `Name` TEXT, `Office` TEXT, `Servers` TEXT, `Age` TEXT, `Exp` TEXT )")
    conn.commit()

    f1 = StringVar()
    f2 = StringVar()
    f3 = StringVar()
    f4 = StringVar()
    f5 = StringVar()

    def Insert():
        global f1, f2, f3, f4, f5
        global conn, cursor
        f1.get(), f2.get(), f3.get(), f4.get(), f5.get()
        cursor.execute("INSERT INTO `Hq` (Name, Office, Servers, Age, Exp) VALUES(?,?,?,?,?)",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get())))
        conn.commit()
        msg()

    def View(fetch):
        global conn, cursor
        view = Toplevel()
        Size(1024, 300, view)
        scrollbarx = Scrollbar(view, orient=HORIZONTAL)
        scrollbary = Scrollbar(view, orient=VERTICAL)
        tree = ttk.Treeview(view, columns=("Name", "Office", "Servers", "Age", "Experience"),
                            selectmode='extended', height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Name', text="Name", anchor=W), tree.heading('Office', text="Office", anchor=W),
        tree.heading('Servers', text="Servers", anchor=W),
        tree.heading('Age', text="Age", anchor=W), tree.heading('Experience', text="Experience", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120),
        tree.column('#2', stretch=NO, minwidth=0, width=200), tree.column('#3', stretch=NO, minwidth=0, width=120),
        tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        cursor.execute("SELECT * FROM Hq")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('','end', values=data)
        tree.pack()

    def Select():
        global conn, cursor
        cursor.execute("SELECT * FROM Hq")
        fetch = cursor.fetchall()
        View(fetch)

    def Count():
        global conn, cursor
        cursor.execute("SELECT COUNT(*) FROM Hq")
        fetch = cursor.fetchall()
        Display(fetch)

    def Distinct():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Hq")
        fetch = cursor.fetchall()
        View(fetch)

    def Update():
        global conn, cursor
        cursor.execute("UPDATE Hq SET Name = ?, Office = ?, Servers = ?, Age = ?, Exp = ?",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get())))
        conn.commit()
        msg()

    def Order():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Hq ORDER BY Exp DESC")
        fetch = cursor.fetchall()
        View(fetch)

    def Delete1():
        global conn, cursor, delete
        frame = Toplevel()
        delete = StringVar()
        Label(frame, text="Name :").pack(side=LEFT)
        e = Entry(frame, textvariable=delete)
        e.pack(side=LEFT)
        Button(frame, text="Delete", command=Delete2).pack(side=LEFT)

    def Delete2():
        global conn, cursor, delete
        cursor.execute("DELETE FROM Hq WHERE Name = ? ", [str(delete.get())])
        conn.commit()

    b3 = Tk()
    b3.title("HQ List")
    b3.config(bg='#99ff99')
    Size(800, 450, b3)
    middle = Frame(b3, bg='#99ff99')
    middle.grid(row=1, column=0, sticky=W + E + S + N, columnspan=2, padx=30)
    lframe = Frame(b3, bg='#99ff99', bd=1, relief=SOLID)
    lframe.grid(row=0, column=0, sticky=W, pady=20, padx=20)
    rframe = Frame(b3, bg='#99ff99', bd=1, relief=SOLID)
    rframe.grid(row=0, column=1, sticky=E, pady=20, padx=20)
    Label(lframe, text="Name", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(lframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(lframe, text="Office", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(lframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(lframe, text="Servers", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(lframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(lframe, text="Age", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(lframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(lframe, text="Experience", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(lframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(rframe, text="Name", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(rframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(rframe, text="Office", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(rframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(rframe, text="Servers", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(rframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(rframe, text="Age", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(rframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(rframe, text="Experience", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(rframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Button(lframe, text="Insert Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(rframe, text="Update Record", command=Update, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(middle, text="Exit", command=b3.destroy, font=('arial', 13), width=10).grid(row=0, column=0, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="SELECT *", command=Select, font=('arial', 13), width=10).grid(row=0, column=1, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="COUNT *", command=Count, font=('arial', 13), width=10).grid(row=0, column=2, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DISTINCT *", command=Distinct, font=('arial', 13), width=10).grid(row=0, column=3, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="ORDER BY", command=Order, font=('arial', 13), width=10).grid(row=0, column=4, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DELETE", command=Delete1, font=('arial', 13), width=10).grid(row=0, column=5, sticky=W + E + N + S, pady=7, padx=10)
    b3.resizable(0, 0)

def b4():
    global f1, f2, f3, f4, f5
    global conn, cursor
    conn = sqlite3.connect("dbms.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `Servers` ( `Region` TEXT, `Location` TEXT, `Capacity` TEXT, `Office` TEXT, `Admin` TEXT )")
    conn.commit()
    f1 = StringVar()
    f2 = StringVar()
    f3 = StringVar()
    f4 = StringVar()
    f5 = StringVar()

    def Insert():
        global f1, f2, f3, f4, f5
        global conn, cursor
        f1.get(), f2.get(), f3.get(), f4.get(), f5.get()
        cursor.execute("INSERT INTO `Servers` (Region, Location, Capacity, Office, Admin) VALUES(?,?,?,?,?)",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get())))
        conn.commit()
        msg()

    def View(fetch):
        global conn, cursor
        view = Toplevel()
        Size(1024, 300, view)
        scrollbarx = Scrollbar(view, orient=HORIZONTAL)
        scrollbary = Scrollbar(view, orient=VERTICAL)
        tree = ttk.Treeview(view, columns=("RegionName", "Location", "Capacity", "Office", "Admin"),
                            selectmode='extended', height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('RegionName', text="RegionName", anchor=W), tree.heading('Location', text="Location", anchor=W),
        tree.heading('Capacity', text="Capacity", anchor=W),
        tree.heading('Office', text="Office", anchor=W), tree.heading('Admin', text="Admin", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120),
        tree.column('#2', stretch=NO, minwidth=0, width=200), tree.column('#3', stretch=NO, minwidth=0, width=120),
        tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        cursor.execute("SELECT * FROM Servers")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        tree.pack()

    def Select():
        global conn, cursor
        cursor.execute("SELECT * FROM Servers")
        fetch = cursor.fetchall()
        View(fetch)

    def Count():
        global conn, cursor
        cursor.execute("SELECT COUNT(*) FROM Servers")
        fetch = cursor.fetchall()
        Display(fetch)

    def Distinct():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Servers")
        fetch = cursor.fetchall()
        View(fetch)

    def Update():
        global conn, cursor
        cursor.execute("UPDATE Servers SET Region = ?, Location = ?, Capacity = ?, Office = ?, Admin = ?",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get())))
        conn.commit()
        msg()

    def Order():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Servers ORDER BY Capacity DESC")
        fetch = cursor.fetchall()
        View(fetch)

    def Delete1():
        global conn, cursor, delete
        frame = Toplevel()
        delete = StringVar()
        Label(frame, text="Name :").pack(side=LEFT)
        e = Entry(frame, textvariable=delete)
        e.pack(side=LEFT)
        Button(frame, text="Delete", command=Delete2).pack(side=LEFT)

    def Delete2():
        global conn, cursor, delete
        cursor.execute("DELETE FROM Servers WHERE Admin = ? ", [str(delete.get())])
        conn.commit()


    b4 = Tk()
    b4.title("Servers List")
    b4.config(bg='#99ff99')
    Size(800, 450, b4)
    middle = Frame(b4, bg='#99ff99')
    middle.grid(row=1, column=0, sticky=W + E + S + N, columnspan=2, padx=30)
    lframe = Frame(b4, bg='#99ff99', bd=1, relief=SOLID)
    lframe.grid(row=0, column=0, sticky=W, pady=20, padx=20)
    rframe = Frame(b4, bg='#99ff99', bd=1, relief=SOLID)
    rframe.grid(row=0, column=1, sticky=E, pady=20, padx=20)
    Label(lframe, text="Region", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(lframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(lframe, text="Location", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(lframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(lframe, text="Capacity", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(lframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(lframe, text="Office", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(lframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(lframe, text="Admin", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(lframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(rframe, text="Region", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(rframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(rframe, text="Location", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(rframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(rframe, text="Capacity", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(rframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(rframe, text="Office", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(rframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(rframe, text="Admin", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(rframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Button(lframe, text="Insert Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(rframe, text="Update Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(middle, text="Exit", command=b4.destroy, font=('arial', 13), width=10).grid(row=0, column=0, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="SELECT *", command=Select, font=('arial', 13), width=10).grid(row=0, column=1, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="COUNT *", command=Count, font=('arial', 13), width=10).grid(row=0, column=2, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DISTINCT *", command=Distinct, font=('arial', 13), width=10).grid(row=0, column=3, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="ORDER BY", command=Order, font=('arial', 13), width=10).grid(row=0, column=4, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DELETE", command=Delete1, font=('arial', 13), width=10).grid(row=0, column=5, sticky=W + E + N + S, pady=7, padx=10)
    b4.resizable(0, 0)

def b5():
    global f1, f2, f3, f4, f5, f6
    global conn, cursor
    conn = sqlite3.connect("dbms.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `Users` ( `Region` TEXT, `Office` TEXT, `Users` TEXT, `Servers` TEXT, `Uptime` TEXT, `Downtime` TEXT )")
    conn.commit()
    f1 = StringVar()
    f2 = StringVar()
    f3 = StringVar()
    f4 = StringVar()
    f5 = StringVar()
    f6 = StringVar()

    def Insert():
        global f1, f2, f3, f4, f5
        global conn, cursor
        f1.get(), f2.get(), f3.get(), f4.get(), f5.get()
        cursor.execute("INSERT INTO `Users` (Region, Office, Users, Servers, Uptime, Downtime) VALUES(?,?,?,?,?,?)",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get()), str(f6.get())))
        conn.commit()
        msg()

    def View(fetch):
        global conn, cursor
        view = Toplevel()
        Size(1024, 300, view)
        scrollbarx = Scrollbar(view, orient=HORIZONTAL)
        scrollbary = Scrollbar(view, orient=VERTICAL)
        tree = ttk.Treeview(view, columns=("RegionName", "Office", "Users", "Servers", "Uptime", "Downtime"),
                            selectmode='extended', height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('RegionName', text="RegionName", anchor=W), tree.heading('Office', text="Office", anchor=W),
        tree.heading('Users', text="Users", anchor=W), tree.heading('Servers', text="Servers", anchor=W),
        tree.heading('Uptime', text="Uptime", anchor=W), tree.heading('Downtime', text="Downtime", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120),
        tree.column('#2', stretch=NO, minwidth=0, width=200), tree.column('#3', stretch=NO, minwidth=0, width=120),
        tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        cursor.execute("SELECT * FROM Users")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        tree.pack()


    def Select():
        global conn, cursor
        cursor.execute("SELECT * FROM Users")
        fetch = cursor.fetchall()
        View(fetch)

    def Count():
        global conn, cursor
        cursor.execute("SELECT COUNT(*) FROM Users")
        fetch = cursor.fetchall()
        Display(fetch)

    def Distinct():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Users")
        fetch = cursor.fetchall()
        View(fetch)

    def Update():
        global conn, cursor
        cursor.execute("UPDATE Users SET Region = ?, Office = ?, Users = ?, Servers = ?, Uptime = ?, Downtime = ?",
                       (str(f1.get()), str(f2.get()), str(f3.get()), str(f4.get()), str(f5.get()), str(f6.get())))
        conn.commit()
        msg()

    def Order():
        global conn, cursor
        cursor.execute("SELECT DISTINCT * FROM Users ORDER BY Servers DESC")
        fetch = cursor.fetchall()
        View(fetch)

    def Delete1():
        global conn, cursor, delete
        frame = Toplevel()
        delete = StringVar()
        Label(frame, text="Office :").pack(side=LEFT)
        e = Entry(frame, textvariable=delete)
        e.pack(side=LEFT)
        Button(frame, text="Delete", command=Delete2).pack(side=LEFT)

    def Delete2():
        global conn, cursor, delete
        cursor.execute("DELETE FROM Servers WHERE Admin = ? ", [str(delete.get())])
        conn.commit()

    b5 = Tk()
    b5.title("Users Record")
    b5.config(bg='#99ff99')
    Size(800, 450, b5)
    middle = Frame(b5, bg='#99ff99')
    middle.grid(row=1, column=0, sticky=W + E + S + N, columnspan=2, padx=30)
    lframe = Frame(b5, bg='#99ff99', bd=1, relief=SOLID)
    lframe.grid(row=0, column=0, sticky=W, pady=20, padx=20)
    rframe = Frame(b5, bg='#99ff99', bd=1, relief=SOLID)
    rframe.grid(row=0, column=1, sticky=E, pady=20, padx=20)
    Label(lframe, text="Region", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(lframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(lframe, text="Office", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(lframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(lframe, text="Users", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(lframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(lframe, text="Servers", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(lframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(lframe, text="Uptime", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(lframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(lframe, text="Downtime", bg='#99ff99', font=('arial', 13)).grid(row=6, column=0, sticky=W)
    f6 = Entry(lframe, font=('arial', 13))
    f6.grid(row=6, column=1, padx=10, pady=10)
    Label(rframe, text="Region", bg='#99ff99', font=('arial', 13)).grid(row=1, column=0, sticky=W)
    f1 = Entry(rframe, font=('arial', 13))
    f1.grid(row=1, column=1, padx=10, pady=10)
    Label(rframe, text="Office", bg='#99ff99', font=('arial', 13)).grid(row=2, column=0, sticky=W)
    f2 = Entry(rframe, font=('arial', 13))
    f2.grid(row=2, column=1, padx=10, pady=10)
    Label(rframe, text="Users", bg='#99ff99', font=('arial', 13)).grid(row=3, column=0, sticky=W)
    f3 = Entry(rframe, font=('arial', 13))
    f3.grid(row=3, column=1, padx=10, pady=10)
    Label(rframe, text="Servers", bg='#99ff99', font=('arial', 13)).grid(row=4, column=0, sticky=W)
    f4 = Entry(rframe, font=('arial', 13))
    f4.grid(row=4, column=1, padx=10, pady=10)
    Label(rframe, text="Uptime", bg='#99ff99', font=('arial', 13)).grid(row=5, column=0, sticky=W)
    f5 = Entry(rframe, font=('arial', 13))
    f5.grid(row=5, column=1, padx=10, pady=10)
    Label(rframe, text="Downtime", bg='#99ff99', font=('arial', 13)).grid(row=6, column=0, sticky=W)
    f6 = Entry(rframe, font=('arial', 13))
    f6.grid(row=6, column=1, padx=10, pady=10)
    Button(lframe, text="Insert Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(rframe, text="Update Record", command=Insert, font=('arial', 13), width=15).grid(row=7, column=0, sticky=W + E, columnspan=2, padx=17, pady=14)
    Button(middle, text="Exit", command=b5.destroy, font=('arial', 13), width=10).grid(row=0, column=0, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="SELECT *", command=Select, font=('arial', 13), width=10).grid(row=0, column=1, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="COUNT *", command=Count, font=('arial', 13), width=10).grid(row=0, column=2, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DISTINCT *", command=Distinct, font=('arial', 13), width=10).grid(row=0, column=3, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="ORDER BY", command=Order, font=('arial', 13), width=10).grid(row=0, column=4, sticky=W + E + N + S, pady=7, padx=10)
    Button(middle, text="DELETE", command=Delete1, font=('arial', 13), width=10).grid(row=0, column=5, sticky=W + E + N + S, pady=7, padx=10)
    b5.resizable(0, 0)

def Queries():
    None


root = Tk()
Size(1024, 600, root)
root.title("Database v1.3")
root.config(bg="#0700ad")
l1 = Label(root, text="Database Management", bg="#ffffff", fg="#000000", bd=3, font=('arial',35))
l1.pack(fill='x')
Button(root, text="Developers Record", command=b1, font=('arial', 20), width=19).pack(pady=8)
Button(root, text="Games Record", command=b2, font=('arial', 20), width=19).pack(pady=8)
Button(root, text="HQ Record", command=b3, font=('arial', 20), width=19).pack(pady=8)
Button(root, text="Servers Record", command=b4, font=('arial', 20), width=19).pack(pady=8)
Button(root, text="User Region Record", command=b5, font=('arial', 20), width=19).pack(pady=8)
Button(root, text="Exit", command=root.quit, font=('arial', 20), width=10).pack(side=LEFT, padx=120)
Button(root, text="Queries", command=Queries, font=('arial', 20), width=10).pack(side=RIGHT, padx=120)
root.resizable(0, 0)
root.mainloop()