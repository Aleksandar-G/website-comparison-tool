import datetime


def compare_contents(
    content_path_old: str, content_path_new: str, differences_folder: str
) -> bool:
    # Open the contents
    with open(content_path_old, "r", encoding="utf-8") as f:
        f1 = f.read()

    with open(content_path_new, "r", encoding="utf-8") as f:
        f2 = f.read()

    page_content_old = sorted(str(f1).split(" "))
    page_content_new = sorted(str(f2).split(" "))

    if page_content_old == page_content_new:
        return True
    else:
        diff = list(set(page_content_old) - set(page_content_new))
        with open(differences_folder + datetime.datetime.now().isoformat(), "w") as f:
            f.write(str(diff))
        return False
