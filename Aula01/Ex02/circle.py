import pygame
#from pygame.locals import *
pos_x = 100

def main():
    global pos_x
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
        
        if pos_x < SCREEN_WIDTH:
            pos_x += 0.05

    
        pygame.draw.circle(screen, (255,0,0), (pos_x,100), 100)

        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()