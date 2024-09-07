import pyautogui
import cv2
import numpy as np
import random
import pyautogui
import time

def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame
def detect_enemy(frame):
    enemy_head = cv2.imread('enemy_head.png', 0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(gray_frame, enemy_head, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Adjust threshold as needed
    locations = np.where(result >= threshold)
    for pt in zip(*locations[::-1]):
        return pt  # Return the coordinates of the enemy's head
    return None
def aim_and_shoot(x, y):
    # Move to the detected head position
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))  # Smooth, human-like movement
    # Add some randomness to avoid detection
    pyautogui.click()  # Shoot


def randomize_movements(x, y):
    offset_x = random.randint(-10, 10)  # Randomize a bit
    offset_y = random.randint(-10, 10)
    pyautogui.moveTo(x + offset_x, y + offset_y, duration=random.uniform(0.1, 0.5))

def random_click():
    if random.uniform(0, 1) > 0.9:  # Occasionally miss the shot
        return  # Simulate a missed shot
    pyautogui.click()
def auto_headshot():
    while True:
        frame = capture_screen()
        enemy_position = detect_enemy(frame)
        if enemy_position:
            randomize_movements(*enemy_position)
            random_click()
            time.sleep(random.uniform(1.0, 3.0))  # Random cooldown between shots
        else:
            time.sleep(0.1)  # Add delay when no enemy is found
def run_bot():
    while True:
        if random.uniform(0, 1) > 0.95:  # Simulate bot taking breaks
            print("Bot resting...")
            time.sleep(random.uniform(5, 10))  # Rest for 5-10 seconds
        else:
            auto_headshot()  # Run the bot logic


def auto_headshot():
    while True:
        # Simulate headshot (replace with your logic)
        pyautogui.moveTo(500, 400)  # Move mouse to headshot position
        pyautogui.click()  # Trigger headshot
        time.sleep(0.1)

if __name__ == "__main__":
    auto_headshot()

