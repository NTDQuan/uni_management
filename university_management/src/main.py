from PyQt5.QtWidgets import QApplication, QMainWindow

from view.LoginView import LoginView
from database.CreateTable import create_all_table
from controller.authentication.Authenticator import Authentication
from controller.user_management.UserCommand import Invoker, CreateUserCommand, DeleteUserCommand
from controller.major_management import MajorCommand
from controller.class_management import ClassCommand
from config import state
from model.Model import *
import sys


def run():
    create_all_table()
    app = QApplication(sys.argv)
    login_view = LoginView()
    login_view.showLogin()
    sys.exit(app.exec_())

def main():
    run()

if __name__ == '__main__':
    main()



