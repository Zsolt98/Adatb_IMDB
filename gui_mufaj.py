import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_mufajok


e_id = None
e_mufajnev = None
mufajokTable = None

def get_mufaj():
    mufaj = db_mufajok.get_mufaj(e_id.get())

    if mufaj is not None:
        rows = mufaj

        for j in mufajokTable.get_children():
            mufajokTable.delete(j)


        for row in rows:
            e_mufajnev.delete(0, 'end')
            e_mufajnev.insert(0, row[1])

        showTable_mufaj()


def insert_mufaj():
    if db_mufajok.insert_mufaj(e_id.get(), e_mufajnev.get()):
        e_id.delete(0, 'end')
        e_mufajnev.delete(0, 'end')
        showTable_mufaj()

def update_mufaj():
    if db_mufajok.update_mufaj(e_id.get(), e_mufajnev.get()):
        e_id.delete(0, 'end')
        e_mufajnev.delete(0, 'end')
        showTable_mufaj()

def delete_mufaj():
    if db_mufajok.delete_mufaj(e_id.get()):
        e_id.delete(0, 'end')
        e_mufajnev.delete(0, 'end')
        showTable_mufaj()

def showTable_mufaj():
    mufajok = db_mufajok.get_mufaj_for_table()

    for j in mufajokTable.get_children():
        mufajokTable.delete(j)

    for i, row in enumerate(mufajok):
        mufajokTable.insert(parent='', index='end', iid=i, text='', values=(row[0], row[1]))


def init_gui(mufajok_tab, windowWidth):
    global e_id, e_mufajnev, mufajokTable

    top_frame = Frame(mufajok_tab, bg='white', width=windowWidth, height=50, pady=3)
    center = Frame(mufajok_tab, bg='gray', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(mufajok_tab, bg='white', width=windowWidth, height=25, pady=3)

    mufajok_tab.grid_rowconfigure(1, weight=1)
    mufajok_tab.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")

    get_button = tk.Button(top_frame, text="Lekérdezés", font=('bold', 12), bg="lightblue", command=get_mufaj)
    get_button.grid(row=0, column=0, sticky="w")

    insert_button = tk.Button(top_frame, text="Beszúrás", font=('bold', 12), bg="lightblue", command=insert_mufaj)
    insert_button.grid(row=0, column=1, sticky="w")

    update_button = tk.Button(top_frame, text="Frissítés", font=('bold', 12), bg="lightblue", command=update_mufaj)
    update_button.grid(row=0, column=2, sticky="w")

    delete_button = tk.Button(top_frame, text="Törlés", font=('bold', 12), bg="#e0230d", command=delete_mufaj, fg="white")
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

    cim = tk.Label(ctr_left, text='Műfaj neve:', font=('bold', 12))
    cim.grid(row=3, column=0, sticky="w", pady=0, padx=5)

    e_mufajnev = tk.Entry(ctr_left, borderwidth=3, width=30, font=('bold', 12))
    e_mufajnev.grid(row=3, column=1, pady=0, padx=5, ipadx=3, ipady=3)



    filmMufajai_frame = Frame(ctr_left)
    filmMufajai_frame.grid(row=7, column=1, sticky="ws", pady=3, padx=5)

    #cB_film_mufaj = ttk.Combobox(ctr_left, width=28, font=('bold', 12), values=db_mufajok.get_mufajokfromDB())
    #cB_film_mufaj.grid(row=7, column=1, pady=0, padx=5, ipadx=3, ipady=3)




    listBoxLabel = tk.Label(ctr_right, text='Műfajok', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    mufajokTable_scrolly = Scrollbar(szineszekTable_frame)
    mufajokTable_scrolly.pack(side=RIGHT, fill=Y)

    mufajokTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    mufajokTable_scrollx.pack(side=BOTTOM, fill=X)

    mufajokTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=mufajokTable_scrolly.set, xscrollcommand=mufajokTable_scrollx.set, height=20)

    mufajokTable_scrolly.config(command=mufajokTable.yview)
    mufajokTable_scrollx.config(command=mufajokTable.xview)

    mufajokTable['columns'] = ('f_id', 'f_title')

    mufajokTable.column("#0", width=0, stretch=NO)
    mufajokTable.column("f_id", anchor=CENTER, width=65)
    mufajokTable.column("f_title", anchor=CENTER, width=150)


    mufajokTable.heading("#0", text="X", anchor=CENTER)
    mufajokTable.heading("f_id", text="Azonosító", anchor=CENTER)
    mufajokTable.heading("f_title", text="Műfaj neve", anchor=CENTER)


    mufajokTable.pack()

    showTable_mufaj()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")