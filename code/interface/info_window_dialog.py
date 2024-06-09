# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_window_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import logging
logger = logging.getLogger(__name__)

class Ui_Dialog(QtWidgets.QDialog):
    signal_to_main_window = QtCore.pyqtSignal(bool)

    def setupUi(self, Dialog, mother_window):
        self.signal_to_main_window.connect(
            mother_window.message_from_info_dialog)

        Dialog.setObjectName("Ахтунг!")
        Dialog.resize(210, 161)
        #Dialog.setStyleSheet("background-color: rgb(255, 200, 202);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 120, 161, 32))
        #self.buttonBox.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelinfo = QtWidgets.QLabel(Dialog)
        self.labelinfo.setGeometry(QtCore.QRect(20, 0, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelinfo.setFont(font)
        self.labelinfo.setStyleSheet("\n"
                                     "")
        self.labelinfo.setWordWrap(True)
        self.labelinfo.setObjectName("labelinfo")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(
            self.send_signal_ok)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(
            self.send_signal_cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelinfo.setText(_translate(
            "D", "Установка уже создана. Закрыть текущую установку и создать новую?"))

    def send_signal_ok(self):
        self.signal_to_main_window.emit(True)

    def send_signal_cancel(self):
        self.signal_to_main_window.emit(False)
