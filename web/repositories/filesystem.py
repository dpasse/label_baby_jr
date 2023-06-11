from typing import List

import os
import re
import json


class Workspace():
    def __init__(self, working_directory: str) -> None:
        self._working_directory = working_directory

    def load_data(self, file_name: str) -> dict:
        file_path = os.path.join(self._working_directory, file_name)
        with open(file_path, 'r', encoding='utf8') as input_file:
            return json.loads(input_file.read())
        
    def save_data(self, file_name: str, data: dict) -> None:
        file_path = os.path.join(self._working_directory, file_name)
        with open(file_path, 'w', encoding='utf8') as output_file:
            output_file.write(
                json.dumps(data, indent=2)
            )

class NewProjectWorkspace(Workspace):
    def __init__(self, name: str, working_directory: str) -> None:
        self._name = name

        super().__init__(working_directory)

    def create(self) -> dict:
        if os.path.exists(self._working_directory):
            raise SystemError('Workspace already exists.')

        settings = {
            'name': self._name,
        }
        
        os.mkdir(self._working_directory)
        self.save_data(
            'settings.json',
            settings
        )

        settings.update({
            'path': self._working_directory
        })

        return settings
    
def get_project_path_from_name(working_directory: str, name: str) -> str:
    folder_name = re.sub(r' +', '-', name)
    return os.path.join(working_directory, folder_name)

def create_new_project_workspace(working_directory: str, name: str) -> NewProjectWorkspace:
    return NewProjectWorkspace(
        name,
        get_project_path_from_name(working_directory, name)
    )
