import pygame
import numpy as np


pos = [100, 100]
target = [800, 100]

velocity = 1

slowRadius = 300

_maxVelocity = 1.5


def main():
    global pos, target, velocity, slowRadius, _maxVelocity
    
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
                
                
            
        # obter vetor direção
        v_dir = np.subtract(target,pos) 
        
        # normalizar vetor direção e aplicar em distancia
        distance = np.linalg.norm(v_dir)
        
       # print(v_dir)
                
        if (distance < slowRadius):
            
            # APLICAR A VELOCIDADE REDUZIDA
            v_dir_norm = v_dir/np.linalg.norm(v_dir) * _maxVelocity * (distance/slowRadius)
            v_dir_norm = v_dir_norm * velocity
            pos = np.add(pos, v_dir_norm)

            
        else:
                    
            # NORMALIZAÇÃO NORMAL
            v_dir_norm = v_dir/np.linalg.norm(v_dir)
            
            v_dir_norm = v_dir_norm * velocity
        
            pos = np.add(pos, v_dir_norm)
        
            
            
            
            
        pygame.draw.circle(screen, (255,0,0), (pos), 10)
        
        pygame.draw.circle(screen, (0,255,0), (target), 12)
        
    
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()