import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, pyqtSignal

from university_management.src.controller.authentication.Authenticator import Authentication
from university_management.src.view.loadLecturerMS import LecturerMainScreen

class LoginView(QWidget):
    """
    Login screen GUI
    """
    def __init__(self):
        super().__init__()
        self.authenticator = Authentication()
        self.main_screen = None
        # Set window properties
        self.setFixedSize(800, 500)
        self.setWindowTitle("Uni Management")

        # Create main layout (horizontal)
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Image widget (replace with your actual image loading authentication)
        self.image_label = QLabel()
        self.image_label.setFixedSize(400, 500)
        self.image_label.setStyleSheet("padding: 0px; margin: 0px; border-image: url(./asserts/login_cover.jpg) 0 0 0 400")

        self.right_half_widget = QWidget(self)
        self.right_half_widget.setFixedSize(400, 500)
        self.right_half_layout = QVBoxLayout(self.right_half_widget)
        self.right_half_layout.setContentsMargins(0, 0, 0, 0)

        # Existing login layout (move this inside widget_area)
        self.label = QLabel("Đăng nhập")
        self.label.setFont(QFont("Poppin", 24))
        self.label.setAlignment(Qt.AlignCenter)

        self.usernameLineEdit = QLineEdit()
        self.usernameLineEdit.setFixedSize(200, 60)
        self.usernameLineEdit.setAlignment(Qt.AlignHCenter)

        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setFixedSize(200, 60)
        self.passwordLineEdit.setAlignment(Qt.AlignHCenter)

        self.loginButton = QPushButton("Đăng nhập")
        self.loginButton.setFixedSize(200, 60)
        self.loginButton.clicked.connect(self.handleLoginButtonClick)

        self.right_half_layout.addWidget(self.label, alignment=Qt.AlignHCenter)
        self.right_half_layout.addWidget(self.usernameLineEdit, alignment=Qt.AlignHCenter)
        self.right_half_layout.addWidget(self.passwordLineEdit, alignment=Qt.AlignHCenter)
        self.right_half_layout.addWidget(self.loginButton, alignment=Qt.AlignHCenter)

        # Add image and widget area to main layout
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.right_half_widget)

    def openMainScreen(self):
        """
        open main screen if login successfully
        """
        if self.main_screen is None:  # If the main screen instance doesn't exist, create it
            self.main_screen = LecturerMainScreen()
        self.hide()
        self.main_screen.show()
  # Hide the login screen

    def handleLoginButtonClick(self):
        """
        login button logic
        """
        loginInfo = [self.usernameLineEdit.text(), self.passwordLineEdit.text()]
        response = self.authenticator.authentication(self.usernameLineEdit.text(), self.passwordLineEdit.text())
        print(response)
        if response == 1:
            print("entering main screen")
            self.openMainScreen()



    def showLogin(self):
        self.show()