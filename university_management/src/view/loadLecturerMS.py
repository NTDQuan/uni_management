from PyQt5.QtWidgets import QMainWindow

from university_management.src.view.lecturerMainScreen import Ui_MainWindow


class LecturerMainScreen(QMainWindow):
    def __init__(self):
        super(LecturerMainScreen, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.studentListBtn.setChecked(True)

        self.ui.studentListBtn.clicked.connect(self.switch_to_studentList_page)
        self.ui.lecturerListBtn.clicked.connect(self.switch_to_lecturerList_page)
        self.ui.majorListBtn.clicked.connect(self.switch_to_majorList_page)
        self.ui.classListBtn.clicked.connect(self.switch_to_classList_page)
        self.ui.courseListBtn.clicked.connect(self.switch_to_courseList_page)

    def switch_to_studentList_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_lecturerList_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_majorList_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_classList_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def switch_to_courseList_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
