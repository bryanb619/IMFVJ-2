import pygame

r = 0
g = 0
b = 255

def main():
    
    global r
    global g
    global b
    
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
    
        screen.fill((124,135,50))
        
        if pygame.mouse.get_pos() == (300,300):
            if r < 254:
                r += 1  
            else :
                r = 0          
        else:
            r = 0
        
        font= pygame.font.SysFont(None, 72)
        img = font.render("Videojogos", True, (r,g,b))
        screen.blit(img, (20, 20))
            
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()