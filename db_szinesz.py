from db_nemzetek import StringToNum_nemzetiseg
from db import insert, delete, update, get, get_info_for_table


def get_szinesz(id):
    field_missing = id == ""
    sql_string = 'select * from szinesz where Szinesz_id="{}"'.format(id)
    sql_string2 = 'SELECT film.Film_cim, szereples.Szereples_szerep FROM szereples, film WHERE szereples.Szereples_Szinesz_id = "{}" AND film.Film_id = szereples.Szereples_Film_id'.format(id)
    return get(field_missing, sql_string, sql_string2)


def insert_szinesz(id, name, nem, szul_datum, nemzetiseg):
    field_missing = id == "" or name == "" or nem == "" or szul_datum == ""
    sql_string = 'insert into szinesz values ("{}","{}","{}","{}","{}")'.format(id, name, nem, szul_datum, StringToNum_nemzetiseg(nemzetiseg))
    return insert(field_missing, sql_string)


def update_szinesz(id, name, nem, szul_datum, nemzetiseg):
    field_missing = id == "" or name == "" or nem == "" or szul_datum == ""
    sql_string = 'update szinesz set Szinesz_nev="{}", Szinesz_neme="{}", Szinesz_szuletes="{}", Szinesz_nemzetiseg_id="{}" where Szinesz_id="{}"'.format(name, nem, szul_datum, StringToNum_nemzetiseg(nemzetiseg), id)
    return update(field_missing, sql_string)


def delete_szinesz(id):
    field_missing = id == ""
    sql_string = 'delete from szinesz where Szinesz_id="{}"'.format(id)
    return delete(field_missing, sql_string)


def StringToNum_szinesz(szineszneve):
    szinesz = get_formattedSzineszekfromDB()
    szinesz_inverted = {i: j for j, i in szinesz.items()}
    return szinesz_inverted.get(szineszneve, "null")


def get_szineszekfromDB():
    sql_string = 'SELECT Szinesz_nev FROM `szinesz` ORDER by `szinesz`.`Szinesz_id` ASC'
    return get_info_for_table(sql_string)

def get_formattedSzineszekfromDB():
    sql_string = 'SELECT  Szinesz_id, Szinesz_nev FROM `szinesz` ORDER by `szinesz`.`Szinesz_id` ASC'
    return dict(get_info_for_table(sql_string))


def get_szineszek_for_table():
    sql_string = 'select * from szinesz order by Szinesz_id ASC'
    return get_info_for_table(sql_string)


def NumToStringSzinesz(ID):
    szineszek = get_formattedSzineszekfromDB()
    return szineszek.get(ID, "null")
