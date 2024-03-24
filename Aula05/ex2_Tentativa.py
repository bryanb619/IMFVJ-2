import pygame
from pygame.math import Vector2
import time


gravity = 9.8

velocity = 2
a = 20

lateral_speed = 0.5

pos = Vector2(400,173)

is_falling = False

def main():

    global pos, gravity, velocity, lateral_speed, is_falling
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
                
        
        # check if end of line
        
        # update position
        
        if(is_falling == False):

            velocity += a * time_step
        
            # use new equation to update position
            pos[0] += velocity * time_step
            
            if pos[0] > 600:
                is_falling = True
                #break
 
        
        
        
        # apply gravity
        if is_falling == True:
                
    
            # update position
            gravity  += gravity * time_step
            
            # use new equation to update position
            pos[1] += gravity * time_step
            
            time.sleep(0.1)
            pos[0] -= lateral_speed
            
 
        # draw circle
        pygame.draw.circle(screen, (255,0,0), (pos), 25)
        
        pygame.draw.line(screen, (0,255,0), (300, 200), (580, 200), 5)

        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()