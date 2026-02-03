from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.jump_state import JumpState
from game.components.velocity import Velocity
from game.core.constants import GRAVITY, MAX_FALL_SPEED


class GravitySystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Velocity, JumpState)
        for entity in entities:
            j_state = world.get_component(entity, JumpState)
            vel = world.get_component(entity, Velocity)
            
            if not j_state.on_ground:
                vel.vy = max(vel.vy - GRAVITY * dt, -MAX_FALL_SPEED)