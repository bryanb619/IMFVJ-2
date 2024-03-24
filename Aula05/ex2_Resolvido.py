import pygame

## CONSTANTS ##

# screen size variables
SCREEN_WIDTH            = 800
SCREEN_HEIGHT           = 800

# Line
#                           (X,Y)
LINE_START              = (300, 200)
LINE_END                = (500, 200)

# gravity
GRAVITY                 = 9.8 # => 9.8 m/s^2


# Main method
def main():
    
    #---------------------------------------------------------------------------
    
    pygame.init()
    
    # set up clock => initialize clock. used later in the loop.
    clock               = pygame.time.Clock()
    
    # Game Variables that can be changed
    
    # Variables for the ball
    ball_x              = LINE_START[0]
    
    # subtract 20 to line end y to compensate
    ball_y              = LINE_START[1] -20 
    
    # ball velocity
    ball_velocity_x     = 0
    ball_velocity_y     = 0
    
    # acceleration
    acceleration        = 1
    
    # Screen
    screen              = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # set caption
    pygame.display.set_caption("Ex: 2 Movement & Free Fall")
    
    # game loop state
    run                 = True
    
    #---------------------------------------------------------------------------
    

    # Game loop
    while run:
        
        # Start looping and counting time
        # lock to 60 fps
        delta_time = clock.tick(60)   
         
        # transform in milliseconds
        time_step = delta_time/100
        
        # ============== Standard game loop structure ============== #
        
        # screen
        screen.fill((0,0,0))
        
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # double acceleration
                    # Only works in X axis movement
                    acceleration *= 2
        # ----------------------------------------------------------------------
                
        # Draw Graphics
                
        # Draw line
        pygame.draw.line(screen, (255,0,0), LINE_START, LINE_END, 5)
        
        # Draw circle                         
        pygame.draw.circle(screen, (0,0,255), (ball_x, ball_y), 15)
        
        
        " ====================  UPDATE CIRCLE POS  ==================== "
        
        # check if ball is falling
        if ball_x <= LINE_END[0]:
          
            # update horizontal position X++
            ball_velocity_x += acceleration * time_step
            
            # lock y velocity => NO FALL 
            ball_velocity_y = 0
            #-------------------------------------------------------------------
            
        # Apply free fall & modify position on Y++ 
        else:
            # Lock x velocity => NO MOVE Left or right
            ball_velocity_x = 0
            
            # apply gravity on velocity Y
            ball_velocity_y += GRAVITY * time_step
            #-------------------------------------------------------------------
            
        # update position of the ball
        ball_x += ball_velocity_x * time_step
        ball_y += ball_velocity_y * time_step
            
            
        # updates screen   
        pygame.display.update()
        # ----------------------------------------------------------------------
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()