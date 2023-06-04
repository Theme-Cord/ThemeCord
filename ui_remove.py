from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import subprocess
import os


class Ui_Remove(object):
    def setupUi(self, Remove):
        Remove.setObjectName("Remove")
        Remove.resize(393, 219)
        self.buttonBox = QtWidgets.QDialogButtonBox(Remove)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Remove)
        self.label.setGeometry(QtCore.QRect(30, 90, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Remove)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Remove.reject)
        QtCore.QMetaObject.connectSlotsByName(Remove)

    def retranslateUi(self, Remove):
        _translate = QtCore.QCoreApplication.translate
        Remove.setWindowTitle(_translate("Remove", "Remove"))
        self.label.setText(_translate("Remove", "Are you sure you want to remove all of the themes applied?"))

    def accept(self):
        subprocess.run([os.path.join(os.path.dirname(__file__), "themecord", "injector.exe"), "--revert"], check=True)
        message_box = QMessageBox()
        message_box.setWindowTitle("Complete")
        message_box.setText("Removed themes on the current running discord.")
        message_box.setIcon(QMessageBox.Information)
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()
