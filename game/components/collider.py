from dataclasses import dataclass

@dataclass
class Collider:
    width: int
    height: int
    solid: bool = True
