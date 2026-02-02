from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.player_tag import PlayerTag
from game.components.position import Position
from game.components.velocity import Velocity


class MovementSystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Position, Velocity)
        for entity in entities:
            actual_position = world.get_component(entity, Position)
            actual_velocity = world.get_component(entity, Velocity)
            
            actual_position.x += actual_velocity.vx * dt 
            actual_position.y += actual_velocity.vy * dt
        
        