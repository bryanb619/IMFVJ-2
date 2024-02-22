import pygame
#from pygame.locals import *


RED = (255,0,0)

GREEN = (0,255,0)


def main():
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
        
        
        pygame.draw.rect(screen, GREEN, (50,20,120,100))
        
        pygame.draw.rect(screen, RED, (200,20,120,100))
        
        
        
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()