from typing import Dict, Any

import os
import json

from ...common.exceptions import NotFoundError
from ..common import AbstractOperation
from .commands import LoadDataArgs, \
                      SaveDataArgs


class LoadDataOperation(AbstractOperation[Dict[str, Any]]):
    def __init__(self, args: LoadDataArgs) -> None:
        self._args = args

    def execute(self) -> Dict[str, Any]:
        if not os.path.exists(self._args.working_directory):
            raise NotFoundError(message='Workspace does not exist.')
        
        file_path = os.path.join(self._args.working_directory, self._args.file_name)
        with open(file_path, 'r', encoding='utf8') as input_file:
            return json.loads(input_file.read())

class SaveDataOperation(AbstractOperation[None]):
    def __init__(self, args: SaveDataArgs) -> None:
        self._args = args

    def execute(self) -> None:
        if not os.path.exists(self._args.working_directory):
            raise NotFoundError(message='Workspace does not exist.')
        
        file_path = os.path.join(self._args.working_directory, self._args.file_name)
        with open(file_path, 'w', encoding='utf8') as output_file:
            output_file.write(
                json.dumps(self._args.data, indent=2)
            )
