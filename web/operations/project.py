from typing import Dict, Any, List

import os
import uuid

from dataclasses import dataclass
from .abstracts import AbstractOperation
from .data import LoadDataArgs, SaveDataArgs, SaveDataOperation
from .directories import CreateDirectoryArgs, \
                         CreateDirectoryOperation, \
                         DeleteDirectoryArgs, \
                         DeleteDirectoryOperation
from ..common.utils import get_project_path_from_name

@dataclass()
class LoadProjectSettings(LoadDataArgs):
    @staticmethod
    def create(working_directory: str):
        return LoadProjectSettings(working_directory, 'settings.json')

@dataclass()
class CreateProjectSettings(SaveDataArgs):
    @staticmethod
    def create(working_directory: str, data: Dict[str, Any]):
        return CreateProjectSettings(working_directory, 'settings.json', data)
    
@dataclass()
class ProjectOperationArgs:
    working_directory: str
    name: str

    @property
    def complete_project_path(self) -> str:
        return get_project_path_from_name(
            self.working_directory,
            self.name
        )
    
    @staticmethod
    def create(working_directory: str, project_name: str):
        return ProjectOperationArgs(working_directory, project_name)

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
    def __init__(self, args: ProjectOperationArgs) -> None:
        self._args = args

    def execute(self) -> Dict[str, Any]:
        working_directory = self._args.complete_project_path
        if os.path.exists(working_directory):
            raise SystemError('Workspace already exists.')

        settings = {
            'id': str(uuid.uuid4()),
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
                    CreateProjectSettings.create(working_directory, settings)
                )
            ]

            for operation in operations:
                operation.execute()
        except:
            DeleteProjectOperation(self._args).execute()

            raise

        return settings
