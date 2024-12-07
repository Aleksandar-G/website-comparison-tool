from PIL import Image, ImageChops
from postprocess_image import apply_blur

DIFFERENCE_THRESHOLD = 60


def compare_screenshots(screenshot_path1: str, screenshot_path2: str) -> bool:
    # Open the screenshots
    screenshot1 = Image.open(screenshot_path1)
    screenshot2 = Image.open(screenshot_path2)

    # Compare screenshots
    diff = ImageChops.difference(screenshot1, screenshot2)

    blur_image = apply_blur(diff)

    # Threshold for significant differences
    diff = blur_image.point(lambda p: p > DIFFERENCE_THRESHOLD and 255)

    # Check if screenshots are identical
    if diff.getbbox() is None:
        return True
    else:
        return False
