# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fragment.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_save(object):
    def setupUi(self, settings_save):
        settings_save.setObjectName("settings_save")
        settings_save.resize(578, 520)
        self.buttonBox = QtWidgets.QDialogButtonBox(settings_save)
        self.buttonBox.setGeometry(QtCore.QRect(130, 380, 331, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(settings_save)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 80, 261, 105))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
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
        self.way_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
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
        self.repeat_measurement_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.repeat_measurement_enter.setEditable(True)
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
        self.repeat_exp_enter = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.repeat_exp_enter.setEditable(True)
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

        self.retranslateUi(settings_save)
        self.buttonBox.accepted.connect(settings_save.accept) # type: ignore
        self.buttonBox.rejected.connect(settings_save.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(settings_save)

    def retranslateUi(self, settings_save):
        _translate = QtCore.QCoreApplication.translate
        settings_save.setWindowTitle(_translate("settings_save", "Dialog"))
        self.label_19.setText(_translate("settings_save", "Как сохранить результаты?"))
        self.way_save_button.setText(_translate("settings_save", "Путь"))
        self.label_21.setText(_translate("settings_save", "Кол-во измерений в точке"))
        self.repeat_measurement_enter.setCurrentText(_translate("settings_save", "1"))
        self.repeat_measurement_enter.setItemText(0, _translate("settings_save", "1"))
        self.repeat_measurement_enter.setItemText(1, _translate("settings_save", "2"))
        self.repeat_measurement_enter.setItemText(2, _translate("settings_save", "3"))
        self.repeat_measurement_enter.setItemText(3, _translate("settings_save", "4"))
        self.repeat_measurement_enter.setItemText(4, _translate("settings_save", "5"))
        self.repeat_measurement_enter.setItemText(5, _translate("settings_save", "6"))
        self.repeat_measurement_enter.setItemText(6, _translate("settings_save", "7"))
        self.repeat_measurement_enter.setItemText(7, _translate("settings_save", "8"))
        self.repeat_measurement_enter.setItemText(8, _translate("settings_save", "9"))
        self.repeat_measurement_enter.setItemText(9, _translate("settings_save", "10"))
        self.label_20.setText(_translate("settings_save", "Кол-во повторов эксперимента"))
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