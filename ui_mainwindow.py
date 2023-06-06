# Source: /UI/Home.ui
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # ui code
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 535)
        MainWindow.setStyleSheet("@import url('https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css');\n   font-family: \'Roboto\', sans-serif;\n"
"    color: #FFF;\n"
"    background-color: #36393f;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 400, 300, 90))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Github = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Github.setStyleSheet("\n"
"\n"
"* {\n"
"    display: inline-block;\n"
"    padding: 12px 30px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    background-color: rgb(89, 89, 89);\n"
"    color: #FFF;\n"
"    border-radius: 4px;\n"
"    text-decoration: none;\n"

"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: rgb(40, 40, 40);\n"
"    color: #FFF;\n"
"}")
        self.Github.setObjectName("Github")
        self.horizontalLayout.addWidget(self.Github)
        self.Discord = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Discord.setStyleSheet("\n"
"\n"
"* {\n"
"    display: inline-block;\n"
"    padding: 12px 30px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    background-color: #4e56cb;\n"
"    color: #FFF;\n"
"    border-radius: 4px;\n"
"    text-decoration: none;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"*:hover {\n"
"    background-color: #3641d4;\n"
"    color: #FFF;\n"
"}")
        self.Discord.setObjectName("Discord")
        self.horizontalLayout.addWidget(self.Discord)
        self.themeText = QtWidgets.QTextEdit(self.centralwidget)
        self.themeText.setGeometry(QtCore.QRect(220, 170, 451, 87))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.themeText.setFont(font)
        self.themeText.setStyleSheet("*{\n"
"            text-align: center;\n"
"}")
        self.themeText.setObjectName("themeText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 80, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("*{\n"
"            text-align: center;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 270, 211, 51))
        self.pushButton.setStyleSheet("        * {\n"
"            display: inline-block;\n"
"            padding: 12px 30px;\n"
"            font-size: 18px;\n"
"            font-weight: bold;\n"
"            text-transform: uppercase;\n"
"            background-color: #65b557;\n"
"            color: #FFF;\n"
"            border-radius: 4px;\n"
"            text-decoration: none;\n"
"            transition: background-color 0.3s ease;\n"
"        }\n"
"        *:hover{\n"
"            background-color: #1f8c0b;\n"
"            color: #FFF;\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 420, 271, 51))
        self.pushButton_2.setStyleSheet("        * {\n"
"            display: inline-block;\n"
"            padding: 12px 30px;\n"
"            font-size: 18px;\n"
"            font-weight: bold;\n"
"            text-transform: uppercase;\n"
"            background-color: red;\n"
"            color: #FFF;\n"
"            border-radius: 4px;\n"
"            text-decoration: none;\n"
"            transition: background-color 0.3s ease;\n"
"        }\n"
"        *:hover{\n"
"            background-color: rgb(140, 0, 0);\n"
"            color: #FFF;\n"
"        }")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Github.setText(_translate("MainWindow", "GitHub"))
        self.Discord.setText(_translate("MainWindow", "Discord"))
        self.themeText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto,sans-serif\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter your theme link</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Theme Cord!"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove all themes"))
