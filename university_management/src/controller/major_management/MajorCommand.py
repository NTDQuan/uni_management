from abc import ABC, abstractmethod

from university_management.src.controller.major_management.add_major import add_major
from university_management.src.controller.major_management.remove_major import delete_major


class MajorCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class CreateMajorCommand(MajorCommand):
    def __init__(self, major_data: dict):
        self.major_data = major_data

    def execute(self) -> None:
        add_major(self.major_data)

class DeleteMajorCommand(MajorCommand):
    def __init__(self, majorID):
        self.majorID = majorID

    def execute(self) -> None:
        delete_major(self.majorID)

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: MajorCommand):
        self._on_start = command

    def set_on_finish(self, command: MajorCommand):
        self._on_finish = command

    def createMajor(self):
        print('Start adding')
        if isinstance(self._on_start, MajorCommand):
            self._on_start.execute()

    def deleteCourse(self) -> None:
        print('Start deleting')
        if isinstance(self._on_start, MajorCommand):
            self._on_start.execute()