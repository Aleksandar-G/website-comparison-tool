from time import sleep
from os import rename
from requests import exceptions

import helper_funcs
from screenshot_taker import take_screenshot
from postprocess_image import convert_screenshot_to_black_white
from compare_screenshots import compare_screenshots
from send_telegram_notification import send_telegram_message

SCREENSHOT_FOLDER = "./screenshots/"
SCREENSHOT_FILE_EXTENSION = "png"
WAIT_PERIOD_SECONDS = 3600  # 60 minutes

websites = [
    helper_funcs.Website(
        name="pararius",
        url="https://www.pararius.com/apartments/eindhoven/0-1000/1-bedrooms",
    ),
    helper_funcs.Website(
        name="funda",
        url="https://www.funda.nl/zoeken/huur?selected_area=%5B%22eindhoven%22%5D&rooms=%221-%22&price=%22-1000%22&sort=%22date_down%22",
    ),
    helper_funcs.Website(
        name="Friendly Housing",
        url="https://friendlyhousing.nl/en/house-listings/?property-type=appartement&min-price=750&max-price=1500&available-from=&type=&sort=",
    ),
]


def initialize():
    try:
        if not helper_funcs.is_folder_full(SCREENSHOT_FOLDER, websites):
            for website in websites:
                startup(website)
        cycle()

    except exceptions.ConnectionError:
        print("Connection error occurred and the script is rerunning")
        cycle()
    except Exception as error:
        print(f"Error has occurred: {error}")
        send_telegram_message(f"Error has occurred: {error}")
        return error


def startup(website):
    screenshot_path = SCREENSHOT_FOLDER + website.name
    screenshot_full_path = f"{screenshot_path}.{SCREENSHOT_FILE_EXTENSION}"
    old_screenshot_file_name = screenshot_path + "_old"
    screenshot_old_full_path = f"{screenshot_path}_old.{SCREENSHOT_FILE_EXTENSION}"

    # take 2 screenshots
    screenshot = take_screenshot(
        old_screenshot_file_name, SCREENSHOT_FILE_EXTENSION, website
    )

    convert_screenshot_to_black_white(screenshot, screenshot_old_full_path)

    take_screenshot(screenshot_path, SCREENSHOT_FILE_EXTENSION, website)

    convert_screenshot_to_black_white(screenshot, screenshot_full_path)


def watchdog(website: helper_funcs.Website):
    screenshot_path = SCREENSHOT_FOLDER + website.name
    screenshot_full_path = f"{screenshot_path}.{SCREENSHOT_FILE_EXTENSION}"
    screenshot_old_full_path = f"{screenshot_path}_old.{SCREENSHOT_FILE_EXTENSION}"

    # make the "new" screenshot "old" and take a new screenshot
    rename(screenshot_full_path, screenshot_old_full_path)
    screenshot = take_screenshot(screenshot_path, SCREENSHOT_FILE_EXTENSION, website)

    convert_screenshot_to_black_white(screenshot, screenshot_full_path)

    # compare the screenshots
    if compare_screenshots(screenshot_old_full_path, screenshot_full_path):
        print(f"{website.name} no updates")
    else:
        print(f"{website.name} has new listings")

        # Message to send
        message = f"{website.name} has new listings URL:{website.url}"
        send_telegram_message(message)


def cycle():
    while True:
        for website in websites:
            watchdog(website)

        print(f"Waiting now for {WAIT_PERIOD_SECONDS} seconds...")
        sleep(WAIT_PERIOD_SECONDS)


initialize()
