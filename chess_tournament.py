from views.home import *
from views.tournament import *
from controllers.menuManager import *
from controllers.round import *

print('Bienvenue sur Chess Tournament')
while True:
    option = menu_home()
    while True:
        if option == '1':
            option = menu_tournament()

            if option == '1':
                create_tournament()
            elif option == '2':
                tournaments = get_all_tournaments()
                ids = []
                for counter, tournament in enumerate(tournaments, start=1):
                    print(counter, tournament['name'])
                    ids.append(tournament.doc_id)

                index = int(input())-1
                tournament_id = ids[index]
                tournament = get_one_tournament(tournament_id)
                print(tournament['name'])
                print('1) Commencer le tournoi')
                print('2) Ajouter un joueur')
                option = str(input())
                if option == '2':
                    create_player(tournament_id)

            elif option == '3':
                print('À bientôt !')
                break

"""
round_counter = 1
tournament_1.players = add_players_to_tournament()
#tournament_1.players = players
while round_counter <= tournament_1.rounds_number:
    print(f'Tour {round_counter}')
    round = create_round(players, round_counter)
    update_score(round)
    round_counter = round_counter + 1

print('Tournoi terminé')
"""
