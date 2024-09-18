import pygame
import random
import math
import time

pygame.init()

width, higth = 800, 600 
window = pygame.display.set_mode(size=(width, higth)) # مشخص کردن اندازه صفحه ی بازی
pygame.display.set_caption("Aim Trainer") # عنوان بازی بر روی صفحه ی بازی

target_increament = 400 # سرعتی که اهداف ما تغییر اندازه می دهند
target_event = pygame.USEREVENT #  custom events
target_pading = 30

background_color = (0, 20, 45) # red, green, blue
lives = 5
top_bar_heigth = 50

label_font = pygame.font.SysFont("comicsans", 26)

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


    def collide(self, x, y):
        distance = math.sqrt((self.x - x)**2  + (self.y - y)**2) # فرمول اندازه گیری فاصله بین 2 نقطه
        return distance <= self.size 


def draw_targets(window, targets):
    window.fill(background_color) # رنگ صقحه ی بازی       

    for target in targets:
        target.draw() # نمایش اهداف بر روی صقحه ی نمایش


def time_format(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

     
def draw_top_bar(window, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(window, "grey", (0, 0, width, top_bar_heigth))
    time_label = label_font.render(
        f"Time: {time_format(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "black")

    hits_label = label_font.render(f"Hits: {targets_pressed}", 1, "black")

    lives_label = label_font.render(f"Lives: {lives - misses}", 1, "black")

    window.blit(time_label, (5, 5))
    window.blit(speed_label, (200, 5))
    window.blit(hits_label, (450, 5))
    window.blit(lives_label, (650, 5))
    
def get_middle_screen(surface):
    return width / 2 - surface.get_width() / 2

def end_screen(window, elapsed_time, target_pressed, clicks):
    window.fill(background_color)

    time_label = label_font.render(
        f"Time: {time_format(elapsed_time)}", 1, "white")
    
    speed = round(target_pressed / elapsed_time, 1)
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "white")

    hits_label = label_font.render(f"Hits: {target_pressed}", 1, "white")

    try:
        accuracy = round((target_pressed / clicks) * 100, 1)
    except ZeroDivisionError:
        accuracy = 0
        
    accuracy_label = label_font.render(f"Accuracy: {accuracy}%", 1, "white")
    
    window.blit(time_label, (get_middle_screen(time_label), 100))
    window.blit(speed_label, (get_middle_screen(speed_label), 200))
    window.blit(hits_label, (get_middle_screen(hits_label), 300))
    window.blit(accuracy_label, (get_middle_screen(accuracy_label), 400))
    
    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def main():
    run = True 
    targets = []
    clock = pygame.time.Clock()
    
    targets_pressed = 0 # تعداد اهدافی که زده شد
    clicks = 0 # تعداد کلیک ها کاربر
    misses = 0 # تعداد اهدافی که کاربر از دست داده
    start_time = time.time()

    pygame.time.set_timer(target_event, target_increament)

    while run:
        clock.tick(60) # defind F
        click = False
        mouse_position = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == target_event:
                x = random.randint(target_pading, width - target_pading)
                y = random.randint(target_pading + target_pading, higth - target_pading)
                target = Target(x, y)
                targets.append(target)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
                
        for target in targets:
            target.update()
            
            if target.size <= 0:
                targets.remove(target)
                misses += 1
                
            if click and target.collide(*mouse_position): # mouse position[0], mouse position[1]
                targets.remove(target)
                targets_pressed += 1
        if misses >= lives:
            end_screen(window, elapsed_time, targets_pressed, clicks)
        
        
        draw_targets(window, targets)
        draw_top_bar(window, elapsed_time, targets_pressed, misses)         
        pygame.display.update() # updates the contents of the entire display
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    