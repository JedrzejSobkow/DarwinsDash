import pygame
from game.render.renderer import Renderer

from game.components.renderable import Renderable
from game.components.position import Position

from game.core.world import World
from game.core.constants import (
    BACKGROUND_COLOR, 
    FLOOR_COLOR,
    FLOOR_HEIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)   

class PygameRenderer(Renderer):
    
    def __init__(self, world: World, screen: pygame.Surface) -> None:
        super().__init__(world)
        self.screen: pygame.Surface = screen
        
    def draw(self):
        # Background
        self.screen.fill(BACKGROUND_COLOR)
        
        rect = pygame.Rect(0, 0, 0, 0)
        # Floor
        pygame.draw.rect(
            surface = self.screen,
            color = FLOOR_COLOR,
            rect = pygame.Rect(0, SCREEN_HEIGHT - FLOOR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        
        entities = self.world.query(Position, Renderable)
        for entity in entities:
            render = self.world.get_component(entity, Renderable)
            pos = self.world.get_component(entity, Position)
            
            screen_x = int(pos.x)
            screen_y = int(SCREEN_HEIGHT - pos.y - render.height)
            
            pygame.draw.rect(
                surface = self.screen,
                color = render.color,
                
                rect = pygame.Rect(screen_x, screen_y, render.width, render.height)
            )
        
        pygame.display.flip()