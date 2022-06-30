from operator import itemgetter
import time
import numpy as np

def get_rank(player):
    return player.get('ranking')

def get_points(player):
    return player['record'].get('points')

def generate_pairs(players, tournament_id, round_counter):
    if round_counter == 1:
        pairs = []
        players.sort(key=get_rank)
        players_number = len(players)
        middle_index = players_number // 2
        upper_class_players = players[:middle_index]
        lower_class_players = players[middle_index:]

        for upper_class_player, lower_class_player in zip(upper_class_players, lower_class_players):
            pairs.append([upper_class_player, lower_class_player])

        return pairs
    else:
        print('Round' + str(round_counter))
        pairs = []
        time.sleep(3)
        players = sorted(players, key=lambda x: (x['record']['points'], x['ranking']))
        players_number = len(players)

        for count, player in enumerate(players):
            if count-1 <= players_number:
                pair = [players.pop(0), players.pop(0)]
                pairs.append(pair)

        pairs.append(players)
                
        return pairs
