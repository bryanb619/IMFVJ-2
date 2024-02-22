import time
import random
import pygame
import math


# screen size variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# frame counter
frame_counter = 0


words = ["bazinga", "gorgonzola", "Jiggly"]
display_text = "Guess the word! :)"
hint_text = "Hint: It's a word"

r = 0
g = 0
color = 0

def main():
    """_summary_
    Main function of the game
    Diplasy text, hint and time
    
    """
    global hint_text
    global display_text
    global r
    global g
    global color
    global frame_counter    
    
    # start time and pygame
    pygame.init()
 
    # Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Random word 
    random_word = random.choice(words)
    if random_word == "bazinga":
        hint_text = "Hint: Word about Sheldon or surprise"
        
    elif random_word == "gorgonzola":
        hint_text = "Hint: Type of really smelly cheese"
        
    elif random_word == "Jiggly":
        hint_text = """Hint: Something that is wobbly"""
        
        
    guess = ""       
            
    #print(random_word)

  
    start = time.time()
    
    # Game loop
    while True:
        
        current_time = time.time()
        
        screen.fill((0, 0, 0))
        
        i = ""
        if current_time - frame_counter >=1:  # Update every 60 frames
            elapsed = current_time - start
            i = str(int(elapsed))
            frame_counter = current_time
            print(i)
            
            
        """Display text on screen"""
        font= pygame.font.SysFont(None, 72)
        img = font.render(display_text, True, (r,g,0))
        screen.blit(img, (SCREEN_HEIGHT/2-100, SCREEN_HEIGHT/2))
        
    
        """Hint text on screen"""
        font= pygame.font.SysFont(None, 30)
        img = font.render(hint_text, True, (255,255,255))
        screen.blit(img, (SCREEN_HEIGHT/2-70, SCREEN_HEIGHT/2 + 50))
        
        """Time text on screen"""
        font= pygame.font.SysFont(None, 30)
        img = font.render(i, True, (255,255,255))
        screen.blit(img, ((50, 50)))
        
        
        
        # Loop for handling game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if guess == random_word:
                        display_text = "You guessed it!"
                    else:
                        display_text = "Try again!"
                #else:
                   # guess += event.unicode
               
               
               
               
        r = (math.sin(color) * 127.5 + 127.5)
        g = (math.sin(color + 2*math.pi/3) * 127.5 + 127.5)
        
        # updates screen   
        color += 0.01
        pygame.display.update()
        
        
    # Quit method is out of the loop since run = False   
    pygame.quit()
    
    
main()