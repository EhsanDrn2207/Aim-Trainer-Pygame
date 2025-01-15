
# Aim Trainer Game 🎯  

A fast-paced game designed to test and improve your reflexes, accuracy, and hand-eye coordination. Built with Python and Pygame, this simple yet challenging game tracks your performance stats, including hits, misses, speed, and accuracy.

---

## 🕹️ Features
- **Dynamic Growing Targets**: Targets appear at random locations and grow/shrink dynamically, adding to the challenge.
- **Performance Metrics**: Tracks your time, hits, misses, accuracy, and speed.
- **Lives System**: Miss too many targets, and the game ends!
- **Game Over Screen**: Displays your final stats (hits, speed, and accuracy).
- **Custom Timer Events**: Targets spawn dynamically at configurable intervals.

---

## 🚀 How to Play
1. Start the game by running the Python script.
2. Targets will appear randomly on the screen, grow, and then shrink.  
   **Your Goal:** Click the targets before they disappear!
3. You lose a life for every missed target or incorrect click.
4. The game ends when you run out of lives.  
5. View your performance stats on the **Game Over Screen** and aim to improve your score!

---

## 🎮 Controls
- **Mouse**: Click to hit the targets.
- **Quit Game**: Close the window or press any key on the Game Over Screen.

---

## 🛠️ Requirements
### Prerequisites
- **Python 3.6 or higher**  
- **Pygame Library**  
  Install Pygame using the following command:
  ```bash
  pip install pygame
  ```

---

## 📂 Code Overview
### 1. **Main Components**  
- **`Target` Class**:  
  Handles all target logic, including creation, dynamic size changes, collision detection, and drawing.  
- **Game Loop**:  
  The heart of the game — handles target generation, user input, collision checks, and stat updates.  
- **End Screen**:  
  Displays the final stats like time, hits, speed, and accuracy after the game ends.

---

### 2. **Custom Functions**
- **`draw_targets(window, targets)`**: Draws all active targets on the screen.  
- **`draw_top_bar(window, elapsed_time, hits, misses)`**: Displays game stats (time, speed, hits, and lives).  
- **`time_format(secs)`**: Converts elapsed time into the format `MM:SS.MS`.  
- **`end_screen(window, elapsed_time, hits, clicks)`**: Displays performance metrics after the game ends.  

---

### 3. **Target Logic**
- Targets grow and shrink at a configurable rate.
- Clicking within a target's radius registers a hit and removes the target.
- Targets disappear when they shrink below a certain size, counting as a missed target.

---

## ⚙️ Customization Options
The following parameters can be adjusted in the code to tweak the gameplay:  

### Target Settings  
- **Max Size**: Maximum size of the targets — `Target.max_size`.  
- **Growth Rate**: How fast the targets grow/shrink — `Target.growth_rate`.  
- **Spawn Rate**: Interval for spawning new targets — `target_increament`.  

### Game Settings  
- **Lives**: Number of allowed misses before the game ends — `lives`.  
- **Window Dimensions**: Width and height of the game window — `width, higth`.  
- **Colors**: Background and target colors — `background_color`, `Target.color`, `Target.second_color`.  

---

## 📊 Game Stats
The game tracks the following stats in real-time:  
- **Time**: Total time elapsed since the start of the game.  
- **Hits**: Total number of targets successfully clicked.  
- **Speed**: Average hits per second (targets per second).  
- **Lives**: Remaining misses allowed.  
- **Accuracy**: Percentage of successful clicks out of total clicks.  

---

## 🏆 How to Run the Game
1. Save the script as `aim_trainer.py` in your working directory.  
2. Run the script in your terminal or IDE:  
   ```bash
   python aim_trainer.py
   ```
3. Enjoy the game, track your stats, and aim for a higher score!  

---

## 📝 License
This project is open-source and free to use or modify for personal or educational purposes.  
