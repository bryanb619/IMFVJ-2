import pygame
m = 0

h = ""

def main():
    
    global m
    global h
    
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
        
        # get mouse position
       # print(pygame.mouse.get_pos())

        # convert mouse position to string
        i = str(pygame.mouse.get_pos())

        font= pygame.font.SysFont(None, 72)
        img = font.render("Cursor pos (x,y) " +i, True, (0,0,255))
        screen.blit(img, (20, 20))
        
        
        # count mouse clicks
        
        # get mouse click
        
        
        #if mouse click is true
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print('Mouse clicked')
                m +=1
                h = str(m)
                
        font= pygame.font.SysFont(None, 72)
        img = font.render("Mouse click: " +h, True, (255,0,255))
        screen.blit(img, (150, 150))   
                
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()