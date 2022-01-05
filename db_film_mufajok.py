from db import insert, delete, update, otherGet, get_info_for_table
import db_film, db_mufajok

def get_fm(id):
    field_missing = id == ""
    sql_string = 'select * from filmmufaj where Filmmufaj_id="{}"'.format(id)
    return otherGet(field_missing, sql_string)


def insert_fm(id, film_ID, mufaj_ID):
    field_missing = id == "" or film_ID == "" or mufaj_ID == ""
    sql_string = 'insert into filmmufaj values ("{}","{}","{}")'.format(id, db_film.StringToNum_film(film_ID), db_mufajok.StringToNum_mufaj(mufaj_ID))
    return insert(field_missing, sql_string)


def update_fm(id, film_ID, mufaj_ID):
    field_missing = id == "" or film_ID == "" or mufaj_ID == ""
    sql_string = 'update filmmufaj set Filmmufaj_id_Film_id="{}", Filmmufaj_id_Film_mufaj_id="{}" where Filmmufaj_id="{}"'.format(db_film.StringToNum_film(film_ID), db_mufajok.StringToNum_mufaj(mufaj_ID), id)
    return update(field_missing, sql_string)


def delete_fm(id):
    field_missing = id == ""
    sql_string = 'delete from filmmufaj where Filmmufaj_id="{}"'.format(id)
    return delete(field_missing, sql_string)


def get_fm_for_table():
    sql_string = 'select * from filmmufaj order by Filmmufaj_id ASC'
    return get_info_for_table(sql_string)

