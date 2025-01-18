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
    system("rm -rf folder_path")
