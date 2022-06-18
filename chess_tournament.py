from controllers.tournament import *
from controllers.round import *
from data.player import *

print('Bienvenue sur Chess Tournament')
while True:
    print('Menu:')
    print('1) Créer un tournoi')
    print('2) Quitter')
    option = str(input())
    if option == '1':
        round_counter = 1
        tournament_1 = create_tournament()
        tournament_1.players = add_players_to_tournament()
        #tournament_1.players = players
        while round_counter <= tournament_1.rounds_number:
            print(f'Tour {round_counter}')
            round = create_round(players, round_counter)
            update_score(round)
            round_counter = round_counter + 1

        print('Tournoi terminé')
    elif option == '2':
        print('À bientôt !')
        break
