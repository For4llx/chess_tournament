from dataclasses import dataclass, field
from datetime import date

@dataclass
class Tournament:
    name: str
    place: str = ''
    time: int = 0
    description: str =''
    rounds: list = field(default_factory=list)
    players: list = field(default_factory=list)
    date: str = date.today().strftime("%d/%m/%Y")
    rounds_number: int = 4
