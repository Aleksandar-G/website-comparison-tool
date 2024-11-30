from PIL import Image
from io import BytesIO


def convert_screenshot_to_black_white(screenshot, screenshot_full_path):
    # Load the colored screenshot
    img = Image.open(BytesIO(screenshot))

    # Convert to grayscale (black and white)
    bw_img = img.convert("L")

    # Save the new grayscaled screenshot
    bw_img.save(screenshot_full_path)
