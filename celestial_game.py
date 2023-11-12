import pygame
import matplotlib.pyplot as plt
import numpy as np

from celestial import Celestial, System
from initial_positions import initial_conditions

G = 6.6743*1e-11
step_size = 360

body_names, body_positions, body_velocities, body_masses = initial_conditions(type = 'Multiple suns')

system = System(body_names, body_positions, body_velocities, body_masses)

pos_sun = np.array(system.objects[0].position)

# Initialize Pygame
pygame.init()

# Constants
width, height = 600, 600
background_color = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Celestial mechanics")

# Ball properties
radius = 3
center_x, center_y = 300,300

# Main game loop
running = True
clock = pygame.time.Clock()
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                step_size *= 1.5  # Increase stepsize
            if event.key == pygame.K_DOWN:
                step_size /= 1.5  # Decrease stepsize
            if event.key == pygame.K_RIGHT:
                system.objects[4].velocity *= 1.1  # Speed up the USS enterprise (10%)
                print(system.objects[3].mass)
            if event.key == pygame.K_LEFT:
                system.objects[4].velocity /= 1.1  # Speed up the USS enterprise (10%)
                print(system.objects[3].mass)

    screen.fill(background_color)

    # Compute next step and handle collision
    system.system_euler_backward()
    
    idx_collided = system.remove_collided_bodies()
    for idx in reversed(idx_collided):
       system.objects.pop(idx)
           
    pos_earth = system.objects[0].position
    
    pos_sun = np.vstack((pos_sun, system.objects[0].position))
    
    # Draw the balls
    earth_at_center = 0
    for body in system.objects:
        pygame.draw.circle(screen, 
                           body.color, 
                           ((body.position[0]-earth_at_center*pos_earth[0])/1e9+300, 
                            (body.position[1]-earth_at_center*pos_earth[1])/1e9+300), 
                           radius)
        
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()


  
