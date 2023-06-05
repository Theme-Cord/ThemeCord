import urllib.request
import subprocess
import os
import webbrowser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui_mainwindow import Ui_MainWindow
from ui_initialize import Ui_MainWindow as Ui_Initialize


class MainWindow(QMainWindow):
    def check_file_exists(self):
        appdata_dir = os.getenv('APPDATA')  # Get the path to the AppData directory
        saves_dir = os.path.join(appdata_dir, 'ThemeCord', 'Saves')  # Create the path to the saves directory
        
        file_path = os.path.join(saves_dir, 'theme-cord.installed')  # Create the path to the file
        
        if os.path.exists(file_path):
            print("File exists!")
            return True
        else:
            print("File does not exist!")
            return False
    def __init__(self):
        super().__init__()
        if self.check_file_exists():
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setFixedSize(861, 535)
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
            self.ui.Discord.clicked.connect(self.open_discord)
            self.ui.Github.clicked.connect(self.open_github)
            self.ui.pushButton.clicked.connect(self.apply)
            self.ui.pushButton_2.clicked.connect(self.remove_theme)

        else:
            self.ui = Ui_Initialize()
            self.ui.setupUi(self)
            self.setFixedSize(546,743)
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
            self.ui.Discord.clicked.connect(self.open_discord)
            self.ui.Github.clicked.connect(self.open_github)
            self.ui.Website.clicked.connect(self.open_website)
            self.ui.WhyInitialize.clicked.connect(self.open_in)
            self.ui.Initialize.clicked.connect(self.init)
            
    def apply(self):
        # Get the input from the QTextEdit
        theme_text = self.ui.themeText.toPlainText()

        # Check if the input is empty or equals "Enter your theme link"
        if theme_text == "Enter your theme link" or theme_text == "":
            return self.ui.themeText.setText("Please fill me!")

        # Set the path to the CSS file
        css_path = os.path.join(os.path.dirname(__file__), "themecord", "template.css")
        
        # Create the new CSS content
        file_content = f"""
        @import url('{theme_text}');
        """

        # Append the new CSS content to the file
        with open(css_path, 'a') as file:
            file.write(file_content)

        message_box = QMessageBox()
        message_box.setWindowTitle("New theme added!")
        message_box.setText("ThemeCord has successfully added a new theme to Discord!")
        message_box.setIcon(QMessageBox.Information)
        message_box.addButton(QMessageBox.Ok)

        message_box.exec_()
    def remove_theme(self):
        # Set the path to the CSS file
        css_path = os.path.join(os.path.dirname(__file__), "themecord", "template.css")

        # Define the CSS content
        file_content = """
        /* CSS style for ThemeCord */
        /* Reset! */
        """

        # Write the CSS file
        with open(css_path, 'w') as file:
            file.write(file_content)
        # Show a success message box
        message_box = QMessageBox()
        message_box.setWindowTitle("All the themes are now removed!")
        message_box.setText("ThemeCord has been successfully removed every theme you applied to the discord.")
        message_box.setIcon(QMessageBox.Information)
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()
        return
    def init(self):
        # Set the path to the CSS file
        css_path = os.path.join(os.path.dirname(__file__), "themecord", "template.css")

        # Define the CSS content
        file_content = """
        /* CSS style for ThemeCord */
        /* Example: import url('url'); */
        """

        # Write the CSS file
        with open(css_path, 'w') as file:
            file.write(file_content)

        # Create the directory if it doesn't exist
        appdata_dir = os.getenv('APPDATA')  # Get the path to the AppData directory
        saves_dir = os.path.join(appdata_dir, 'ThemeCord', 'Saves')  # Create the path to the saves directory
        os.makedirs(saves_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Write the "theme-cord.installed" file
        file_path = os.path.join(saves_dir, 'theme-cord.installed')  # Create the path to the file
        with open(file_path, 'w') as file:
            file.write("true")

        # Run the ThemeCord injector
        subprocess.run([os.path.join(os.path.dirname(__file__), "themecord", "injector.exe"), "--css", css_path], check=True)

        # Show a success message box
        message_box = QMessageBox()
        message_box.setWindowTitle("Initialization Successful")
        message_box.setText("ThemeCord has been successfully initialized in the current Discord session. Please close and re-launch the app to start using the app.")
        message_box.setIcon(QMessageBox.Information)
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()
    def open_url(self, url):
        if webbrowser.open(url):
            print("URL opened successfully.")
        else:
            print("Failed to open the URL.")
    def open_discord(self):
        return self.open_url("https://discord.gg/FTK3txBsAS")
    def open_github(self):
        return self.open_url("https://github.com/Theme-Cord")
    def open_website(self):
        return self.open_url("https://Theme-Cord.Github.Io")
    def open_in(self):
        return self.open_url("https://github.com/Theme-Cord/.github/blob/main/why_init.md")
    def inject_theme(self):
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
