import sqlite3


class Database:


    def get_janre():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        result = cursor.execute("""SELECT * FROM janre""").fetchall()
        conn.close()
        return result
    
    def add_janre(janre):
        conn = sqlite3.connect("scripts/database.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO janre (janre_book) VALUES (?)""", (janre,))
        conn.commit()
        conn.close()
        return True



