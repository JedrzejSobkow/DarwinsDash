from game.core.world import World
# from game.render.pygame_renderer import Renderer
from game.systems.movement_system import MovementSystem
from game.components.player_tag import PlayerTag
from game.components.position import Position
from game.components.velocity import Velocity


def main():
    world = World()
    movement_system = MovementSystem()
    world.add_system(movement_system)
    # renderer = Renderer(world)

    player = world.create_entity()
    world.add_component(player, PlayerTag)    
    world.add_component(player, Position(x = 0, y = 0))    
    world.add_component(player, Velocity(vx = 100, vy = 0))    

    # running = True
    for i in range(5):
        world.update(dt = 0.1)
        pos = world.get_component(player, Position)
        print(f"Frame: Player position = ({pos.x}, {pos.y})")

        # renderer.draw()

if __name__ == "__main__":
    main()