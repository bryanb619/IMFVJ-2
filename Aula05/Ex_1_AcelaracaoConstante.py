import pygame
from pygame.math import Vector2
import numpy as np




a = 20
velocity = 2

pos = Vector2(0,200)


""" P = P0 + V0*t + (1/2)*a*t^2
"""


def main():
    global pos, velocity
    
    clock = pygame.time.Clock()
    
    pygame.init()

    # screen size variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400

    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    run = True



    # Game loop
    while run:
        
        # initialize clock. used later in the loop.
        delta_time = clock.tick(60)    
        time_step = delta_time/1000
    
        # screen
        screen.fill((0,0,0))
            
    
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
                
        # update position
        velocity += a * time_step
        
        # use new equation to update position
        pos[0] += velocity * time_step
        
        
        # draw circle
        pygame.draw.circle(screen, (255,0,0), (pos), 10)
        
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()