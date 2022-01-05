from tkinter import messagebox as MessageBox
import mysql.connector as mysql

dbhost = 'localhost'
dbuser = 'dbuser'
dbpass = 'dbpass'
dbname = 'imdb'

def insert(field_missing, insert_query):
    if field_missing:
        MessageBox.showinfo("Figyelem!", "Minden mező megadása kötelező!")
        return False
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(insert_query)
        cursor.execute('commit')
        MessageBox.showinfo('Info', 'Sikeres beszúrás')
        con.close()
        return True


def delete(field_missing, insert_query):
    if field_missing:
        MessageBox.showinfo("Figyelem!", "ID mező megadása kötelező!")
        return False
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(insert_query)
        cursor.execute('commit')
        MessageBox.showinfo('Info', 'Sikeres törlés')
        con.close()
        return True


def update(field_missing, insert_query):
    if field_missing:
        MessageBox.showinfo("Figyelem!", "Minden mező megadása kötelező!")
        return False
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(insert_query)
        cursor.execute('commit')
        MessageBox.showinfo('Info', 'Sikeres frissítés')
        con.close()
        return True


def get(field_missing, insert_query, insert_query2):
    if field_missing:
        MessageBox.showinfo("Figyelem!", "ID mező megadása kötelező!")
        return None
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(insert_query)
        rows = cursor.fetchmany(1)

        cursor2 = con.cursor()
        cursor2.execute(insert_query2)
        rows2 = cursor2.fetchall()
        con.close()
        return (rows, rows2)

def otherGet(field_missing, insert_query):
    if field_missing:
        MessageBox.showinfo("Figyelem!", "ID mező megadása kötelező!")
        return None
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(insert_query)
        rows = cursor.fetchall()
        con.close()
        return rows


def get_info_for_table(insert_query):
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute(insert_query)
    con.close()
    return cursor.fetchall()


