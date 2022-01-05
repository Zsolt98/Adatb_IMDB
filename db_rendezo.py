from db_nemzetek import StringToNum_nemzetiseg
from db import insert, delete, update, get, get_info_for_table
from gui_film import *


def get_rendezo(Rendezo_id):
    field_missing = Rendezo_id == ""
    sql_string = 'select * from rendezo where Rendezo_id="{}"'.format(Rendezo_id)
    sql_string2 = 'SELECT film.Film_cim, film.Film_megjelenesEve FROM film WHERE film.Film_rendezo_id = "{}" order by Film_megjelenesEve desc'.format(Rendezo_id)
    return get(field_missing, sql_string, sql_string2)


def insert_rendezo(id, name, nemzetiseg):
    field_missing = id == "" or name == ""
    sql_string = 'insert into rendezo values ("{}","{}","{}")'.format(id, name, StringToNum_nemzetiseg(nemzetiseg))
    return insert(field_missing, sql_string)


def update_rendezo(id, name, nemzetiseg):
    field_missing = id == "" or name == ""
    sql_string = 'update rendezo set Rendezo_nev="{}", Rendezo_nemzetiseg_id="{}" where Rendezo_id="{}"'.format(name, StringToNum_nemzetiseg(nemzetiseg), id)
    return update(field_missing, sql_string)


def delete_rendezo(id):
    field_missing = id == ""
    sql_string = 'delete from rendezo where Rendezo_id="{}"'.format(id)
    return delete(field_missing, sql_string)


def StringToNum_rendezo(rendezoneve):
    szinesz = get_formattedRendezofromDB()
    szinesz_inverted = {i: j for j, i in szinesz.items()}
    return szinesz_inverted.get(rendezoneve, "null")


def get_rendezofromDB():
    sql_string = 'SELECT Rendezo_nev FROM `rendezo` ORDER by `rendezo`.`Rendezo_id` ASC'
    return get_info_for_table(sql_string)

def get_formattedRendezofromDB():
    sql_string = 'SELECT  Rendezo_id, Rendezo_nev FROM `rendezo` ORDER by `rendezo`.`Rendezo_id` ASC'
    return dict(get_info_for_table(sql_string))


def get_rendezo_for_table():
    sql_string = 'select * from rendezo order by Rendezo_id ASC'
    return get_info_for_table(sql_string)


def NumToStringRendezo(ID):
    szineszek = get_formattedRendezofromDB()
    return szineszek.get(ID, "null")
