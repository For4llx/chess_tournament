import os 
from dataclasses import dataclass, field
from datetime import date, datetime
from tinydb import TinyDB

os.makedirs(os.path.dirname('data/tournament.json'), exist_ok=True)
tournament_database = TinyDB('data/tournament.json')

@dataclass
class Round:
    name: str
    matches: list
    start_time: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    end_time: str = ''

    def save(round, tournament_id):
        rounds = tournament_database.get(doc_id=tournament_id)['rounds']
        rounds.append(round.__dict__)
        tournament_database.update({'rounds': rounds}, doc_ids=[tournament_id])