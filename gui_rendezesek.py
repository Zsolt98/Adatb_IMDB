import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_film, db_rendezo, db_rendezesek


e_id = None
e_Rendezo_id = None
e_Film_id = None
rendezesekTable = None

def get():
    rendezes = db_rendezesek.get_rendezesek(e_id.get())

    if rendezes is not None:
        rows = rendezes

        for j in rendezesekTable.get_children():
            rendezesekTable.delete(j)


        for row in rows:
            e_Rendezo_id.delete(0, 'end')
            e_Film_id.delete(0, 'end')

            e_Rendezo_id.current(row[1] - 1)
            e_Film_id.current(row[2] - 1)

        showTable_rendezesek()


def insert():
    if db_rendezesek.insert_rendezesek(e_id.get(), e_Rendezo_id.get(), e_Film_id.get()):
        e_id.delete(0, 'end')
        e_Rendezo_id.delete(0, 'end')
        e_Film_id.delete(0, 'end')
        showTable_rendezesek()

def update():
    if db_rendezesek.update_rendezesek(e_id.get(), e_Rendezo_id.get(), e_Film_id.get()):
        e_id.delete(0, 'end')
        e_Rendezo_id.delete(0, 'end')
        e_Film_id.delete(0, 'end')
        showTable_rendezesek()

def delete():
    if db_rendezesek.delete_rendezesek(e_id.get()):
        e_id.delete(0, 'end')
        e_Rendezo_id.delete(0, 'end')
        e_Film_id.delete(0, 'end')
        showTable_rendezesek()

def showTable_rendezesek():
    rendezesek = db_rendezesek.get_rendezesek_for_table()

    for j in rendezesekTable.get_children():
        rendezesekTable.delete(j)

    for i, row in enumerate(rendezesek):
        rendezesekTable.insert(parent='', index='end', iid=i, text='', values=(row[0], db_rendezo.NumToStringRendezo(row[1]), db_film.NumToStringFilmek(row[2])))


def init_gui(tab, windowWidth):
    global e_id, rendezesekTable, e_Rendezo_id, e_Film_id


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


    sz_id = tk.Label(ctr_left, text='Rendező:', font=('bold', 12))
    sz_id.grid(row=3, column=0, sticky="w", pady=0, padx=5)

    e_Rendezo_id = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_rendezo.get_rendezofromDB()])
    e_Rendezo_id.grid(row=3, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    f_sz = tk.Label(ctr_left, text='Film:', font=('bold', 12))
    f_sz.grid(row=4, column=0, sticky="w", pady=0, padx=5)

    e_Film_id = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_film.get_filmekfromDB()])
    e_Film_id.grid(row=4, column=1, pady=0, padx=5, ipadx=3, ipady=3)




    listBoxLabel = tk.Label(ctr_right, text='Rendezések', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    mufajokTable_scrolly = Scrollbar(szineszekTable_frame)
    mufajokTable_scrolly.pack(side=RIGHT, fill=Y)

    mufajokTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    mufajokTable_scrollx.pack(side=BOTTOM, fill=X)

    rendezesekTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=mufajokTable_scrolly.set, xscrollcommand=mufajokTable_scrollx.set, height=20)

    mufajokTable_scrolly.config(command=rendezesekTable.yview)
    mufajokTable_scrollx.config(command=rendezesekTable.xview)

    rendezesekTable['columns'] = ('id', 'rendezo', 'film')

    rendezesekTable.column("#0", width=0, stretch=NO)
    rendezesekTable.column("id", anchor=CENTER, width=65)
    rendezesekTable.column("rendezo", anchor=CENTER, width=150)
    rendezesekTable.column("film", anchor=CENTER, width=150)


    rendezesekTable.heading("#0", text="X", anchor=CENTER)
    rendezesekTable.heading("id", text="Azonosító", anchor=CENTER)
    rendezesekTable.heading("rendezo", text="Rendező", anchor=CENTER)
    rendezesekTable.heading("film", text="Film címe", anchor=CENTER)


    rendezesekTable.pack()

    showTable_rendezesek()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")