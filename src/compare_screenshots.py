from PIL import Image, ImageChops


def compare_screenshots(screenshot_path1: str, screenshot_path2: str) -> bool:
    # Open the screenshots
    screenshot1 = Image.open(screenshot_path1)
    screenshot2 = Image.open(screenshot_path2)

    # Compare screenshots
    diff = ImageChops.difference(screenshot1, screenshot2)

    # Check if screenshots are identical
    if diff.getbbox() is None:
        return True
    else:
        return False
