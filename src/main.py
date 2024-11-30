from time import sleep
from os import rename

import helper_funcs
from screenshot_taker import take_screenshot
from postprocess_image import convert_screenshot_to_black_white
from compare_screenshots import compare_screenshots

SCREENSHOT_FOLDER = "./screenshots/"
SCREENSHOT_FILE_NAME_PREFIX = "ss"
SCREENSHOT_FILE_EXTENSION = "png"
WEBSITE_URL = "https://www.pararius.com/apartments/eindhoven/0-1200/1-bedrooms"
WAIT_PERIOD_SECONDS = 60

screenshot_path = SCREENSHOT_FOLDER + SCREENSHOT_FILE_NAME_PREFIX
old_screenshot_file_name = screenshot_path + "_old"
screenshot_full_path = f"{screenshot_path}.{SCREENSHOT_FILE_EXTENSION}"
screenshot_old_full_path = f"{screenshot_path}_old.{SCREENSHOT_FILE_EXTENSION}"


def main():

    # Check if that is the first time that the script is running
    if helper_funcs.is_folder_empty(SCREENSHOT_FOLDER):
        # take 2 screenshots
        screenshot = take_screenshot(
            old_screenshot_file_name, SCREENSHOT_FILE_EXTENSION, WEBSITE_URL
        )

        convert_screenshot_to_black_white(screenshot, screenshot_old_full_path)

        take_screenshot(screenshot_path, SCREENSHOT_FILE_EXTENSION, WEBSITE_URL)

        convert_screenshot_to_black_white(screenshot, screenshot_full_path)
    else:
        # make the "new" screenshot "old" and take a new screenshot
        rename(screenshot_full_path, screenshot_old_full_path)
        screenshot = take_screenshot(
            screenshot_path, SCREENSHOT_FILE_EXTENSION, WEBSITE_URL
        )
        # convert_screenshot_to_black_white(screenshot_path, SCREENSHOT_FILE_EXTENSION)
        convert_screenshot_to_black_white(screenshot, screenshot_full_path)

    # compare the screenshots
    if compare_screenshots(screenshot_old_full_path, screenshot_full_path):
        print("The same")
    else:
        print("Different")

    # send a notification on whatsapp or telegram


def loop():
    while True:
        main()
        print(f"Waiting now for {WAIT_PERIOD_SECONDS} seconds...")
        sleep(WAIT_PERIOD_SECONDS)


loop()
