import pygame
#from pygame.locals import *


circleRadius1 = 70
circleRadius2 = 50


def main():
    global circleRadius1
    global circleRadius2
    pygame.init()

    # screen size variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    


    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                  
        # screen
        screen.fill((30,30,30))
        
        if circleRadius1 < 100:
            circleRadius1 += 0.02
            circleRadius2 += 0.02
        else:
            circleRadius1 = 70
            circleRadius2 = 50
    
            
        pygame.draw.circle(screen, (255,0,0), (150,100), circleRadius1)
        pygame.draw.circle(screen, (0,255,0), (150,100), circleRadius2)
  
        
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()