from typing import List, Dict, Any

import os
from ..repositories.filesystem import Workspace, create_new_project_workspace


class ProjectService():
    def get_all(self, workspace_directory: str) -> List[Dict[str, Any]]:
        directories = (
            project
            for project in (
                os.path.join(workspace_directory, item)
                for item in os.listdir(workspace_directory)
            )
            if os.path.isdir(project)
        )

        projects: List[Dict[str, Any]] = []
        for project_directory in directories:
            settings = Workspace(project_directory).load_data('settings.json')
            projects.append(settings)

        return projects
    
    def create(self, workspace_directory: str, name: str) -> Dict[str, Any]:
        new_project_workspace = create_new_project_workspace(
            name,
            workspace_directory
        )

        return new_project_workspace.create()
