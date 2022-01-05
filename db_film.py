from db import insert, delete, update, get, get_info_for_table
import db_rendezo


def get_film(Film_id):
    field_missing = Film_id == ""
    sql_string = 'select * from film where Film_id="{}"'.format(Film_id)
    sql_string2 = 'SELECT mufaj.Mufaj_neve, film.Film_cim FROM film, mufaj, filmmufaj WHERE film.Film_id = "{}" AND filmmufaj.FilmMufaj_id_Film_id = "{}" AND mufaj.Mufaj_id = filmmufaj.FilmMufaj_id_Film_mufaj_id'.format(Film_id, Film_id)
    return get(field_missing, sql_string, sql_string2)


def insert_film(Film_id, Film_cim, Film_megjelenesEve, Film_jatekido, Film_rendezo_id):
    field_missing = Film_id == "" or Film_cim == "" or Film_megjelenesEve == "" or Film_jatekido == "" or Film_rendezo_id == ""
    sql_string = 'insert into film values ("{}","{}","{}","{}","{}")'.format(Film_id, Film_cim, Film_megjelenesEve, Film_jatekido, db_rendezo.StringToNum_rendezo(Film_rendezo_id))
    return insert(field_missing, sql_string)


def update_film(Film_id, Film_cim, Film_megjelenesEve, Film_jatekido, Film_rendezo_id):
    field_missing = Film_id == "" or Film_cim == "" or Film_megjelenesEve == "" or Film_jatekido == "" or Film_rendezo_id == ""
    sql_string = 'update film set Film_cim="{}", Film_megjelenesEve="{}", Film_jatekido="{}", Film_rendezo_id="{}" where Film_id="{}"'.format(Film_cim, Film_megjelenesEve, Film_jatekido, db_rendezo.StringToNum_rendezo(Film_rendezo_id), Film_id)
    return update(field_missing, sql_string)


def delete_film(Film_id):
    field_missing = id == ""
    sql_string = 'delete from film where Film_id="{}"'.format(Film_id)
    return delete(field_missing, sql_string)


def get_film_for_table():
    sql_string = 'select * from film order by Film_id ASC'
    return get_info_for_table(sql_string)


def StringToNum_film(filmneve):
    film = get_formattedFilmekfromDB()
    film_inverted = {i: j for j, i in film.items()}
    return film_inverted.get(filmneve, "null")


def get_filmekfromDB():
    sql_string = 'SELECT Film_cim FROM `film` ORDER by `film`.`Film_id` ASC'
    return get_info_for_table(sql_string)


def get_formattedFilmekfromDB():
    sql_string = 'SELECT  Film_id, Film_cim FROM `film` ORDER by `film`.`Film_id` ASC'
    return dict(get_info_for_table(sql_string))


def get_filmek_for_table():
    sql_string = 'select * from film order by Film_id ASC'
    return get_info_for_table(sql_string)


def NumToStringFilmek(ID):
    filmek = get_formattedFilmekfromDB()
    return filmek.get(ID, "null")
