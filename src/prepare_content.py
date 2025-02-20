from bs4 import BeautifulSoup


def remove_attributes(soup: BeautifulSoup) -> str:
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
        tag.attrs.pop("data-smartmenus-id", None)

    return soup.prettify()


def remove_tags(content: str) -> str:
    pure_content = []
    line_content = content.splitlines()
    for line in line_content:
        line = line.strip()
        if line == "<div>" or line == "</div>":
            continue
        else:
            pure_content.append(line)
    return str(pure_content)


def remove_special_characters(content: list) -> list:
    special_characters = ["<", ">", ",", "/"]

    for sc in special_characters:
        filtered_lst = list(filter(lambda x: True if x == sc else False, content))

    return filtered_lst


def clean_content(content: BeautifulSoup) -> str:
    clean_content = remove_attributes(content)
    clean_content = remove_tags(clean_content)
    return clean_content
    clean_content = remove_special_characters(clean_content)

    return clean_content
