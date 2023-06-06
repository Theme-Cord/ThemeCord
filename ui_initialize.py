# Source: /UI/Intialize.ui

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # ui code
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 473)
        MainWindow.setStyleSheet("@import url('https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css');\n    font-family: \'Roboto\', sans-serif;\n"
"    color: #FFF;\n"
"    background-color: #36393f;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 310, 439, 98))
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
        self.Website = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Website.setStyleSheet("\n"
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
        self.Website.setObjectName("Website")
        self.horizontalLayout.addWidget(self.Website)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 40, 431, 251))
        self.frame.setStyleSheet("*{\n"
"            width: 300px;\n"
"            background-color: #4e56cb;\n"
"            border-radius: 8px;\n"
"            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);\n"
"            margin: 10px;\n"
"            padding: 20px;\n"
"            text-align: center;\n"
"            color: #fff;\n"
"}\n"
"* img {\n"
"            max-width: 100%;\n"
"            height: auto;\n"
"            margin-bottom: 10px;\n"
"        }\n"
"\n"
"       * h3 {\n"
"            font-size: 1.2rem;\n"
"            font-weight: bold;\n"
"            margin-bottom: 10px;\n"
"        }\n"
"\n"
"        * p {\n"
"            font-size: 0.9rem;\n"
"            color: #fff;\n"
"        }\n"
"        * a {\n"
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
"        * a:hover{\n"
"            background-color: #1f8c0b;\n"
"            color: #FFF;\n"
"        }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 371, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Initialize = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.Initialize.setObjectName("Initialize")
        self.verticalLayout.addWidget(self.Initialize)
        self.WhyInitialize = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.WhyInitialize.setObjectName("WhyInitialize")
        self.verticalLayout.addWidget(self.WhyInitialize)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 24))
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
        self.Website.setText(_translate("MainWindow", "Website"))
        self.label.setText(_translate("MainWindow", "Initialize the theme cord"))
        self.Initialize.setText(_translate("MainWindow", "Initialize"))
        self.WhyInitialize.setText(_translate("MainWindow", "Why need to initialize?"))
