import re
import os


def get_project_path_from_name(working_directory: str, name: str) -> str:
    folder_name = re.sub(r' +', '-', name)
    return os.path.join(working_directory, folder_name)
