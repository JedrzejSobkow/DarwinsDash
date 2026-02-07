from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.velocity import Velocity
from game.components.position import Position
from game.core.constants import PLAYER_MOVE_SPEED, PLAYER_CROUCH_SPEED


class PhysicsSystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Position, Velocity)
        for entity in entities:
            vel = world.get_component(entity, Velocity)
            pos = world.get_component(entity, Position)
            
            pos.last_x = pos.x
            pos.last_y = pos.y
            
            pos.x += dt * vel.vx
            pos.y += dt * vel.vy