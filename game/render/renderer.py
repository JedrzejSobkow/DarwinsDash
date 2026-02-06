from abc import ABC, abstractmethod
from game.core.world import World

class Renderer(ABC):
    
    def __init__(self, world: World):
        self.world: World = world
        
    @abstractmethod
    def draw(self) -> None:
        """
        Render the current state of the world.
        Subclasses must implement this method.
        """
        pass