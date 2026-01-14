import sqlite3 


conekt = sqlite3.connect("piar_user.db")
cursor = conekt.cursor()

comand = """
    CREATE TABLE IF NOT EXISTS
    Produkt(id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT , user_name TEXT , pasword TEXT , podpiski TEXT , koina INTEGER , pol_id INTEGER )
"""

cursor.execute(comand)

conekt.commit()

def polushit_id_polz(pol_id: int):
    conn = sqlite3.connect("piar_user.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Produkt WHERE pol_id = ?",
        (pol_id,)
    )

    result = cursor.fetchone()
    conn.close()
    return result

def polushit_user_name(user_name): # даем юзер имя получяем или нет
    cursor.execute("SELECT * FROM Produkt WHERE user_name = ?" , (user_name , )) 
    users = cursor.fetchall()  

    return users


def zapisuwat_polzuwatela(name , name_user  , password , podpiski , koina , pol_id ):
    cursor.execute("INSERT INTO Produkt (name , user_name, pasword , podpiski ,  koina , pol_id) VALUES (?,?,?,?,?,?)" , (name , name_user  , password , podpiski , koina ,  pol_id))
    conekt.commit()


def polushit_user_name_parol(user_name): # даем юзер имя получяем или нет
    cursor.execute("SELECT pasword FROM Produkt WHERE user_name = ?" , (user_name , )) 
    users = cursor.fetchone()  

    return users

def zapisuwat_polzuwatela2(name: str,user_name: str,pasword: str,podpiski: str,koina: int,pol_id: int):
    conn = sqlite3.connect("piar_user.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Produkt SET name = ?, user_name = ?, pasword = ?, podpiski = ?, koina = ? WHERE pol_id = ? """, (name, user_name, pasword, podpiski, koina, pol_id))
    
    conn.commit()
    conn.close()





cursor2 = conekt.cursor()

comand2 = """
    CREATE TABLE IF NOT EXISTS
    Kanal(id INTEGER PRIMARY KEY AUTOINCREMENT , prem_podpiska BOOLEAN , name TEXT , kategorii TEXT , sulka TEXT, dlitelnost_podpiski INTEGER , opisanie TEXT , fotoshka TEXT  )

"""

cursor2.execute(comand2)

conekt.commit()


def zapisuwat_kanal(prem_podpiska , name , kategorii , sulka , dlitelnost_podpiski , opisanie , fotoshka ):
    cursor2.execute("INSERT INTO Kanal (prem_podpiska , name , kategorii , sulka , dlitelnost_podpiski , opisanie ,  fotoshka ) VALUES (?,?,?,?,?,?,?)" , (prem_podpiska , name , kategorii , sulka , dlitelnost_podpiski , opisanie ,  fotoshka ))
    conekt.commit()



def poluShet_kanal():
    cursor2.execute(""" SELECT * FROM Kanal """, ())
    
    return cursor2.fetchall()


def poluShet_kanal_wan(id_kanal ):
    cursor2.execute(""" SELECT * FROM Kanal WHERE id = ?""", (id_kanal , ))
    return cursor2.fetchall()  












































#def zapis_primerka(primer , result , data_primerow):
#    cursor.execute("INSERT INTO Produkt (primer , result , data_primerow  ) VALUES (?,?,?)" , (str(primer), str(result), str(data_primerow)))
#    conekt2.commit()
#
#
#
#
#def poluchatel_vse_calkun():
#    cursor2.execute("SELECT * FROM loger")
#    users = cursor2.fetchall()  
#    text = ""
#
#    for user in users:
#        text += f"ID: {user[0]}, пример: {user[1]}, результат: {user[2]}, дата: {user[3]}\n"
#    return text
#
#
#
#
#def zapis_polzuwatel(login , user_name  , pasword , bio):
#    cursor.execute("INSERT INTO User (login , user_nmae , pasword , namber ) VALUES (?,?,?,?)" , (login , user_name , pasword , bio))
#    conekt.commit()
#
#
#
#
#
#def poluchatel_vse2(user_nmae):
#    cursor.execute("SELECT user_nmae , namber FROM User WHERE user_nmae = ?  " , (user_nmae , )) 
#    user_nmae = cursor.fetchone()  
#    if user_nmae:
#        return user_nmae
#