from typing import TypeVar, Generic

from abc import ABC, abstractmethod


T = TypeVar('T')

class AbstractOperation(ABC, Generic[T]):
    @abstractmethod
    def execute(self) -> T:
        pass
