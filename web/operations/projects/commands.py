from typing import Dict, Any, List

import os
import uuid
import enum

from dataclasses import dataclass

from ..data.actions import LoadDataArgs, SaveDataArgs


class ProjectFile(enum.Enum):
    SETTINGS = 'settings.json'
    ENTITIES = 'entities.json'
    RELATIONS = 'relations.json'

    def __str__(self):
        return str(self.value)

class GetLoadProjectDataCommand(LoadDataArgs):
    @staticmethod
    def create(working_directory: str, project_file: ProjectFile):
        return LoadDataArgs(working_directory, str(project_file))
    
class GetCreateProjectDataCommand(LoadDataArgs):
    @staticmethod
    def create(working_directory: str, project_file: ProjectFile, data: Dict[str, Any]):
        return SaveDataArgs(working_directory, str(project_file), data)
    
@dataclass()
class ProjectOperationArgs:
    working_directory: str
    id: str

    @property
    def complete_project_path(self) -> str:
        return os.path.join(
            self.working_directory,
            self.id
        )
    
    @staticmethod
    def create(working_directory: str, id: str):
        return ProjectOperationArgs(working_directory, id)

@dataclass()
class CreateProjectOperationArgs(ProjectOperationArgs):
    name: str

    @staticmethod
    def create(working_directory: str, name: str):
        id = str(uuid.uuid4())
        return CreateProjectOperationArgs(working_directory, id, name)
