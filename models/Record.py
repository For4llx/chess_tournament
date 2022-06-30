import os
from dataclasses import dataclass, field
from tinydb import TinyDB, Query

os.makedirs(os.path.dirname('data/player.json'), exist_ok=True)
player_database = TinyDB('data/player.json')

@dataclass
class Record:
    tournament_id: int
    points: int
    opponents: list