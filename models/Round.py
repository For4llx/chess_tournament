from dataclasses import dataclass, field
from datetime import date, datetime

@dataclass
class Round:
    name: str
    matches: list
    start_time: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    end_time: str = ''
