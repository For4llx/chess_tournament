import sys

sys.path.append('../chess_tournament')

from models.Tournament import Tournament
from views.tournament import *
from models.Player import Player
from views.player import *

def create_tournament():
    tournament = new_tournament_form()
    tournament_1 = Tournament(tournament['name'])
    return tournament_1

def add_players_to_tournament():
    players = player_form()
    all_players = []

    for player in players:
        full_name = player.split()
        last_name = full_name[0]
        first_name = full_name[1]
        rank = full_name[2]
        test = Player(last_name, first_name, rank)
        all_players.append(test)

    return all_players