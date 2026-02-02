import pygame
from game.io.input_provider import InputProvider
from game.io.input_state import InputState
class KeyboardInputProvider(InputProvider):
    def __init__(self):
        self._previous_jump = False
        
    def get_input_state(self) -> InputState:
        keys = pygame.key.get_pressed()
        
        move_left = keys[pygame.K_a]
        move_right = keys[pygame.K_d]
        crouch = keys[pygame.K_s]
        
        jump_now = keys[pygame.K_SPACE]
        jump = jump_now and not self._previous_jump
        
        self._previous_jump = jump_now
        
        return InputState(
            move_left=move_left,
            move_right=move_right,
            crouch=crouch,
            jump=jump,
        )
        
    def reset(self) -> None:
        self._previous_jump = False