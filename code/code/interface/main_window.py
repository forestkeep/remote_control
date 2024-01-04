# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainprogram.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 340)
        MainWindow.setStyleSheet("font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(220, 220, 220, 30), stop:0.427447 rgba(240, 240, 240,30), stop:1 rgba(255, 255, 255, 30));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 371, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 120))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(224, 250, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setFamily("Noto Sans SC")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(224, 250, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.actionMaisheng = QtWidgets.QAction(MainWindow)
        self.actionMaisheng.setObjectName("actionMaisheng")
        self.actionSVPS34 = QtWidgets.QAction(MainWindow)
        self.actionSVPS34.setObjectName("actionSVPS34")
        self.actionLock_in = QtWidgets.QAction(MainWindow)
        self.actionLock_in.setObjectName("actionLock_in")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.menu.addSeparator()
        self.menu_2.addAction(self.action_2)
        self.menu_2.addSeparator()
        self.menu_3.addAction(self.actionMaisheng)
        self.menu_3.addAction(self.actionSVPS34)
        self.menu_3.addAction(self.actionLock_in)
        self.menu_3.addAction(self.action_9)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Удаленное управление"))
        self.pushButton.setText(_translate("MainWindow", "Локальное управление приборами"))
        self.pushButton_2.setText(_translate("MainWindow", "Создание экспериментальной установки"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Создание установки"))
        self.menu_3.setTitle(_translate("MainWindow", "Приборы"))
        self.action_2.setText(_translate("MainWindow", "Выбор приборов"))
        self.action_4.setText(_translate("MainWindow", "один"))
        self.actionMaisheng.setText(_translate("MainWindow", "Maisheng"))
        self.actionSVPS34.setText(_translate("MainWindow", "SVPS34"))
        self.actionLock_in.setText(_translate("MainWindow", "Lock in"))
        self.action_9.setText(_translate("MainWindow", "АКИП"))