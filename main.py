from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import sys
import pwnedPassword
from absPath import resource_path


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(resource_path('ui/passwordChecker.ui'), self)

        self.setWindowTitle("Password Checker")
        self.setWindowIcon(QIcon(resource_path('assets/check-shield-solid-24.png')))
        self.status = self.findChild(QLabel, "statusText")

        self.inputPass = self.findChild(QLineEdit, "inputPassword")
        self.inputPass.setPlaceholderText('password')

        self.check = self.findChild(QPushButton, "checkBtn")
        self.check.clicked.connect(lambda: self.checkPassword())

        self.response = self.findChild(QLabel, "responseText")
        self.response.setText("Type some Password")

        self.show()

        self.checkStatus()

    def checkStatus(self):
        self.res = pwnedPassword.request_api_data()
        if self.res:
            self.status.setText('Connected')
            self.check.setEnabled(True)
        else:
            self.status.setText('Error')
            self.status.setStyleSheet("color: red;")
            self.response.setText("Connection Error")
            self.check.setEnabled(False)

    def checkPassword(self):
        if self.inputPass.text():
            self.res = pwnedPassword.password_Check(self.inputPass.text())
            self.response.setText(self.res)
        else:
            self.response.setText("Type some password")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
