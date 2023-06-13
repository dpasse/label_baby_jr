import os
import shutil

from ..common import AbstractOperation
from .commands import CreateDirectoryArgs, \
                      DeleteDirectoryArgs


class CreateDirectoryOperation(AbstractOperation[None]):
    def __init__(self, args: CreateDirectoryArgs) -> None:
        self._args = args

    def execute(self) -> None:
        if self._args.must_create and os.path.exists(self._args.directory_path):
            raise SystemError(message='Directory already exists.')
        
        os.mkdir(self._args.directory_path)

class DeleteDirectoryOperation(AbstractOperation[None]):
    def __init__(self, args: DeleteDirectoryArgs) -> None:
        self._args = args

    def execute(self) -> None:
        if os.path.exists(self._args.directory_path):
            shutil.rmtree(self._args.directory_path)
