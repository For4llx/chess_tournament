import os
from dataclasses import dataclass
from tinydb import TinyDB, Query

os.makedirs(os.path.dirname('data/tournament.json'), exist_ok=True)
tournament_database = TinyDB('data/tournament.json')

@dataclass
class Player:
    last_name: str
    first_name: str
    ranking: int
    birth_date: str = ''
    sex: str = ''

    def save(player, tournament_id):
        players = tournament_database.get(doc_id=tournament_id)['players']
        players.append(player.__dict__)
        tournament_database.update({'players': players}, doc_ids=[tournament_id])