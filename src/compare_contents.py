def compare_contents(content_path_old: str, content_path_new: str) -> bool:
    # Open the contents
    with open(content_path_old, "r", encoding="utf-8") as f:
        f1 = f.read()

    with open(content_path_new, "r", encoding="utf-8") as f:
        f2 = f.read()

    page_content_old = sorted(str(f1).split(" "))
    page_content_new = sorted(str(f2).split(" "))

    return page_content_old == page_content_new
