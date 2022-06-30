import os
from dataclasses import dataclass, field
from tinydb import TinyDB, Query

os.makedirs(os.path.dirname('data/player.json'), exist_ok=True)
player_database = TinyDB('data/player.json')

@dataclass
class Player:
    last_name: str
    first_name: str
    ranking: int
    birth_date: str = ''
    sex: str = ''
    record: list = field(default_factory=list)

    def save(player):
        player_database.insert(player.__dict__)
