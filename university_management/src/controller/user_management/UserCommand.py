from abc import ABC, abstractmethod
from .add_user import UserFactory
from .remove_user import deleteUser


class UserCommand(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class CreateUserCommand(UserCommand):
    def __init__(self, user_data: dict, profile_data: dict):
        self._user_data = user_data
        self._profile_data = profile_data

    def execute(self):
        userFactory = UserFactory()
        userFactory.create_user(self._user_data, self._profile_data)
        print("Created successfully")

class DeleteUserCommand(UserCommand):
    def __init__(self, userID: int):
        self._userID = userID

    def execute(self):
        print("Delete user: " + str(self._userID))
        deleteUser(self._userID)


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: UserCommand):
        self._on_start = command

    def set_on_finish(self, command: UserCommand):
        self._on_finish = command

    def createUser(self) -> None:
        print('Start adding')
        if isinstance(self._on_start, UserCommand):
            self._on_start.execute()

    def deleteUser(self) -> None:
        print('Start deteting')
        if isinstance(self._on_start, UserCommand):
            self._on_start.execute()


