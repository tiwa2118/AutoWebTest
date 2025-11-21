import os
import time
from pathlib import Path
from openpyxl.styles import Font


# スクリーンショット
def capture_screenshot(driver, name, screenshot_dir):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    Path(screenshot_dir).mkdir(parents=True, exist_ok=True)
    path = f"{screenshot_dir}/{name}_{timestamp}.png"
    driver.save_screenshot(path)

    # 絶対パス変換
    abs_path = os.path.abspath(path)
    return abs_path

def set_hyperlink(cell, path):
    if path:
        cell.hyperlink = path
        cell.value = "View Screenshot"
        cell.font = Font(color="0000FF", underline="single")