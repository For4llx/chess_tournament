from tinydb import TinyDB, Query
from helpers import get_rank, generate_pairs

from models.Player import Player
from models.Tournament import Tournament
from models.Round import Round
from models.Record import Record

from controllers.tournament import TournamentController
from controllers.player import PlayerController

tournament_database = TinyDB('data/tournament.json')
player_database = TinyDB('data/player.json')


class MenuController:
    def __init__(self, view):
        self.view = view

    def tournament_menu(self):
        all_tournaments = TournamentController.get_all_tournaments(self)

        while True:
            tournament_id = self.view.tournaments_select(all_tournaments)
            tournament_id = int(tournament_id)
            tournament = TournamentController.get_one_tournament(self, tournament_id)
            option = self.view.tournament_select(tournament)

            if option == '1': # start tournament
                players = TournamentController.get_all_players_in_one_tournament(self, tournament_id)
                round_counter = 1
                while round_counter <= tournament['rounds_number']:
                    matches = []
                    pairs = generate_pairs(players, tournament_id, round_counter)
                    for pair in pairs:
                        option = self.view.score_select(pair)
                        if option == '1':
                            match = ([{'player_id': pair[0].doc_id}, {'score': 1}] ,[{'player_id': pair[1].doc_id}, {'score': 0}])
                            matches.append(match)

                            player_1 = PlayerController.get_one_player(pair[0].doc_id)
                            player_2 = PlayerController.get_one_player(pair[1].doc_id)
                            
                            record_1 = Record(tournament_id, 1, [{'opponent_id': player_2.doc_id}])
                            record_2 = Record(tournament_id, 0, [{'opponent_id': player_1.doc_id}])
                            player_database.update({'record': record_1.__dict__}, doc_ids=[player_1.doc_id])
                            player_database.update({'record': record_2.__dict__}, doc_ids=[player_2.doc_id])
                            
                        elif option == '2':
                            match = ([{'player_id': pair[0].doc_id}, {'score': 0}] ,[{'player_id': pair[1].doc_id}, {'score': 1}])
                            matches.append(match)

                            player_1 = PlayerController.get_one_player(pair[0].doc_id)
                            player_2 = PlayerController.get_one_player(pair[1].doc_id)
                            
                            record_1 = Record(tournament_id, 0, [{'opponent_id': player_2.doc_id}])
                            record_2 = Record(tournament_id, 1, [{'opponent_id': player_1.doc_id}])
                            player_database.update({'record': record_1.__dict__}, doc_ids=[player_1.doc_id])
                            player_database.update({'record': record_2.__dict__}, doc_ids=[player_2.doc_id])
                            
                        elif option == '3':
                            match = ([{'player_id': pair[0].doc_id}, {'score': 0.5}] ,[{'player_id': pair[1].doc_id}, {'score': 0.5}])
                            matches.append(match)

                            player_1 = PlayerController.get_one_player(pair[0].doc_id)
                            player_2 = PlayerController.get_one_player(pair[1].doc_id)
                            
                            record_1 = Record(tournament_id, 0.5, [{'opponent_id': player_2.doc_id}])
                            record_2 = Record(tournament_id, 0.5, [{'opponent_id': player_1.doc_id}])
                            player_database.update({'record': record_1.__dict__}, doc_ids=[player_1.doc_id])
                            player_database.update({'record': record_2.__dict__}, doc_ids=[player_2.doc_id])
                            
                      

                    round = Round('Round 1', matches)
                    tournament_database.update({'rounds': [round.__dict__]}, doc_ids=[tournament_id])
                    round_counter = round_counter + 1

            elif option == '2': # add player
                all_players = self.get_all_players()

                while True:
                    player_id = self.view.players_select(all_players)
                    self.update_one_tournament_players(tournament_id, player_id)

    def main_menu(self, view):
        while True:
            option = self.view.main_menu_select()
            if option == '1':
                TournamentController.create_tournament(self)
            elif option == '2':
                PlayerController.create_player(self)
            elif option == '3':
                self.tournament_menu()
            elif option == '4':
                break
"""
    def create_round(self, tournament_id):
        tournament_id = int(tournament_id)
        players = []
        matches = []
        ids = tournament_database.get(doc_id=tournament_id)['players']

        for player_id in ids:
            players.append(player_database.get(doc_id=player_id))
        
        players.sort(key=get_rank)
        players_number = len(players)
        middle_index = players_number // 2
        upper_class_players = players[:middle_index]
        lower_class_players = players[middle_index:]

        for i in range(4):
            match = [[upper_class_players[i].doc_id, {'score': 0}] ,[lower_class_players[i].doc_id, {'score': 0}]]
            match = tuple(match)
            matches.append(match)
        round = Round('Round 1', matches)
        tournament_database.update({'rounds': [round.__dict__]}, doc_ids=[tournament_id])
"""