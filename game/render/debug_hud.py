import pygame
import uuid

from game.core.world import World
from game.components.position import Position
from game.components.velocity import Velocity
from game.components.jump_state import JumpState
from game.components.action import Action


class DebugHUD:
    def __init__(self, font_size: int = 18, color: tuple[int, int, int] = (255, 255, 255)):
        self.font: pygame.font.Font = pygame.font.Font(None, font_size)
        self.color: tuple[int, int, int] = color
        self.margin: int = 10
        self.line_height: int = font_size + 4

    def draw(self, screen: pygame.Surface, world: World, player_entity: uuid.UUID) -> None:

        lines = []

        # Position
        if world.has_component(player_entity, Position):
            pos = world.get_component(player_entity, Position)
            lines.append(f"Position x={pos.x:.0f}")
            lines.append(f"Position y={pos.y:.0f}")
        # Velocity 
        if world.has_component(player_entity, Velocity):
            vel = world.get_component(player_entity, Velocity)
            lines.append(f"Velocity x={vel.vx:.0f}")
            lines.append(f"Velocity y={vel.vy:.0f}")

        # Jump state 
        if world.has_component(player_entity, JumpState):
            js = world.get_component(player_entity, JumpState)
            lines.append(f"On ground: {js.on_ground}")
            lines.append(f"Jumps left: {js.jumps_left}/{js.max_jumps}")

        # Action (input)
        if world.has_component(player_entity, Action):
            action = world.get_component(player_entity, Action)
            lines.append(
                f"Action: L={action.move_left} R={action.move_right} "
                f"J={action.jump} C={action.crouch}"
            )



        for i, text in enumerate(lines):
            surface = self.font.render(text, True, self.color)
            screen.blit(
                surface,
                (self.margin, self.margin + i * self.line_height)
            )
