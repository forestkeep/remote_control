# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relay_set.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_relay(QtWidgets.QDialog):
    def setupUi(self, Set_power_supply):
        Set_power_supply.setObjectName("Set_power_supply")
        Set_power_supply.resize(300, 350)
        Set_power_supply.setSizeGripEnabled(False)
        Set_power_supply.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Set_power_supply)
        self.buttonBox.setGeometry(QtCore.QRect(90, 310, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 281, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        # self.label_12.setMouseTracking(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setEnabled(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.change_pol_button = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_2)
        self.change_pol_button.setChecked(True)
        self.change_pol_button.setObjectName("change_pol_button")
        self.horizontalLayout_2.addWidget(self.change_pol_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_10.setGeometry(
            QtCore.QRect(10, 100, 280, 120))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        # self.label_15.setMouseTracking(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_sourse = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_sourse.setObjectName("label_sourse_2")
        self.gridLayout.addWidget(self.label_sourse, 1, 0, 1, 1)
        self.label_sourse_3 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_sourse_3.setObjectName("label_sourse")
        self.gridLayout.addWidget(self.label_sourse_3, 0, 0, 1, 1)
        self.triger_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        # self.triger_enter.setMouseTracking(True)
        self.triger_enter.setEditable(True)
        self.triger_enter.setObjectName("sourse_enter")
        self.triger_enter.addItem("")
        self.gridLayout.addWidget(self.triger_enter, 0, 1, 1, 1)#3333333333333333333333333
        self.sourse_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        # self.sourse_enter.setMouseTracking(True)
        self.sourse_enter.setEditable(True)
        self.sourse_enter.setObjectName("sourse_enter_2")
        self.sourse_enter.addItem("")
        self.sourse_enter.addItem("")
        self.sourse_enter.addItem("")
        self.sourse_enter.addItem("")
        self.sourse_enter.addItem("")
        self.gridLayout.addWidget(self.sourse_enter, 1, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)
        
        #self.horizontalLayout = QtWidgets.QHBoxLayout()
        #self.horizontalLayout.setObjectName("horizontalLayout")

        self.num_meas_label = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.num_meas_label.setObjectName("num_meas_label")
        #self.horizontalLayout.addWidget(self.num_meas_label)
        self.gridLayout.addWidget(self.num_meas_label,2,0,1,1)

        self.num_meas_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        self.num_meas_enter.setEditable(True)
        self.num_meas_enter.setObjectName("num_meas_enter")
        #self.horizontalLayout.addWidget(self.num_meas_enter)
        self.gridLayout.addWidget(self.num_meas_enter,2,1,1,1)

        #self.verticalLayout_10.addLayout(self.horizontalLayout)

        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------
        
        
        self.label_154 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        #font = QtGui.QFont()
        #font.setPointSize(10)
        #self.label_154.setFont(font)
        self.label_154.setObjectName("label_154")
        self.gridLayout.addWidget(self.label_154, 3,0,1,1)

        self.num_series_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)

        self.num_series_enter.setEditable(True)
        self.num_series_enter.setObjectName("num_series_enter")
        self.num_series_enter.addItem("")
        self.num_series_enter.addItem("")
        #self.num_series_enter.setStyleSheet(
         #       "background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.num_series_enter,3,1,1,1)
        #--------------------------------------------------
        #--------------------------------------------------
        #--------------------------------------------------

        self.verticalLayoutWidget_11 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_11.setGeometry(
            QtCore.QRect(10, 220, 281, 80))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        # self.label_2.setMouseTracking(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.boudrate = QtWidgets.QComboBox(self.verticalLayoutWidget_11)
        # self.boudrate.setMouseTracking(True)
        self.boudrate.setEditable(True)
        self.boudrate.setObjectName("boudrate")
        self.boudrate.addItem("")
        self.horizontalLayout_5.addWidget(self.boudrate)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.comportslist = QtWidgets.QComboBox(self.verticalLayoutWidget_11)
        self.comportslist.setMouseTracking(True)
        self.comportslist.setEditable(True)
        self.comportslist.setObjectName("comportslist")
        self.horizontalLayout_4.addWidget(self.comportslist)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        '''
        self.line = QtWidgets.QFrame(Set_power_supply)
        self.line.setGeometry(QtCore.QRect(10, 210, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Set_power_supply)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        '''

        self.retranslateUi(Set_power_supply)
        self.buttonBox.accepted.connect(
            Set_power_supply.accept)  # type: ignore
        self.buttonBox.rejected.connect(
            Set_power_supply.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Set_power_supply)

    def mouseMoveEvent(self, event):
        print(event)
        print('coords: ( % d : % d )' % (event.x(), event.y()))

    def retranslateUi(self, Set_power_supply):
        _translate = QtCore.QCoreApplication.translate
        Set_power_supply.setWindowTitle(
            _translate("Set_power_supply", "Relay_set"))
        self.label_12.setText(_translate("Set_power_supply", "Режим работы"))
        self.label_154.setText(_translate("Set_power_supply", "Количество серий"))
        self.radioButton.setText(_translate(
            "Set_power_supply", "Включение - Выключение"))
        self.change_pol_button.setText(_translate(
            "Set_power_supply", "Смена полярности"))
        self.label_15.setText(_translate("Set_power_supply", "Срабатывание"))
        self.label_sourse.setText(_translate(
            "Set_power_supply", "Время (сек)"))
        self.label_sourse_3.setText(_translate("Set_power_supply", "Триггер"))
        self.triger_enter.setCurrentText(
            _translate("Set_power_supply", "Таймер"))
        self.triger_enter.setItemText(
            0, _translate("Set_power_supply", "Таймер"))
        self.sourse_enter.setCurrentText(_translate("Set_power_supply", "1"))
        self.sourse_enter.setItemText(0, _translate("Set_power_supply", "1"))
        self.sourse_enter.setItemText(1, _translate("Set_power_supply", "5"))
        self.sourse_enter.setItemText(
            2, _translate("Set_power_supply", "10"))
        self.sourse_enter.setItemText(
            3, _translate("Set_power_supply", "20"))
        self.sourse_enter.setItemText(
            4, _translate("Set_power_supply", "30"))
        self.num_meas_label.setText(_translate(
            "Set_power_supply", "Количество изм в серии"))
        self.label_2.setText(_translate(
            "Set_power_supply", "Настройки подключения"))
        self.label_11.setText(_translate("Set_power_supply", "Baudrate"))
        self.boudrate.setItemText(0, _translate("Set_power_supply", "9600"))
        self.label_10.setText(_translate("Set_power_supply", "COM"))
