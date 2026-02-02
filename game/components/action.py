from dataclasses import dataclass

@dataclass
class Action:
    move_left: bool = False
    move_right: bool = False
    crouch: bool = False
    jump: bool = False