import os
import time

def take_screenshot(driver, name="screenshot"):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{name}_{timestamp}.png"
    screenshot_directory = os.path.join(os.getcwd(), "screenshots")
    
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)
    
    file_path = os.path.join(screenshot_directory, filename)
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")
