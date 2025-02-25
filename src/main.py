from time import sleep
from os import path, rename, remove

import helper_funcs
from content_extractor import extract_content
from compare_contents import compare_contents
from send_telegram_notification import send_telegram_message

CONTENT_FOLDER = "./contents/"
CONTENT_FILE_EXTENSION = "html"
WAIT_PERIOD_SECONDS = 1800  # 30 minutes
DIFFERENCE_FOLDER = "./differences/"

websites = [
    helper_funcs.Website(
        name="Pararius",
        url="https://www.pararius.com/apartments/eindhoven/800-1200",
    ),
    helper_funcs.Website(
        name="FriendlyHousing",
        url="https://friendlyhousing.nl/en/house-listings/?property-type=appartement&min-price=750&max-price=1500&available-from=&type=&sort=",
    ),
    helper_funcs.Website(
        name="Rotsvast",
        url="https://www.rotsvast.nl/en/property-listings/?type=2&city=Eindhoven&distance=5&office=0&minimumPrice[2]=800&maximumPrice[2]=1250",
    ),
    helper_funcs.Website(
        name="H2S",
        url="https://holland2stay.com/residences?page=1&available_to_book%5Bfilter%5D=Available+to+book%2C179&city%5Bfilter%5D=Eindhoven%2C29",
    ),
]

logger = helper_funcs.logger(__name__)


def initialize():
    try:
        if not helper_funcs.is_folder_full(CONTENT_FOLDER, websites):
            for website in websites:
                startup(website)
        cycle()

    except Exception as error:
        logger.error(error)
        if "net::ERR_NETWORK_CHANGED" in str(error):
            logger.error(f"Network error has occurred the script continues")

        helper_funcs.clean_folder(CONTENT_FOLDER)
        initialize()

        logger.error(f"Error has occurred: {error}")
        send_telegram_message(f"The error is: {error}")


def startup(website):
    content_path = CONTENT_FOLDER + website.name
    old_content_file_name = content_path + "_old"
    # take 2 contents
    extract_content(old_content_file_name, CONTENT_FILE_EXTENSION, website, logger)

    extract_content(content_path, CONTENT_FILE_EXTENSION, website, logger)


def watchdog(website: helper_funcs.Website):
    content_path = CONTENT_FOLDER + website.name
    content_full_path = f"{content_path}.{CONTENT_FILE_EXTENSION}"
    content_old_full_path = f"{content_path}_old.{CONTENT_FILE_EXTENSION}"

    # delete "old" content
    if path.exists(content_old_full_path):
        remove(content_old_full_path)
    else:
        logger.error(
            f"{content_old_full_path} Cannot be deleted because if does not exists"
        )
    # make the "new" content "old" and take a new content
    rename(content_full_path, content_old_full_path)

    # fetch fresh content
    extract_content(content_path, CONTENT_FILE_EXTENSION, website, logger)

    # compare the contents
    if compare_contents(content_old_full_path, content_full_path):
        logger.info(f"{website.name} no updates")
    else:
        logger.info(f"{website.name} has new listings")

        # Message to send
        message = f"{website.name} has new listings URL:{website.url}"
        send_telegram_message(message, logger)


def cycle():
    while True:
        for website in websites:
            watchdog(website)

        logger.info(f"Waiting now for {WAIT_PERIOD_SECONDS} seconds...")
        sleep(WAIT_PERIOD_SECONDS)


try:
    initialize()
except Exception as exp:
    logger.error(f"Error has occurred: {exp}")
    send_telegram_message("ERROR THE SCRIPT HAS STOPPED", logger)
