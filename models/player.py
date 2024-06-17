import sqlite3
import random

class Player:
    def __init__(self, name, character_class, health=100, level=1, experience=0, player_id=None):
        self.id = player_id
        self.name = name
        self.character_class = character_class
        self.health = health
        self.level = level
        self.experience = experience

    @staticmethod
    def create_table():
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS players
                         (id INTEGER PRIMARY KEY, name TEXT, character_class TEXT, health INTEGER, level INTEGER, experience INTEGER)''')
            conn.commit()

    def save(self):
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            if self.id is None:
                c.execute("INSERT INTO players (name, character_class, health, level, experience) VALUES (?, ?, ?, ?, ?)",
                          (self.name, self.character_class, self.health, self.level, self.experience))
                self.id = c.lastrowid
            else:
                c.execute("UPDATE players SET name=?, character_class=?, health=?, level=?, experience=? WHERE id=?",
                          (self.name, self.character_class, self.health, self.level, self.experience, self.id))
            conn.commit()

    @staticmethod
    def delete(player_id):
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM players WHERE id=?", (player_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM players")
            rows = c.fetchall()
            return [Player(*row[1:], player_id=row[0]) for row in rows]

    @staticmethod
    def find_by_id(player_id):
        with sqlite3.connect('Aluposiak.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM players WHERE id=?", (player_id,))
            row = c.fetchone()
            if row:
                return Player(*row[1:], player_id=row[0])
            return None

    def attack(self):
        return random.randint(10, 20)

    def cast_spell(self):
        return random.randint(15, 25)

    def sneak_attack(self):
        return random.randint(20, 30)

    def level_up(self):
        self.level += 1
        self.health = 100
        self.experience = 0
        print(f"Congratulations! You leveled up to level {self.level}. Your health has been restored.")