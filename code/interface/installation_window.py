# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installation_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
import time
import copy
import enum
from Classes import not_ready_style_border, not_ready_style_background, ready_style_border, ready_style_background, warning_style_border, warning_style_background

# https://habr.com/ru/companies/skillfactory/articles/648845/


class state_ch(enum.Enum):
    closed = 0
    open = 1


class device_page(QtWidgets.QWidget):
    def __init__(self, device_class, installation_class, parent=None):
        super(device_page, self).__init__()
        self.device_class = device_class
        self.installation_class = installation_class
        self.verticalLayout = QtWidgets.QGridLayout(self)
        self.verticalLayout.setHorizontalSpacing(2)
        self.verticalLayout.setVerticalSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.name_device = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.channels = {}
        self.ch_state = []

        for i in device_class.channels:
            if i.is_active == True:
                self.ch_state.append(state_ch.open)
            else:
                self.ch_state.append(state_ch.closed)

        self.name_device.setFont(font)
        self.name_device.setAlignment(QtCore.Qt.AlignCenter)
        self.name_device.setObjectName(
            "name_device_" + device_class.get_name())
        self.name_device.setText(device_class.get_name())
        self.name_device.setStyleSheet(not_ready_style_border)
        #self.name_device.setStyleSheet("background-color: rgb(20, 20, 20);")




        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/close.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.del_button = QtWidgets.QToolButton()
        self.del_button.setStyleSheet("background-color: rgb(150, 30, 0);border: 1px solid rgb(70, 70, 10); border-radius: 1px;")
        self.del_button.setFixedSize(20, 20)
        self.del_button.clicked.connect(lambda: self.click_del_button())
        self.del_button.setToolTip("удалить прибор")
        self.del_button.setIcon(icon)
        
        self.verticalLayout.addWidget(self.name_device, 0, 0)
        self.verticalLayout.addWidget(self.del_button, 0, 1)

        self.add_ch_button = {}
        for i in range(device_class.get_number_channels()):
            self.add_ch_button[i+1] = QtWidgets.QToolButton()
            self.add_ch_button[i+1].setFixedSize(9, 180)
            self.add_ch_button[i +1].setStyleSheet("background-color: rgb(90, 90, 50);border: 1px solid rgb(70, 70, 10); border-radius: 1px;")
            self.add_ch_button[i+1].setToolTip(f"добавить канал {1+i}")

        self.channelsLayout = QtWidgets.QHBoxLayout()

        self.channelsLayout.setObjectName("channelsLayout")
        self.verticalLayout.addLayout(self.channelsLayout, 1, 0, 12, 2)

        for j in range(device_class.get_number_channels()):
            page = channel_page(j+1, installation_class,
                                device_class.get_name())
            self.channels[j+1] = page

            if self.ch_state[j] == state_ch.open:
                self.channelsLayout.addWidget(page)
            else:
                self.channelsLayout.addWidget(self.add_ch_button[j+1])

        if len(self.add_ch_button) > 0:
            self.add_ch_button[1].clicked.connect(
                lambda: self.click_change_ch(1))
            self.channels[1].state_Button.clicked.connect(
                lambda: self.click_change_ch(1))
        if len(self.add_ch_button) > 1:
            self.add_ch_button[2].clicked.connect(
                lambda: self.click_change_ch(2))
            self.channels[2].state_Button.clicked.connect(
                lambda: self.click_change_ch(2))
        if len(self.add_ch_button) > 2:
            self.add_ch_button[3].clicked.connect(
                lambda: self.click_change_ch(3))
            self.channels[3].state_Button.clicked.connect(
                lambda: self.click_change_ch(3))
        if len(self.add_ch_button) > 3:
            self.add_ch_button[4].clicked.connect(
                lambda: self.click_change_ch(4))
            self.channels[4].state_Button.clicked.connect(
                lambda: self.click_change_ch(4))
        if len(self.add_ch_button) > 4:
            self.add_ch_button[5].clicked.connect(
                lambda: self.click_change_ch(5))
            self.channels[5].state_Button.clicked.connect(
                lambda: self.click_change_ch(5))

    def click_change_ch(self, num, is_open = None):
        '''открыть или закрыть канал'''

        num = int(num)
        if is_open == None:
        # меняем состояние
            if self.ch_state[num-1] == state_ch.open:
                self.ch_state[num-1] = state_ch.closed
            else:
                self.ch_state[num-1] = state_ch.open
                #self.installation_class.add_new_channel(self.device_class.get_name(),num)
        elif is_open == True:
            self.ch_state[num-1] = state_ch.open
        else:
            self.ch_state[num-1] = state_ch.closed

        self.installation_class.set_state_ch(self.device_class.get_name(), num, self.ch_state[num-1] == state_ch.open)

        self.update_widgets()

    def update_widgets(self):
        # удаляем виджеты
        for i in reversed(range(self.channelsLayout.count())):
            self.channelsLayout.itemAt(i).widget().setParent(None)

        # добавляем виджеты
        for j in range(self.device_class.get_number_channels()):
            if self.ch_state[j] == state_ch.open:
                self.channelsLayout.addWidget(self.channels[j+1])
            else:
                pass
                self.channelsLayout.addWidget(self.add_ch_button[j+1])


    def click_del_button(self):
        self.setParent(None)#удаляем виджет устройства
        self.installation_class.delete_device(self.device_class.get_name())

    def set_ch_color(self, ch_num, color):
        self.channels[ch_num].set_color(color)

    def set_state_ch_widget(self, num, state):
        num = int(num)
        if state == True:
            self.ch_state[num-1] = state_ch.open
        else:
            self.ch_state[num-1] = state_ch.closed

        self.installation_class.set_state_ch(self.device_class.get_name(), num, self.ch_state[num-1] == state_ch.open)

class channel_page(QtWidgets.QWidget):
    def __init__(self, num, installation_class, name_device, parent=None):
        super(channel_page, self).__init__()
        self.installation_class = installation_class
        self.name_device = name_device
        self.number = num
        self.set_text = "Не настроено"
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        # self.layout.setHorizontalSpacing(1)
        # self.layout.setVerticalSpacing(100)
        self.layout.setObjectName("ch" + str(num))
        # self.label_channel = QtWidgets.QLabel()
        # self.label_channel.setObjectName("labelch" + str(num))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(80)
        # self.label_channel.setFont(font)
        # self.label_channel.setText("Ch" + str(num))
        # self.label_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_settings_channel = QtWidgets.QLabel()
        self.label_settings_channel.setObjectName("labelchset" + str(num))
        self.label_settings_channel.setText(
            self.set_text)
        self.label_settings_channel.setStyleSheet(not_ready_style_border)
        self.label_settings_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_settings_channel.setWordWrap(True)
        self.state_Button = QtWidgets.QPushButton('Ch ' + str(self.number))
        self.state_Button.setToolTip(f"Удалить ch {self.number}")

        self.pushButton = QtWidgets.QPushButton('Настройка')
        self.pushButton.clicked.connect(lambda: self.click_set())
        # self.pushButton.setFixedSize(20, 58)
        self.layout.addWidget(self.state_Button, 0, 0)
        self.layout.addWidget(self.label_settings_channel, 2, 0, 9, 1)
        self.layout.addWidget(self.pushButton, 11, 0)

    def click_set(self):
        self.installation_class.click_set(self.name_device, self.number)

    def hide_elements(self):
        self.state_Button.setMinimumSize(5, 5)
        self.state_Button.setFixedSize(5, 5)
        self.pushButton.hide()
        self.pushButton.setFixedSize(5, 5)
        self.label_settings_channel.hide()
        self.label_settings_channel.setFixedSize(5, 5)

class Ui_Installation(QtWidgets.QMainWindow):
    installation_close_signal = QtCore.pyqtSignal(int)

    def setupUi(self, base_window, installation_class, class_of_devices):
        base_window.setObjectName("Installation")
        self.list_of_device = class_of_devices
        self.N = 0
        for device in class_of_devices.values():
            self.N += device.get_number_channels()
        if self.N < 3:
            self.N = 3
        if self.N > 10:
            self.N = 10
        base_window.resize(self.N*160+10+270, 540)
        self.centralwidget = QtWidgets.QWidget(base_window)
        self.centralwidget.setObjectName("centralwidget")
        # --------------------------
        self.Layout_devices = (QtWidgets.QWidget(self.centralwidget))
        self.Layout_devices.setGeometry(QtCore.QRect(
            15, 0, self.N*160-10, 320))
        self.Layout_devices.setObjectName("Layout_devices")
        #self.Layout_devices.setStyleSheet(
        #    "background-color: rgb(20, 20, 30);")

        self.horLayout = QtWidgets.QHBoxLayout(
            self.Layout_devices)
        self.horLayout.setObjectName("horLayout")

        self.devices_lay = {}

        for device in class_of_devices:
            dev = device_page(class_of_devices[device], installation_class)
            self.horLayout.addWidget(dev)
            self.devices_lay[device] = dev

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
            sizePolicy.setHorizontalStretch(class_of_devices[device].get_number_channels())
            dev.setSizePolicy(sizePolicy)


        self.pbar = QtWidgets.QProgressBar(self.centralwidget)
        self.pbar.setGeometry(QtCore.QRect(
            10, 450, 15+160*self.N, 20))
        self.pbar.setValue(0)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(
            30+160*self.N, 345, 221, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(
            150+160*self.N, 450, 101, 23))
        self.pause_button.setObjectName("pause_button")

        self.label_state = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_state.setFont(font)
        self.label_state.setGeometry(QtCore.QRect(
            10, 470, 15+160*self.N, 20))
        self.label_state.setObjectName("label_state")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(base_window)
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
        self.repeat_measurement_enter.addItems(["1","2","3","4","5","6","7","8","9","10"])

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
        self.repeat_exp_enter.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.horizontalLayout_2.addWidget(self.repeat_exp_enter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # ================================================================

        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(
            10, 345, 10+160*self.N, 100))
        self.log.setObjectName("log_text")
        #self.log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.log.setReadOnly(True)

        self.clear_log_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_log_button.setGeometry(QtCore.QRect(
            10, 325, 18, 18))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/clean.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.clear_log_button.setIcon(icon)
        self.clear_log_button.setIconSize(QtCore.QSize(15, 15))
        self.clear_log_button.setObjectName("clear_log_button")

        base_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(base_window)
        self.menubar.setGeometry(QtCore.QRect(10, 0, 590, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        base_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(base_window)
        self.statusbar.setObjectName("statusbar")
        base_window.setStatusBar(self.statusbar)
        self.save_installation_button_as = QtWidgets.QAction(base_window)
        self.save_installation_button_as.setObjectName(
            "save_installation_button_as")
        self.save_installation_button = QtWidgets.QAction(base_window)
        self.save_installation_button.setObjectName("save_installation_button")
        self.open_installation_button = QtWidgets.QAction(base_window)
        self.open_installation_button.setObjectName("open_installation_button")
        self.add_device_button = QtWidgets.QAction(base_window)
        self.add_device_button.setObjectName("add_device_button")
        self.menu.addAction(self.save_installation_button)
        self.menu.addAction(self.save_installation_button_as)
        self.menu.addAction(self.open_installation_button)
        self.menu.addSeparator()
        self.menu.addAction(self.add_device_button)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(base_window)
        QtCore.QMetaObject.connectSlotsByName(base_window)

    def closeEvent(self, event):  # эта функция вызывается при закрытии окна
        #print("окно инталляции закрыто крестиком")
        for dev_win in self.devices_lay.values():
            dev_win.setParent(None)
        self.installation_close_signal.emit(1)

    def retranslateUi(self, Installation):
        _translate = QtCore.QCoreApplication.translate
        Installation.setWindowTitle(_translate(
            "Installation", "Experiment control"))
        '''
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
        '''
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
        self.label_state.setText(_translate(
            "settings_save", "Состояние"))
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
