from PyQt5.QtWidgets import QApplication
from view.LoginView import LoginView
from database.CreateTable import create_all_table
from controller.authentication.Authenticator import Authentication
from controller.user_management.UserCommand import Invoker, CreateUserCommand, DeleteUserCommand
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

def run():
    create_all_table()
    auth = Authentication()
    auth.authentication("21522499", "1")
    invoker = Invoker()

    command = CreateUserCommand(user, per_info)
    invoker.set_on_start(command)
    invoker.createUser()

    command = DeleteUserCommand(21522499)
    invoker.set_on_start(command)
    invoker.deleteUser()



if __name__ == "__main__":
    run()


'''
def main():
    app = QApplication(sys.argv)
    mysql_pooling = ConnectionPoolHolder().getConnectionPool
    login_view = LoginView()
    login_view.showLogin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''

