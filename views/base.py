class View:
    def main_menu_select(self):
        print('Menu principal:')
        print('1) Créer un nouveau tournoi')
        print('2) Ajouter un nouveau joueur')
        print('3) Continuer un tournoi')
        print('4) Quitter')
        option = str(input())
        return option

    def player_form(self):
        print('Ajouter un joueur:\n')
        last_name = input('Nom:')
        first_name = input('Prénom:')
        birth_date = input('Date de naissance:')
        sex = input('Sex:')
        ranking = input('Classement:')

        return {
          'last_name': last_name,
          'first_name': first_name,
          'birth_date': birth_date,
          'sex': sex,
          'ranking': ranking
        }

    
    def tournament_form(self):
        name = input('Nom:')
        place = input('Lieu:')
        rounds_number = input('Nombre de tours:')

        while True:
            print('Temps:\n')
            print('1) Bullet')
            print('2) Blitz')
            print('3) Coup rapide')
            time_control = str(input())
            if time_control == '1':
                time_control = 'Bullet'
                break
            elif time_control == '2':
                time_control = 'Blitz'
                break
            elif time_control == '3':
                time_control = 'Coup rapide'
                break
            else:
                print('entrer une option valide (1, 2 ou 3)')

        description = input('description')

        return {
            'name': name,
            'place': place,
            'rounds_number': rounds_number,
            'time_control': time_control,
            'description': description
        }
    
    def tournaments_select(self, tournaments):
        for tournament in tournaments:
            print(str(tournament.doc_id) + ')' + ' ' + tournament['name'])

        return str(input())
    
    def players_select(self, players):
        for player in players:
            print(str(player.doc_id) + ')' + ' ' + player['last_name'] + ' ' + player['first_name'])
        
        return str(input())
    
    def tournament_select(self, tournament):
        print('Tournoi:' + tournament['name'])
        print('1) Continuer le tournoi')
        print('2) Ajouter un nouveau joueur')
        print('3) Retour')
        return str(input())

    def score_select(self, pair):
        print('Sélectionner le résultat du match:')
        print('1)' + ' ' + pair[0]['last_name'] + ' ' + pair[0]['first_name'])
        print('2)' + ' ' + pair[1]['last_name'] + ' ' + pair[1]['first_name'])
        print('3) Égalité')

        return str(input())