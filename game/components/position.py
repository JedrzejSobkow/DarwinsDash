from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float
    last_x: float = None
    last_y: float = None
    
    def __post_init__(self):
        self.last_x = self.x
        self.last_y = self.y