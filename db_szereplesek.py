from db import insert, delete, update, otherGet, get_info_for_table
import db_szinesz, db_film


def get_szereplesek(Szereples_id):
    field_missing = Szereples_id == ""
    sql_string = 'select * from szereples where Szereples_id="{}"'.format(Szereples_id)
    return otherGet(field_missing, sql_string)


def insert_szereplesek(Szereples_id, Szereples_szerep, szinesz, film):
    field_missing = Szereples_id == "" or Szereples_szerep == "" or szinesz == "" or film == ""
    sql_string = 'insert into szereples values (NULL,"{}","{}","{}")'.format(Szereples_szerep, db_szinesz.StringToNum_szinesz(szinesz), db_film.StringToNum_film(film))
    return insert(field_missing, sql_string)


def update_szereplesek(Szereples_id, Szereples_szerep, szinesz, film):
    field_missing = Szereples_id == "" or Szereples_szerep == "" or szinesz == "" or film == ""
    sql_string = 'update szereples set Szereples_szerep="{}", Szereples_Szinesz_id="{}", Szereples_Film_id="{}" where Szereples_id="{}"'.format(Szereples_szerep, db_szinesz.StringToNum_szinesz(szinesz), db_film.StringToNum_film(film), Szereples_id)
    return update(field_missing, sql_string)


def delete_szereplesek(Szereples_id):
    field_missing = Szereples_id == ""
    sql_string = 'delete from szereples where Szereples_id="{}"'.format(Szereples_id)
    return delete(field_missing, sql_string)


def get_szereplesek_for_table():
    sql_string = 'select * from szereples order by Szereples_id ASC'
    return get_info_for_table(sql_string)



def get_szereplesekfromDB():
    sql_string = 'SELECT Szereples_szerep FROM `szereples` ORDER by `szereples`.`Szereples_id` ASC'
    return get_info_for_table(sql_string)


def get_formattedSzereplesfromDB():
    sql_string = 'SELECT  Szereples_id, Szereples_szerep FROM `szereples` ORDER by `szereples`.`Szereples_id` ASC'
    return dict(get_info_for_table(sql_string))


def StringToNum_szereples(szerep_neve):
    szerepek = get_formattedSzereplesfromDB()
    szerepek_inverted = {i: j for j, i in szerepek.items()}
    return szerepek_inverted.get(szerep_neve, "null")


def NumToStringSzereples(mufajID):
    szerepek = get_formattedSzereplesfromDB()
    return szerepek.get(mufajID, "null")
