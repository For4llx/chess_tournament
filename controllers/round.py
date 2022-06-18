import sys

sys.path.append('../chess_tournament')

from data.player import *
from models.Round import Round
from views.round import round_form
from helpers import get_rank

def create_round(players, round_counter):
    if round_counter == 1:
        chess_matches = []
        chess_match = []

        players.sort(key=get_rank)
        players_number = len(players)
        middle_index = players_number // 2
        upper_class_players = players[:middle_index]
        lower_class_players = players[middle_index:]

        for i in range(middle_index):
            chess_match = [[upper_class_players[i], {'score': 0}] ,[lower_class_players[i], {'score': 0}]]
            chess_matches.append(chess_match)

        chess_round = Round(f'Round_{round_counter}', chess_matches)

        return chess_round
    else:
        pass

def update_score(rounds):
    results = round_form(rounds)

    for result in results:
        if result == '1':
            print('winner 1')
        elif result == '2':
            print('winner 2')
        elif result == '3':
            print('égalité')
