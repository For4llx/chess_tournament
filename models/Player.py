from dataclasses import dataclass

@dataclass
class Player:
    last_name: str
    first_name: str
    ranking: int
    birth_date: str = ''
    sex: str = ''
