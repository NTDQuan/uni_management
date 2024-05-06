from abc import ABC, abstractmethod
from .add_course import add_course
from .remove_course import delete_course

class CourseCommand(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class CreateCourseCommand(CourseCommand):
    def __init__(self, course_data: dict):
        self.course_data = course_data

    def execute(self) -> None:
        add_course(self.course_data)

class DeleteCourseCommand(CourseCommand):
    def __init__(self, courseID):
        self.courseID = courseID

    def execute(self) -> None:
        delete_course(self.courseID)

class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: CourseCommand):
        self._on_start = command

    def set_on_finish(self, command: CourseCommand):
        self._on_finish = command

    def createCourse(self) -> None:
        print('Start adding')
        if isinstance(self._on_start, CourseCommand):
            self._on_start.execute()

    def deleteCourse(self) -> None:
        print('Start deleting')
        if isinstance(self._on_start, CourseCommand):
            self._on_start.execute()
