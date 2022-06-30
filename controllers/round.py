from models.Round import Round
from views.round import round_form
from helpers import get_rank
from tinydb import TinyDB, Query

tournament_database = TinyDB('data/tournament.json')

def create_round():
    print(tournament_database.get['players'])

def update_score(tournament_id, round_counter):
    round_counter = round_counter-1
    round = tournament_database.get(doc_id=tournament_id)['rounds'][round_counter]

    results = round_form(round)
    for index, result in enumerate(results):
        if result == '1':
            round['matches'][index][0][1]['score'] = round['matches'][index][0][1]['score'] + 1 #score joueur 1 + 1
        elif result == '2':
            round['matches'][index][1][1]['score'] = round['matches'][index][1][1]['score'] + 1 #score joueur 2 + 1
        elif result == '3':
            round['matches'][index][0][1]['score'] = round['matches'][index][0][1]['score'] + 0.5
            round['matches'][index][1][1]['score'] = round['matches'][index][1][1]['score'] + 0.5

    tournament_database.update({'rounds': [round]}, doc_ids=[tournament_id])


  """
    if round_counter == 1:
        matches = []

        players.sort(key=get_rank)
        players_number = len(players)
        middle_index = players_number // 2
        upper_class_players = players[:middle_index]
        lower_class_players = players[middle_index:]

        for i in range(middle_index):
            match = [[upper_class_players[i], {'score': 0}] ,[lower_class_players[i], {'score': 0}]]
            matches.append(match)

        round = Round(f'Round_{round_counter}', matches)
        round.save(tournament_id)
    else:
        pass
        #tournament = tournament_database.get(doc_id=tournament_id)
        #print(tournament['rounds'][0]['matches'][0][0][1])
"""