import os
from views.player import player_form
from models.Player import Player
from tinydb import TinyDB

os.makedirs(os.path.dirname('data/player.json'), exist_ok=True)
player_database = TinyDB('data/player.json')


def create_player():
    player = player_form()
    player = Player(
        player['last_name'],
        player['first_name'],
        player['ranking'],
        player['birth_date'],
        player['sex'])
    player.save()

def get_all_players():
    return player_database.all()

def get_one_player(id):
    return player_database.get(doc_id=id)