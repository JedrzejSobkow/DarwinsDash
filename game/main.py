import pygame
from game.core.world import World
from game.render.pygame_renderer import PygameRenderer
from game.systems.input_system import InputSystem
from game.systems.jump_system import JumpSystem
from game.systems.movement_system import MovementSystem
from game.systems.gravity_system import GravitySystem
from game.systems.collision_system import CollisionSystem
from game.systems.physics_system import PhysicsSystem

from game.components.player_tag import PlayerTag
from game.components.position import Position
from game.components.velocity import Velocity
from game.components.action import Action
from game.components.jump_state import JumpState
from game.components.renderable import Renderable

from game.io.input_provider import InputProvider
from game.io.keyboard_input import KeyboardInputProvider

from game.core.constants import (
    FLOOR_HEIGHT, 
    SCREEN_HEIGHT, 
    SCREEN_WIDTH,
    PLAYER_COLOR
)


def main():
    world = World()
    
    input_system = InputSystem()
    jump_system = JumpSystem()
    movement_system = MovementSystem()
    gravity_system = GravitySystem()
    collision_system = CollisionSystem()
    physics_system = PhysicsSystem()

    world.add_system(input_system)
    world.add_system(jump_system)
    world.add_system(movement_system)
    world.add_system(collision_system)
    world.add_system(gravity_system)
    world.add_system(physics_system)


    
    # renderer = Renderer(world)

    player = world.create_entity()
    world.add_component(player, PlayerTag())    
    world.add_component(player, Action())
    world.add_component(player, Position(x = 0, y = FLOOR_HEIGHT))    
    world.add_component(player, Velocity(vx = 0, vy = 0)) 
    world.add_component(player, JumpState(on_ground = True, jumps_left = 2, max_jumps = 2)) 
    world.add_component(player, Renderable(width = 20, height = 20, color = PLAYER_COLOR))
    
    input_provider: InputProvider = KeyboardInputProvider()
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Darwin's Dash")
    clock = pygame.time.Clock()
    
    renderer = PygameRenderer(world, screen)
      
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        input_state = input_provider.get_input_state()
        world.update(dt, input_state)
        
        pos = world.get_component(player, Position)
        vel = world.get_component(player, Velocity)
        print(f"Velocity: {vel}")
        print(f"Frame: Player position = ({pos.x}, {pos.y})")

        renderer.draw()

if __name__ == "__main__":
    main()