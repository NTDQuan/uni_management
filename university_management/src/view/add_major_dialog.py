# -*- coding: utf-8 -*-
from random import randint

# Form implementation generated from reading ui file 'add_major_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from university_management.src.controller.major_management.MajorCommand import Invoker, CreateMajorCommand
from university_management.src.database.initSession import session
from university_management.src.model.Model import Major


class Ui_add_major_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("add_major_dialog")
        self.resize(466, 242)
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 441, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.majorNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.majorNameEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.majorNameEdit.setObjectName("majorNameEdit")
        self.verticalLayout_5.addWidget(self.majorNameEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.layoutWidget_2 = QtWidgets.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(250, 190, 201, 43))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_Btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.add_Btn.setMinimumSize(QtCore.QSize(0, 41))
        self.add_Btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}")
        self.add_Btn.setObjectName("add_Btn")
        self.horizontalLayout_2.addWidget(self.add_Btn)
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
        self.label_3.setText(_translate("Dialog", "Tên ngành"))
        self.add_Btn.setText(_translate("Dialog", "Thêm"))
        self.cancel_Btn.setText(_translate("Dialog", "Hủy"))
        self.label.setText(_translate("Dialog", "Thêm ngành mới"))

        self.add_Btn.clicked.connect(self.add_major)
        self.cancel_Btn.clicked.connect(self.close)

    def getInfo(self):
        print("Get info...")
        major_info = {
            "major_id": self.generate_majorID(),
            "major_name": self.majorNameEdit.text()
        }
        return major_info

    def add_new_major(self):
        major_info = self.getInfo()
        print("add new lecturer...")
        invoker = Invoker()
        command = CreateMajorCommand(major_info)
        invoker.set_on_start(command)
        invoker.createMajor()
        self.show_added_message()

    def generate_majorID(self):
        majorID = randint(1, 1000)
        major = session.query(Major).get(majorID)
        if major:
            self.generate_majorID()
        else:
            return majorID

    def show_added_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText("Đã thêm thành công")
        msg_box.exec()

    def add_major(self):
        self.add_new_major()
        self.accept()
        print("Send accept signal")
