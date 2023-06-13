from dataclasses import dataclass


@dataclass()
class DeleteDirectoryArgs:
    directory_path: str

    @staticmethod
    def create(directory_path: str):
        return DeleteDirectoryArgs(directory_path)

@dataclass()
class CreateDirectoryArgs:
    directory_path: str
    must_create: bool

    @staticmethod
    def create(directory_path: str, must_create=False):
        return CreateDirectoryArgs(directory_path, must_create)
