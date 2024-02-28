# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installation_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Installation(QtWidgets.QMainWindow):
    installation_close_signal = QtCore.pyqtSignal(int)

    def setupUi(self, Installation, list_of_device):
        Installation.setObjectName("Installation")
        self.list_of_device = list_of_device
        self.N = len(list_of_device)
        if self.N < 3:
            self.N = 3
        Installation.resize(self.N*160+10+270, 510)
        self.centralwidget = QtWidgets.QWidget(Installation)
        self.centralwidget.setObjectName("centralwidget")
        # --------------------------
        i = 0
        self.verticalLayoutWidget = {}
        self.verticalLayout = {}
        self.horizontalLayout = {}
        self.name_device = {}
        self.number_device = {}
        self.label = {}
        self.change_device_button = {}
        for device in self.list_of_device:
            self.verticalLayoutWidget[device] = (
                QtWidgets.QWidget(self.centralwidget))
            self.verticalLayoutWidget[device].setGeometry(
                QtCore.QRect(25+(int((150*self.N)/len(self.list_of_device)))*i, 0, int((150*self.N)/len(self.list_of_device))-10, 320))
            self.verticalLayoutWidget[device].setObjectName(
                "verticalLayoutWidget" + str(i))
            self.verticalLayoutWidget[device].setStyleSheet(
                "background-color: rgb(194, 191, 190);")
            self.verticalLayout[device] = (
                QtWidgets.QVBoxLayout(self.verticalLayoutWidget[device]))
            self.verticalLayout[device].setContentsMargins(5, 0, 0, 0)
            self.verticalLayout[device].setObjectName(
                "verticalLayout" + str(i))
            self.horizontalLayout[device] = (QtWidgets.QHBoxLayout())
            self.horizontalLayout[device].setObjectName(
                "horizontalLayout_" + str(i))
            self.name_device[device] = (QtWidgets.QLabel(
                self.verticalLayoutWidget[device]))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.name_device[device].setFont(font)
            self.name_device[device].setLayoutDirection(QtCore.Qt.RightToLeft)
            self.name_device[device].setAlignment(QtCore.Qt.AlignCenter)
            self.name_device[device].setObjectName("name_device_" + device)
            self.number_device[device] = (
                QtWidgets.QLabel(self.verticalLayoutWidget[device]))
            self.number_device[device].setFont(font)
            self.number_device[device].setAlignment(QtCore.Qt.AlignCenter)
            self.number_device[device].setObjectName("number_device_"+str(i+1))
            self.horizontalLayout[device].addWidget(self.number_device[device])
            self.horizontalLayout[device].addWidget(self.name_device[device])
            self.verticalLayout[device].addLayout(
                self.horizontalLayout[device])
            self.label[device] = (QtWidgets.QLabel(
                self.verticalLayoutWidget[device]))
            self.label[device].setObjectName("label+" + str(i+1))
            self.verticalLayout[device].addWidget(self.label[device])
            self.change_device_button[device] = (QtWidgets.QPushButton(device))
            self.change_device_button[device].setObjectName(
                "change_device_button_" + str(i+1))
            self.verticalLayout[device].addWidget(
                self.change_device_button[device])
            i += 1

        self.pbar = QtWidgets.QProgressBar(self.centralwidget)
        self.pbar.setGeometry(QtCore.QRect(
            10, 440, 15+160*self.N, 20))
        self.pbar.setValue(0)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(
            30+160*self.N, 340, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(
            150+160*self.N, 440, 101, 23))
        self.pause_button.setObjectName("pause_button")

        # self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        # self.cancel_button.setGeometry(QtCore.QRect(
        #    150+160*self.N, 440, 101, 23))
        # self.cancel_button.setObjectName("cancel_button")

        '''
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(
            20+160*self.N, 0, 231, 200))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.save_repeat_set_button = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.save_repeat_set_button.setObjectName("general_settings")
        self.gridLayout.addWidget(self.save_repeat_set_button, 0, 0, 1, 1)

        self.save_repeat_set_button1 = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.save_repeat_set_button1.setObjectName("general_settings")
        self.gridLayout.addWidget(self.save_repeat_set_button1, 1, 0, 1, 1)

        self.save_repeat_set_button2 = QtWidgets.QPushButton(
            self.gridLayoutWidget)
        self.save_repeat_set_button2.setObjectName("general_settings")
        self.gridLayout.addWidget(self.save_repeat_set_button2, 0, 1, 1, 1)

        # self.schematic_installation = QtWidgets.QGraphicsView(
        #    self.gridLayoutWidget)
        # self.schematic_installation.setObjectName("schematic_installation")
        # self.gridLayout.addWidget(self.schematic_installation, 1, 0, 1, 1)

        # self.log = QtWidgets.QLineEdit(self.centralwidget)
        # self.log.setGeometry(QtCore.QRect(10, 320, 10+160*self.N, 110))
        # self.log.setObjectName("log_text")
        '''
        # =====================================================================
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Installation)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(10+160*self.N, 30, 261, 100))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.way_save_text = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.way_save_text.setObjectName("way_save_text")
        self.horizontalLayout.addWidget(self.way_save_text)
        self.way_save_button = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        self.way_save_button.setObjectName("way_save_button")
        self.horizontalLayout.addWidget(self.way_save_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.repeat_measurement_enter = QtWidgets.QComboBox(
            self.verticalLayoutWidget_2)
        self.repeat_measurement_enter.setEditable(False)
        self.repeat_measurement_enter.setObjectName("repeat_measurement_enter")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")
        self.repeat_measurement_enter.addItem("")

        self.horizontalLayout_3.addWidget(self.repeat_measurement_enter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.repeat_exp_enter = QtWidgets.QComboBox(
            self.verticalLayoutWidget_2)
        self.repeat_exp_enter.setEditable(False)
        self.repeat_exp_enter.setObjectName("repeat_exp_enter")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.repeat_exp_enter.addItem("")
        self.horizontalLayout_2.addWidget(self.repeat_exp_enter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # ================================================================

        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(
            10, 320, 10+160*self.N, 110))
        self.log.setObjectName("log_text")
        self.log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.log.setReadOnly(True)

        Installation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Installation)
        self.menubar.setGeometry(QtCore.QRect(10, 0, 590, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Installation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Installation)
        self.statusbar.setObjectName("statusbar")
        Installation.setStatusBar(self.statusbar)
        self.save_installation_button_as = QtWidgets.QAction(Installation)
        self.save_installation_button_as.setObjectName(
            "save_installation_button_as")
        self.save_installation_button = QtWidgets.QAction(Installation)
        self.save_installation_button.setObjectName("save_installation_button")
        self.open_installation_button = QtWidgets.QAction(Installation)
        self.open_installation_button.setObjectName("open_installation_button")
        self.add_device_button = QtWidgets.QAction(Installation)
        self.add_device_button.setObjectName("add_device_button")
        self.menu.addAction(self.save_installation_button)
        self.menu.addAction(self.save_installation_button_as)
        self.menu.addAction(self.open_installation_button)
        self.menu.addSeparator()
        self.menu.addAction(self.add_device_button)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Installation)
        QtCore.QMetaObject.connectSlotsByName(Installation)

    def closeEvent(self, event):  # эта функция вызывается при закрытии окна
        print("окно инталляции закрыто крестиком")
        self.installation_close_signal.emit(1)

    def retranslateUi(self, Installation):
        _translate = QtCore.QCoreApplication.translate
        Installation.setWindowTitle(_translate(
            "Installation", "Experiment control"))
        i = 0
        for device in self.list_of_device:
            self.name_device[device].setText(
                _translate("Installation", device))
            self.number_device[device].setText(
                _translate("Installation", str(i+1)))
            self.label[device].setText(_translate(
                "Installation", "Не настроено"))
            self.change_device_button[device].setText(
                _translate("Installation", "Изменить настройки"))
            i += 1
        self.start_button.setText(_translate("Installation", "Запуск"))
        self.pause_button.setText(_translate("Installation", "Пауза"))
        # self.cancel_button.setText(_translate("Installation", "Отмена"))
        '''
        self.save_repeat_set_button.setText(
            _translate("Installation", "Общие настройки установки"))
        self.save_repeat_set_button1.setText(
            _translate("Installation", "Общие настройки установки"))
        self.save_repeat_set_button2.setText(
            _translate("Installation", "Общие настройки установки"))
        '''
        # self.label_schematic.setText(_translate("Installation", "Схема установки"))

        self.menu.setTitle(_translate("Installation", "Меню"))
        self.save_installation_button.setText(
            _translate("Installation", "Сохранить установку"))
        self.save_installation_button_as.setText(
            _translate("Installation", "Сохранить установку как..."))
        self.open_installation_button.setText(
            _translate("Installation", "Открыть установку"))
        self.add_device_button.setText(
            _translate("Installation", "Добавить прибор"))


# =========================================================================================
        self.label_19.setText(_translate(
            "settings_save", "Как сохранить результаты?"))
        self.way_save_button.setText(_translate("settings_save", "Путь"))
        self.label_21.setText(_translate(
            "settings_save", "Кол-во измерений в точке"))
        self.repeat_measurement_enter.setCurrentText(
            _translate("settings_save", "1"))
        self.repeat_measurement_enter.setItemText(
            0, _translate("settings_save", "1"))
        self.repeat_measurement_enter.setItemText(
            1, _translate("settings_save", "2"))
        self.repeat_measurement_enter.setItemText(
            2, _translate("settings_save", "3"))
        self.repeat_measurement_enter.setItemText(
            3, _translate("settings_save", "4"))
        self.repeat_measurement_enter.setItemText(
            4, _translate("settings_save", "5"))
        self.repeat_measurement_enter.setItemText(
            5, _translate("settings_save", "6"))
        self.repeat_measurement_enter.setItemText(
            6, _translate("settings_save", "7"))
        self.repeat_measurement_enter.setItemText(
            7, _translate("settings_save", "8"))
        self.repeat_measurement_enter.setItemText(
            8, _translate("settings_save", "9"))
        self.repeat_measurement_enter.setItemText(
            9, _translate("settings_save", "10"))
        self.label_20.setText(_translate(
            "settings_save", "Кол-во повторов эксперимента"))
        self.repeat_exp_enter.setCurrentText(_translate("settings_save", "1"))
        self.repeat_exp_enter.setItemText(0, _translate("settings_save", "1"))
        self.repeat_exp_enter.setItemText(1, _translate("settings_save", "2"))
        self.repeat_exp_enter.setItemText(2, _translate("settings_save", "3"))
        self.repeat_exp_enter.setItemText(3, _translate("settings_save", "4"))
        self.repeat_exp_enter.setItemText(4, _translate("settings_save", "5"))
        self.repeat_exp_enter.setItemText(5, _translate("settings_save", "6"))
        self.repeat_exp_enter.setItemText(6, _translate("settings_save", "7"))
        self.repeat_exp_enter.setItemText(7, _translate("settings_save", "8"))
        self.repeat_exp_enter.setItemText(8, _translate("settings_save", "9"))
        self.repeat_exp_enter.setItemText(9, _translate("settings_save", "10"))
