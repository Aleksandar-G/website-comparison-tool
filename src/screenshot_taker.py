from playwright.sync_api import sync_playwright


def take_screenshot(
    screenshot_path: str, screenshot_file_extension: str, website_url: str
):

    screenshot_full_file_path = screenshot_path + "." + screenshot_file_extension

    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open a website
        page.goto(website_url)

        # Take a screenshot
        screenshot = page.screenshot(path=screenshot_full_file_path)

        print(f"Screenshot taken")

        # Clean up
        browser.close()

        return screenshot
