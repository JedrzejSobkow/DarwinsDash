from dataclasses import dataclass

@dataclass
class InputState:
    left: bool = False
    right: bool = False
    jump: bool = False
    crouch: bool = False