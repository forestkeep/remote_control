# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import serial
import time
import pymodbus
import datetime
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets

class On_Off_state(Enum):
    On = True
    Off = False
class state_device(Enum):
    Remote = True
    Hand = False

class channel():
    def __init__(self,number) -> None:
        self.number = number
        self.current_current_value = 0
        self.channel_status = On_Off_state.Off
        self.relay_status = On_Off_state.Off
        #print("channel" + str(number) + "is done")
    def set_current(self, value):
        self.current_current_value = value

    def set_channel_status(self,state):
        self.channel_status = state

    def set_relay_status(self,state):
        self.relay_status = state

    def get_relay_status(self):
        return self.relay_status
    
    def get_channel_status(self):
        return self.channel_status
    
    def toggle_channel_state(self):
        if self.channel_status == On_Off_state.Off:
            self.channel_status = On_Off_state.On
        else:
            self.channel_status = On_Off_state.Off

    def toggle_relay_state(self):
        if self.relay_status_status == On_Off_state.Off:
            self.relay_status_status = On_Off_state.On
        else:
            self.relay_status_status = On_Off_state.Off

class device():
    """device parameters"""

    def __init__(self,name,com_port,baudrate) -> None:
        self.name = name
        self.ser = serial.Serial(com_port,baudrate=baudrate,timeout=0.2)


        self.status = state_device.Hand
        self.current_temperature = ""

        self.ch1 = channel(1)
        self.ch2 = channel(2)
        self.ch3 = channel(3)
        self.ch4 = channel(4)
        self.ch5 = channel(5)
        self.ch6 = channel(6)
        self.ch7 = channel(7)
        self.channels = [self.ch1,self.ch2,self.ch3,self.ch4,self.ch5,self.ch6,self.ch7]
    def check_connect(self):
        self.ser.write(b'status')
        ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: " + "status")
        answer = str(self.ser.read(50))
        ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
        print(answer)
        if answer.find("Remote control") != -1 or answer.find("Hand control") != -1:
            #self.status = state_device.Connect
            print("connect")
            return True
        else:
            print("fail connect")
            return False
    def get_temperature(self):
        self.ser.write(b'temp')
        ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: " + "temp")
        answer = str(self.ser.read(50))
        ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
        try:
            end_index = answer.find("C")
            temp = float(answer[end_index-6:end_index-1])
            return temp
        except:
            return False
    def remote_connect(self):

        if self.check_connect():
            self.ser.write(b'status')
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: status" )
            answer = str(self.ser.read(50))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
            if self.status == state_device.Hand:
                if answer.find("Hand control") != -1:
                    self.ser.write(b'remote')
                    ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: remote" )
                    answer2 = str(self.ser.read(50))
                    ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer2)
                    if answer2.find("Remote control enable") != -1:
                        self.status = state_device.Remote
                        return True
                    else:
                        return False
                else:
                    self.status = state_device.Remote
                    return True
            elif self.status == state_device.Remote:
                if answer.find("Remote control") != -1:
                    self.ser.write(b'hand')
                    ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: hand" )
                    answer2 = str(self.ser.read(50))
                    ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer2)
                    if answer2.find("Remote control disable") != -1:
                        self.status = state_device.Hand
                        return True
                    else:
                        return False
                else:
                    self.status = state_device.Hand
                    return True
        else:
            return False
    def get_state(self):
        return self.status
    def button_action(self, number):
        if self.channels[number-1].get_channel_status() == On_Off_state.Off:
            self.ser.write(bytes("C" + str(number)+"N",encoding='utf8'))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: " + "C" + str(number)+"N")
            answer = str(self.ser.read(20))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
            if answer.find("C" + str(number) + "N - OK") != -1:
                self.channels[number-1].channel_status = On_Off_state.On
                return self.channels[number-1].channel_status
            else:
                return False
        else:
            self.ser.write(bytes("C" + str(number)+"F",encoding='utf8'))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: " + "C" + str(number)+"F")
            answer = str(self.ser.read(20))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
            if answer.find("C" + str(number) + "F - OK") != -1:
                self.channels[number-1].channel_status = On_Off_state.Off
                return self.channels[number-1].channel_status
            else:
                return False
    def relay_action(self, number):
        if self.channels[number-1].get_relay_status() == On_Off_state.Off:
            self.ser.write(bytes("R" + str(number) + "N",encoding='utf8'))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: " + "R" + str(number) + "N")
            answer = str(self.ser.read(20))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
            if answer.find("R" + str(number) + "N - OK") != -1:
                self.channels[number-1].relay_status = On_Off_state.On
                return self.channels[number-1].relay_status
            else:
                return False
        else:
            self.ser.write(bytes("R" + str(number)+"F",encoding='utf8'))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" send: " + "R" + str(number)+"F")
            answer = str(self.ser.read(20))
            ui.log.append(str(datetime.datetime.now().strftime("%H:%M:%S"))+" receive: " + answer)
            if answer.find("R" + str(number) + "F - OK") != -1:
                self.channels[number-1].relay_status = On_Off_state.Off
                return self.channels[number-1].relay_status
            else:
                return False


        



class Ui_SVPS34_control(object):
    def setupUi(self, SVPS34_control):

        self.is_device_connect = False
        self.connect_devices = []
        SVPS34_control.setObjectName("SVPS34_control")
        SVPS34_control.resize(912, 638)
        self.centralwidget = QtWidgets.QWidget(SVPS34_control)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 410, 931, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(20, 10, 171, 161))
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 126, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scan_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setObjectName("scan_button")
        self.verticalLayout_2.addWidget(self.scan_button)
        self.comportslist = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comportslist.setObjectName("comportslist")
        self.verticalLayout_2.addWidget(self.comportslist)
        self.comportslist_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comportslist_2.setObjectName("comportslist_2")
        self.verticalLayout_2.addWidget(self.comportslist_2)
        self.connect_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.connect_button.setMouseTracking(False)
        self.connect_button.setObjectName("connect_button")
        self.verticalLayout_2.addWidget(self.connect_button)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 175, 881, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 194, 194);")
        self.label_2.setObjectName("label_2")

        #self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        #self.lineEdit_2.setGeometry(QtCore.QRect(200, 20, 701, 151))
        #self.lineEdit_2.setObjectName("lineEdit_2")


        self.log = QtWidgets.QTextEdit(self.frame_2)
        self.log.setGeometry(QtCore.QRect(200, 20, 701, 151))
        self.log.setObjectName("lineEdit_2")
        self.log.setStyleSheet("background-color: rgb(180, 255, 255);")
        self.log.setReadOnly(True)


        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(200, 0, 511, 16))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 281, 121))
        self.lcdNumber.setObjectName("lcdNumber")
        self.common_button = QtWidgets.QPushButton(self.centralwidget)
        self.common_button.setGeometry(QtCore.QRect(20, 270, 81, 41))
        self.common_button.setMouseTracking(False)
        self.common_button.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.common_button.setObjectName("common_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 260, 751, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ch1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch1.setMouseTracking(False)
        self.ch1.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch1.setObjectName("ch1")
        self.horizontalLayout.addWidget(self.ch1)
        self.ch2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch2.setMouseTracking(False)
        self.ch2.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch2.setObjectName("ch2")
        self.horizontalLayout.addWidget(self.ch2)
        self.ch3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch3.setMouseTracking(False)
        self.ch3.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch3.setObjectName("ch3")
        self.horizontalLayout.addWidget(self.ch3)
        self.ch4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch4.setMouseTracking(False)
        self.ch4.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch4.setObjectName("ch4")
        self.horizontalLayout.addWidget(self.ch4)
        self.ch5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch5.setMouseTracking(False)
        self.ch5.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch5.setObjectName("ch5")
        self.horizontalLayout.addWidget(self.ch5)
        self.ch6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch6.setMouseTracking(False)
        self.ch6.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch6.setObjectName("ch6")
        self.horizontalLayout.addWidget(self.ch6)
        self.ch7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ch7.setMouseTracking(False)
        self.ch7.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.ch7.setObjectName("ch7")
        self.horizontalLayout.addWidget(self.ch7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 320, 751, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rel1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel1.setMouseTracking(False)
        self.rel1.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel1.setObjectName("rel1")
        self.horizontalLayout_2.addWidget(self.rel1)
        self.rel2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel2.setMouseTracking(False)
        self.rel2.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel2.setObjectName("rel2")
        self.horizontalLayout_2.addWidget(self.rel2)
        self.rel3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel3.setMouseTracking(False)
        self.rel3.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel3.setObjectName("rel3")
        self.horizontalLayout_2.addWidget(self.rel3)
        self.rel4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel4.setMouseTracking(False)
        self.rel4.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel4.setObjectName("rel4")
        self.horizontalLayout_2.addWidget(self.rel4)
        self.rel5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel5.setMouseTracking(False)
        self.rel5.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel5.setObjectName("rel5")
        self.horizontalLayout_2.addWidget(self.rel5)
        self.rel6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel6.setMouseTracking(False)
        self.rel6.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel6.setObjectName("rel6")
        self.horizontalLayout_2.addWidget(self.rel6)
        self.rel7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.rel7.setMouseTracking(False)
        self.rel7.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.rel7.setObjectName("rel7")
        self.horizontalLayout_2.addWidget(self.rel7)
        self.common_rel_button = QtWidgets.QPushButton(self.centralwidget)
        self.common_rel_button.setGeometry(QtCore.QRect(20, 320, 81, 41))
        self.common_rel_button.setMouseTracking(False)
        self.common_rel_button.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.common_rel_button.setObjectName("common_rel_button")
        self.remote_button = QtWidgets.QPushButton(self.centralwidget)
        self.remote_button.setGeometry(QtCore.QRect(300, 50, 81, 41))
        self.remote_button.setMouseTracking(False)
        self.remote_button.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.remote_button.setObjectName("remote_button")
        self.get_temp_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_temp_button.setGeometry(QtCore.QRect(750, 10, 101, 51))
        self.get_temp_button.setMouseTracking(False)
        self.get_temp_button.setStyleSheet("background-color: rgb(81, 244, 244);")
        self.get_temp_button.setObjectName("get_temp_button")
        self.temp_label = QtWidgets.QLabel(self.centralwidget)
        self.temp_label.setGeometry(QtCore.QRect(700, 70, 201, 41))
        self.temp_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.temp_label.setObjectName("temp_label")
        SVPS34_control.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SVPS34_control)
        self.statusbar.setObjectName("statusbar")
        SVPS34_control.setStatusBar(self.statusbar)
        self.write_boud_rate(("50", "75", "110", "150", "300", "600", "1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"))


        

        self.retranslateUi(SVPS34_control)
        QtCore.QMetaObject.connectSlotsByName(SVPS34_control)


        self.functions()
        

    def functions(self):

        self.scan_button.clicked.connect(lambda: self.scan_active_com_ports())
        self.connect_button.clicked.connect(lambda: self.connect_to_com_port())
        #self.connect_button.clicked.connect(lambda: self.modbustest(25036))#mV

        self.ch1.clicked.connect(lambda:self.click_channel_button(1))
        self.ch2.clicked.connect(lambda:self.click_channel_button(2))
        self.ch3.clicked.connect(lambda:self.click_channel_button(3))
        self.ch4.clicked.connect(lambda:self.click_channel_button(4))
        self.ch5.clicked.connect(lambda:self.click_channel_button(5))
        self.ch6.clicked.connect(lambda:self.click_channel_button(6))
        self.ch7.clicked.connect(lambda:self.click_channel_button(7))
        self.rel1.clicked.connect(lambda:self.click_relay_button(1))
        self.rel2.clicked.connect(lambda:self.click_relay_button(2))
        self.rel3.clicked.connect(lambda:self.click_relay_button(3))
        self.rel4.clicked.connect(lambda:self.click_relay_button(4))
        self.rel5.clicked.connect(lambda:self.click_relay_button(5))
        self.rel6.clicked.connect(lambda:self.click_relay_button(6))
        self.rel7.clicked.connect(lambda:self.click_relay_button(7))
        self.get_temp_button.clicked.connect(lambda: self.get_temperature())
        self.remote_button.clicked.connect(lambda: self.remote_connect())
    def remote_connect(self):
        if self.is_device_connect:
            self.connect_devices[0].remote_connect()
            if self.connect_devices[0].get_state() == state_device.Hand :
                self.remote_button.setStyleSheet("background-color: rgb(206, 206, 206);")
                self.label_2.setText("Устройство SVPS34 подключено к порту " + str(self.connect_devices[0].ser.name) + " в режиме ручного управления")
            else:
                self.remote_button.setStyleSheet("background-color: rgb(85, 255, 127);")
                self.label_2.setText("Устройство SVPS34 подключено к порту " + str(self.connect_devices[0].ser.name) + " в режиме удаленного управления")


    def get_temperature(self):
        if self.is_device_connect:
            temp = self.connect_devices[0].get_temperature()
            if temp != False:
                self.temp_label.setText("Temperature = " + str(temp) + "C")

        
    def connect_to_com_port(self):
        try:
            com = self.comportslist.currentText()
            baudrate = self.comportslist_2.currentText()
            SVPS34 = device("SVPS34",com,baudrate)
            if SVPS34.check_connect() and not self.is_device_connect:
                self.connect_devices.append(SVPS34)#добавляем в массив подключенных устройств svps34
                if self.connect_devices[0].status == state_device.Remote:
                    self.label_2.setText("Устройство SVPS34 подключено к порту " + str(SVPS34.ser.name) + " в режиме удаленного управления")
                else:
                    self.label_2.setText("Устройство SVPS34 подключено к порту " + str(SVPS34.ser.name) + " в режиме ручного управления")
                self.label_2.setStyleSheet("background-color: rgb(85, 255, 127);")
                self.is_device_connect = True
        except:
            ui.log.append("fail connect to svps34: check device")
       
    def click_channel_button(self,number_of_channel):
        if self.is_device_connect:
            #print("number channel = " + str(number_of_channel))
            answer = self.connect_devices[0].button_action(number_of_channel)
            if answer != False:
                if answer == On_Off_state.On:
                    if number_of_channel == 1:
                        self.ch1.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_channel == 2:
                        self.ch2.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_channel == 3:
                        self.ch3.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_channel == 4:
                        self.ch4.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_channel == 5:
                        self.ch5.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_channel == 6:
                        self.ch6.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_channel == 7:
                        self.ch7.setStyleSheet("background-color: rgb(85, 255, 127);")
                    else:
                        print("error number of channel too much")
                else:
                    if number_of_channel == 1:
                        self.ch1.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_channel == 2:
                        self.ch2.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_channel == 3:
                        self.ch3.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_channel == 4:
                        self.ch4.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_channel == 5:
                        self.ch5.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_channel == 6:
                        self.ch6.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_channel == 7:
                        self.ch7.setStyleSheet("background-color: rgb(206, 206, 206);")
                    else:
                        print("error number of channel too much")
    def click_relay_button(self,number_of_relay):
        if self.is_device_connect:
            answer = self.connect_devices[0].relay_action(number_of_relay)
            #print(answer)
            if answer != False:
                if answer == On_Off_state.On:
                    if number_of_relay == 1:
                        self.rel1.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_relay == 2:
                        self.rel2.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_relay == 3:
                        self.rel3.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_relay == 4:
                        self.rel4.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_relay == 5:
                        self.rel5.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_relay == 6:
                        self.rel6.setStyleSheet("background-color: rgb(85, 255, 127);")
                    elif number_of_relay == 7:
                        self.rel7.setStyleSheet("background-color: rgb(85, 255, 127);")
                    else:
                        print("error number of channel too much")
                else:
                    if number_of_relay == 1:
                        self.rel1.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_relay == 2:
                        self.rel2.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_relay == 3:
                        self.rel3.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_relay == 4:
                        self.rel4.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_relay == 5:
                        self.rel5.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_relay == 6:
                        self.rel6.setStyleSheet("background-color: rgb(206, 206, 206);")
                    elif number_of_relay == 7:
                        self.rel7.setStyleSheet("background-color: rgb(206, 206, 206);")
                    else:
                        print("error number of channel too much")
        
    def scan_active_com_ports(self):
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        active_ports = []
    
        for port in ports:
            try:
                # Попытаемся открыть порт
                ser = serial.Serial(port.device)
                # Если порт успешно открыт, добавляем его в список активных портов
                active_ports.append(port.device)
                # Закрываем порт
                ser.close()
            except (OSError, serial.SerialException):
                pass
        self.comportslist.clear()
        self.comportslist.addItems(active_ports)
        

        #print(active_ports)
    def write_boud_rate(self,list):
        self.comportslist_2.addItems(list)
        if "115200" in list:
            self.comportslist_2.setCurrentText("115200")
  
#==================================================================

    def retranslateUi(self, SVPS34_control):
        _translate = QtCore.QCoreApplication.translate
        SVPS34_control.setWindowTitle(_translate("SVPS34_control", "Calc"))
        self.scan_button.setText(_translate("SVPS34_control", "Scan"))
        self.connect_button.setText(_translate("SVPS34_control", "Connect"))
        self.label_2.setText(_translate("SVPS34_control", "Нет подключенных портов"))
        self.label.setText(_translate("SVPS34_control", "Журнал"))
        self.common_button.setText(_translate("SVPS34_control", "Common"))
        self.ch1.setText(_translate("SVPS34_control", "+3.3V"))
        self.ch2.setText(_translate("SVPS34_control", "+5V"))
        self.ch3.setText(_translate("SVPS34_control", "+12V"))
        self.ch4.setText(_translate("SVPS34_control", "Ch4"))
        self.ch5.setText(_translate("SVPS34_control", "Ch5"))
        self.ch6.setText(_translate("SVPS34_control", "Ch6"))
        self.ch7.setText(_translate("SVPS34_control", "Ch7"))
        self.rel1.setText(_translate("SVPS34_control", "Rel"))
        self.rel2.setText(_translate("SVPS34_control", "Rel"))
        self.rel3.setText(_translate("SVPS34_control", "Rel"))
        self.rel4.setText(_translate("SVPS34_control", "Rel"))
        self.rel5.setText(_translate("SVPS34_control", "Rel"))
        self.rel6.setText(_translate("SVPS34_control", "Rel"))
        self.rel7.setText(_translate("SVPS34_control", "Rel"))
        self.common_rel_button.setText(_translate("SVPS34_control", "Common Rel"))
        self.remote_button.setText(_translate("SVPS34_control", "Remote"))
        self.get_temp_button.setText(_translate("SVPS34_control", "Get temperature"))
        self.temp_label.setText(_translate("SVPS34_control", "Temperature = "))
    def ty(self):
        print(666666)


if __name__ == "__main__":
    import sys
    number = 9
    #print(bytes("C" + str(number),encoding='utf8'))



    app = QtWidgets.QApplication(sys.argv)
    SVPS34_control = QtWidgets.QMainWindow()
    ui = Ui_SVPS34_control()
    ui.setupUi(SVPS34_control)
    SVPS34_control.show()
    sys.exit(app.exec_())
