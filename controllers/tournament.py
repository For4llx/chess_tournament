from models.Tournament import Tournament
from views.tournament import tournament_form
from models.Player import Player
from views.player import *
from tinydb import TinyDB, Query

tournament_database = TinyDB('data/tournament.json')
player_database = TinyDB('data/player.json')

class TournamentController:
    def create_tournament(self):
        tournament = self.view.tournament_form()
        tournament = Tournament(
            tournament['name'],
            tournament['place'],
            tournament['time_control'],
            tournament['description'],
            tournament['rounds_number'])
        tournament.save()

    def update_one_tournament_players(self, tournament_id, player_id):
        players = tournament_database.get(doc_id=tournament_id)['players']
        players.append({'player_id': player_id})
        player_database.update({'players': players}, doc_ids=[tournament_id])

    def get_all_tournaments(self):
        return tournament_database.all()

    def get_one_tournament(self, tournamend_id):
        return tournament_database.get(doc_id=tournamend_id)

    def update_one_tournament_players(player_id, tournament_id):
        tournament.save_player(tournament_id, player_id)

    def get_all_players_in_one_tournament(self, tournament_id):
        players = []

        player_ids = tournament_database.get(doc_id=tournament_id)['players']

        for player_id in player_ids:
            id = player_id['player_id']
            players.append(player_database.get(doc_id=id))
        
        return players

"""
def update_one_tournament_players(tournament_id):
    player = player_form()
    player = Player(
        player['last_name'],
        player['first_name'],
        player['ranking'],
        player['birth_date'],
        player['sex'])
    player.save(tournament_id)
"""