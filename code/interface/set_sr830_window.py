# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_sr830.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Set_sr830(QtWidgets.QDialog):
    def setupUi(self, Set_power_supply):
        Set_power_supply.setObjectName("Set_sr830")
        Set_power_supply.resize(303, 664)
        Set_power_supply.setSizeGripEnabled(False)
        Set_power_supply.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Set_power_supply)
        self.buttonBox.setGeometry(QtCore.QRect(100, 620, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 330, 281, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.frequency_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.frequency_enter.setCurrentText("")
        self.frequency_enter.setObjectName("frequency_enter")
        self.horizontalLayout_3.addWidget(self.frequency_enter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.amplitude_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.amplitude_enter.setCurrentText("")
        self.amplitude_enter.setObjectName("amplitude_enter")
        self.horizontalLayout_2.addWidget(self.amplitude_enter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 281, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.time_const_enter_number = QtWidgets.QComboBox(
            self.verticalLayoutWidget_3)
        self.time_const_enter_number.setEditable(False)
        self.time_const_enter_number.setObjectName("time_const_enter_number")
        self.time_const_enter_number.addItem("")
        self.time_const_enter_number.addItem("")
        self.horizontalLayout_7.addWidget(self.time_const_enter_number)
        self.time_const_enter_factor = QtWidgets.QComboBox(
            self.verticalLayoutWidget_3)
        self.time_const_enter_factor.setEditable(False)
        self.time_const_enter_factor.setObjectName("time_const_enter_factor")
        self.time_const_enter_factor.addItem("")
        self.time_const_enter_factor.addItem("")
        self.time_const_enter_factor.addItem("")
        self.horizontalLayout_7.addWidget(self.time_const_enter_factor)
        self.time_const_enter_decimal_factor = QtWidgets.QComboBox(
            self.verticalLayoutWidget_3)
        self.time_const_enter_decimal_factor.setStyleSheet("")
        self.time_const_enter_decimal_factor.setEditable(False)
        self.time_const_enter_decimal_factor.setObjectName(
            "time_const_enter_decimal_factor")
        self.time_const_enter_decimal_factor.addItem("")
        self.time_const_enter_decimal_factor.addItem("")
        self.time_const_enter_decimal_factor.addItem("")
        self.time_const_enter_decimal_factor.addItem("")
        self.horizontalLayout_7.addWidget(self.time_const_enter_decimal_factor)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.Filt_slope_enter_level = QtWidgets.QComboBox(
            self.verticalLayoutWidget_3)
        self.Filt_slope_enter_level.setEditable(False)
        self.Filt_slope_enter_level.setObjectName("Filt_slope_enter_level")
        self.Filt_slope_enter_level.addItem("")
        self.Filt_slope_enter_level.addItem("")
        self.Filt_slope_enter_level.addItem("")
        self.Filt_slope_enter_level.addItem("")
        self.verticalLayout_7.addWidget(self.Filt_slope_enter_level)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.line_8 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_10.addWidget(self.line_8)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.SYNK_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.SYNK_enter.setEditable(False)
        self.SYNK_enter.setObjectName("min_enter_7")
        self.SYNK_enter.addItem("")
        self.SYNK_enter.addItem("")
        self.verticalLayout_8.addWidget(self.SYNK_enter)
        self.horizontalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 130, 171, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sensitivity_enter_number = QtWidgets.QComboBox(
            self.verticalLayoutWidget_4)
        self.sensitivity_enter_number.setEditable(False)
        self.sensitivity_enter_number.setObjectName("sensitivity_enter_number")
        self.sensitivity_enter_number.addItem("")
        self.sensitivity_enter_number.addItem("")
        self.sensitivity_enter_number.addItem("")
        self.horizontalLayout_8.addWidget(self.sensitivity_enter_number)
        self.sensitivity_enter_factor = QtWidgets.QComboBox(
            self.verticalLayoutWidget_4)
        self.sensitivity_enter_factor.setEditable(False)
        self.sensitivity_enter_factor.setObjectName("sensitivity_enter_factor")
        self.sensitivity_enter_factor.addItem("")
        self.sensitivity_enter_factor.addItem("")
        self.sensitivity_enter_factor.addItem("")
        self.horizontalLayout_8.addWidget(self.sensitivity_enter_factor)
        self.sensitivity_enter_decimal_factor = QtWidgets.QComboBox(
            self.verticalLayoutWidget_4)
        self.sensitivity_enter_decimal_factor.setStyleSheet("")
        self.sensitivity_enter_decimal_factor.setEditable(False)
        self.sensitivity_enter_decimal_factor.setObjectName(
            "sensitivity_enter_decimal_factor")
        self.sensitivity_enter_decimal_factor.addItem("")
        self.sensitivity_enter_decimal_factor.addItem("")
        self.sensitivity_enter_decimal_factor.addItem("")
        self.sensitivity_enter_decimal_factor.addItem("")
        self.horizontalLayout_8.addWidget(
            self.sensitivity_enter_decimal_factor)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 230, 171, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.input_channels_enter = QtWidgets.QComboBox(
            self.verticalLayoutWidget_5)
        self.input_channels_enter.setEditable(False)
        self.input_channels_enter.setObjectName("input_channels_enter")
        self.input_channels_enter.addItem("")
        self.input_channels_enter.addItem("")
        self.input_channels_enter.addItem("")
        self.input_channels_enter.addItem("")
        self.horizontalLayout_9.addWidget(self.input_channels_enter)
        self.input_type_enter = QtWidgets.QComboBox(
            self.verticalLayoutWidget_5)
        self.input_type_enter.setEditable(False)
        self.input_type_enter.setObjectName("input_type_enter")
        self.input_type_enter.addItem("")
        self.input_type_enter.addItem("")
        self.horizontalLayout_9.addWidget(self.input_type_enter)
        self.connect_ch_enter = QtWidgets.QComboBox(
            self.verticalLayoutWidget_5)
        self.connect_ch_enter.setStyleSheet("")
        self.connect_ch_enter.setEditable(False)
        self.connect_ch_enter.setObjectName("step_enter_3")
        self.connect_ch_enter.addItem("")
        self.connect_ch_enter.addItem("")
        self.horizontalLayout_9.addWidget(self.connect_ch_enter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(200, 130, 91, 80))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.reserve_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_6)
        self.reserve_enter.setEditable(False)
        self.reserve_enter.setObjectName("reserve_enter")
        self.reserve_enter.addItem("")
        self.reserve_enter.addItem("")
        self.reserve_enter.addItem("")
        self.horizontalLayout_12.addWidget(self.reserve_enter)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(200, 230, 91, 80))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_9.addWidget(self.label_19)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.filters_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_9)
        self.filters_enter.setEditable(False)
        self.filters_enter.setObjectName("min_enter_5")
        self.filters_enter.addItem("")
        self.filters_enter.addItem("")
        self.filters_enter.addItem("")
        self.filters_enter.addItem("")
        self.horizontalLayout_13.addWidget(self.filters_enter)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.verticalLayoutWidget_10 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_10.setGeometry(
            QtCore.QRect(10, 430, 281, 95))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.label_sourse = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_sourse.setObjectName("label_sourse_2")
        self.gridLayout.addWidget(self.label_sourse, 1, 0, 1, 1)

        self.label_triger = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_triger.setObjectName("label_sourse")
        self.gridLayout.addWidget(self.label_triger, 0, 0, 1, 1)
        self.triger_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        self.triger_enter.setObjectName("triger_enter")
        self.triger_enter.addItem("")
        self.gridLayout.addWidget(self.triger_enter, 0, 1, 1, 1)

        self.sourse_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        self.sourse_enter.setCurrentText("")
        self.sourse_enter.setObjectName("sourse_enter")
        self.gridLayout.addWidget(self.sourse_enter, 1, 1, 1, 1)

        self.num_meas_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        self.num_meas_enter.setCurrentText("")
        self.num_meas_enter.setObjectName("sourse_enter1")
        self.gridLayout.addWidget(self.num_meas_enter, 2, 1, 1, 1)

        self.label_num_meas = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_num_meas.setObjectName("label_num_meas")
        self.gridLayout.addWidget(self.label_num_meas, 2, 0, 1, 1)

        self.verticalLayout_10.addLayout(self.gridLayout)

        self.verticalLayoutWidget_11 = QtWidgets.QWidget(Set_power_supply)
        self.verticalLayoutWidget_11.setGeometry(
            QtCore.QRect(10, 530, 281, 80))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.boudrate = QtWidgets.QComboBox(self.verticalLayoutWidget_11)
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
        self.comportslist.setObjectName("comportslist")
        self.horizontalLayout_4.addWidget(self.comportslist)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Set_power_supply)
        self.line.setGeometry(QtCore.QRect(10, 525, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Set_power_supply)
        self.line_2.setGeometry(QtCore.QRect(10, 410, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Set_power_supply)
        self.line_3.setGeometry(QtCore.QRect(10, 310, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Set_power_supply)
        self.line_4.setGeometry(QtCore.QRect(10, 210, 281, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Set_power_supply)
        self.line_5.setGeometry(QtCore.QRect(10, 110, 281, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Set_power_supply)
        self.line_6.setGeometry(QtCore.QRect(180, 130, 20, 81))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Set_power_supply)
        self.line_7.setGeometry(QtCore.QRect(180, 230, 20, 81))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.retranslateUi(Set_power_supply)
        self.buttonBox.accepted.connect(
            Set_power_supply.accept)  # type: ignore
        self.buttonBox.rejected.connect(
            Set_power_supply.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Set_power_supply)

    def retranslateUi(self, Set_power_supply):
        _translate = QtCore.QCoreApplication.translate
        Set_power_supply.setWindowTitle(
            _translate("Set_power_supply", "Dialog"))
        self.label_12.setText(_translate(
            "Set_power_supply", "Параметры генератора"))
        self.label_5.setText(_translate("Set_power_supply", "Частота(Гц)"))
        self.label_4.setText(_translate("Set_power_supply", "Амплитуда(В)"))
        self.label.setText(_translate(
            "Set_power_supply", "Временная константа"))
        self.time_const_enter_number.setCurrentText(
            _translate("Set_power_supply", "1"))
        self.time_const_enter_number.setItemText(
            0, _translate("Set_power_supply", "1"))
        self.time_const_enter_number.setItemText(
            1, _translate("Set_power_supply", "3"))
        self.time_const_enter_factor.setCurrentText(
            _translate("Set_power_supply", "X1"))
        self.time_const_enter_factor.setItemText(
            0, _translate("Set_power_supply", "X1"))
        self.time_const_enter_factor.setItemText(
            1, _translate("Set_power_supply", "X10"))
        self.time_const_enter_factor.setItemText(
            2, _translate("Set_power_supply", "X100"))
        self.time_const_enter_decimal_factor.setCurrentText(
            _translate("Set_power_supply", "ks"))
        self.time_const_enter_decimal_factor.setItemText(
            0, _translate("Set_power_supply", "ks"))
        self.time_const_enter_decimal_factor.setItemText(
            1, _translate("Set_power_supply", "s"))
        self.time_const_enter_decimal_factor.setItemText(
            2, _translate("Set_power_supply", "ms"))
        self.time_const_enter_decimal_factor.setItemText(
            3, _translate("Set_power_supply", "us"))
        self.label_16.setText(_translate("Set_power_supply", "Filter slope"))
        self.Filt_slope_enter_level.setCurrentText(
            _translate("Set_power_supply", "6 dB"))
        self.Filt_slope_enter_level.setItemText(
            0, _translate("Set_power_supply", "6 dB"))
        self.Filt_slope_enter_level.setItemText(
            1, _translate("Set_power_supply", "12 dB"))
        self.Filt_slope_enter_level.setItemText(
            2, _translate("Set_power_supply", "18 dB"))
        self.Filt_slope_enter_level.setItemText(
            3, _translate("Set_power_supply", "24 dB"))
        self.label_17.setText(_translate("Set_power_supply", "SYNK < 200 Hz"))
        self.SYNK_enter.setCurrentText(_translate("Set_power_supply", "On"))
        self.SYNK_enter.setItemText(0, _translate("Set_power_supply", "On"))
        self.SYNK_enter.setItemText(1, _translate("Set_power_supply", "Off"))
        self.label_13.setText(_translate(
            "Set_power_supply", "Чувствительность"))
        self.sensitivity_enter_number.setCurrentText(
            _translate("Set_power_supply", "1"))
        self.sensitivity_enter_number.setItemText(
            0, _translate("Set_power_supply", "1"))
        self.sensitivity_enter_number.setItemText(
            1, _translate("Set_power_supply", "2"))
        self.sensitivity_enter_number.setItemText(
            2, _translate("Set_power_supply", "5"))
        self.sensitivity_enter_factor.setCurrentText(
            _translate("Set_power_supply", "X1"))
        self.sensitivity_enter_factor.setItemText(
            0, _translate("Set_power_supply", "X1"))
        self.sensitivity_enter_factor.setItemText(
            1, _translate("Set_power_supply", "X10"))
        self.sensitivity_enter_factor.setItemText(
            2, _translate("Set_power_supply", "X100"))
        self.sensitivity_enter_decimal_factor.setCurrentText(
            _translate("Set_power_supply", "V/uA"))
        self.sensitivity_enter_decimal_factor.setItemText(
            0, _translate("Set_power_supply", "V/uA"))
        self.sensitivity_enter_decimal_factor.setItemText(
            1, _translate("Set_power_supply", "mV/nA"))
        self.sensitivity_enter_decimal_factor.setItemText(
            2, _translate("Set_power_supply", "uV/pA"))
        self.sensitivity_enter_decimal_factor.setItemText(
            3, _translate("Set_power_supply", "nV/fA"))
        self.label_14.setText(_translate("Set_power_supply", "Вход сигнала"))
        self.input_channels_enter.setCurrentText(
            _translate("Set_power_supply", "A"))
        self.input_channels_enter.setItemText(
            0, _translate("Set_power_supply", "A"))
        self.input_channels_enter.setItemText(
            1, _translate("Set_power_supply", "A - B"))
        self.input_channels_enter.setItemText(
            2, _translate("Set_power_supply", "I (10^6)"))
        self.input_channels_enter.setItemText(
            3, _translate("Set_power_supply", "I (10^8)"))
        self.input_type_enter.setCurrentText(
            _translate("Set_power_supply", "AC"))
        self.input_type_enter.setItemText(
            0, _translate("Set_power_supply", "AC"))
        self.input_type_enter.setItemText(
            1, _translate("Set_power_supply", "DC"))
        self.connect_ch_enter.setCurrentText(
            _translate("Set_power_supply", "float"))
        self.connect_ch_enter.setItemText(
            0, _translate("Set_power_supply", "float"))
        self.connect_ch_enter.setItemText(
            1, _translate("Set_power_supply", "ground"))
        self.label_18.setText(_translate("Set_power_supply", "Reserve"))
        self.reserve_enter.setCurrentText(
            _translate("Set_power_supply", "high reserve"))
        self.reserve_enter.setItemText(
            0, _translate("Set_power_supply", "high reserve"))
        self.reserve_enter.setItemText(
            1, _translate("Set_power_supply", "normal"))
        self.reserve_enter.setItemText(
            2, _translate("Set_power_supply", "low noise"))
        self.label_19.setText(_translate("Set_power_supply", "Filters"))
        self.filters_enter.setCurrentText(
            _translate("Set_power_supply", "line"))
        self.filters_enter.setItemText(
            0, _translate("Set_power_supply", "line"))
        self.filters_enter.setItemText(
            1, _translate("Set_power_supply", "2X line"))
        self.filters_enter.setItemText(
            2, _translate("Set_power_supply", "both"))
        self.filters_enter.setItemText(
            3, _translate("Set_power_supply", "out"))
        self.label_15.setText(_translate(
            "Set_power_supply", "Считывание параметров"))
        self.label_sourse.setText(_translate(
            "Set_power_supply", "Время (сек)"))
        self.label_triger.setText(_translate("Set_power_supply", "Триггер"))
        self.triger_enter.setCurrentText(
            _translate("Set_power_supply", "Таймер"))
        self.triger_enter.setItemText(
            0, _translate("Set_power_supply", "Таймер"))
        self.label_2.setText(_translate(
            "Set_power_supply", "Настройки подключения"))
        self.label_11.setText(_translate("Set_power_supply", "Baudrate"))
        self.label_num_meas.setText(_translate(
            "Set_power_supply", "Кол-во измерений"))
        self.boudrate.setItemText(0, _translate("Set_power_supply", "9600"))
        self.label_10.setText(_translate("Set_power_supply", "COM"))