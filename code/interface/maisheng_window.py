# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maisheng.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logging
logger = logging.getLogger(__name__)

class maisheng_ui_window(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 611)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.onoffoutputbutton = QtWidgets.QPushButton(self.centralwidget)
        self.onoffoutputbutton.setGeometry(QtCore.QRect(590, 90, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.onoffoutputbutton.setFont(font)
        self.onoffoutputbutton.setObjectName("onoffoutputbutton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 330, 771, 231))
        self.frame_2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.startstopButton = QtWidgets.QPushButton(self.frame_2)
        self.startstopButton.setGeometry(QtCore.QRect(210, 120, 231, 61))
        self.startstopButton.setObjectName("startstopButton")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(600, 10, 171, 201))
        self.frame.setStyleSheet("background-color: rgb(172, 172, 190);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 126, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scan_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setObjectName("scan_button")
        self.verticalLayout_3.addWidget(self.scan_button)
        self.comportslist = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comportslist.setObjectName("comportslist")
        self.verticalLayout_3.addWidget(self.comportslist)
        self.comportslist_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comportslist_2.setObjectName("comportslist_2")
        self.verticalLayout_3.addWidget(self.comportslist_2)
        self.connect_button = QtWidgets.QPushButton(
            self.verticalLayoutWidget_3)
        self.connect_button.setMouseTracking(False)
        self.connect_button.setObjectName("connect_button")
        self.verticalLayout_3.addWidget(self.connect_button)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(20, 174, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 10, 111, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectmode = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.selectmode.setObjectName("selectmode")
        self.verticalLayout_2.addWidget(self.selectmode)
        self.selectstart_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.selectstart_2.setObjectName("selectstart_2")
        self.verticalLayout_2.addWidget(self.selectstart_2)
        self.selectfinish_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.selectfinish_2.setObjectName("selectfinish_2")
        self.verticalLayout_2.addWidget(self.selectfinish_2)
        self.numberofpoints = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.numberofpoints.setObjectName("numberofpoints")
        self.verticalLayout_2.addWidget(self.numberofpoints)
        self.selecttrigger = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.selecttrigger.setObjectName("selecttrigger")
        self.verticalLayout_2.addWidget(self.selecttrigger)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_4.setGeometry(
            QtCore.QRect(330, 10, 111, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.selectstart_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.selectstart_5.setObjectName("selectstart_5")
        self.verticalLayout_4.addWidget(self.selectstart_5)
        self.selectfinish_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.selectfinish_3.setObjectName("selectfinish_3")
        self.verticalLayout_4.addWidget(self.selectfinish_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 71, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_5.setGeometry(
            QtCore.QRect(210, 10, 111, 101))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(210, 190, 231, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(37, 10, 41, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 10, 201, 301))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.VoltageLCD = QtWidgets.QLCDNumber(self.widget1)
        self.VoltageLCD.setDigitCount(7)
        self.VoltageLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.VoltageLCD.setObjectName("VoltageLCD")
        self.verticalLayout_7.addWidget(self.VoltageLCD)
        self.currentLCD = QtWidgets.QLCDNumber(self.widget1)
        self.currentLCD.setDigitCount(4)
        self.currentLCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currentLCD.setObjectName("currentLCD")
        self.verticalLayout_7.addWidget(self.currentLCD)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(300, 10, 241, 311))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Voltage = QtWidgets.QDial(self.widget2)
        self.Voltage.setMaximum(20000)
        self.Voltage.setSingleStep(1)
        self.Voltage.setObjectName("Voltage")
        self.verticalLayout_6.addWidget(self.Voltage)
        self.Current = QtWidgets.QDial(self.widget2)
        self.Current.setMaximum(1200)
        self.Current.setObjectName("Current")
        self.verticalLayout_6.addWidget(self.Current)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.setWindowTitle("MainWindow")
        self.onoffoutputbutton.setText("Вкл")
        self.startstopButton.setText("Start")
        self.scan_button.setText("Scan")
        self.connect_button.setText("Connect")
        self.label_10.setText("Status:")
        self.label_7.setText("Mode")
        self.label_3.setText("Start")
        self.label_4.setText("Finish")
        self.label_5.setText("Points")
        self.label_6.setText("Period(s)")
        self.label_8.setText("Max Voltage")
        self.label_9.setText("Max Current")
        self.label.setText("V")
        self.label_2.setText("A")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.onoffoutputbutton.setText(_translate("MainWindow", "Вкл"))
        self.startstopButton.setText(_translate("MainWindow", "Start"))
        self.scan_button.setText(_translate("MainWindow", "Scan"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.label_10.setText(_translate("MainWindow", "Status:"))
        self.label_7.setText(_translate("MainWindow", "Mode"))
        self.label_3.setText(_translate("MainWindow", "Start"))
        self.label_4.setText(_translate("MainWindow", "Finish"))
        self.label_5.setText(_translate("MainWindow", "Points"))
        self.label_6.setText(_translate("MainWindow", "Period(s)"))
        self.label_8.setText(_translate("MainWindow", "Max Voltage"))
        self.label_9.setText(_translate("MainWindow", "Max Current"))
        self.label.setText(_translate("MainWindow", "V"))
        self.label_2.setText(_translate("MainWindow", "A"))
