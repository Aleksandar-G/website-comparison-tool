from os import listdir


def is_folder_empty(folder: str) -> bool:
    if not listdir(folder):
        return True
    else:
        return False


class Website:
    name = ""
    url = ""

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url


def is_folder_full(folder: str, websites: list[Website]):
    return len(listdir(folder)) == len(websites) * 2
