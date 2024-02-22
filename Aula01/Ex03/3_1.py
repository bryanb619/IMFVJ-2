import pygame


green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 128)

def main():
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
                
        # screen
        screen.fill((30,30,30))
        
        
        font= pygame.font.SysFont(None, 72)
        img = font.render('hello!!!!', True, (0,0,255))
        screen.blit(img, (20, 20))
            
        # updates screen   
        pygame.display.update()
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()