# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_Multibot.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 605)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.shopping_list = QtWidgets.QGroupBox(self.groupBox)
        self.shopping_list.setGeometry(QtCore.QRect(10, 20, 371, 501))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.shopping_list.setFont(font)
        self.shopping_list.setObjectName("shopping_list")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.shopping_list)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_2.addWidget(self.checkBox_1, 12, 1, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_2.addWidget(self.checkBox_19, 8, 1, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout_2.addWidget(self.checkBox_21, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 11, 1, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout_2.addWidget(self.checkBox_29, 10, 0, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout_2.addWidget(self.checkBox_28, 9, 0, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_2.addWidget(self.checkBox_20, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 9, 1, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_2.addWidget(self.checkBox_18, 7, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_2.addWidget(self.checkBox_7, 13, 0, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout_2.addWidget(self.checkBox_25, 5, 0, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_2.addWidget(self.checkBox_14, 3, 1, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_2.addWidget(self.checkBox_13, 2, 1, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout_2.addWidget(self.checkBox_22, 3, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_2.addWidget(self.checkBox_12, 1, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 12, 0, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout_2.addWidget(self.checkBox_27, 8, 0, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout_2.addWidget(self.checkBox_26, 7, 0, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_2.addWidget(self.checkBox_15, 4, 1, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_30.setObjectName("checkBox_30")
        self.gridLayout_2.addWidget(self.checkBox_30, 10, 1, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout_2.addWidget(self.checkBox_24, 11, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 15, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 14, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_2.addWidget(self.checkBox_6, 13, 1, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout_2.addWidget(self.checkBox_23, 4, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 6, 0, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_2.addWidget(self.checkBox_17, 6, 1, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_2.addWidget(self.checkBox_16, 5, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.shopping_list)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 0, 1, 1, 1)
        self.groupBox_top = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_top.setGeometry(QtCore.QRect(390, 20, 391, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_top.sizePolicy().hasHeightForWidth())
        self.groupBox_top.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_top.setFont(font)
        self.groupBox_top.setObjectName("groupBox_top")
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_top)
        self.pushButton_stop.setGeometry(QtCore.QRect(200, 20, 171, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.basket = QtWidgets.QPlainTextEdit(self.groupBox_top)
        self.basket.setGeometry(QtCore.QRect(10, 110, 361, 371))
        self.basket.setObjectName("basket")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_top)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 20, 181, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_start.clicked.connect(MainWindow.savebasket) # type: ignore
        self.pushButton_stop.clicked.connect(MainWindow.clearbasket) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shopping_list.setTitle(_translate("MainWindow", " list"))
        self.checkBox_1.setText(_translate("MainWindow", "포테토칩"))
        self.checkBox_19.setText(_translate("MainWindow", "포카칩"))
        self.checkBox_21.setText(_translate("MainWindow", "파인애플"))
        self.checkBox_4.setText(_translate("MainWindow", "예감"))
        self.checkBox_29.setText(_translate("MainWindow", "감자"))
        self.checkBox_28.setText(_translate("MainWindow", "양배추"))
        self.checkBox_20.setText(_translate("MainWindow", "바나나"))
        self.checkBox_2.setText(_translate("MainWindow", "빈츠"))
        self.checkBox_18.setText(_translate("MainWindow", "뿌셔뿌셔"))
        self.checkBox_7.setText(_translate("MainWindow", "가지"))
        self.checkBox_25.setText(_translate("MainWindow", "멜론"))
        self.checkBox_14.setText(_translate("MainWindow", "이프로"))
        self.checkBox_13.setText(_translate("MainWindow", "파워에이드"))
        self.checkBox_22.setText(_translate("MainWindow", "포도"))
        self.checkBox_12.setText(_translate("MainWindow", "사이다"))
        self.checkBox_9.setText(_translate("MainWindow", "오이"))
        self.checkBox_27.setText(_translate("MainWindow", "당근"))
        self.checkBox_26.setText(_translate("MainWindow", "고구마"))
        self.checkBox_15.setText(_translate("MainWindow", "게토레이"))
        self.checkBox_30.setText(_translate("MainWindow", "버터와플"))
        self.checkBox_24.setText(_translate("MainWindow", "호박"))
        self.checkBox_10.setText(_translate("MainWindow", "사과 "))
        self.checkBox_3.setText(_translate("MainWindow", "양배추"))
        self.checkBox_5.setText(_translate("MainWindow", "대파"))
        self.checkBox_6.setText(_translate("MainWindow", "새콤달콤"))
        self.checkBox_23.setText(_translate("MainWindow", "복숭아"))
        self.checkBox_8.setText(_translate("MainWindow", "딸기"))
        self.checkBox_17.setText(_translate("MainWindow", "나랑드사이다"))
        self.checkBox_16.setText(_translate("MainWindow", "링티"))
        self.checkBox_11.setText(_translate("MainWindow", "콜라"))
        self.groupBox_top.setTitle(_translate("MainWindow", "장바구니"))
        self.pushButton_stop.setText(_translate("MainWindow", "비우기"))
        self.pushButton_start.setText(_translate("MainWindow", "완료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())