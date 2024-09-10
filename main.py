import math
import random
import time
import pygame


pygame.init()

width, higth = 600, 400 
window = pygame.display.set_mode(size=(width, higth)) # مشخص کردن اندازه صفحه ی بازی
pygame.display.set_caption("Aim Trainer") # عنوان بازی بر روی صفحه ی بازی


def main():
    """_summary_
    create a infinity loop for showing the window.
    """
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()