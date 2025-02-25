import datetime
from helper_funcs import extract_website_name_from_path, create_folder, move_file


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
        diff = list(set(page_content_new) - set(page_content_old))
        # extract website name
        website_name = extract_website_name_from_path(content_path_old)
        # create folder
        new_folder_path = (
            differences_folder + website_name + str(datetime.datetime.now().isoformat())
        )
        create_folder(new_folder_path)
        # put original files
        move_file(page_content_old, new_folder_path)
        move_file(page_content_new, new_folder_path)
        # put diff file there
        with open(new_folder_path + "-diff", "w") as f:
            f.write(str(diff))
        return False
