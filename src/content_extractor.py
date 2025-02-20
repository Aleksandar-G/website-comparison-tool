from time import sleep
from bs4 import BeautifulSoup

from logging import Logger
from playwright.sync_api import sync_playwright
from helper_funcs import Website
from prepare_content import clean_content


def extract_content(
    content_path: str,
    content_file_extension: str,
    website: Website,
    logger: Logger,
):

    content_full_file_path = content_path + "." + content_file_extension

    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            page.goto(website.url)
            sleep(30)

        finally:
            soup = BeautifulSoup(page.content(), "html.parser")

            pure_content = clean_content(soup)

            with open(f"{content_full_file_path}", "w") as e:
                e.write(str(pure_content))

        logger.info(f"Content for {website.name} taken")

        # Clean up
        browser.close()
