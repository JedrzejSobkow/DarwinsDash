from abc import ABC, abstractmethod
from game.io.input_state import InputState

class System(ABC):
    @abstractmethod
    def update(self, world: "World", dt: float, input_state: InputState = None) -> None:
        """
        Updates the system for a single frame.

        :param world: The current game world (all entities and components)
        :param dt: Delta time in seconds since the last update
        :param input_state: Player, AI, or replay input (optional)
        """
        pass