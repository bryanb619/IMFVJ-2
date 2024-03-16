import pygame
import numpy as np


pos = [100, 100]
target = [600, 100]

velocity = 1

slowRadius = 300

_maxVelocity = 1.5


def main():
    global pos, target, velocity, slowRadius, _maxVelocity
    
    pygame.init()

    # screen size variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400

    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True

    # Game loop
    while run:
        
        # screen
        screen.fill((0,0,0))
        
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
        # when pos x is < target x position continue incrementing
        if(pos[0] < target[0]):
            # add 0.1 
            pos[0] += 0.1
            
            
        # Target circle
        pygame.draw.circle(screen, (0,255,0), (target), 12)
            
        # Moving circle
        pygame.draw.circle(screen, (255,0,0), (pos), 10)
        
        # updates screen   
        pygame.display.update()
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()