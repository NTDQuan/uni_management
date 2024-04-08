import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class LoginView():
    def __init__(self):
        self.__desktop_widget =  QDesktopWidget()
        self.__window = QWidget()
        self.__screen_geometry = self.__desktop_widget.screenGeometry()
        self.__window.setGeometry(100, 100, 400 , 500)
        self.__window.setWindowTitle("Uni Management")
        self.__window.setFixedSize(900, 800)
        self.__window_geometry = self.__window.geometry()

        #center window
        x_pos = int((self.__screen_geometry.width() - self.__window_geometry.width()) / 2)
        y_pos = int((self.__screen_geometry.height() - self.__window_geometry.height()) / 2)
        self.__window.move(x_pos, y_pos)

        self.__layout = QFormLayout()

        self.__label = QLabel(self.__window)
        self.__label.setText("Đăng nhập")
        self.__label.setFont(QFont("Poppin", 16))

        self.__usernameLineEdit = QLineEdit()
        self.__usernameLineEdit.setFixedSize(200, 30)

        self.__passwordLineEdit = QLineEdit()
        self.__passwordLineEdit.setFixedSize(200, 30)
        
        self.__layout.addRow(self.__label)
        self.__layout.addRow('' ,self.__usernameLineEdit)
        self.__layout.addRow('' ,self.__passwordLineEdit)

        self.__window.setLayout(self.__layout)



    def showLogin(self):
        self.__window.show()