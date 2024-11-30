from os import listdir

def is_folder_empty(folder: str) -> bool:
    if not listdir(folder):
        return True
    else:
        return False