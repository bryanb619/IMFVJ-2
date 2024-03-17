import pygame
import random

# position of the line start
pos = [400,300]

BLUE = (0,0,255)

# screen size variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def main():
    global screen
    
    pygame.init()

    
    screen.fill((0,0,0))

    # Game loop
    while True:
        
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    print("detected")
                    # call new method
                    draw_line()
                
            
            # 4  Declare event to detect a key
            #if event.type == pygame.KEYDOWN:
                
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()


# Line logic
def draw_line():

    global pos
    
    # randomizar em +- 62% cada eixo
    random_x = random.randint(400, 462)
    random_y = random.randint(300, 362)
    
    pygame.draw.line(screen, (BLUE), (pos[0], pos[1]), (random_x, random_y), 1)
    
    # igualar nova posicao a posicao atual, posição de começo da linha
    pos[0] = random_x
    pos[1] = random_y
        
    
 
main()