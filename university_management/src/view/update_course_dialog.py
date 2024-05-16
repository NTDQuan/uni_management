# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_course_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox

from university_management.src.controller.course_management.edit_course import editCourse
from university_management.src.controller.course_management.get_course_info import get_course_for_display_table, \
        get_full_course_info
from university_management.src.controller.major_management.get_major import get_all_major, get_major_id


class Ui_update_course_dialog(QDialog):
    """
    update course dialog GUI
    """
    data_updated = pyqtSignal()

    def __init__(self, row_index, row_data):
        super().__init__()
        self.row_index = row_index
        self.row_data = row_data
        self.course_info = get_full_course_info(self.row_data[0])

        #get selected course info
        self.course_id_info = self.course_info[0]
        print(self.course_id_info)
        self.course_name_info = self.course_info[1]
        self.course_credit_info = self.course_info[2]
        self.course_major_info = self.course_info[3]

        self.setObjectName("Dialog")
        self.resize(466, 400)
        self.setStyleSheet("QDialog {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid rgb(31, 149, 239);\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"    border: 1px solid rgb(31, 149, 239);\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 31px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid rgb(31, 149, 239);\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 31px;\n"
"}")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 60, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 441, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.courseIDEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.courseIDEdit.setEnabled(False)
        self.courseIDEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.courseIDEdit.setObjectName("courseIDEdit")
        self.verticalLayout.addWidget(self.courseIDEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.numCredit_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.numCredit_comboBox.setObjectName("numCredit_comboBox")
        self.numCredit_comboBox.addItem("")
        self.numCredit_comboBox.addItem("")
        self.numCredit_comboBox.addItem("")
        self.numCredit_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.numCredit_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.courseMajor_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.courseMajor_comboBox.setObjectName("courseMajor_comboBox")
        major_list = get_all_major()
        print(len(major_list))
        for major in major_list:
            self.courseMajor_comboBox.addItem(major)
        self.verticalLayout_3.addWidget(self.courseMajor_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.courseNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.courseNameEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.courseNameEdit.setObjectName("courseNameEdit")
        self.verticalLayout_5.addWidget(self.courseNameEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.layoutWidget_2 = QtWidgets.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(250, 350, 201, 43))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.update_Btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.update_Btn.setMinimumSize(QtCore.QSize(0, 41))
        self.update_Btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}")
        self.update_Btn.setObjectName("update_Btn")
        self.horizontalLayout_2.addWidget(self.update_Btn)
        self.cancel_Btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.cancel_Btn.setMinimumSize(QtCore.QSize(0, 41))
        self.cancel_Btn.setStyleSheet("QPushButton {\n"
"    background-color: red;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}")
        self.cancel_Btn.setObjectName("cancel_Btn")
        self.horizontalLayout_2.addWidget(self.cancel_Btn)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Mã môn học"))
        self.label_5.setText(_translate("Dialog", "Số tín chỉ"))
        self.numCredit_comboBox.setItemText(0, _translate("Dialog", "1"))
        self.numCredit_comboBox.setItemText(1, _translate("Dialog", "2"))
        self.numCredit_comboBox.setItemText(2, _translate("Dialog", "3"))
        self.numCredit_comboBox.setItemText(3, _translate("Dialog", "4"))
        self.label_6.setText(_translate("Dialog", "Ngành"))
        self.label_3.setText(_translate("Dialog", "Tên môn học"))
        self.update_Btn.setText(_translate("Dialog", "Sửa"))
        self.cancel_Btn.setText(_translate("Dialog", "Hủy"))
        self.label.setText(_translate("Dialog", "Chỉnh sửa thông tin"))

        self.courseIDEdit.setText(str(self.course_id_info))
        self.courseNameEdit.setText(str(self.course_name_info))
        self.numCredit_comboBox.setCurrentText(str(self.course_credit_info))
        self.courseMajor_comboBox.setCurrentText(str(self.course_major_info))

        self.update_Btn.clicked.connect(self.update_course)
        self.cancel_Btn.clicked.connect(self.close)

        from loadLecturerMS import LecturerMainScreen
        self.update_major = LecturerMainScreen()
        self.update_major.majorListUpdated.connect(self.update_major_comboBox)

    def update_course(self):
        """
        update course button logic
        """
        params = {
            "course_id": self.course_id_info,
            "course_name": self.courseNameEdit.text(),
            "course_credit": int(self.numCredit_comboBox.currentText()),
            "major" : int(get_major_id(self.courseMajor_comboBox.currentText()))
        }

        editCourse(self.course_id_info, params)
        self.show_updated_message()

        self.data_updated.emit()
        self.close()

    def show_updated_message(self):
        """
        show update message
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText("Đã sửa thành công")
        msg_box.exec()

    def update_major_comboBox(self, new_major_list):
        """
        update major selection if major table change
        """
        self.courseMajor_comboBox.clear()
        for major in new_major_list:
            self.courseMajor_comboBox.addItem(major)



