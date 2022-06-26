import os
from dataclasses import dataclass, field
from datetime import date
from tinydb import TinyDB

os.makedirs(os.path.dirname('data/tournament.json'), exist_ok=True)
tournament_database = TinyDB('data/tournament.json')

@dataclass
class Tournament:
    name: str
    place: str
    time_control: str
    description: str
    rounds_number: int = 4
    date: str = date.today().strftime("%d/%m/%Y")
    rounds: list = field(default_factory=list)
    players: list = field(default_factory=list)

    def save(tournament):
        tournament_database.insert(tournament.__dict__)
    
    def save_round(round, tournament_id):
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds.append(round.__dict__)
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])

    def save_player(player, tournament_id):
        players = tournament_database.get(doc_id=tournament_id)['players']
        players.append(player.__dict__)
        tournament_database.update({'players': players}, doc_ids=[tournament_id])