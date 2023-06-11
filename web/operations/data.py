from typing import Dict, Any

import os
import json

from dataclasses import dataclass

from .abstracts import AbstractOperation


@dataclass()
class LoadDataArgs:
    working_directory: str
    file_name: str

    @staticmethod
    def create(working_directory: str, file_name: str):
        return LoadDataArgs(working_directory, file_name)

class LoadDataOperation(AbstractOperation[Dict[str, Any]]):
    def __init__(self, args: LoadDataArgs) -> None:
        self._args = args

    def execute(self) -> Dict[str, Any]:
        if not os.path.exists(self._args.working_directory):
            raise SystemError(message='Workspace does not exist.')
        
        file_path = os.path.join(self._args.working_directory, self._args.file_name)
        with open(file_path, 'r', encoding='utf8') as input_file:
            return json.loads(input_file.read())

@dataclass()
class SaveDataArgs(LoadDataArgs):
    data: Dict[str, Any]

    @staticmethod
    def create(working_directory: str, file_name: str, data: Dict[str, Any]):
        return SaveDataArgs(working_directory, file_name, data)

class SaveDataOperation(AbstractOperation[None]):
    def __init__(self, args: SaveDataArgs) -> None:
        self._args = args

    def execute(self) -> None:
        if not os.path.exists(self._args.working_directory):
            raise SystemError(message='Workspace does not exist.')
        
        file_path = os.path.join(self._args.working_directory, self._args.file_name)
        with open(file_path, 'w', encoding='utf8') as output_file:
            output_file.write(
                json.dumps(self._args.data, indent=2)
            )