import pygame
import numpy as np


pos = [100, 100]
target = [600, 100]

velocity = 0.2

slowRadius = target[0] -50

_maxVelocity = 1.2


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
        
        # TESTING
        #print(v_dir)
       
       
        # distancia do valor total do raio "Estou a 50 unidades de 600"
        # estou a menos de 600, portanto continuar com velocidade maxima
        if (distance < slowRadius):
            
            # Apply normalization and 
            v_dir_norm = v_dir/np.linalg.norm(v_dir) 
            
            # Apply max velocity
            v_dir_norm *=  _maxVelocity * (distance/slowRadius)

            # Add to position
            pos = np.add(pos, v_dir_norm)

            
        # continuar com velocidade reduzida
        else:
                    
            # NORMALIZAÇÃO NORMAL
            v_dir_norm = v_dir/np.linalg.norm(v_dir)
            
            # APPLY REDUCED VELOCITY * (0.5)
            v_dir_norm = v_dir_norm * velocity

            # Add values to position
            pos = np.add(pos, v_dir_norm)
        
        
            
        # Target circle
        pygame.draw.circle(screen, (0,255,0), (target), 20)
            
        # moving circle
        pygame.draw.circle(screen, (255,0,0), (pos), 10)
        
        
        
        # updates screen   
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
main()