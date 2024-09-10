import pygame


pygame.init()

width, higth = 800, 600 
window = pygame.display.set_mode(size=(width, higth)) # مشخص کردن اندازه صفحه ی بازی
pygame.display.set_caption("Aim Trainer") # عنوان بازی بر روی صفحه ی بازی


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
        pygame.draw.circle(surface=window, color=self.second_color, center=(self.x, self.y), radius=self.size + 0.8)
        pygame.draw.circle(surface=window, color=self.color, center=(self.x, self.y), radius=self.size + 0.6)
        pygame.draw.circle(surface=window, color=self.second_color, center=(self.x, self.y), radius=self.size + 0.4)
        
def main():
    """_summary_
    create a infinity loop for showing the window
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