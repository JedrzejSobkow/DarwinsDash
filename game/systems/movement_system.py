from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.velocity import Velocity
from game.components.action import Action
from game.components.jump_state import JumpState
from game.core.constants import PLAYER_MOVE_SPEED, PLAYER_CROUCH_SPEED


class MovementSystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Action, Velocity, JumpState)
        for entity in entities:
            actual_velocity = world.get_component(entity, Velocity)
            action =  world.get_component(entity, Action)
            j_state = world.get_component(entity, JumpState)
            new_vel_x = 0
            if action.move_left:
                new_vel_x -= 1
            if action.move_right:
                new_vel_x += 1
                
            if action.crouch and j_state.on_ground:
                actual_velocity.vx = new_vel_x * PLAYER_CROUCH_SPEED
            else:
                actual_velocity.vx = new_vel_x * PLAYER_MOVE_SPEED