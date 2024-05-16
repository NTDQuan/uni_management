# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lecturerMainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

from university_management.src.controller.major_management.get_major import get_all_major


class Ui_MainWindow(object):
    """
    Main screen GUI
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 600)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.nav_bar_widget = QtWidgets.QWidget(self.centralwidget)
        self.nav_bar_widget.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.nav_bar_widget.setFont(font)
        self.nav_bar_widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    text-align: left;\n"
"    height: 30px;\n"
"    border:none;\n"
"    padding-left: 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #F5FAFE;\n"
"    color:  #1F95EF;\n"
"    font-weight: bold;\n"
"}")
        self.nav_bar_widget.setObjectName("nav_bar_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.nav_bar_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.nav_bar_widget)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/default_ava.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.nav_bar_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.studentListBtn = QtWidgets.QPushButton(self.nav_bar_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.studentListBtn.setFont(font)
        self.studentListBtn.setCheckable(True)
        self.studentListBtn.setAutoExclusive(True)
        self.studentListBtn.setObjectName("studentListBtn")
        self.verticalLayout.addWidget(self.studentListBtn)
        self.lecturerListBtn = QtWidgets.QPushButton(self.nav_bar_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.lecturerListBtn.setFont(font)
        self.lecturerListBtn.setCheckable(True)
        self.lecturerListBtn.setAutoExclusive(True)
        self.lecturerListBtn.setObjectName("lecturerListBtn")
        self.verticalLayout.addWidget(self.lecturerListBtn)
        self.majorListBtn = QtWidgets.QPushButton(self.nav_bar_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.majorListBtn.setFont(font)
        self.majorListBtn.setCheckable(True)
        self.majorListBtn.setAutoExclusive(True)
        self.majorListBtn.setObjectName("majorListBtn")
        self.verticalLayout.addWidget(self.majorListBtn)
        self.classListBtn = QtWidgets.QPushButton(self.nav_bar_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.classListBtn.setFont(font)
        self.classListBtn.setCheckable(True)
        self.classListBtn.setAutoExclusive(True)
        self.classListBtn.setObjectName("classListBtn")
        self.verticalLayout.addWidget(self.classListBtn)
        self.courseListBtn = QtWidgets.QPushButton(self.nav_bar_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.courseListBtn.setFont(font)
        self.courseListBtn.setCheckable(True)
        self.courseListBtn.setAutoRepeat(False)
        self.courseListBtn.setAutoExclusive(True)
        self.courseListBtn.setObjectName("courseListBtn")
        self.verticalLayout.addWidget(self.courseListBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 337, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.signoutBtn = QtWidgets.QPushButton(self.nav_bar_widget)
        self.signoutBtn.setObjectName("signoutBtn")
        self.verticalLayout_2.addWidget(self.signoutBtn)
        self.gridLayout.addWidget(self.nav_bar_widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.studentListPage = QtWidgets.QWidget()
        self.studentListPage.setObjectName("studentListPage")
        self.label_3 = QtWidgets.QLabel(self.studentListPage)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.addBtn = QtWidgets.QPushButton(self.studentListPage)
        self.addBtn.setGeometry(QtCore.QRect(10, 100, 120, 41))
        self.addBtn.setMinimumSize(QtCore.QSize(120, 41))
        self.addBtn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}")
        self.addBtn.setObjectName("addBtn")
        self.tableWidget = QtWidgets.QTableWidget(self.studentListPage)
        self.tableWidget.setGeometry(QtCore.QRect(10, 210, 650, 371))
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white\n"
"}\n"
"\n"
"QTableWidget {\n"
"    alternate-background-color: #BOEDF8;\n"
"    background-color: #F4F9FA;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.layoutWidget = QtWidgets.QWidget(self.studentListPage)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 160, 508, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gender_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.gender_comboBox.setMinimumSize(QtCore.QSize(101, 0))
        self.gender_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid rgb(31, 149, 239);\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 31px;\n"
"}")
        self.gender_comboBox.setObjectName("gender_comboBox")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.gender_comboBox)
        self.major_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.major_comboBox.setMinimumSize(QtCore.QSize(132, 0))
        self.major_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid rgb(31, 149, 239);\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 31px;\n"
"}")
        self.major_comboBox.setObjectName("major_comboBox")
        self.major_comboBox.addItem("")
        major_list = get_all_major()
        print(len(major_list))
        for major in major_list:
            self.major_comboBox.addItem(major)
        self.horizontalLayout_2.addWidget(self.major_comboBox)
        self.searchBarEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.searchBarEdit.setMinimumSize(QtCore.QSize(261, 31))
        self.searchBarEdit.setStyleSheet("QLineEdit {\n"
"    padding-left: 10px;\n"
"    border-radius: 8px;\n"
"    border: 1px solid rgb(31, 149, 239);\n"
"}")
        self.searchBarEdit.setObjectName("searchBarEdit")
        self.horizontalLayout_2.addWidget(self.searchBarEdit)
        self.stackedWidget.addWidget(self.studentListPage)
        self.lecturerListPage = QtWidgets.QWidget()
        self.lecturerListPage.setObjectName(u"lecturerListPage")
        self.label_4 = QtWidgets.QLabel(self.lecturerListPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(10, 10, 251, 71))
        self.label_4.setFont(font)
        self.addLecturerBtn = QtWidgets.QPushButton(self.lecturerListPage)
        self.addLecturerBtn.setObjectName(u"addLecturerBtn")
        self.addLecturerBtn.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.addLecturerBtn.setMinimumSize(QtCore.QSize(120, 41))
        self.addLecturerBtn.setStyleSheet(u"QPushButton {\n"
                                          "	background-color: rgb(31, 149, 239);\n"
                                          "	color: white;\n"
                                          "	border: none;\n"
                                          "	border-radius: 8px;\n"
                                          "	font-weight: bold;\n"
                                          "	font-size: 15px;\n"
                                          "}")
        self.lecturerTableWidget = QtWidgets.QTableWidget(self.lecturerListPage)
        if (self.lecturerTableWidget.columnCount() < 5):
            self.lecturerTableWidget.setColumnCount(5)
        __qtablewidgetitem5 = QtWidgets.QTableWidgetItem()
        self.lecturerTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QtWidgets.QTableWidgetItem()
        self.lecturerTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QtWidgets.QTableWidgetItem()
        self.lecturerTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QtWidgets.QTableWidgetItem()
        self.lecturerTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QtWidgets.QTableWidgetItem()
        self.lecturerTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.lecturerTableWidget.setObjectName(u"lecturerTableWidget")
        self.lecturerTableWidget.setGeometry(QtCore.QRect(10, 210, 650, 371))
        self.lecturerTableWidget.setStyleSheet(u"QHeaderView::section {\n"
                                               "	font-weight: bold;\n"
                                               "	background-color: rgb(31, 149, 239);\n"
                                               "	color: white\n"
                                               "}\n"
                                               "\n"
                                               "QTableWidget {\n"
                                               "	alternate-background-color: #BOEDF8;\n"
                                               "	background-color: #F4F9FA;\n"
                                               "}")
        self.widget = QtWidgets.QWidget(self.lecturerListPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QtCore.QRect(10, 160, 508, 35))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lecturerGender_comboBox = QtWidgets.QComboBox(self.widget)
        self.lecturerGender_comboBox.addItem("")
        self.lecturerGender_comboBox.addItem("")
        self.lecturerGender_comboBox.addItem("")
        self.lecturerGender_comboBox.setObjectName(u"lecturerGender_comboBox")
        self.lecturerGender_comboBox.setMinimumSize(QtCore.QSize(101, 0))
        self.lecturerGender_comboBox.setStyleSheet(u"QComboBox {\n"
                                                   "	border: 1px solid rgb(31, 149, 239);\n"
                                                   "	border-radius: 6px;\n"
                                                   "	padding-left: 15px;\n"
                                                   "	height: 31px;\n"
                                                   "}")

        self.horizontalLayout_3.addWidget(self.lecturerGender_comboBox)

        self.lecturerMajor_comboBox = QtWidgets.QComboBox(self.widget)
        self.lecturerMajor_comboBox.addItem("")
        major_list = get_all_major()
        print(len(major_list))
        for major in major_list:
            self.lecturerMajor_comboBox.addItem(major)
        self.lecturerMajor_comboBox.setObjectName(u"lecturerMajor_comboBox")
        self.lecturerMajor_comboBox.setMinimumSize(QtCore.QSize(132, 0))
        self.lecturerMajor_comboBox.setStyleSheet(u"QComboBox {\n"
                                                  "	border: 1px solid rgb(31, 149, 239);\n"
                                                  "	border-radius: 6px;\n"
                                                  "	padding-left: 15px;\n"
                                                  "	height: 31px;\n"
                                                  "}")

        self.horizontalLayout_3.addWidget(self.lecturerMajor_comboBox)

        self.lecturerSearchBarEdit = QtWidgets.QLineEdit(self.widget)
        self.lecturerSearchBarEdit.setObjectName(u"lecturerSearchBarEdit")
        self.lecturerSearchBarEdit.setMinimumSize(QtCore.QSize(261, 31))
        self.lecturerSearchBarEdit.setStyleSheet(u"QLineEdit {\n"
                                                 "	padding-left: 10px;\n"
                                                 "	border-radius: 8px;\n"
                                                 "	border: 1px solid rgb(31, 149, 239);\n"
                                                 "}")

        self.horizontalLayout_3.addWidget(self.lecturerSearchBarEdit)

        self.stackedWidget.addWidget(self.lecturerListPage)
        self.majorListPage = QtWidgets.QWidget()
        self.majorListPage.setObjectName("majorListPage")
        self.label_8 = QtWidgets.QLabel(self.majorListPage)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.addMajorBtn = QtWidgets.QPushButton(self.majorListPage)
        self.addMajorBtn.setGeometry(QtCore.QRect(10, 100, 120, 41))
        self.addMajorBtn.setMinimumSize(QtCore.QSize(120, 41))
        self.addMajorBtn.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(31, 149, 239);\n"
                                       "    color: white;\n"
                                       "    border: none;\n"
                                       "    border-radius: 8px;\n"
                                       "    font-weight: bold;\n"
                                       "    font-size: 15px;\n"
                                       "}")
        self.addMajorBtn.setObjectName("addMajorBtn")
        self.majorTableWidget = QtWidgets.QTableWidget(self.majorListPage)
        self.majorTableWidget.setGeometry(QtCore.QRect(10, 210, 650, 371))
        self.majorTableWidget.setStyleSheet("QHeaderView::section {\n"
                                            "    font-weight: bold;\n"
                                            "    background-color: rgb(31, 149, 239);\n"
                                            "    color: white\n"
                                            "}\n"
                                            "\n"
                                            "QTableWidget {\n"
                                            "    alternate-background-color: #BOEDF8;\n"
                                            "    background-color: #F4F9FA;\n"
                                            "}")
        self.majorTableWidget.setObjectName("majorTableWidget")
        self.majorTableWidget.setColumnCount(5)
        self.majorTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.majorTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.majorTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.majorTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.majorTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.majorTableWidget.setHorizontalHeaderItem(4, item)
        self.majorSearchBarEdit = QtWidgets.QLineEdit(self.majorListPage)
        self.majorSearchBarEdit.setGeometry(QtCore.QRect(10, 160, 261, 31))
        self.majorSearchBarEdit.setMinimumSize(QtCore.QSize(261, 31))
        self.majorSearchBarEdit.setStyleSheet("QLineEdit {\n"
                                              "    padding-left: 10px;\n"
                                              "    border-radius: 8px;\n"
                                              "    border: 1px solid rgb(31, 149, 239);\n"
                                              "}")
        self.majorSearchBarEdit.setObjectName("majorSearchBarEdit")
        self.stackedWidget.addWidget(self.majorListPage)
        self.classListPage = QtWidgets.QWidget()
        self.classListPage.setObjectName("classListPage")
        self.label_10 = QtWidgets.QLabel(self.classListPage)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.addClassBtn = QtWidgets.QPushButton(self.classListPage)
        self.addClassBtn.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.addClassBtn.setMinimumSize(QtCore.QSize(120, 41))
        self.addClassBtn.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(31, 149, 239);\n"
                                       "    color: white;\n"
                                       "    border: none;\n"
                                       "    border-radius: 8px;\n"
                                       "    font-weight: bold;\n"
                                       "    font-size: 15px;\n"
                                       "}")
        self.addClassBtn.setObjectName("addClassBtn")
        self.classSearchBarEdit = QtWidgets.QLineEdit(self.classListPage)
        self.classSearchBarEdit.setGeometry(QtCore.QRect(10, 160, 261, 31))
        self.classSearchBarEdit.setMinimumSize(QtCore.QSize(261, 31))
        self.classSearchBarEdit.setStyleSheet("QLineEdit {\n"
                                              "    padding-left: 10px;\n"
                                              "    border-radius: 8px;\n"
                                              "    border: 1px solid rgb(31, 149, 239);\n"
                                              "}")
        self.classSearchBarEdit.setObjectName("classSearchBarEdit")
        self.classTableWidget = QtWidgets.QTableWidget(self.classListPage)
        self.classTableWidget.setGeometry(QtCore.QRect(10, 210, 731, 371))
        self.classTableWidget.setStyleSheet("QHeaderView::section {\n"
                                            "    font-weight: bold;\n"
                                            "    background-color: rgb(31, 149, 239);\n"
                                            "    color: white\n"
                                            "}\n"
                                            "\n"
                                            "QTableWidget {\n"
                                            "    alternate-background-color: #BOEDF8;\n"
                                            "    background-color: #F4F9FA;\n"
                                            "}")
        self.classTableWidget.setObjectName("classTableWidget")
        self.classTableWidget.setColumnCount(11)
        self.classTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTableWidget.setHorizontalHeaderItem(10, item)
        self.stackedWidget.addWidget(self.classListPage)
        self.courseListPage = QtWidgets.QWidget()
        self.courseListPage.setObjectName("courseListPage")
        self.label_9 = QtWidgets.QLabel(self.courseListPage)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.addCourseBtn = QtWidgets.QPushButton(self.courseListPage)
        self.addCourseBtn.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.addCourseBtn.setMinimumSize(QtCore.QSize(120, 41))
        self.addCourseBtn.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(31, 149, 239);\n"
                                        "    color: white;\n"
                                        "    border: none;\n"
                                        "    border-radius: 8px;\n"
                                        "    font-weight: bold;\n"
                                        "    font-size: 15px;\n"
                                        "}")
        self.addCourseBtn.setObjectName("addCourseBtn")
        self.courseTableWidget = QtWidgets.QTableWidget(self.courseListPage)
        self.courseTableWidget.setGeometry(QtCore.QRect(10, 210, 650, 371))
        self.courseTableWidget.setStyleSheet("QHeaderView::section {\n"
                                             "    font-weight: bold;\n"
                                             "    background-color: rgb(31, 149, 239);\n"
                                             "    color: white\n"
                                             "}\n"
                                             "\n"
                                             "QTableWidget {\n"
                                             "    alternate-background-color: #BOEDF8;\n"
                                             "    background-color: #F4F9FA;\n"
                                             "}")
        self.courseTableWidget.setObjectName("courseTableWidget")
        self.courseTableWidget.setColumnCount(5)
        self.courseTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(4, item)
        self.courseSearchBarEdit = QtWidgets.QLineEdit(self.courseListPage)
        self.courseSearchBarEdit.setGeometry(QtCore.QRect(10, 160, 261, 31))
        self.courseSearchBarEdit.setMinimumSize(QtCore.QSize(261, 31))
        self.courseSearchBarEdit.setStyleSheet("QLineEdit {\n"
                                               "    padding-left: 10px;\n"
                                               "    border-radius: 8px;\n"
                                               "    border: 1px solid rgb(31, 149, 239);\n"
                                               "}")
        self.courseSearchBarEdit.setObjectName("courseSearchBarEdit")
        self.stackedWidget.addWidget(self.courseListPage)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.signoutBtn.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tên"))
        self.studentListBtn.setText(_translate("MainWindow", "DS học sinh"))
        self.lecturerListBtn.setText(_translate("MainWindow", "DS giảng viên"))
        self.majorListBtn.setText(_translate("MainWindow", "DS ngành"))
        self.classListBtn.setText(_translate("MainWindow", "DS lớp"))
        self.courseListBtn.setText(_translate("MainWindow", "DS môn"))
        self.signoutBtn.setText(_translate("MainWindow", "Đăng xuất"))
        self.label_3.setText(_translate("MainWindow", "Danh sách sinh viên"))
        self.addBtn.setText(_translate("MainWindow", "Thêm sinh viên"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MSSV"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ và tên"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngành"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Thao tác"))
        self.gender_comboBox.setItemText(0, _translate("MainWindow", "Giới tính"))
        self.gender_comboBox.setItemText(1, _translate("MainWindow", "Nam"))
        self.gender_comboBox.setItemText(2, _translate("MainWindow", "Nữ"))

        #get major list
        major_list = get_all_major()
        self.major_comboBox.setItemText(0, _translate("MainWindow", "Ngành"))
        major_index = 1
        print(len(major_list))
        for major in major_list:
            self.major_comboBox.setItemText(major_index, _translate("MainWindow", major_list[major_index - 1]))
        self.searchBarEdit.setPlaceholderText(_translate("MainWindow", "Tìm sinh viên ..."))
        self.label_4.setText(_translate("MainWindow", "Danh sách giảng viên"))
        self.addLecturerBtn.setText(_translate("MainWindow", "Thêm giảng viên"))
        item = self.lecturerTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MSGV"))
        item = self.lecturerTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ và tên"))
        item = self.lecturerTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngành"))
        item = self.lecturerTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.lecturerTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Thao tác"))
        self.lecturerGender_comboBox.setItemText(0, _translate("MainWindow", "Giới tính"))
        self.lecturerGender_comboBox.setItemText(1, _translate("MainWindow", "Nam"))
        self.lecturerGender_comboBox.setItemText(2, _translate("MainWindow", "Nữ"))
        self.lecturerMajor_comboBox.setItemText(0, _translate("MainWindow", "Ngành"))
        major_index = 1
        print(len(major_list))
        for major in major_list:
            self.lecturerMajor_comboBox.setItemText(major_index, _translate("MainWindow", major_list[major_index - 1]))
        self.lecturerSearchBarEdit.setPlaceholderText(_translate("MainWindow", "Tìm giảng viên ..."))
        self.label_8.setText(_translate("MainWindow", "Danh sách ngành"))
        self.addMajorBtn.setText(_translate("MainWindow", "Thêm ngành"))
        item = self.majorTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã ngành"))
        item = self.majorTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên ngành"))
        item = self.majorTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số sinh viên"))
        item = self.majorTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Số giảng viên"))
        item = self.majorTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Thao tác"))
        self.majorSearchBarEdit.setPlaceholderText(_translate("MainWindow", "Tìm ngành ..."))
        self.label_10.setText(_translate("MainWindow", "Danh sách lớp học"))
        self.addClassBtn.setText(_translate("MainWindow", "Thêm lớp học"))
        self.classSearchBarEdit.setPlaceholderText(_translate("MainWindow", "Tìm lớp ..."))
        item = self.classTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã lớp học"))
        item = self.classTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên lớp học"))
        item = self.classTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kì"))
        item = self.classTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Năm học"))
        item = self.classTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Giảng viên"))
        item = self.classTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Môn học"))
        item = self.classTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Trạng thái"))
        item = self.classTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tiết Bắt đầu"))
        item = self.classTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Tiết kết thúc"))
        item = self.classTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Thứ"))
        item = self.classTableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Thao tác"))
        self.label_9.setText(_translate("MainWindow", "Danh sách môn học"))
        self.addCourseBtn.setText(_translate("MainWindow", "Thêm môn học"))
        item = self.courseTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã môn học"))
        item = self.courseTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên môn học"))
        item = self.courseTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tín chỉ"))
        item = self.courseTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngành"))
        item = self.courseTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Thao tác"))
        self.courseSearchBarEdit.setPlaceholderText(_translate("MainWindow", "Tìm môn học ..."))

import ava_rc
