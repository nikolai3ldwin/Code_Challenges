import cv2
import pyautogui
from PIL import ImageGrab, ImageOps

def click_if_present(matching):
    # Load the image you want to search for on the webpage
    image = cv2.imread(f'system_files/{matching}.png')

    # Get the current screen
    screen = ImageGrab.grab()

    # Convert the screen to OpenCV format
    screen_cv = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    # Find the location of the image on the screen
    result = cv2.matchTemplate(screen_cv, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the image is found, click on its location
    if max_val > 0.8:
        x, y = pyautogui.locateCenterOnScreen(f'system_files/{matching}.png', confidence=0.8)
        pyautogui.click(x, y)
        return True
    else:
        return False

# Example usage
path = 'button'
if click_if_present(path):
    print(f"Clicked on {path} image")
else:
    print(f"{path} image not found")
