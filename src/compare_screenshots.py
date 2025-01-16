from PIL import Image, ImageChops
from significant_difference_threshold import significant_difference_threshold


def compare_screenshots(screenshot_path1: str, screenshot_path2: str) -> bool:
    # Open the screenshots
    screenshot1 = Image.open(screenshot_path1)
    screenshot2 = Image.open(screenshot_path2)

    # Compare screenshots
    diff = ImageChops.difference(screenshot1, screenshot2)

    # Check if the difference is significant
    return significant_difference_threshold(diff)
