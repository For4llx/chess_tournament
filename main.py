from models.Tournament import Tournament
from models.Player import Player

from controllers.base import Controller
from views.base import View

def main():
    view = View()
    controller = Controller(view)
    controller.main_menu(view)

main()































"""
while True:
    option = menu_home()

    if option == '1':
        create_tournament()
    elif option == '2':
        create_player()
    elif option == '3':
        all_tournaments = get_all_tournaments()
        tournament_id = menu_tournament(all_tournaments)
        tournament = get_one_tournament(tournament_id)
"""
"""
    while True:
        if option == '1':
            option = menu_tournament()

            if option == '1':
                create_tournament()
            elif option == '2':
                create_player()
            elif option == '3':
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
                if option == '1':
                    round_counter = 1
                    while round_counter <= tournament['rounds_number']:
                        print(f'Tour {round_counter}')
                        create_round(tournament['players'], tournament_id, round_counter)
                        update_score(tournament_id, round_counter)
                        round_counter = round_counter + 1

                    print('Tournoi terminé')
                elif option == '2':
                    create_player(tournament_id)
                    break

            elif option == '3':
                print('À bientôt !')
                break
"""
"""
round_counter = 1
while round_counter <= tournament_1.rounds_number:
    print(f'Tour {round_counter}')
    round = create_round(players, round_counter)
    update_score(round)
    round_counter = round_counter + 1

print('Tournoi terminé')
"""
