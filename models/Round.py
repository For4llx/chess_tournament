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
