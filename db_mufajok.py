from db import insert, delete, update, otherGet, get_info_for_table


def get_mufaj(Mufaj_id):
    field_missing = Mufaj_id == ""
    sql_string = 'select * from mufaj where Mufaj_id="{}"'.format(Mufaj_id)
    return otherGet(field_missing, sql_string)


def insert_mufaj(Mufaj_id, Mufaj_neve):
    field_missing = Mufaj_id == "" or Mufaj_neve == ""
    sql_string = 'insert into mufaj values ("{}","{}")'.format(Mufaj_id, Mufaj_neve)
    return insert(field_missing, sql_string)


def update_mufaj(Mufaj_id, Mufaj_neve):
    field_missing = Mufaj_id == "" or Mufaj_neve == ""
    sql_string = 'update mufaj set Mufaj_neve="{}" where Mufaj_id="{}"'.format(Mufaj_neve, Mufaj_id)
    return update(field_missing, sql_string)


def delete_mufaj(Mufaj_id):
    field_missing = Mufaj_id == ""
    sql_string = 'delete from mufaj where Mufaj_id="{}"'.format(Mufaj_id)
    return delete(field_missing, sql_string)


def get_mufaj_for_table():
    sql_string = 'select * from mufaj order by Mufaj_id ASC'
    return get_info_for_table(sql_string)






def get_mufajokfromDB():
    sql_string = 'SELECT Mufaj_neve FROM `mufaj` ORDER by `mufaj`.`Mufaj_id` ASC'
    return get_info_for_table(sql_string)


def get_formattedMufajokfromDB():
    sql_string = 'SELECT  Mufaj_id, Mufaj_neve FROM `mufaj` ORDER by `mufaj`.`Mufaj_id` ASC'
    return dict(get_info_for_table(sql_string))


def StringToNum_mufaj(mufajneve):
    mufajok = get_formattedMufajokfromDB()
    mufajok_inverted = {i: j for j, i in mufajok.items()}
    return mufajok_inverted.get(mufajneve, "null")


def NumToStringMufaj(mufajID):
    mufajok = get_formattedMufajokfromDB()
    return mufajok.get(mufajID, "null")