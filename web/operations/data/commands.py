from typing import Any, Dict
from dataclasses import dataclass


@dataclass()
class LoadDataArgs:
    working_directory: str
    file_name: str

    @staticmethod
    def create(working_directory: str, file_name: str):
        return LoadDataArgs(working_directory, file_name)

@dataclass()
class SaveDataArgs(LoadDataArgs):
    data: Dict[str, Any]

    @staticmethod
    def create(working_directory: str, file_name: str, data: Dict[str, Any]):
        return SaveDataArgs(working_directory, file_name, data)
