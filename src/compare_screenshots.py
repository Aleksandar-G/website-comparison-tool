from PIL import Image, ImageChops, ImageFilter

DIFFERENCE_THRESHOLD = 60


def compare_screenshots(screenshot_path1: str, screenshot_path2: str) -> bool:
    # Open the screenshots
    screenshot1 = Image.open(screenshot_path1)
    screenshot2 = Image.open(screenshot_path2)

    # Compare screenshots
    diff = ImageChops.difference(screenshot1, screenshot2)

    # Apply a blur to reduce noise
    diff = diff.filter(ImageFilter.GaussianBlur(radius=1))

    # Threshold for significant differences
    diff = diff.point(lambda p: p > DIFFERENCE_THRESHOLD and 255)

    # Check if screenshots are identical
    if diff.getbbox() is None:
        return True
    else:
        return False
