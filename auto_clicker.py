import pyautogui
import time

# Delay before starting
time.sleep(5)

try:
    while True:
        # Click at the current mouse position
        pyautogui.tripleClick()
        # Wait for a specified interval
        time.sleep(0.0001)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Auto-clicker stopped.")
