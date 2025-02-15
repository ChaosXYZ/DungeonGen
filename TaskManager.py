import sqlite3

class TaskManager():
    def __init__(self):
        self.con = sqlite3.connect("Tasks.db")
        self.cursor = self.con.cursor()
        self.create_schema()

    def create_schema(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Tasks (task_id INTEGER PRIMARY KEY NOT NULL, type TEXT CHECK(type IN ('Physical', 'Maths', 'Puzzle', 'Coding')) NOT NULL, difficulty INTEGER CHECK(difficulty BETWEEN 1 AND 10) NOT NULL, source TEXT NOT NULL ); ")
