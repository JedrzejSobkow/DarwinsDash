from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.player_tag import PlayerTag
from game.components.position import Position
from game.components.velocity import Velocity
from game.components.action import Action
from game.core.constants import PLAYER_MOVE_SPEED, PLAYER_CROUCH_SPEED


class MovementSystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Action, Position, Velocity)
        for entity in entities:
            
            actual_position = world.get_component(entity, Position)
            actual_velocity = world.get_component(entity, Velocity)
            
            actual_position.x += actual_velocity.vx * dt 
            actual_position.y += actual_velocity.vy * dt
        
            action =  world.get_component(entity, Action)
            new_vel_x = 0
            if action.move_left:
                new_vel_x -= 1
            if action.move_right:
                new_vel_x += 1
                
            actual_velocity.vx = new_vel_x * (PLAYER_CROUCH_SPEED if action.crouch else PLAYER_MOVE_SPEED)