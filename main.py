import pygame
import random

pygame.init()

width, higth = 800, 600 
window = pygame.display.set_mode(size=(width, higth)) # مشخص کردن اندازه صفحه ی بازی
pygame.display.set_caption("Aim Trainer") # عنوان بازی بر روی صفحه ی بازی

target_increament = 400 # سرعتی که اهداف ما تغییر اندازه می دهند
target_event = pygame.USEREVENT #  custom events
target_pading = 30
background_color = (0, 20, 45) # red, green, blue

class Target:
    max_size = 30 # حداکثر تعداد پیکسل که هر هدف بهش میرسه
    growth_rate = 0.2 # سرعت رشد هر هدف در صفحه ی بازی
    color = "red" # رنگ اهداف در صفحه ی بازی
    second_color = "white" # رنگ اهداف در صفحه ی بازی

    def __init__(self, x, y): # موقعیت مکانی و اندازه اولیه هر هدفی که ساخته می شود در اینجا تعیین می شود
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        
    def update(self):
        if self.size + self.growth_rate >= self.max_size: # اندازه اهداف به 30 رسید دیگر بزرگتر نمی شوند
            self.grow = False

        if self.grow: 
            self.size += self.growth_rate #  اندازه اهداف تا به 30 برسند دائما بزرگتر می شوند
        else:
            self.size -= self.growth_rate # اندازه اهداف وقتی به 30 برسند دائما کوچک تر می شوند         

    def draw(self):
        pygame.draw.circle(surface=window, color=self.color, center=(self.x, self.y), radius=self.size)
        pygame.draw.circle(surface=window, color=self.second_color, center=(self.x, self.y), radius=self.size * 0.8)
        pygame.draw.circle(surface=window, color=self.color, center=(self.x, self.y), radius=self.size * 0.6)
        pygame.draw.circle(surface=window, color=self.second_color, center=(self.x, self.y), radius=self.size * 0.4)


def draw_targets(window, targets):
    window.fill(background_color) # رنگ صقحه ی بازی       

    for target in targets:
        target.draw() # نمایش اهداف بر روی صقحه ی نمایش
        
    pygame.display.update() # updates the contents of the entire display

def main():
    targets = []
    pygame.time.set_timer(target_event, target_increament)
    
    clock = pygame.time.Clock()
    
    run = True 
    while run:
        clock.tick(60) # defind F
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == target_event:
                x = random.randint(target_pading, width - target_pading)
                y = random.randint(target_pading, higth - target_pading)
                target = Target(x, y)
                targets.append(target)

        for target in targets:
            target.update()

        draw_targets(window, targets)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()