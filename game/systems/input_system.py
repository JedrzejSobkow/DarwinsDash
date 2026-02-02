from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.action import Action
from game.components.player_tag import PlayerTag


class InputSystem(System):
            
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        entities_with_action = world.query(Action, PlayerTag)
        for entity_id in entities_with_action:
            action = world.get_component(entity_id, Action)
            
            action.move_left = input_state.move_left
            action.move_right = input_state.move_right
            action.jump = input_state.jump
            action.crouch = input_state.crouch