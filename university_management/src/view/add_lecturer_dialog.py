# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_lecturer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from university_management.src.controller.major_management.get_major import get_major_id, get_all_major
from university_management.src.controller.user_management.UserCommand import Invoker, CreateUserCommand
from university_management.src.database.initSession import session
from university_management.src.model.Model import User
from university_management.src.util.getFirstAndLastName import getFirstAndLastName
from university_management.src.util.getGenderId import get_gender_id


class Ui_add_lecturer_dialog(QDialog):
    """
    add lecturer dialog
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Dialog")
        self.resize(466, 517)
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 441, 361))
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
        self.lecturerIDEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lecturerIDEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lecturerIDEdit.setObjectName("lecturerIDEdit")
        self.verticalLayout.addWidget(self.lecturerIDEdit)
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
        self.lecturerGender_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.lecturerGender_comboBox.setObjectName("lecturerGender_comboBox")
        self.lecturerGender_comboBox.addItem("")
        self.lecturerGender_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.lecturerGender_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.lecturerMajor_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.lecturerMajor_comboBox.setObjectName("lecturerMajor_comboBox")
        major_list = get_all_major()
        print(len(major_list))
        for major in major_list:
            self.lecturerMajor_comboBox.addItem(major)
        self.verticalLayout_3.addWidget(self.lecturerMajor_comboBox)
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
        self.lecturerNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lecturerNameEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lecturerNameEdit.setObjectName("lecturerNameEdit")
        self.verticalLayout_5.addWidget(self.lecturerNameEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.lecturerPhoneEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lecturerPhoneEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lecturerPhoneEdit.setObjectName("lecturerPhoneEdit")
        self.verticalLayout_6.addWidget(self.lecturerPhoneEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.lecturerAddressEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lecturerAddressEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lecturerAddressEdit.setObjectName("lecturerAddressEdit")
        self.verticalLayout_7.addWidget(self.lecturerAddressEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.layoutWidget_2 = QtWidgets.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(250, 460, 201, 43))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addLecturer_Btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.addLecturer_Btn.setMinimumSize(QtCore.QSize(0, 41))
        self.addLecturer_Btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}")
        self.addLecturer_Btn.setObjectName("addLecturer_Btn")
        self.horizontalLayout_2.addWidget(self.addLecturer_Btn)
        self.cancelAddLecturer_Btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.cancelAddLecturer_Btn.setMinimumSize(QtCore.QSize(0, 41))
        self.cancelAddLecturer_Btn.setStyleSheet("QPushButton {\n"
"    background-color: red;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}")
        self.cancelAddLecturer_Btn.setObjectName("cancelAddLecturer_Btn")
        self.horizontalLayout_2.addWidget(self.cancelAddLecturer_Btn)
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
        self.label_2.setText(_translate("Dialog", "Mã số giảng viên"))
        self.label_5.setText(_translate("Dialog", "Giới tính"))
        self.lecturerGender_comboBox.setItemText(0, _translate("Dialog", "Nam"))
        self.lecturerGender_comboBox.setItemText(1, _translate("Dialog", "Nữ"))
        self.label_6.setText(_translate("Dialog", "Ngành"))
        self.label_3.setText(_translate("Dialog", "Họ tên"))
        self.label_4.setText(_translate("Dialog", "Số điện thoại"))
        self.label_8.setText(_translate("Dialog", "Địa chỉ"))
        self.addLecturer_Btn.setText(_translate("Dialog", "Thêm"))
        self.cancelAddLecturer_Btn.setText(_translate("Dialog", "Hủy"))
        self.label.setText(_translate("Dialog", "Thêm giảng viên mới"))

        #button logic
        self.addLecturer_Btn.clicked.connect(self.add_lecturer)
        self.cancelAddLecturer_Btn.clicked.connect(self.close)



    def getInfo(self):
        """
        get user input
        """
        print("Get info...")
        user_info = {
            "User_id": self.lecturerIDEdit.text(),
            "Password": "1",
            "User_email": self.lecturerIDEdit.text() + "@gm.uit.edu.vn",
            "User_role": 2
        }
        lastName, firstName = getFirstAndLastName(self.lecturerNameEdit.text())
        lecturer_info = {
            "Lecturer_id": self.lecturerIDEdit.text(),
            "firstName": firstName,
            "lastName": lastName,
            "telephone": self.lecturerPhoneEdit.text(),
            "address": self.lecturerAddressEdit.text(),
            "profile_image": "image",
            "gender": get_gender_id(self.lecturerGender_comboBox.currentText()),
            "major":  get_major_id(self.lecturerMajor_comboBox.currentText()),
        }
        return user_info, lecturer_info

    def add_new_lecturer(self):
        """
        add new lecturer
        """
        user_info, lecturer_info = self.getInfo()
        if not self.isUserExist(user_info["User_id"]):
            print("add new lecturer...")
            invoker = Invoker()
            command = CreateUserCommand(user_info, lecturer_info)
            invoker.set_on_start(command)
            invoker.createUser()
            self.show_added_message()

    def isUserExist(self, userID):
        """
        check if user id already exist in database
        args:
            userID(int)
        return
            True if user is exist
            False if user is not exist
        """
        user = session.query(User).get(userID)
        if user:
            return True
        else:
            return False

    def show_added_message(self):
        """
        create message
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText("Đã thêm thành công")
        msg_box.exec()


    def add_lecturer(self):
        """
        add lecturer and emit signal
        """
        self.add_new_lecturer()
        self.accept()

