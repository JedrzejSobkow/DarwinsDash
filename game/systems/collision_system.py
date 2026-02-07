from dataclasses import dataclass

from game.core.system import System
from game.core.world import World
from game.io.input_state import InputState
from game.components.jump_state import JumpState
from game.components.position import Position
from game.components.velocity import Velocity
from game.components.collider import Collider
from game.core.constants import Y_VELOCITY_SETTLING_EPSILON, RESTITUTION_COEFFICIENT


class CollisionSystem(System):
    @dataclass
    class CollisionState:
        left_edge_collision: bool = False
        top_edge_collision: bool = False
        right_edge_collision: bool = False
        bottom_edge_collision: bool = False
        containment_collision: bool = False

        
    def update(self, world: World, dt: float, input_state: InputState = None) -> None:
        
        non_static_colliders = world.query(Position, Velocity, Collider)
        colliders = world.query(Position, Collider)
        
        for subject in non_static_colliders:
            sub_pos = world.get_component(subject, Position)
            sub_vel = world.get_component(subject, Velocity)
            sub_col = world.get_component(subject, Collider)

            for object in colliders:
                if object != subject:
                    obj_pos = world.get_component(object, Position)
                    obj_col = world.get_component(object, Collider)
                    
                    collision_state = self.detect_collisions(
                        subject = (sub_col, sub_pos), 
                        object = (obj_col, obj_pos)
                    )
                    print(collision_state)
                    
                    if world.has_component(subject, JumpState) and world.get_component(subject, JumpState).jumps_left < 2:
                        pass
                    
                    if collision_state.left_edge_collision or collision_state.right_edge_collision:
                        sub_pos.x = sub_pos.last_x
                        sub_vel.vx = - sub_vel.vx * RESTITUTION_COEFFICIENT
                    if collision_state.top_edge_collision:
                        sub_pos.y = sub_pos.last_y
                        sub_vel.vy = - sub_vel.vy * RESTITUTION_COEFFICIENT
                    if collision_state.bottom_edge_collision:
                        
                        # jump
                        if world.has_component(subject, JumpState) and not world.get_component(subject, JumpState).on_ground and sub_vel.vy > Y_VELOCITY_SETTLING_EPSILON:
                            pass
                        # stop
                        else:
                            sub_vel.vy = 0
                            sub_pos.y = obj_pos.y + obj_col.height
                            if world.has_component(subject, JumpState) and not world.get_component(subject, JumpState).on_ground:
                                j_state = world.get_component(subject, JumpState)
                                j_state.on_ground = True
                                j_state.jumps_left = j_state.max_jumps
                        # TODO bounce [maybe in another universe]
                        
                    
                    
    def detect_collisions(self, subject: tuple[Collider, Position], object: tuple[Collider, Position]) -> CollisionState:
        subject_left_edge = subject[1].x
        subject_right_edge = subject[1].x + subject[0].width
        subject_top_edge = subject[1].y + subject[0].height
        subject_bottom_edge = subject[1].y
        
        object_left_edge = object[1].x
        object_right_edge = object[1].x + object[0].width
        object_top_edge = object[1].y  + object[0].height
        object_bottom_edge = object[1].y
        
        # print(f'SUBJECT_LEFT = {subject_left_edge}')
        # print(f'SUBJECT_RIGHT = {subject_right_edge}')
        # print(f'OBJECT_LEFT = {object_left_edge}')
        # print(f'OBJECT_RIGHT = {object_right_edge}')
        # print(f'COLLIDER = {subject[0]}')
        
        vertical_overlap = subject_top_edge > object_bottom_edge and object_top_edge > subject_bottom_edge
        horizontal_overlap = subject_left_edge < object_right_edge and object_left_edge < subject_right_edge
        
        print(f'VERTICAL_OVERLAP = {vertical_overlap}')
        print(f'HORIZONTAL_OVERLAP = {horizontal_overlap}')
        
        collision_state = self.CollisionState()
        
        collision_counter = 0
        
        # left collision
        if (subject_left_edge < object_right_edge < subject_right_edge) and vertical_overlap:
            collision_state.left_edge_collision = True
            collision_counter += 1
        # right collision
        if (subject_left_edge < object_left_edge < subject_right_edge) and vertical_overlap:
            collision_state.right_edge_collision = True
            collision_counter += 1
        # top collision
        if (subject_bottom_edge <= object_bottom_edge <= subject_top_edge) and horizontal_overlap:
            collision_state.top_edge_collision = True
            collision_counter += 1
        # bottom collision
        if (subject_bottom_edge <= object_top_edge <= subject_top_edge) and horizontal_overlap:
            collision_state.bottom_edge_collision = True
            collision_counter += 1
        # containment collision
        if vertical_overlap and horizontal_overlap and collision_counter == 0:
            collision_state.containment_collision = True
            
        return collision_state
        