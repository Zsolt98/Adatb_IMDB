import tkinter as tk
from tkinter import *
from tkinter import ttk
import db_szinesz
import db_nemzetek

e_id = None
e_name = None
e_szul_datum = None
e_neme = None
ferfi = None
no = None
szineszekTable = None
szineszSzereplesekTable = None
cB_szinesz_nemzetiseg = None

def get_szinesz():
    szineszunk = db_szinesz.get_szinesz(e_id.get())

    if szineszunk is not None:
        (rows, rows2) = szineszunk

        for j in szineszSzereplesekTable.get_children():
            szineszSzereplesekTable.delete(j)

        i = 0
        for row2 in rows2:
            szineszSzereplesekTable.insert(parent='', index='end', iid=i, text='', values=(row2[0], row2[1]))
            i += 1

        for row in rows:
            e_name.delete(0, 'end')
            ferfi.deselect()
            no.deselect()
            e_szul_datum.delete(0, 'end')
            cB_szinesz_nemzetiseg.delete(0, 'end')

            e_name.insert(0, row[1])
            if row[2] == 0:
                ferfi.select()
            else:
                no.select()
            e_szul_datum.insert(0, row[3])
            cB_szinesz_nemzetiseg.current(row[4]-1) #combobox nullától indexel

        showTable_szinesz()

def insert_szinesz():
    if db_szinesz.insert_szinesz(e_id.get(), e_name.get(), e_neme.get(), e_szul_datum.get(), cB_szinesz_nemzetiseg.get()):
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_szul_datum.delete(0, 'end')
        cB_szinesz_nemzetiseg.delete(0, 'end')
        showTable_szinesz()

def update_szinesz():
    if db_szinesz.update_szinesz(e_id.get(), e_name.get(), e_neme.get(), e_szul_datum.get(), cB_szinesz_nemzetiseg.get()):
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        ferfi.deselect()
        no.deselect()
        e_szul_datum.delete(0, 'end')
        cB_szinesz_nemzetiseg.delete(0, 'end')
        showTable_szinesz()

def delete_szinesz():
    if db_szinesz.delete_szinesz(e_id.get()):
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        ferfi.deselect()
        no.deselect()
        e_szul_datum.delete(0, 'end')
        cB_szinesz_nemzetiseg.delete(0, 'end')
        showTable_szinesz()

def showTable_szinesz():
    szineszek = db_szinesz.get_szineszek_for_table()

    for j in szineszekTable.get_children():
        szineszekTable.delete(j)

    for i, row in enumerate(szineszek):
        nemzetID = row[4]
        szineszekTable.insert(parent='', index='end', iid=i, text='', values=(row[0], row[1], "Férfi" if row[2] == 0 else "Nő", row[3], db_nemzetek.NumToStringnemzetiseg(nemzetID)))


def init_gui(szineszek_tab, windowWidth):
    global e_id, e_name, e_neme, e_szul_datum, ferfi, no, szineszSzereplesekTable, cB_szinesz_nemzetiseg, szineszekTable

    top_frame = Frame(szineszek_tab, bg='white', width=windowWidth, height=50, pady=3)
    center = Frame(szineszek_tab, bg='gray', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(szineszek_tab, bg='white', width=windowWidth, height=25, pady=3)

    szineszek_tab.grid_rowconfigure(1, weight=1)
    szineszek_tab.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=3, sticky="ew")

    get_button = tk.Button(top_frame, text="Lekérdezés", font=('bold', 12), bg="lightblue", command=get_szinesz)
    get_button.grid(row=0, column=0, sticky="w")

    insert_button = tk.Button(top_frame, text="Beszúrás", font=('bold', 12), bg="lightblue", command=insert_szinesz)
    insert_button.grid(row=0, column=1, sticky="w")

    update_button = tk.Button(top_frame, text="Frissítés", font=('bold', 12), bg="lightblue", command=update_szinesz)
    update_button.grid(row=0, column=2, sticky="w")

    delete_button = tk.Button(top_frame, text="Törlés", font=('bold', 12), bg="#e0230d", command=delete_szinesz, fg="white")
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

    neme = tk.Label(ctr_left, text='Nemi identitás:', font=('bold', 12))
    neme.grid(row=4, column=0, sticky="w", pady=0, padx=5)

    e_neme = tk.IntVar()
    ferfi = tk.Radiobutton(ctr_left, text="Férfi", padx=20, variable=e_neme, value=0, font=('bold', 12))
    no = tk.Radiobutton(ctr_left, text="Nő", padx=20, variable=e_neme, value=1, font=('bold', 12))

    ferfi.grid(row=4, column=1, pady=0, padx=0, sticky="w")
    no.grid(row=4, column=1, pady=0, padx=0, sticky="e")

    szul_datum = tk.Label(ctr_left, text='Születési dátum:', font=('bold', 12))
    szul_datum.grid(row=5, column=0, sticky="w", pady=0, padx=5)

    e_szul_datum = tk.Entry(ctr_left, width=30, borderwidth=3, font=('bold', 12))
    e_szul_datum.grid(row=5, column=1, pady=0, padx=5, ipadx=3, ipady=3)


    szinesz_nemzetiseg = tk.Label(ctr_left, text='Nemzetiség:', font=('bold', 12))
    szinesz_nemzetiseg.grid(row=6, column=0, sticky="w", pady=0, padx=5)

    cB_szinesz_nemzetiseg = ttk.Combobox(ctr_left, state="readonly", width=28, font=('bold', 12), values=[k[0] for k in db_nemzetek.get_nemzetekfromDB()])
    cB_szinesz_nemzetiseg.grid(row=6, column=1, pady=0, padx=5, ipadx=3, ipady=3)

    szereples = tk.Label(ctr_left, text='Szereplések:', font=('bold', 12))
    szereples.grid(row=7, column=0, sticky="wn", pady=0, padx=5, ipady=0)



    szineszSzereplesekTable_frame = Frame(ctr_left)
    szineszSzereplesekTable_frame.grid(row=7, column=1, sticky="ws", pady=3, padx=5)

    szineszSzereplesekTable_scrolly = Scrollbar(szineszSzereplesekTable_frame)
    szineszSzereplesekTable_scrolly.pack(side=RIGHT, fill=Y)

    szineszSzereplesekTable_scrollx = Scrollbar(szineszSzereplesekTable_frame, orient='horizontal')
    szineszSzereplesekTable_scrollx.pack(side=BOTTOM, fill=X)

    szineszSzereplesekTable = ttk.Treeview(szineszSzereplesekTable_frame, yscrollcommand=szineszSzereplesekTable_scrolly.set, xscrollcommand=szineszSzereplesekTable_scrollx.set)

    szineszSzereplesekTable_scrolly.config(command=szineszSzereplesekTable.yview)
    szineszSzereplesekTable_scrollx.config(command=szineszSzereplesekTable.xview)

    szineszSzereplesekTable['columns'] = ('sz_f', 'sz_sz')

    szineszSzereplesekTable.column("#0", width=0, stretch=NO)
    szineszSzereplesekTable.column("sz_f", anchor=CENTER, width=130)
    szineszSzereplesekTable.column("sz_sz", anchor=CENTER, width=130)

    szineszSzereplesekTable.heading("#0", text="X", anchor=CENTER)
    szineszSzereplesekTable.heading("sz_f", text="Film", anchor=CENTER)
    szineszSzereplesekTable.heading("sz_sz", text="Szerep", anchor=CENTER)

    szineszSzereplesekTable.pack()

    listBoxLabel = tk.Label(ctr_right, text='Színészek', font=('bold', 14), pady=3)
    listBoxLabel.grid(row=0, column=0)

    szineszekTable_frame = Frame(ctr_right)
    szineszekTable_frame.grid(row=1, column=0, sticky="s")

    szineszekTable_scrolly = Scrollbar(szineszekTable_frame)
    szineszekTable_scrolly.pack(side=RIGHT, fill=Y)

    szineszekTable_scrollx = Scrollbar(szineszekTable_frame, orient='horizontal')
    szineszekTable_scrollx.pack(side=BOTTOM, fill=X)

    szineszekTable = ttk.Treeview(szineszekTable_frame, yscrollcommand=szineszekTable_scrolly.set, xscrollcommand=szineszekTable_scrollx.set, height=20)

    szineszekTable_scrolly.config(command=szineszekTable.yview)
    szineszekTable_scrollx.config(command=szineszekTable.xview)

    szineszekTable['columns'] = ('sz_id', 'sz_name', 'sz_neme', 'sz_date', 'sz_nemzetiseg')

    szineszekTable.column("#0", width=0, stretch=NO)
    szineszekTable.column("sz_id", anchor=CENTER, width=65)
    szineszekTable.column("sz_name", anchor=CENTER, width=150)
    szineszekTable.column("sz_neme", anchor=CENTER, width=50)
    szineszekTable.column("sz_date", anchor=CENTER, width=95)
    szineszekTable.column("sz_nemzetiseg", anchor=CENTER, width=90)

    szineszekTable.heading("#0", text="X", anchor=CENTER)
    szineszekTable.heading("sz_id", text="Azonosító", anchor=CENTER)
    szineszekTable.heading("sz_name", text="Név", anchor=CENTER)
    szineszekTable.heading("sz_neme", text="Neme", anchor=CENTER)
    szineszekTable.heading("sz_date", text="Születési dátum", anchor=CENTER)
    szineszekTable.heading("sz_nemzetiseg", text="Nemzetiség", anchor=CENTER)

    szineszekTable.pack()

    showTable_szinesz()

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")