import pygame
import random
import math
import time

pygame.init()

width, higth = 800, 600 
window = pygame.display.set_mode(size=(width, higth)) 
pygame.display.set_caption("Aim Trainer") # Set the game window's title

target_increament = 400 # The rate at which targets grow and change size
target_event = pygame.USEREVENT # Custom event for target appearance
target_pading = 30  # Padding from the edges to generate targets

background_color = (0, 20, 45) # RGB color for the background
lives = 5 # Number of lives (misses allowed)
top_bar_heigth = 50 # Height of the top bar

label_font = pygame.font.SysFont("comicsans", 26) # Font for labels (score, time, etc.)

class Target:
    max_size = 30  # Maximum size in pixels for each target
    growth_rate = 0.2 # The speed at which each target grows
    color = "red" # Primary color of the targets
    second_color = "white" 

    def __init__(self, x, y): # Initialize target's position and starting size
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True # Indicates if the target is growing or shrinking
        
    def update(self):
        if self.size + self.growth_rate >= self.max_size: # Targets stop growing when they reach max size
            self.grow = False

        if self.grow: 
            self.size += self.growth_rate # Increase the size until the target reaches max size
        else:
            self.size -= self.growth_rate  # Decrease the size once max size is reached       

    def draw(self): # Draw the target with concentric colored rings
        pygame.draw.circle(surface=window, color=self.color, center=(self.x, self.y), radius=self.size)
        pygame.draw.circle(surface=window, color=self.second_color, center=(self.x, self.y), radius=self.size * 0.8)
        pygame.draw.circle(surface=window, color=self.color, center=(self.x, self.y), radius=self.size * 0.6)
        pygame.draw.circle(surface=window, color=self.second_color, center=(self.x, self.y), radius=self.size * 0.4)


    def collide(self, x, y):  # Check if the player clicked within the target's radius
        distance = math.sqrt((self.x - x)**2  + (self.y - y)**2) # Formula for distance between two points
        return distance <= self.size # Return True if click is inside the target


def draw_targets(window, targets): # Draw all active targets on the screen
    window.fill(background_color) # background'c color       

    for target in targets:
        target.draw() # disply targets on the screen


def time_format(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

     
def draw_top_bar(window, elapsed_time, targets_pressed, misses): # Draw top bar with time, score, and misses
    pygame.draw.rect(window, "grey", (0, 0, width, top_bar_heigth)) # Draw top bar
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

def end_screen(window, elapsed_time, target_pressed, clicks): # Display game over screen with stats
    window.fill(background_color)

    time_label = label_font.render(
        f"Time: {time_format(elapsed_time)}", 1, "white")
    
    speed = round(target_pressed / elapsed_time, 1)
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "white")

    hits_label = label_font.render(f"Hits: {target_pressed}", 1, "white")

    try:
        accuracy = round((target_pressed / clicks) * 100, 1) # Calculate accuracy percentage
    except ZeroDivisionError:
        accuracy = 0
        
    accuracy_label = label_font.render(f"Accuracy: {accuracy}%", 1, "white")
    
    window.blit(time_label, (get_middle_screen(time_label), 100))
    window.blit(speed_label, (get_middle_screen(speed_label), 200))
    window.blit(hits_label, (get_middle_screen(hits_label), 300))
    window.blit(accuracy_label, (get_middle_screen(accuracy_label), 400))
    
    pygame.display.update()

    # Wait for the player to quit the game
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def main():
    run = True 
    targets = [] # List to store active targets
    clock = pygame.time.Clock()
    
    targets_pressed = 0 # Number of targets hit
    clicks = 0 # Total number of clicks
    misses = 0  # Number of missed targets
    start_time = time.time() # Record the start time

    pygame.time.set_timer(target_event, target_increament) # Set a timer to spawn new targets

    while run:
        clock.tick(60) # Define frame rate (60 frames per second)
        click = False
        mouse_position = pygame.mouse.get_pos() # Get current mouse position
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit game
                run = False
                break
            
            if event.type == target_event:
                x = random.randint(target_pading, width - target_pading)  # Randomize target's x position
                y = random.randint(target_pading + target_pading, higth - target_pading) # Randomize target's y position
                target = Target(x, y)
                targets.append(target) # Add target to the list
            
            if event.type == pygame.MOUSEBUTTONDOWN: # Register click
                click = True
                clicks += 1
                
        for target in targets:
            target.update() # Update target's size
            
            if target.size <= 0: # Remove target if it shrinks below a certain size
                targets.remove(target)
                misses += 1  # Increment missed targets count
                
            if click and target.collide(*mouse_position): # Check if the click hit the target
                targets.remove(target)
                targets_pressed += 1  # Increment hits count
        if misses >= lives:  # End game if misses exceed allowed lives
            end_screen(window, elapsed_time, targets_pressed, clicks) # Show game over screen
        
        
        draw_targets(window, targets) # Draw all targets
        draw_top_bar(window, elapsed_time, targets_pressed, misses)  # Draw top bar with stats   
        pygame.display.update() # Update the display
        
    pygame.quit() # Quit the game
    
    
if __name__ == "__main__":
    main()
    