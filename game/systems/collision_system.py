from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.jump_state import JumpState
from game.components.position import Position
from game.components.velocity import Velocity
from game.components.action import Action
from game.core.constants import PLAYER_MOVE_SPEED, PLAYER_CROUCH_SPEED


class CollisionSystem(System):
        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        entities = world.query(Position, Velocity, JumpState)
        for entity in entities:
            pos = world.get_component(entity, Position)
            vel = world.get_component(entity, Velocity)
            j_state = world.get_component(entity, JumpState)
            
            j_state.on_ground = False
            if pos.y <= 0:
                pos.y = 0
                vel.vy = 0
                j_state.on_ground = True