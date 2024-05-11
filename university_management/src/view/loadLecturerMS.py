from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton, QMessageBox

from university_management.src.controller.major_management.get_major import get_major_id
from university_management.src.controller.user_management.remove_user import deleteUser, deleteStudent
from university_management.src.util.getGenderId import get_gender_id
from university_management.src.view.lecturerMainScreen import Ui_MainWindow
from university_management.src.controller.user_management.get_user_info import get_student_for_display_table, search_student

class LecturerMainScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.studentListBtn.setChecked(True)

        self.studentListBtn.clicked.connect(self.switch_to_studentList_page)
        self.lecturerListBtn.clicked.connect(self.switch_to_lecturerList_page)
        self.majorListBtn.clicked.connect(self.switch_to_majorList_page)
        self.classListBtn.clicked.connect(self.switch_to_classList_page)
        self.courseListBtn.clicked.connect(self.switch_to_courseList_page)

        self.addBtn.clicked.connect(self.open_addStudent_dialog)

        #Load data
        self.load_students_info()
        self.gender_comboBox.currentIndexChanged.connect(self.reload_data)
        self.major_comboBox.currentIndexChanged.connect(self.reload_data)
        self.searchBarEdit.textChanged.connect(self.search_student)

        #Controll columns width
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 180)

    def switch_to_studentList_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_lecturerList_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_majorList_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_classList_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_courseList_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def open_addStudent_dialog(self):
        from add_student_dialog import Ui_add_student_dialog
        addStudent_dialog = Ui_add_student_dialog(self)
        result = addStudent_dialog.exec()

        if result == Ui_add_student_dialog.Accepted:
            self.reload_data()

    def load_students_info(self):
        print("Loading all student data...")
        self.tableWidget.setRowCount(0)

        selected_major = self.major_comboBox.currentText()
        selected_gender = self.gender_comboBox.currentText()

        data = self.get_data_from_table(selected_major, selected_gender)

        for row_index, row_data in enumerate(data):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

            # Action widget
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
            self.tableWidget.setCellWidget(row_index, 4, double_button_widget)
            self.tableWidget.setRowHeight(row_index, 50)

    def get_data_from_table(self, major_filler, gender_filler):

        data = get_student_for_display_table(major_filler, gender_filler)

        if data:
            for student in data:
                print(f"Student ID: {student[0]}")
                print(f"Full Name: {student[1]}")
                # Uncomment the following lines if you have gender and major relationships defined
                print(f"Major: {student[2]}")  # Assuming gender information is available
                print(f"Khoa học máy tính: {student[3]}")  # Assuming major information is available
                print("-" * 20)  # Separator
        else:
            print("No students found based on the provided filters.")
        return data

    def reload_data(self):
        self.tableWidget.clearContents()
        self.load_students_info()

    def search_student(self):
        self.tableWidget.setRowCount(0)
        query = self.searchBarEdit.text()
        data = search_student(query)
        for row_index, row_data in enumerate(data):
            self.tableWidget.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.tableWidget.setItem(row_index, col_index, item)

            # Action widget
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
            self.tableWidget.setCellWidget(row_index, 4, double_button_widget)
            self.tableWidget.setRowHeight(row_index, 50)



class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data, lecturerMainScreen):
        super().__init__()

        self.row_index = row_index
        self.row_data = row_data
        self.lecturerMainScreen = lecturerMainScreen

        self.student_id = self.row_data[0]

        layout = QHBoxLayout(self)

        self.edit_button = QPushButton("Sửa", self)
        self.edit_button.setStyleSheet("background-color: blue; color: white")
        self.edit_button.setFixedSize(61, 31)

        self.delete_button = QPushButton("Xóa", self)
        self.delete_button.setStyleSheet("background-color: red; color: white")
        self.delete_button.setFixedSize(61, 31)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        #Button logic
        self.edit_button.clicked.connect(self.edit_clicked)
        self.delete_button.clicked.connect(self.delete_clicked)

    def edit_clicked(self):
        from update_student_dialog import Ui_update_student_dialog
        self.update_dialog = Ui_update_student_dialog(self.row_index, self.row_data)

        #Connect the custom signal reload data after update record
        self.update_dialog.data_updated.connect(self.lecturerMainScreen.reload_data)

        self.update_dialog.exec()

    def delete_clicked(self):

        message = QMessageBox.question(
            self,
            'Xác nhận', 'Bạn có chắc chắn muốn xóa học sinh này không ?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if message == QMessageBox.StandardButton.Yes:
            deleteStudent(self.student_id)

        self.lecturerMainScreen.reload_data()