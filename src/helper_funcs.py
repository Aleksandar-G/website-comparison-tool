from os import listdir, system
import logging


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


def logger(name: str):

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger


def clean_folder(folder_path):
    system(f"rm -rf {folder_path}")


def create_folder(folder_path: str):
    system(f"mkdir {folder_path}")


def extract_website_name_from_path(path: str) -> str:
    parts = path.split("/")
    return parts[len(parts) - 1]


def copy_file(original_file_path: str, new_file_path: str):
    system(f"cp {original_file_path} {new_file_path}")
