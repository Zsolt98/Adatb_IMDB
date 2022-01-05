import db_film
import db_rendezo
from db import insert, delete, update, otherGet, get_info_for_table


def get_rendezesek(id):
    field_missing = id == ""
    sql_string = 'select * from rendezes where Rendezes_id="{}"'.format(id)
    return otherGet(field_missing, sql_string)


def insert_rendezesek(id, rendezoID, filmID):
    field_missing = id == "" or rendezoID == "" or filmID == ""
    sql_string = 'insert into rendezes values ("{}","{}","{}")'.format(id, db_rendezo.StringToNum_rendezo(rendezoID), db_film.StringToNum_film(filmID))
    return insert(field_missing, sql_string)


def update_rendezesek(id, rendezoID, filmID):
    field_missing = id == "" or rendezoID == "" or filmID == ""
    sql_string = 'update rendezes set Rendezes_Rendezo_id="{}", Rendezes_Film_id="{}" where Rendezes_id="{}"'.format(db_rendezo.StringToNum_rendezo(rendezoID), db_film.StringToNum_film(filmID), id)
    return update(field_missing, sql_string)


def delete_rendezesek(id):
    field_missing = id == ""
    sql_string = 'delete from rendezes where Rendezes_id="{}"'.format(id)
    return delete(field_missing, sql_string)


def get_rendezesek_for_table():
    sql_string = 'select * from rendezes order by Rendezes_id ASC'
    return get_info_for_table(sql_string)


