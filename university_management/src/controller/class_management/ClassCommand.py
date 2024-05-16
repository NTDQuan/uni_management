from abc import ABC, abstractmethod

from .add_class import add_class
from .remove_class import delete_class


class ClassCommand(ABC):
    """
    Abstract class for command
    """
    @abstractmethod
    def execute(self) -> None:
        pass

class CreateClassCommand(ClassCommand):
    """
    Create command
    """
    def __init__(self, class_data: dict):
        self.class_data = class_data

    def execute(self) -> None:
        add_class(self.class_data)

class DeleteClassCommand(ClassCommand):
    """
    Handle delete class command
    """
    def __init__(self, classID):
        self.classID = classID

    def execute(self) -> None:
        delete_class(self.classID)

class Invoker:
    """
    Invoker
    """
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: ClassCommand):
        self._on_start = command

    def set_on_finish(self, command: ClassCommand):
        self._on_finish = command

    def createClass(self) -> None:
        print('Start adding')
        if isinstance(self._on_start, ClassCommand):
            self._on_start.execute()

    def deleteClass(self) -> None:
        print('Start deleting')
        if isinstance(self._on_start, ClassCommand):
            self._on_start.execute()