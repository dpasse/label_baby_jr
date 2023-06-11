from typing import List
import os


class ProjectService():
    def __init__(self, working_directory: str) -> None:
        self._working_directory = working_directory

    def get(self) -> List[str]:
        projects = [
            item
            for item in os.listdir(
                self._working_directory
            )
            if os.path.isdir(
                os.path.join(self._working_directory, item)
            )
        ]

        return projects
