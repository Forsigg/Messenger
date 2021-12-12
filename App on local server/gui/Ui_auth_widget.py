# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QMainWindow)

from gui.Ui_auth_false_dialog import run_dialog as dialog_auth_false
from gui.Ui_pass_not_conf import run_dialog as dialog_pass_not_conf
from gui.Ui_register_window import run_window as register_window
from gui.Ui_messenger_window import Ui_Messenger_window, run_messenger

import json
import requests



class Ui_auth_widget(object):
    def setupUi(self, auth_widget):
        if not auth_widget.objectName():
            auth_widget.setObjectName(u"auth_widget")
        auth_widget.resize(400, 350)
        self.login_edit = QLineEdit(auth_widget)
        self.login_edit.setObjectName(u"login_edit")
        self.login_edit.setGeometry(QRect(40, 130, 300, 30))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(10)
        self.login_edit.setFont(font)
        self.login_edit.setMaxLength(30)
        self.login_edit.setClearButtonEnabled(False)
        self.enter_btn_2 = QPushButton(auth_widget)
        self.enter_btn_2.setObjectName(u"enter_btn_2")
        self.enter_btn_2.setGeometry(QRect(260, 280, 85, 30))
        self.enter_btn = QPushButton(auth_widget)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setGeometry(QRect(40, 280, 85, 30))
        self.label_auth_window = QLabel(auth_widget)
        self.label_auth_window.setObjectName(u"label_auth_window")
        self.label_auth_window.setGeometry(QRect(80, 10, 200, 30))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_auth_window.setFont(font1)
        self.label_auth_window.setAlignment(Qt.AlignCenter)
        self.label_password = QLabel(auth_widget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(40, 190, 151, 20))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_password.setFont(font2)
        self.label_password.setTextFormat(Qt.PlainText)
        self.label_password.setAlignment(Qt.AlignCenter)
        self.label_password.setMargin(0)
        self.label_login = QLabel(auth_widget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(40, 100, 141, 20))
        self.label_login.setFont(font2)
        self.label_login.setTextFormat(Qt.PlainText)
        self.label_login.setAlignment(Qt.AlignCenter)
        self.label_login.setMargin(0)
        self.password_edit = QLineEdit(auth_widget)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setGeometry(QRect(40, 220, 300, 30))
        self.password_edit.setFont(font)
        self.password_edit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.retranslateUi(auth_widget)

        QMetaObject.connectSlotsByName(auth_widget)

        self.session = ''

        # signals for buttons
        self.enter_btn.clicked.connect(self.dialog_in_auth)
        self.enter_btn_2.clicked.connect(self.register_window)

    @Slot()
    def dialog_in_auth(self):
        users = json.loads(requests.get('http://localhost:8080/users').json())
        if json.loads(requests.get(f'http://localhost:8080/users/{self.login_edit.text()}/auth').json()) != False:
            user_pass = json.loads(requests.get(f'http://localhost:8080/users/{self.login_edit.text()}/auth').json())[0][1]
            if user_pass != self.password_edit.text():
                print(2)
                dialog_pass_not_conf()
            else:
                request = requests.get(f'http://localhost:8080/users/{self.login_edit.text()}')
                user = request.json()
                run_messenger(user)
        else:
            dialog_auth_false()


    @Slot()
    def register_window(self):
        register_window()

    def retranslateUi(self, auth_widget):
        auth_widget.setWindowTitle(QCoreApplication.translate("auth_widget", u"Messenger Auth", None))
        self.login_edit.setInputMask("")
        self.enter_btn_2.setText(QCoreApplication.translate("auth_widget", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.enter_btn.setText(QCoreApplication.translate("auth_widget", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_auth_window.setText(QCoreApplication.translate("auth_widget", u"\u041e\u043a\u043d\u043e \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_password.setText(QCoreApplication.translate("auth_widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_login.setText(QCoreApplication.translate("auth_widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d:", None))
        self.password_edit.setInputMask("")
    # retranslateUi

def main():
    app = QApplication()
    window = QWidget()
    ui_window = Ui_auth_widget()
    ui_window.setupUi(window)

    session = ui_window.session

    window.show()

    app.exec()

    window.close()


    window = QMainWindow()
    ui_window = Ui_Messenger_window()
    ui_window.setupUi(window)
    ui_window.session = session
    window.show()



