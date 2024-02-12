import sqlite3

class Database:
    def __init__(self):
        self.__con = sqlite3.connect("todo/todo.db")
        cursor = self.__con.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                completed INTEGER DEFAULT 0
            )""")
        self.__con.commit()

    def add(self, name, desc):
        cursor = self.__con.cursor()
        cursor.execute("INSERT INTO todo (name, description) VALUES (?, ?)", (name, desc))
        self.__con.commit()

    def show(self):
        cursor = self.__con.cursor();
        cursor.execute("SELECT * FROM todo")
        return cursor.fetchall()
        
    def completed(self, _id):
        cursor = self.__con.cursor()
        cursor.execute("UPDATE todo SET completed = 1 WHERE id = ?", (_id))
        self.__con.commit()

    def delete(self, _id):
        cursor = self.__con.cursor()
        cursor.execute("DELETE FROM todo WHERE id = ?", (_id))
        self.__con.commit()
    
