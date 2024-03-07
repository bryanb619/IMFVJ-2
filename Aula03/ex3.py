import pygame
import random


randomVal_x = 0
randomVal_y = 0

def main():
    global randomVal_x, randomVal_y
    
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
                
            if event.type == pygame.KEYDOWN:
        
                if event.key == pygame.K_RETURN:
                    
                    randomVal_x = random.randrange(1,8)
                    randomVal_y = random.randrange(1,8)
                    
                    print(randomVal_x)
                    #drawLine(randomVal, randomVal)
                    pygame.draw.line(screen, (255,0,0), (randomVal_x, randomVal_y), width=1)
                    
                
       
            
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()

#def drawLine(x,y):
    