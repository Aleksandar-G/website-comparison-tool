from time import sleep
from os import rename

import helper_funcs
from screenshot_taker import take_screenshot
from postprocess_image import convert_screenshot_to_black_white
from compare_screenshots import compare_screenshots
from send_telegram_notification import send_telegram_message

SCREENSHOT_FOLDER = "./screenshots/"
SCREENSHOT_FILE_EXTENSION = "png"
WAIT_PERIOD_SECONDS = 1800  # 30 minutes

websites = [
    helper_funcs.Website(
        name="pararius",
        url="https://www.pararius.com/apartments/eindhoven/0-1200/1-bedrooms",
    ),
    helper_funcs.Website(
        name="funda",
        url="https://www.funda.nl/zoeken/huur?selected_area=%5B%22eindhoven%22%5D&rooms=%221-%22&price=%22-1250%22&sort=%22date_down%22",
    ),
    helper_funcs.Website(
        name="holland2stayLoterry",
        url="https://holland2stay.com/residences?page=1&available_to_book%5Bfilter%5D=Available+in+lottery%2C336&city%5Bfilter%5D=Eindhoven%2C29",
    ),
    helper_funcs.Website(
        name="holland2stayBookingDirectly",
        url="https://holland2stay.com/residences?page=1&available_to_book%5Bfilter%5D=Available+to+book%2C179&city%5Bfilter%5D=Eindhoven%2C29",
    ),
]


def main():
    if helper_funcs.is_folder_empty(SCREENSHOT_FOLDER):
        for website in websites:
            startup(website)
    else:
        for website in websites:
            watchdog(website)


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


def loop():
    while True:
        try:
            main()
            print(f"Waiting now for {WAIT_PERIOD_SECONDS} seconds...")
            sleep(WAIT_PERIOD_SECONDS)
        except Exception as error:
            send_telegram_message(f"Error has occured: {error}")


loop()
