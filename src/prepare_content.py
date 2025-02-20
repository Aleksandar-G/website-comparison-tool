from bs4 import BeautifulSoup


def prepare_content(soup: BeautifulSoup) -> BeautifulSoup:

    # kill all script and style elements
    for content in soup(["script", "style", "head", "footer", "iframe", "input"]):
        content.extract()  # rip it out

    # Remove 'for' and 'id' attributes from every tag
    for tag in soup.find_all(True):
        tag.attrs.pop("for", None)
        tag.attrs.pop("data-google-query-id", None)
        tag.attrs.pop("id", None)
        tag.attrs.pop("class", None)
        tag.attrs.pop("style", None)
        tag.attrs.pop("aria-controls", None)
        tag.attrs.pop("aria-labelledby", None)

    return soup
