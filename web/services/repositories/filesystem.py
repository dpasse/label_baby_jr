from typing import List

import os
import json


def get_directories(working_directory: str) -> List[str]:
    return [
        project
        for project in (
            os.path.join(working_directory, item)
            for item in os.listdir(working_directory)
        )
        if os.path.isdir(project)
    ]

def load_data(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf8') as input_file:
        return json.loads(input_file.read())
