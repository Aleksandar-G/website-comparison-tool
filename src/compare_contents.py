import datetime
from helper_funcs import extract_website_name_from_path, create_folder, copy_file


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

    if list(set(page_content_new) - set(page_content_old)) == []:
        return True
    else:
        diff1 = list(set(page_content_new) - set(page_content_old))
        diff2 = list(set(page_content_old) - set(page_content_new))
        # extract website name
        website_name = extract_website_name_from_path(content_path_old)
        # create folder
        new_folder_path = (
            differences_folder + website_name + str(datetime.datetime.now().isoformat())
        )
        create_folder(new_folder_path)
        # put original files
        copy_file(content_path_old, new_folder_path)
        copy_file(content_path_new, new_folder_path)
        # put diff file there
        with open(new_folder_path + f"/{website_name}-diff1", "w") as f:
            f.write(str(diff1))
        with open(new_folder_path + f"/{website_name}-diff2", "w") as f:
            f.write(str(diff2))
        return False
