import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_nemzetek
import db_rendezo

e_id = None
e_name = None
rendezesekTable = None
rendezettFilmekTable = None
cB_szinesz_nemzetiseg = None

def get():
    rendezo = db_rendezo.get_rendezo(e_id.get())

    if rendezo is not None:
        (rows, rows2) = rendezo

        for j in rendezettFilmekTable.get_children():
            rendezettFilmekTable.delete(j)

        i = 0
        for row2 in rows2:
            rendezettFilmekTable.insert(parent='', index='end', iid=i, text='', values=(row2[0], row2[1]))
            i += 1

        for row in rows:
            e_name.delete(0, 'end')
            cB_szinesz_nemzetiseg.delete(0, 'end')
            e_name.insert(0, row[1])
            cB_szinesz_nemzetiseg.current(row[2]-1) #combobox nullától indexel

        showTable_rendezok()

def insert():
    if db_rendezo.insert_rendezo(e_id.get(), e_name.get(), cB_szinesz_nemzetiseg.get()):
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        cB_szinesz_nemzetiseg.delete(0, 'end')
        showTable_rendezok()

def update():
    if db_rendezo.update_rendezo(e_id.get(), e_name.get(), cB_szinesz_nemzetiseg.get()):
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        cB_szinesz_nemzetiseg.delete(0, 'end')
        showTable_rendezok()

def delete():
    if db_rendezo.delete_rendezo(e_id.get()):
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        cB_szinesz_nemzetiseg.delete(0, 'end')
        showTable_rendezok()

def showTable_rendezok():
    rendezok = db_rendezo.get_rendezo_for_table()

    for j in rendezesekTable.get_children():
        rendezesekTable.delete(j)

    for i, row in enumerate(rendezok):
        rendezesekTable.insert(parent='', index='end', iid=i, text='', values=(row[0], row[1], db_nemzetek.NumToStringnemzetiseg(row[2])))


def init_gui(tab, windowWidth):
    global e_id, e_name, rendezesekTable, cB_szinesz_nemzetiseg, rendezettFilmekTable

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

    name = tk.Label(ctr_left, text='Név:', font=('bold', 12))
    name.grid(row=3, column=0, sticky="w", pady=0, padx=5)

    e_name = tk.Entry(ctr_left, borderwidth=3, width=30, font=('bold', 12))
    e_name.grid(row=3, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    nemzetiseg = tk.Label(ctr_left, text='Nemzetiség:', font=('bold', 12))
    nemzetiseg.grid(row=4, column=0, sticky="w", pady=0, padx=5)

    cB_szinesz_nemzetiseg = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_nemzetek.get_nemzetekfromDB()])
    cB_szinesz_nemzetiseg.grid(row=4, column=1, pady=0, padx=5, ipadx=3, ipady=3)


    rendezes = tk.Label(ctr_left, text='Rendezett filmek:', font=('bold', 12))
    rendezes.grid(row=5, column=0, sticky="wn", pady=0, padx=5, ipady=0)

    rendezettFilmekTable_frame = Frame(ctr_left)
    rendezettFilmekTable_frame.grid(row=5, column=1, sticky="ws", pady=3, padx=5)

    rendezettFilmekTable_scrolly = Scrollbar(rendezettFilmekTable_frame)
    rendezettFilmekTable_scrolly.pack(side=RIGHT, fill=Y)

    rendezettFilmekTable_scrollx = Scrollbar(rendezettFilmekTable_frame, orient='horizontal')
    rendezettFilmekTable_scrollx.pack(side=BOTTOM, fill=X)

    rendezettFilmekTable = ttk.Treeview(rendezettFilmekTable_frame, yscrollcommand=rendezettFilmekTable_scrolly.set, xscrollcommand=rendezettFilmekTable_scrollx.set)

    rendezettFilmekTable_scrolly.config(command=rendezettFilmekTable.yview)
    rendezettFilmekTable_scrollx.config(command=rendezettFilmekTable.xview)

    rendezettFilmekTable['columns'] = ('sz_f', 'sz_sz')

    rendezettFilmekTable.column("#0", width=0, stretch=NO)
    rendezettFilmekTable.column("sz_f", anchor=CENTER, width=130)
    rendezettFilmekTable.column("sz_sz", anchor=CENTER, width=130)

    rendezettFilmekTable.heading("#0", text="X", anchor=CENTER)
    rendezettFilmekTable.heading("sz_f", text="Film", anchor=CENTER)
    rendezettFilmekTable.heading("sz_sz", text="Megjelenés éve", anchor=CENTER)

    rendezettFilmekTable.pack()


    listBoxLabel = tk.Label(ctr_right, text='Rendezők', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    szineszekTable_scrolly = Scrollbar(szineszekTable_frame)
    szineszekTable_scrolly.pack(side=RIGHT, fill=Y)

    szineszekTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    szineszekTable_scrollx.pack(side=BOTTOM, fill=X)

    rendezesekTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=szineszekTable_scrolly.set, xscrollcommand=szineszekTable_scrollx.set, height=20)

    szineszekTable_scrolly.config(command=rendezesekTable.yview)
    szineszekTable_scrollx.config(command=rendezesekTable.xview)

    rendezesekTable['columns'] = ('sz_id', 'sz_name', 'sz_nemzetiseg')

    rendezesekTable.column("#0", width=0, stretch=NO)
    rendezesekTable.column("sz_id", anchor=CENTER, width=65)
    rendezesekTable.column("sz_name", anchor=CENTER, width=150)
    rendezesekTable.column("sz_nemzetiseg", anchor=CENTER, width=90)

    rendezesekTable.heading("#0", text="X", anchor=CENTER)
    rendezesekTable.heading("sz_id", text="Azonosító", anchor=CENTER)
    rendezesekTable.heading("sz_name", text="Rendező", anchor=CENTER)
    rendezesekTable.heading("sz_nemzetiseg", text="Nemzetiség", anchor=CENTER)

    rendezesekTable.pack()

    showTable_rendezok()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")