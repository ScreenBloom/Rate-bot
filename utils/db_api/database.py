import random
import sqlite3
from datetime import datetime

from data import config as cfg
from loader import bot

conn = sqlite3.connect(r"utils\db_api\database.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id PRIMARY KEY,
    username TEXT,
    date INT,
    vip INT,
    ban INT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS ankets(
    id PRIMARY KEY,
    name TEXT,
    photo INT,
    floor TEXT,
    about_me TEXT,
    who TEXT,
    rating INT)
""")


cur.execute("""CREATE TABLE IF NOT EXISTS assessed(
    id_user PRIMARY KEY,
    id_ankets INT)
""")

#Users

def create_user_assessed(userId):
    try:
        cur.execute("INSERT INTO assessed VALUES(?,?)",(userId,0))
        conn.commit()
    except Exception as e:
        pass

def create_user(userId,username):
    try:
        date = str(datetime.now())[:19]
        cur.execute("INSERT INTO users VALUES(?,?,?,?,?)",(userId,username,date,0,0))
        conn.commit()
    except Exception as e:
        pass

def get_user_ids():
    result = []
    cortejs = cur.execute("SELECT * FROM users")
    for crtj in cortejs:
        result.append(int(crtj[0]))
    return result

def get_user(userId):
    try:
        user_data = cur.execute("SELECT * FROM users WHERE id = ?",(userId,)).fetchone()
        return parse_user_data(user_data)
    except:
        pass

def update_userfield(user_id,field,update):
    cur.execute(f"UPDATE users SET {field} = ? WHERE id = ?",(update,user_id))
    conn.commit()

def plus_userfield(user_id,field,plus_value):
    old = cur.execute(f"SELECT {field} FROM users WHERE id = ?", (user_id,)).fetchone()[0]
    if old == None:
        old = ""
    new = old + plus_value
    update_userfield(user_id,field,new)

def parse_user_data(data):
    return {'id': data[0],'username': data[1],'date': data[2],'vip': data[3],'ban': data[4]}

#ANKETS
def create_ankets(user_id,name,photo_id):
    try:
        cur.execute("INSERT INTO ankets VALUES(?,?,?,?,?,?,?)", (user_id, name, photo_id, "Not specified", "Not specified","Not specified",0))
        conn.commit()
    except Exception as e:
        print(e)
        pass

def get_user_ankets(userId):
    try:
        data = cur.execute("SELECT * FROM ankets WHERE id = ?", (userId,)).fetchone()
        return parse_user_anket_data(data)
    except Exception as e:
        print(e)
        return None

def parse_user_anket_data(data):
    return {'id': data[0],'name': data[1],'photo': data[2],'floor': data[3],'about_me': data[4],'who': data[5],'rating': data[6]}


def update_ankets(user_id,field,update):
    cur.execute(f"UPDATE ankets SET {field} = ? WHERE id = ?",(update,user_id))
    conn.commit()


def best_profiles():
    try:
        data = cur.execute("SELECT * FROM ankets ORDER BY rating DESC LIMIT 3;").fetchall()
        return data
    except Exception as e:
        print(e)

def all_man_ankets():
    try:
       data = cur.execute("SELECT id FROM ankets WHERE floor = 'Парень'").fetchall()
       return data
    except Exception as e:
        print(e)

def all_girl_ankets():
    try:
       data = cur.execute("SELECT id FROM ankets WHERE floor == 'Девушка'").fetchall()
       return data
    except Exception as e:
        print(e)

def all_ankets():
    try:
        data = cur.execute("SELECT id FROM ankets").fetchall()
        ids = [row[0] for row in data]
        random_id = random.choice(ids)
        return random_id
    except Exception as e:
        print(e)


def get_all_history_ankets(user_id):
    try:
        user_data = cur.execute("SELECT * FROM assessed WHERE id_user = ?",(user_id,)).fetchone()
        return parse_user_assessed_data(user_data)
    except:
        pass

def parse_user_assessed_data(data):
    return {'id_user': data[0],'id_ankets': data[1]}