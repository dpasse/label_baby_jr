import re
import os


def clean_project_name(name: str) -> str:
    return re.sub(r' +', '-', name)

def get_project_path_from_name(working_directory: str, name: str) -> str:
    return os.path.join(working_directory, clean_project_name(name))
