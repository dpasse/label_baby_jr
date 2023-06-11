from typing import List, Dict, Any

import os

from ..operations.data import LoadDataOperation
from ..operations.project import CreateProjectOperationArgs, \
                                 CreateProjectOperation, \
                                 LoadProjectSettings


class ProjectService():
    def get_all_projects(self, workspace_directory: str) -> List[Dict[str, Any]]:
        operations = (
            LoadDataOperation(
                LoadProjectSettings.create(project)
            )
            for project in (
                os.path.join(workspace_directory, item)
                for item in os.listdir(workspace_directory)
            )
            if os.path.isdir(project)
        )
        
        return [
            operation.execute()
            for operation in operations
        ]
    
    def create(self, workspace_directory: str, project_name: str) -> Dict[str, Any]:
        args = CreateProjectOperationArgs.create(
            workspace_directory,
            project_name
        )

        return CreateProjectOperation(args).execute()
