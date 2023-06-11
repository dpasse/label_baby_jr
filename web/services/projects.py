from typing import List, Dict, Any

import os
from .repositories import filesystem as db


class ProjectService():
    def __init__(self, working_directory: str) -> None:
        self._working_directory = working_directory

    def get(self) -> List[Dict[str, Any]]:
        projects: List[Dict[str, Any]] = []
        for project_directory in db.get_directories(self._working_directory):
            settings = db.load_data(
                os.path.join(project_directory, 'settings.json')
            )

            settings.update({
                'path': project_directory,
            })

            projects.append(settings)

        return projects
