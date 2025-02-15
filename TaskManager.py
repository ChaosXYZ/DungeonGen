import sqlite3

class TaskManager():
    def __init__(self):
        self.con = sqlite3.connect("Tasks.db")
        self.cursor = self.con.cursor()
        self.create_schema()

    def create_schema(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Tasks (task_id INTEGER PRIMARY KEY NOT NULL, type TEXT CHECK(type IN ('Physical', 'Maths', 'Puzzle', 'Coding')) NOT NULL, difficulty INTEGER CHECK(difficulty BETWEEN 1 AND 10) NOT NULL, source TEXT NOT NULL ); ")

    def get_task(self, task_id):
        self.cursor.execute(f"SELECT * FROM Tasks where task_id = {task_id}")
    
    def fetch_tasks(self, task_type, difficulty):
        type_cond, difficulty_cond = "", ""

        if task_type != "ALL":
            if len(task_type) > 1:
                type_formatted = [f"'{t}'" for t in task_type]
                type_cond = f"AND type in ({','.join(type_formatted)})"
            else:
                type_cond = f"AND type = '{task_type[0]}'"

        if difficulty != "ALL":
            if len(difficulty) > 1:
                difficulty_formatted = [str(t) for t in difficulty]
                difficulty_cond = f"AND difficulty in ({','.join(difficulty_formatted)})"
            else:
                difficulty_cond = f"AND difficulty = {difficulty[0]}"

        self.cursor.execute(f"SELECT task_id FROM Tasks where 1=1 {type_cond} {difficulty_cond}")