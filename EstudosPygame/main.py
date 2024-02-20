import pygame

pygame.init()

# screen size variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True

# Game loop
while run:
    
    # Loop for handling game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
         
    # updates screen   
    pygame.display.update()
    
# Quit method is out of the loop since run = False   
pygame.quit()
    

