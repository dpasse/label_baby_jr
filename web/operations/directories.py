import os
import shutil

from dataclasses import dataclass

from .abstracts import AbstractOperation


@dataclass()
class CreateDirectoryArgs:
    directory_path: str
    must_create: bool

    @staticmethod
    def create(directory_path: str, must_create=False):
        return CreateDirectoryArgs(directory_path, must_create)

class CreateDirectoryOperation(AbstractOperation[None]):
    def __init__(self, args: CreateDirectoryArgs) -> None:
        self._args = args

    def execute(self) -> None:
        if self._args.must_create and os.path.exists(self._args.directory_path):
            raise SystemError(message='Directory already exists.')
        
        os.mkdir(self._args.directory_path)

@dataclass()
class DeleteDirectoryArgs:
    directory_path: str

    @staticmethod
    def create(directory_path: str):
        return DeleteDirectoryArgs(directory_path)

class DeleteDirectoryOperation(AbstractOperation[None]):
    def __init__(self, args: DeleteDirectoryArgs) -> None:
        self._args = args

    def execute(self) -> None:
        if os.path.exists(self._args.directory_path):
            shutil.rmtree(self._args.directory_path)
