from tinydb import TinyDB, Query

tournament_database = TinyDB('data/tournament.json')
player_database = TinyDB('data/player.json')


class Controller:
    def __init__(self, view):
        self.view = view

    def get_all_players(self):
        return player_database.all()

    def update_one_tournament_players(self, tournament_id, player_id):
        tournament_id = int(tournament_id)
        player_id = int(player_id)
        players = tournament_database.get(doc_id=tournament_id)['players']
        players.append(player_id)
        tournament_database.update({'players': players}, doc_ids=[tournament_id])

    def create_tournament(self):
        tournament = self.view.tournament_form()
        tournament = Tournament(
            tournament['name'],
            tournament['place'],
            tournament['time_control'],
            tournament['description'],
            tournament['rounds_number'])
        tournament.save()

    def get_all_tournaments(self):
        return tournament_database.all()

    def create_player(self):
        player = self.view.player_form()
        player = Player(
            player['last_name'],
            player['first_name'],
            player['ranking'],
            player['birth_date'],
            player['sex'])
        player.save()

    def get_one_tournament(self, id):
        return tournament_database.get(doc_id=id)
    
    def get_one_player(self, player_id):
        return player_database.get(doc_id=player_id)

    def tournament_menu(self):
        all_tournaments = self.get_all_tournaments()

        while True:
            tournament_id = self.view.tournaments_select(all_tournaments)
            tournament = self.get_one_tournament(tournament_id)
            option = self.view.tournament_select(tournament)

            if option == '1':
                pass
            elif option == '2':
                all_players = self.get_all_players()

                while True:
                    player_id = self.view.players_select(all_players)
                    self.update_one_tournament_players(tournament_id, player_id)

    def main_menu(self, view):
        while True:
            option = self.view.main_menu_select()
            if option == '1':
                self.create_tournament()
            elif option == '2':
                self.create_player()
            elif option == '3':
                self.tournament_menu()
            elif option == '4':
                break