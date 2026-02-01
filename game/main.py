from game.core.world import World
from game.render.pygame_renderer import Renderer

def main():
    world = World()
    renderer = Renderer(world)

    running = True
    while running:
        world.update()
        renderer.draw()

if __name__ == "__main__":
    main()