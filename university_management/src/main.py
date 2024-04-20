from PyQt5.QtWidgets import QApplication
from view.LoginView import LoginView
from database.CreateTable import create_all_table

import sys

def run():
    create_all_table()

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

