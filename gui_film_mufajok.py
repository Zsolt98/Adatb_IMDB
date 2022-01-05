import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_film, db_mufajok, db_film_mufajok


e_id = None
e_Film_id = None
e_Mufaj_id = None
film_mufajokTable = None

def get():
    film_mufaj = db_film_mufajok.get_fm(e_id.get())

    if film_mufaj is not None:
        rows = film_mufaj

        for j in film_mufajokTable.get_children():
            film_mufajokTable.delete(j)


        for row in rows:
            e_Film_id.delete(0, 'end')
            e_Mufaj_id.delete(0, 'end')

            e_Film_id.current(row[1] - 1)
            e_Mufaj_id.current(row[2] - 1)

        showTable_film_mufajok()


def insert():
    if db_film_mufajok.insert_fm(e_id.get(), e_Film_id.get(), e_Mufaj_id.get()):
        e_id.delete(0, 'end')
        e_Film_id.delete(0, 'end')
        e_Mufaj_id.delete(0, 'end')
        showTable_film_mufajok()

def update():
    if db_film_mufajok.update_fm(e_id.get(), e_Film_id.get(), e_Mufaj_id.get()):
        e_id.delete(0, 'end')
        e_Film_id.delete(0, 'end')
        e_Mufaj_id.delete(0, 'end')
        showTable_film_mufajok()

def delete():
    if db_film_mufajok.delete_fm(e_id.get()):
        e_id.delete(0, 'end')
        e_Film_id.delete(0, 'end')
        e_Mufaj_id.delete(0, 'end')
        showTable_film_mufajok()

def showTable_film_mufajok():
    film_mufajok = db_film_mufajok.get_fm_for_table()

    for j in film_mufajokTable.get_children():
        film_mufajokTable.delete(j)

    for i, row in enumerate(film_mufajok):
        film_mufajokTable.insert(parent='', index='end', iid=i, text='', values=(row[0], db_film.NumToStringFilmek(row[1]), db_mufajok.NumToStringMufaj(row[2])))


def init_gui(tab, windowWidth):
    global e_id, film_mufajokTable, e_Film_id, e_Mufaj_id


    top_frame = Frame(tab, bg='white', width=windowWidth, height=50, pady=3)
    center = Frame(tab, bg='gray', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(tab, bg='white', width=windowWidth, height=25, pady=3)

    tab.grid_rowconfigure(1, weight=1)
    tab.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")

    get_button = tk.Button(top_frame, text="Lekérdezés", font=('bold', 12), bg="lightblue", command=get)
    get_button.grid(row=0, column=0, sticky="w")

    insert_button = tk.Button(top_frame, text="Beszúrás", font=('bold', 12), bg="lightblue", command=insert)
    insert_button.grid(row=0, column=1, sticky="w")

    update_button = tk.Button(top_frame, text="Frissítés", font=('bold', 12), bg="lightblue", command=update)
    update_button.grid(row=0, column=2, sticky="w")

    delete_button = tk.Button(top_frame, text="Törlés", font=('bold', 12), bg="#e0230d", command=delete, fg="white")
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


    sz_id = tk.Label(ctr_left, text='Film:', font=('bold', 12))
    sz_id.grid(row=4, column=0, sticky="w", pady=0, padx=5)

    e_Film_id = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_film.get_filmekfromDB()])
    e_Film_id.grid(row=4, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    f_sz = tk.Label(ctr_left, text='Műfaja:', font=('bold', 12))
    f_sz.grid(row=5, column=0, sticky="w", pady=0, padx=5)

    e_Mufaj_id = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_mufajok.get_mufajokfromDB()])
    e_Mufaj_id.grid(row=5, column=1, pady=0, padx=5, ipadx=3, ipady=3)




    listBoxLabel = tk.Label(ctr_right, text='Filmek műfajai', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    mufajokTable_scrolly = Scrollbar(szineszekTable_frame)
    mufajokTable_scrolly.pack(side=RIGHT, fill=Y)

    mufajokTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    mufajokTable_scrollx.pack(side=BOTTOM, fill=X)

    film_mufajokTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=mufajokTable_scrolly.set, xscrollcommand=mufajokTable_scrollx.set, height=20)

    mufajokTable_scrolly.config(command=film_mufajokTable.yview)
    mufajokTable_scrollx.config(command=film_mufajokTable.xview)

    film_mufajokTable['columns'] = ('id', 'film', 'mufaj')

    film_mufajokTable.column("#0", width=0, stretch=NO)
    film_mufajokTable.column("id", anchor=CENTER, width=65)
    film_mufajokTable.column("film", anchor=CENTER, width=150)
    film_mufajokTable.column("mufaj", anchor=CENTER, width=150)


    film_mufajokTable.heading("#0", text="X", anchor=CENTER)
    film_mufajokTable.heading("id", text="Azonosító", anchor=CENTER)
    film_mufajokTable.heading("film", text="Film címe", anchor=CENTER)
    film_mufajokTable.heading("mufaj", text="Film műfaja", anchor=CENTER)


    film_mufajokTable.pack()

    showTable_film_mufajok()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")