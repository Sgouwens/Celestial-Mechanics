import pygame
import matplotlib.pyplot as plt
import numpy as np

from celestial import Celestial, System
from initial_positions import initial_conditions

G = 6.6743*1e-11
step_size = 720

body_names, body_positions, body_velocities, body_masses = initial_conditions(type='Solar System')
#body_names, body_positions, body_velocities, body_masses = initial_conditions(type='Random Solar System')

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
 
zoom_scalar = 1e9
earth_at_center = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                step_size *= 1.5  # Increase stepsize
                print('Stepsize changed to: ', step_size)
            if event.key == pygame.K_DOWN:
                step_size /= 1.5  # Decrease stepsize
                print('Stepsize changed to: ', step_size)
            if event.key == pygame.K_RIGHT:
                G *= 1.5  # Increase gravitational constant by 5%
                print('Grav. const. multiplied by: ', round(G/(6.6743*1e-11),1))
            if event.key == pygame.K_LEFT:
                G /= 1.5  # Decrease gravitational constant by 5%
                print('Grav. const. multiplied by: ', round(G/(6.6743*1e-11),1))
            if event.key == pygame.K_q:
                print("Zoom out")
                screen.fill(background_color)
                zoom_scalar *= 1.2  # Increase gravitational constant by 5%
            if event.key == pygame.K_w:
                print("Zoom in")
                screen.fill(background_color)
                zoom_scalar /= 1.2  # Decrease gravitational constant by 5%
            if event.key == pygame.K_a:
                print("'Sun centered' view")
                screen.fill(background_color)
                earth_at_center = 0  # Increase gravitational constant by 5%
            if event.key == pygame.K_s:
                print("Earth centered view")
                screen.fill(background_color)
                earth_at_center = 1  # Decrease gravitational constant by 5%
                
    # Compute next step and handle collision
    system.system_euler_backward(stepsize=step_size)
    
    pos_earth = system.objects[3].position
    pos_sun = np.vstack((pos_sun, system.objects[0].position))
    
    idx_collided = system.remove_collided_bodies()
    for idx in reversed(idx_collided):
       system.objects.pop(idx)
     
    # Draw the balls
    for body in system.objects:
        pygame.draw.circle(screen, 
                           body.color, 
                           ((body.position[0]-earth_at_center*pos_earth[0])/zoom_scalar+300, 
                            (body.position[1]-earth_at_center*pos_earth[1])/zoom_scalar+300), 
                           radius)
        
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()


  
