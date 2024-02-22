import pygame
from pygame.locals import *


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

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
        
        # connect lines
        pygame.draw.line(screen, RED, (400, 200), (600, 200), 5)
        pygame.draw.line(screen, BLUE, (400, 200), (500, 100), 7)
        pygame.draw.line(screen, GREEN, (500, 100), (600, 200), 3)
        
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()