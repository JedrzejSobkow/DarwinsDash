from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.jump_state import JumpState
from game.components.velocity import Velocity
from game.components.action import Action
from game.core.constants import JUMP_INITIAL_SPEED


class JumpSystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Velocity, JumpState, Action)
        for entity in entities:
            j_state = world.get_component(entity, JumpState)
            vel = world.get_component(entity, Velocity)
            action = world.get_component(entity, Action)

            j_state.on_ground = False

            if action.jump and j_state.jumps_left > 0:
                j_state.on_ground = False
                vel.vy = JUMP_INITIAL_SPEED
                j_state.jumps_left -= 1
            