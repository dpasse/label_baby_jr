from typing import List, Dict, Any, Optional

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

    def get_project(self, identifier: str) -> Optional[Dict[str, Any]]:
        workspace_path = os.path.join(self._workspace_directory, identifier)

        if not os.path.exists(workspace_path):
            return None
        
        if not os.path.isdir(workspace_path):
            return None

        args = LoadProjectSettings.create(
            os.path.join(self._workspace_directory, identifier)
        )

        return LoadDataOperation(args).execute()

    def get_all_projects(self) -> List[Dict[str, Any]]:
        operations = (
            self.get_project(identifier)
            for identifier in os.listdir(self._workspace_directory)
        )
        
        return list(
            filter(lambda op: not op is None, operations)
        )
    
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
