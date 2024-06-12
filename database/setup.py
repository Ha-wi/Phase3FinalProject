from models.player import Player
from models.enemy import Enemy

def create_tables():
    Player.create_table()
    Enemy.create_table()
