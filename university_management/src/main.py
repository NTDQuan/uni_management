from PyQt5.QtWidgets import QApplication
from view.LoginView import LoginView
from database.CreateTable import create_all_table
from controller.authentication.Authenticator import Authentication
from controller.user_management.UserCommand import Invoker, CreateUserCommand, DeleteUserCommand
from controller.major_management import MajorCommand
from controller.class_management import ClassCommand
from config import state
from model.Model import *
import sys

user = {
    "User_id": 21522499,
    "Password": "1",
    "User_email": "21522499@gmm",
    "User_role": 3
}

per_info = {
    "Student_id": 21522499,
    "firstName": "Quan",
    "lastName": "Nguyen Tran Dinh",
    "telephone": "0398633229",
    "address": "UTTTTTT",
    "profile_image": "image",
    "gender": 1,
    "major": 1,
    "credit": 100,
    "year": 3,
    "period": 2
}

course_info = {
    "course_name": "ky thuat lap trinh python",
    "course_credit": 4,
    "major_id": 1
}

major_info = {
    "major_id": 1,
    "major_name": "Kỹ thuật máy tính"
}

class_info = {
    "class_name": "CS111",
    "semester": 1,
    "year": 2024,
    "lecturer_id": None,
    "course_id": 1,
    "status": "ONGOING",
    "start_period": 1,
    "end_period": 5,
    "day": 2
}
'''
def run():
    create_all_table()
    auth = Authentication()
    auth.authentication("21522499", "1")
    invoker = Invoker()

    invoker = MajorCommand.Invoker()
    """
    command = MajorCommand.CreateMajorCommand(major_info)
    invoker.set_on_start(command)
    invoker.createMajor()
    """

    invoker = ClassCommand.Invoker()
    command = ClassCommand.DeleteClassCommand("CS111")
    invoker.set_on_start(command)
    invoker.deleteClass()
    """
    invoker = Invoker()
    command = CreateUserCommand(user, per_info)
    invoker.set_on_start(command)
    invoker.createUser()

    command = DeleteUserCommand(21522499)
    invoker.set_on_start(command)
    invoker.deleteUser() 
    
    """
'''

def run():
    app = QApplication(sys.argv)
    login_view = LoginView()
    login_view.showLogin()
    sys.exit(app.exec_())

def main():
    run()

if __name__ == '__main__':
    main()



