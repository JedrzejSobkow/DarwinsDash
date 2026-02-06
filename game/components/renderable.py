from dataclasses import dataclass

@dataclass
class Renderable:
    width: int
    height: int
    color: tuple[int, int, int]