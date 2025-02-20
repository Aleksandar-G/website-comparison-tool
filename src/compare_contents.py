def compare_contents(content_path1: str, content_path2: str) -> bool:
    # Open the contents
    with open(content_path1, "r", encoding="utf-8") as f:
        f1 = f.read()

    with open(content_path2, "r", encoding="utf-8") as f:
        f2 = f.read()

    content1 = sorted(str(f1).split(" "))
    content2 = sorted(str(f2).split(" "))

    return content1 == content2
