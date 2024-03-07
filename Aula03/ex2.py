import pygame
import random


randomValue = 0 
pos_x = 50
pos_x_2 = 50
pos_x_3 = 50

pos_y = 100
pos_y_2 = 150
pos_y_3 = 200



def main():
    global randomValue
    global pos_x, pos_x_2, pos_x_3
    global pos_y, pos_y_2, pos_y_3

    
    pygame.init()

    # screen size variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400

    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True

    # Game loop
    while run:
        

        screen.fill((0,0,0))
        
        # Loop for handling game exit
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    
                    
                    randomValue = random.randint(1,6)
                    print(randomValue)
                    
                    if (randomValue ==1):
                        
                        print("Random direction")
                        
                        pos_y += random.randint(-10,10)
                        pos_y_2 +=  random.randint(-10,10)
                        pos_y_3 +=  random.randint(-10,10)
                        
                    
                    pos_x += 10 * random.randint(1,6)
                    pos_x_2 += 10 * random.randint(1,6)
                    pos_x_3 += 10 * random.randint(1,6)
        
        
        
        if(pos_x > 700):
            font = pygame.font.SysFont(None, 30)
            img = font.render("Player 1 wins", True, (255,255,255))
            screen.blit(img, (20, 20))
            print("Player 1 wins")
            
        if (pos_x_2 > 700):
            font = pygame.font.SysFont(None, 30)
            img = font.render("Player 2 wins", True, (255,255,255))
            screen.blit(img, (20, 20))
            print("Player 2 wins")
            return
            
        if (pos_x_3 > 700):
            font = pygame.font.SysFont(None, 30)
            img = font.render("Player 3 wins", True, (255,255,255))
            screen.blit(img, (20, 20))
            print("Player 3 wins")
      

    
        pygame.draw.circle(screen, (255,0,0), (pos_x,pos_y), 10)
        
        pygame.draw.circle(screen, (0,255,0), (pos_x_2,pos_y_2), 10)
        
        pygame.draw.circle(screen, (255,255,0), (pos_x_3,pos_y_3), 10)
                
                
        

            
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()


    

    
    




       