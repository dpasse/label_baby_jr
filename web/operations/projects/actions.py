from typing import Dict, Any, List

import os

from ..common import AbstractOperation
from ..data import SaveDataOperation
from ..directories import CreateDirectoryArgs, \
                          CreateDirectoryOperation, \
                          DeleteDirectoryArgs, \
                          DeleteDirectoryOperation
from .commands import ProjectOperationArgs, \
                      CreateProjectOperationArgs, \
                      GetCreateProjectDataCommand, \
                      ProjectFile


class DeleteProjectOperation(AbstractOperation[None]):
    def __init__(self, args: ProjectOperationArgs) -> None:
        self._args = args

    def execute(self) -> None:
        working_directory = self._args.complete_project_path

        if not os.path.exists(working_directory):
            return
        
        DeleteDirectoryOperation(
            DeleteDirectoryArgs.create(working_directory)
        ).execute()

class CreateProjectOperation(AbstractOperation[Dict[str, Any]]):
    def __init__(self, args: CreateProjectOperationArgs) -> None:
        self._args = args

    def execute(self) -> Dict[str, Any]:
        working_directory = self._args.complete_project_path
        if os.path.exists(working_directory):
            raise SystemError('Workspace already exists.')

        settings = {
            'id': self._args.id,
            'name': self._args.name,
        }

        try:
            operations: List[AbstractOperation[None]] = [
                CreateDirectoryOperation(
                    CreateDirectoryArgs.create(working_directory)
                ),
                CreateDirectoryOperation(
                    CreateDirectoryArgs.create(os.path.join(working_directory, '1'))
                ),
                SaveDataOperation(
                    GetCreateProjectDataCommand.create(working_directory, ProjectFile.SETTINGS, settings),
                )
            ]

            for operation in operations:
                operation.execute()
        except:
            DeleteProjectOperation(self._args).execute()

            raise

        return settings
