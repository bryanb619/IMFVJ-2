import pygame
import random



# screen size variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


# position of the line at start
pos = [SCREEN_WIDTH /2, SCREEN_HEIGHT /2]

BLUE = (0,0,255)

# screen variable = do display mode and res size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# turn

i = 0


def main():
    global screen, i
    
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
                    i+=1
                    print(f" Turn ==> {i}")
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
    
    # randomizar em +- 6.2% cada eixo = 12.4% total 
    random_x = random.randint(500, 562)
    random_y = random.randint(400, 462)
    
    pygame.draw.line(screen, (BLUE), (pos[0], pos[1]), (random_x, random_y), 1)
    
    # igualar nova posicao a posicao atual, posição de começo da linha
    pos[0] = random_x
    pos[1] = random_y
        
    
 
main()