from flask_sqlalchemy import SQLAlchemy
import sqlite3
from werkzeug.exceptions import abort 


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_newestpet():
    conn = get_db_connection()
    pet = conn.execute('SELECT * FROM pets ORDER BY ID DESC LIMIT 1').fetchone()
    conn.close()
    if pet is None:
        abort(404)
    return pet

def get_pet(pet):
    conn = get_db_connection()
    pet = conn.execute('SELECT * FROM pets WHERE Name=?', (pet,)).fetchone()
    conn.close()
    if pet is None:
        abort(404)
    return pet 

def get_all():
    conn = get_db_connection()
    pets = conn.execute('SELECT * FROM pets').fetchall()
    conn.close()
    return pets