import pygame
import random


randomValue = 0 
pos_x = 400


def main():
    global randomValue
    global pos_x
    
    pygame.init()

    # screen size variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400

    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True

    # Game loop
    while run:
        
        #number = input("Press Enter to roll the dice")
        """
        if(pos_x > 800):
            pos_x = 400
            
        elif(pos_x < 0):
            pos_x = 400
        """
        screen.fill((0,0,0))
        
        # Loop for handling game exit
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    
                    randomValue = random.randint(1,6)
                    #print(randomValue)
                    
                    pos_x += 1 * randomValue
                
                
                        
                    
                    
               
      
        # screen
        pygame.draw.circle(screen, (255,0,0), (pos_x,300), 50)
            
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()