from playwright.sync_api import sync_playwright, TimeoutError
from helper_funcs import Website


def take_screenshot(
    screenshot_path: str, screenshot_file_extension: str, website: Website
):

    screenshot_full_file_path = screenshot_path + "." + screenshot_file_extension

    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            # Open a website
            page.goto(website.url, wait_until="networkidle")

            # Take a screenshot
            screenshot = page.screenshot(path=screenshot_full_file_path)

        except TimeoutError:
            screenshot = page.screenshot(path=screenshot_full_file_path)

        print(f"Screenshot for {website.name} taken")

        # Clean up
        browser.close()

        return screenshot
