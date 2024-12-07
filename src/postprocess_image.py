from PIL import Image, ImageFilter
from io import BytesIO


def convert_screenshot_to_black_white(screenshot, screenshot_full_path):
    # Load the colored screenshot
    img = Image.open(BytesIO(screenshot))

    # Convert to grayscale (black and white)
    bw_img = img.convert("L")

    # Save the new grayscaled screenshot
    bw_img.save(screenshot_full_path)


def apply_blur(image: Image) -> Image:
    # Apply a blur to reduce noise
    return image.filter(ImageFilter.GaussianBlur(radius=1))
