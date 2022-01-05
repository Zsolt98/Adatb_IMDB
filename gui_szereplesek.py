import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_szereplesek, db_szinesz, db_film


e_id = None
e_Szereples_szerep = None
e_Szereples_Szinesz_id = None
e_Szereples_Film_id = None
szereplesekTable = None

def get_szereplesek():
    szerep = db_szereplesek.get_szereplesek(e_id.get())

    if szerep is not None:
        rows = szerep

        for j in szereplesekTable.get_children():
            szereplesekTable.delete(j)


        for row in rows:
            e_Szereples_szerep.delete(0, 'end')
            e_Szereples_Szinesz_id.delete(0, 'end')
            e_Szereples_Film_id.delete(0, 'end')

            e_Szereples_szerep.insert(0, row[1])
            e_Szereples_Szinesz_id.current(row[2] - 1)
            e_Szereples_Film_id.current(row[3] - 1)

        showTable_szereplesek()


def insert_szereplesek():
    if db_szereplesek.insert_szereplesek(e_id.get(), e_Szereples_szerep.get(), e_Szereples_Szinesz_id.get(), e_Szereples_Film_id.get()):
        e_id.delete(0, 'end')
        e_Szereples_szerep.delete(0, 'end')
        e_Szereples_Szinesz_id.delete(0, 'end')
        e_Szereples_Film_id.delete(0, 'end')
        showTable_szereplesek()

def update_szereplesek():
    if db_szereplesek.update_szereplesek(e_id.get(), e_Szereples_szerep.get(), e_Szereples_Szinesz_id.get(), e_Szereples_Film_id.get()):
        e_id.delete(0, 'end')
        e_Szereples_szerep.delete(0, 'end')
        e_Szereples_Szinesz_id.delete(0, 'end')
        e_Szereples_Film_id.delete(0, 'end')
        showTable_szereplesek()

def delete_szereplesek():
    if db_szereplesek.delete_szereplesek(e_id.get()):
        e_id.delete(0, 'end')
        e_Szereples_szerep.delete(0, 'end')
        e_Szereples_Szinesz_id.delete(0, 'end')
        e_Szereples_Film_id.delete(0, 'end')
        showTable_szereplesek()

def showTable_szereplesek():
    mufajok = db_szereplesek.get_szereplesek_for_table()

    for j in szereplesekTable.get_children():
        szereplesekTable.delete(j)

    for i, row in enumerate(mufajok):
        szereplesekTable.insert(parent='', index='end', iid=i, text='', values=(row[0], row[1], db_szinesz.NumToStringSzinesz(row[2]), db_film.NumToStringFilmek(row[3])))


def init_gui(tab, windowWidth):
    global e_id, e_Szereples_szerep, szereplesekTable, e_Szereples_Szinesz_id, e_Szereples_Film_id


    top_frame = Frame(tab, bg='white', width=windowWidth, height=50, pady=3)
    center = Frame(tab, bg='gray', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(tab, bg='white', width=windowWidth, height=25, pady=3)

    tab.grid_rowconfigure(1, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")

    get_button = tk.Button(top_frame, text="Lekérdezés", font=('bold', 12), bg="lightblue", command=get_szereplesek)
    get_button.grid(row=0, column=0, sticky="w")

    insert_button = tk.Button(top_frame, text="Beszúrás", font=('bold', 12), bg="lightblue", command=insert_szereplesek)
    insert_button.grid(row=0, column=1, sticky="w")

    update_button = tk.Button(top_frame, text="Frissítés", font=('bold', 12), bg="lightblue", command=update_szereplesek)
    update_button.grid(row=0, column=2, sticky="w")

    delete_button = tk.Button(top_frame, text="Törlés", font=('bold', 12), bg="#e0230d", command=delete_szereplesek, fg="white")
    delete_button.grid(row=0, column=3, sticky="w")

    # center
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, width=100)
    ctr_mid = Frame(center, width=20, padx=3, pady=3)
    ctr_right = Frame(center, width=100, padx=3, pady=3)

    inputsLabel = tk.Label(ctr_left, text='Adatok bevitele', font=('bold', 14), pady=3)
    inputsLabel.grid(row=1, column=0, columnspan=2)

    id = tk.Label(ctr_left, text='Azonosító:', font=('bold', 12))
    id.grid(row=2, column=0, sticky="w", pady=0, padx=5)

    e_id = tk.Entry(ctr_left, borderwidth=3, width=30, font=('bold', 12))
    e_id.grid(row=2, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    szerep = tk.Label(ctr_left, text='Szerep:', font=('bold', 12))
    szerep.grid(row=3, column=0, sticky="w", pady=0, padx=5)

    e_Szereples_szerep = tk.Entry(ctr_left, borderwidth=3, width=30, font=('bold', 12))
    e_Szereples_szerep.grid(row=3, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    sz_id = tk.Label(ctr_left, text='Színész:', font=('bold', 12))
    sz_id.grid(row=4, column=0, sticky="w", pady=0, padx=5)

    e_Szereples_Szinesz_id = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_szinesz.get_szineszekfromDB()])
    e_Szereples_Szinesz_id.grid(row=4, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    f_sz = tk.Label(ctr_left, text='Film:', font=('bold', 12))
    f_sz.grid(row=5, column=0, sticky="w", pady=0, padx=5)

    e_Szereples_Film_id = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_film.get_filmekfromDB()])
    e_Szereples_Film_id.grid(row=5, column=1, pady=0, padx=5, ipadx=3, ipady=3)




    listBoxLabel = tk.Label(ctr_right, text='Szereplések', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    mufajokTable_scrolly = Scrollbar(szineszekTable_frame)
    mufajokTable_scrolly.pack(side=RIGHT, fill=Y)

    mufajokTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    mufajokTable_scrollx.pack(side=BOTTOM, fill=X)

    szereplesekTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=mufajokTable_scrolly.set, xscrollcommand=mufajokTable_scrollx.set, height=20)

    mufajokTable_scrolly.config(command=szereplesekTable.yview)
    mufajokTable_scrollx.config(command=szereplesekTable.xview)

    szereplesekTable['columns'] = ('id', 'szerep', 'sz_id', 'f_id')

    szereplesekTable.column("#0", width=0, stretch=NO)
    szereplesekTable.column("id", anchor=CENTER, width=65)
    szereplesekTable.column("szerep", anchor=CENTER, width=150)
    szereplesekTable.column("sz_id", anchor=CENTER, width=150)
    szereplesekTable.column("f_id", anchor=CENTER, width=150)


    szereplesekTable.heading("#0", text="X", anchor=CENTER)
    szereplesekTable.heading("id", text="Azonosító", anchor=CENTER)
    szereplesekTable.heading("szerep", text="Szerep", anchor=CENTER)
    szereplesekTable.heading("sz_id", text="Színész", anchor=CENTER)
    szereplesekTable.heading("f_id", text="Film", anchor=CENTER)


    szereplesekTable.pack()

    showTable_szereplesek()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")