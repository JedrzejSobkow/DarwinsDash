from abc import ABC, abstractmethod
from game.io.input_state import InputState

class InputProvider(ABC):
    
    @abstractmethod
    def get_input_state(self) -> InputState:
        """
        Returns an InputState snapshot representing
        player intent for the current frame.
        """
        pass

    def reset(self) -> None:
        """
        Resets internal provider state (optional).
        Called when starting a new run / episode.
        """
        pass