import pygame

pos = 100


def main():
    global pos

    
    pygame.init()

    # screen size variables
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400

    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True

    # Game loop
    while run:
        
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print('Mouse clicked')
                pos +=10
                
                
        # screen
        screen.fill((30,30,30))
        
        # get mouse position
       # print(pygame.mouse.get_pos())

        # convert mouse position to string
        i = str(pygame.mouse.get_pos())

        font= pygame.font.SysFont(None, 72)
        img = font.render(i, True, (0,0,255))
        screen.blit(img, (20, 20))
        
        
               
        pygame.draw.circle(screen, (255,0,0), (pos, 100), 100)
    
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()