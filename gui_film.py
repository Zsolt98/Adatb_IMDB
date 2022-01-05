import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_film
import db_rendezo

e_id = None
e_cim = None
e_megjelenes_datum = None
e_jatekido = None
filmekTable = None
cB_film_rendezo = None
cB_film_mufaj = None
filmMufajaiTable = None

def get_film():
    film = db_film.get_film(e_id.get())

    if film is not None:
        (rows, rows2) = film

        for j in filmMufajaiTable.get_children():
            filmMufajaiTable.delete(j)

        i = 0
        for row2 in rows2:
            filmMufajaiTable.insert(parent='', index='end', iid=i, text='', values=(row2[0]))
            i += 1

        for row in rows:
            e_cim.delete(0, 'end')
            e_megjelenes_datum.delete(0, 'end')
            e_jatekido.delete(0, 'end')
            cB_film_rendezo.set('')

            e_cim.insert(0, row[1])
            e_megjelenes_datum.insert(0, row[2])
            e_jatekido.insert(0, row[3])
            cB_film_rendezo.current(row[4] - 1) #combobox nullától indexel

        showTable_film()


def insert_film():
    if db_film.insert_film(e_id.get(), e_cim.get(), e_megjelenes_datum.get(), e_jatekido.get(), cB_film_rendezo.get()):
        e_id.delete(0, 'end')
        e_cim.delete(0, 'end')
        e_megjelenes_datum.delete(0, 'end')
        e_jatekido.delete(0, 'end')
        cB_film_rendezo.delete(0, 'end')
        showTable_film()

def update_film():
    if db_film.update_film(e_id.get(), e_cim.get(), e_megjelenes_datum.get(), e_jatekido.get(), cB_film_rendezo.get()):
        e_id.delete(0, 'end')
        e_cim.delete(0, 'end')
        e_megjelenes_datum.delete(0, 'end')
        e_jatekido.delete(0, 'end')
        cB_film_rendezo.delete(0, 'end')
        showTable_film()

def delete_film():
    if db_film.delete_film(e_id.get()):
        e_id.delete(0, 'end')
        e_cim.delete(0, 'end')
        e_megjelenes_datum.delete(0, 'end')
        e_jatekido.delete(0, 'end')
        cB_film_rendezo.delete(0, 'end')
        showTable_film()

def showTable_film():
    filmek = db_film.get_film_for_table()

    for j in filmekTable.get_children():
        filmekTable.delete(j)

    for i, row in enumerate(filmek):
        rendezoID = row[4]
        filmekTable.insert(parent='', index='end', iid=i, text='', values=(row[0], row[1], row[2], row[3], db_rendezo.NumToStringRendezo(rendezoID)))


def init_gui(filmek_tab, windowWidth):
    global e_id, e_cim,  e_megjelenes_datum, e_jatekido, filmMufajaiTable, cB_film_rendezo, filmekTable, cB_film_mufaj

    top_frame = Frame(filmek_tab, bg='white', width=windowWidth, height=50, pady=3)
    center = Frame(filmek_tab, bg='gray', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(filmek_tab, bg='white', width=windowWidth, height=25, pady=3)

    filmek_tab.grid_rowconfigure(1, weight=1)
    filmek_tab.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")

    get_button = tk.Button(top_frame, text="Lekérdezés", font=('bold', 12), bg="lightblue", command=get_film)
    get_button.grid(row=0, column=0, sticky="w")

    insert_button = tk.Button(top_frame, text="Beszúrás", font=('bold', 12), bg="lightblue", command=insert_film)
    insert_button.grid(row=0, column=1, sticky="w")

    update_button = tk.Button(top_frame, text="Frissítés", font=('bold', 12), bg="lightblue", command=update_film)
    update_button.grid(row=0, column=2, sticky="w")

    delete_button = tk.Button(top_frame, text="Törlés", font=('bold', 12), bg="#e0230d", command=delete_film, fg="white")
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

    cim = tk.Label(ctr_left, text='Cím:', font=('bold', 12))
    cim.grid(row=3, column=0, sticky="w", pady=0, padx=5)

    e_cim = tk.Entry(ctr_left, borderwidth=3, width=30, font=('bold', 12))
    e_cim.grid(row=3, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    megjelenes_datum = tk.Label(ctr_left, text='Megjelenés éve:', font=('bold', 12))
    megjelenes_datum.grid(row=4, column=0, sticky="w", pady=0, padx=5)

    e_megjelenes_datum = tk.Entry(ctr_left, width=30, borderwidth=3, font=('bold', 12))
    e_megjelenes_datum.grid(row=4, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    jatekido = tk.Label(ctr_left, text='Film játékidő:', font=('bold', 12))
    jatekido.grid(row=5, column=0, sticky="w", pady=0, padx=5)

    e_jatekido = tk.Entry(ctr_left, width=30, borderwidth=3, font=('bold', 12))
    e_jatekido.grid(row=5, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    rendezo = tk.Label(ctr_left, text='Rendező:', font=('bold', 12))
    rendezo.grid(row=6, column=0, sticky="w", pady=0, padx=5)

    cB_film_rendezo = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_rendezo.get_rendezofromDB()])
    cB_film_rendezo.grid(row=6, column=1, pady=0, padx=5, ipadx=3, ipady=3)


    mufaj = tk.Label(ctr_left, text='Film műfaja:', font=('bold', 12))
    mufaj.grid(row=7, column=0, sticky="wn", pady=0, padx=5, ipady=0)

    filmMufajai_frame = Frame(ctr_left)
    filmMufajai_frame.grid(row=7, column=1, sticky="ws", pady=3, padx=5)



    filmMufajaiTable_scrolly = Scrollbar(filmMufajai_frame)
    filmMufajaiTable_scrolly.pack(side=RIGHT, fill=Y)

    filmMufajaiTable_scrollx = Scrollbar(filmMufajai_frame, orient='horizontal')
    filmMufajaiTable_scrollx.pack(side=BOTTOM, fill=X)

    filmMufajaiTable = ttk.Treeview(filmMufajai_frame, yscrollcommand=filmMufajaiTable_scrolly.set, xscrollcommand=filmMufajaiTable_scrollx.set)

    filmMufajaiTable_scrolly.config(command=filmMufajaiTable.yview)
    filmMufajaiTable_scrollx.config(command=filmMufajaiTable.xview)

    filmMufajaiTable['columns'] = ('sz_f')

    filmMufajaiTable.column("#0", width=0, stretch=NO)
    filmMufajaiTable.column("sz_f", anchor=CENTER, width=150)

    filmMufajaiTable.heading("#0", text="X", anchor=CENTER)
    filmMufajaiTable.heading("sz_f", text="Film Műfaja/Műfajai", anchor=CENTER)

    filmMufajaiTable.pack()

    listBoxLabel = tk.Label(ctr_right, text='Filmek', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    szineszekTable_scrolly = Scrollbar(szineszekTable_frame)
    szineszekTable_scrolly.pack(side=RIGHT, fill=Y)

    szineszekTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    szineszekTable_scrollx.pack(side=BOTTOM, fill=X)

    filmekTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=szineszekTable_scrolly.set, xscrollcommand=szineszekTable_scrollx.set, height=20)

    szineszekTable_scrolly.config(command=filmekTable.yview)
    szineszekTable_scrollx.config(command=filmekTable.xview)

    filmekTable['columns'] = ('f_id', 'f_title', 'f_meg', 'f_ido', 'f_rendezo')

    filmekTable.column("#0", width=0, stretch=NO)
    filmekTable.column("f_id", anchor=CENTER, width=65)
    filmekTable.column("f_title", anchor=CENTER, width=150)
    filmekTable.column("f_meg", anchor=CENTER, width=70)
    filmekTable.column("f_ido", anchor=CENTER, width=55)
    filmekTable.column("f_rendezo", anchor=CENTER, width=110)

    filmekTable.heading("#0", text="X", anchor=CENTER)
    filmekTable.heading("f_id", text="Azonosító", anchor=CENTER)
    filmekTable.heading("f_title", text="Cím", anchor=CENTER)
    filmekTable.heading("f_meg", text="Megjelenés", anchor=CENTER)
    filmekTable.heading("f_ido", text="Játékidő", anchor=CENTER)
    filmekTable.heading("f_rendezo", text="Rendező", anchor=CENTER)

    filmekTable.pack()

    showTable_film()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")