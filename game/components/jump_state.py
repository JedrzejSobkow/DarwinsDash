from dataclasses import dataclass

@dataclass
class JumpState:
    on_ground: bool = True
    jumps_left: int = 2
    max_jumps: int = 2
