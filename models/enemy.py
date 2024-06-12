import sqlite3

class Enemy:
    def __init__(self, name, health, attack_power, enemy_id=None):
        self.id = enemy_id
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @staticmethod
    def create_table():
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS enemies
                         (id INTEGER PRIMARY KEY, name TEXT, health INTEGER, attack_power INTEGER)''')
            conn.commit()

    def save(self):
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            if self.id is None:
                c.execute("INSERT INTO enemies (name, health, attack_power) VALUES (?, ?, ?)",
                          (self.name, self.health, self.attack_power))
                self.id = c.lastrowid
            else:
                c.execute("UPDATE enemies SET name=?, health=?, attack_power=? WHERE id=?",
                          (self.name, self.health, self.attack_power, self.id))
            conn.commit()

    @staticmethod
    def delete(enemy_id):
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM enemies WHERE id=?", (enemy_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM enemies")
            rows = c.fetchall()
            return [Enemy(*row[1:], enemy_id=row[0]) for row in rows]

    @staticmethod
    def find_by_id(enemy_id):
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM enemies WHERE id=?", (enemy_id,))
            row = c.fetchone()
            if row:
                return Enemy(*row[1:], enemy_id=row[0])
            return None

    def attack(self):
        return self.attack_power
