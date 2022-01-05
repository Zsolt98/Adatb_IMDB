from db import insert, delete, update, otherGet, get_info_for_table


def get_nemzet(id):
    field_missing = id == ""
    sql_string = 'select * from nemzetiseg where Nemzetiseg_id="{}"'.format(id)
    return otherGet(field_missing, sql_string)


def insert_nemzet(id, nev):
    field_missing = id == "" or nev == ""
    sql_string = 'insert into nemzetiseg values ("{}","{}")'.format(id, nev)
    return insert(field_missing, sql_string)


def update_nemzet(id, nev):
    field_missing = id == "" or nev == ""
    sql_string = 'update nemzetiseg set Nemzetiseg_neve="{}" where Nemzetiseg_id="{}"'.format(nev, id)
    return update(field_missing, sql_string)


def delete_nemzet(id):
    field_missing = id == ""
    sql_string = 'delete from nemzetiseg where Nemzetiseg_id="{}"'.format(id)
    return delete(field_missing, sql_string)


def get_nemzet_for_table():
    sql_string = 'select * from nemzetiseg order by Nemzetiseg_id ASC'
    return get_info_for_table(sql_string)





def get_nemzetekfromDB():
    sql_string = 'SELECT Nemzetiseg_neve FROM `nemzetiseg` ORDER by `nemzetiseg`.`Nemzetiseg_id` ASC'
    return get_info_for_table(sql_string)


def get_formattedNemzetekfromDB():
    sql_string = 'SELECT  Nemzetiseg_id, Nemzetiseg_neve FROM `nemzetiseg` ORDER by `nemzetiseg`.`Nemzetiseg_id` ASC'
    return dict(get_info_for_table(sql_string))


def StringToNum_nemzetiseg(nemzetneve):
    nemzetek = get_formattedNemzetekfromDB()
    nemzetek_inverted = {i: j for j, i in nemzetek.items()}
    return nemzetek_inverted.get(nemzetneve, "null")


def NumToStringnemzetiseg(nemzetID):
    nemzetek = get_formattedNemzetekfromDB()
    return nemzetek.get(nemzetID, "null")
