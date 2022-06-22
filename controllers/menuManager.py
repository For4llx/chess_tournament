import sys

sys.path.append('../chess_tournament')

from models.Tournament import Tournament
from views.tournament import tournament_form
from models.Player import Player
from views.player import *
from tinydb import TinyDB, Query

tournament_database = TinyDB('data/tournament.json')
player_database = TinyDB('data/player.json')


def create_tournament():
    tournament = tournament_form()
    tournament = Tournament(
        tournament['name'],
        tournament['place'],
        tournament['time_control'],
        tournament['description'],
        tournament['rounds_number'])
    tournament.save()

def get_all_tournaments():
    return tournament_database.all()

def get_one_tournament(id):
    return tournament_database.get(doc_id=id)

def create_player(tournament_id):
    player = player_form()
    player = Player(
        player['last_name'],
        player['first_name'],
        player['ranking'],
        player['birth_date'],
        player['sex'])
    player.save(tournament_id)

def get_players():
    return player_database.all()
