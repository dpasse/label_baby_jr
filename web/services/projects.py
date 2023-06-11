from typing import List, Dict, Any

import os

from ..operations.data import LoadDataOperation
from ..operations.project import ProjectOperationArgs, \
                                 CreateProjectOperationArgs, \
                                 CreateProjectOperation, \
                                 DeleteProjectOperation, \
                                 LoadProjectSettings


class WorkspaceService():
    def __init__(self, workspace_directory: str) -> None:
        self._workspace_directory = workspace_directory

    def get_all_projects(self) -> List[Dict[str, Any]]:
        operations = (
            LoadDataOperation(
                LoadProjectSettings.create(project)
            )
            for project in (
                os.path.join(self._workspace_directory, item)
                for item in os.listdir(self._workspace_directory)
            )
            if os.path.isdir(project)
        )
        
        return [
            operation.execute()
            for operation in operations
        ]
    
    def create(self, project_name: str) -> Dict[str, Any]:
        args = CreateProjectOperationArgs.create(
            self._workspace_directory,
            project_name
        )

        return CreateProjectOperation(args).execute()
    
    def delete(self, id: str) -> None:
        args = ProjectOperationArgs.create(
            self._workspace_directory,
            id
        )

        DeleteProjectOperation(args).execute()
