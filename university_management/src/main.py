from PyQt5.QtWidgets import QApplication
from database.ConnectionPoolHolder import ConnectionPoolHolder
from view.LoginView import LoginView

import sys

def main():
    app = QApplication(sys.argv)
    mysql_pooling = ConnectionPoolHolder().getConnectionPool
    login_view = LoginView()
    login_view.showLogin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()