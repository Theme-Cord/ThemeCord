import urllib.request
import subprocess
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from ui_remove import Ui_Remove


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.inject_theme)
        self.ui.pushButton_2.clicked.connect(self.remove_theme)

    def remove_theme(self):
        dialog = QtWidgets.QDialog(self)
        ui = Ui_Remove()
        ui.setupUi(dialog)
        dialog.exec_()

    def inject_theme(self):
        css_url = self.ui.textEdit.toPlainText()
        if css_url == "":
            self.ui.label.setText("Please fill the input")
            return
        css_filename = css_url.split("/")[-1]
        css_path = os.path.join(os.path.dirname(__file__), "themecord", css_filename)
        urllib.request.urlretrieve(css_url, css_path)
        subprocess.run([os.path.join(os.path.dirname(__file__), "themecord", "injector.exe"), "--css", css_path], check=True)
        message_box = QMessageBox()
        message_box.setWindowTitle("Complete")
        message_box.setText("Installed theme on the current running discord.")
        message_box.setIcon(QMessageBox.Information)
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
