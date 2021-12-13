# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

from gui.Ui_login_reserved_dialog import run_dialog as dialog_login_reserved
from gui.Ui_pass_not_conf import run_dialog as dialog_not_conf

import json
import requests
import config


class Ui_register_window(object):
    def setupUi(self, register_window):
        if not register_window.objectName():
            register_window.setObjectName(u"register_window")
        register_window.resize(350, 300)
        self.centralwidget = QWidget(register_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_register = QLabel(self.centralwidget)
        self.label_register.setObjectName(u"label_register")
        self.label_register.setGeometry(QRect(80, 20, 180, 30))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(13)
        font.setBold(True)
        self.label_register.setFont(font)
        self.label_register.setMouseTracking(False)
        self.label_register.setAlignment(Qt.AlignCenter)
        self.login_lineedit = QLineEdit(self.centralwidget)
        self.login_lineedit.setObjectName(u"login_lineedit")
        self.login_lineedit.setGeometry(QRect(20, 80, 300, 25))
        self.label_insert_login = QLabel(self.centralwidget)
        self.label_insert_login.setObjectName(u"label_insert_login")
        self.label_insert_login.setGeometry(QRect(20, 60, 100, 15))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(9)
        self.label_insert_login.setFont(font1)
        self.label_insert_login.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_insert_pass = QLabel(self.centralwidget)
        self.label_insert_pass.setObjectName(u"label_insert_pass")
        self.label_insert_pass.setGeometry(QRect(20, 110, 100, 15))
        self.label_insert_pass.setFont(font1)
        self.label_insert_pass.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.passw_lineedit_2 = QLineEdit(self.centralwidget)
        self.passw_lineedit_2.setObjectName(u"passw_lineedit_2")
        self.passw_lineedit_2.setGeometry(QRect(20, 130, 300, 25))
        self.passw_lineedit_2.setEchoMode(QLineEdit.Password)
        self.label_confirm_pass = QLabel(self.centralwidget)
        self.label_confirm_pass.setObjectName(u"label_confirm_pass")
        self.label_confirm_pass.setGeometry(QRect(20, 160, 150, 15))
        self.label_confirm_pass.setFont(font1)
        self.label_confirm_pass.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confirm_pass_lineedit = QLineEdit(self.centralwidget)
        self.confirm_pass_lineedit.setObjectName(u"confirm_pass_lineedit")
        self.confirm_pass_lineedit.setGeometry(QRect(20, 180, 300, 25))
        self.confirm_pass_lineedit.setEchoMode(QLineEdit.Password)
        self.register_btn = QPushButton(self.centralwidget)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(200, 220, 120, 30))
        register_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(register_window)

        QMetaObject.connectSlotsByName(register_window)

        # signal for button
        self.register_btn.clicked.connect(self.register)

    @Slot()
    def register(self):
        users = json.loads(requests.get(f'http://{config.host}:{config.port}/users').json())
        user_login = self.login_lineedit.text()
        user_pass = self.passw_lineedit_2.text()
        user_pass_conf = self.confirm_pass_lineedit.text()
        if user_login in users:
            dialog_login_reserved()
        elif user_pass != user_pass_conf:
            dialog_not_conf()
        else:
            data = {
                'login': user_login,
                'password': user_pass
            }
            requests.post(f'http://{config.host}:{config.port}/users', data=data)
            window.close()



    def retranslateUi(self, register_window):
        register_window.setWindowTitle(QCoreApplication.translate("register_window", u"MainWindow", None))
        self.label_register.setText(QCoreApplication.translate("register_window", u"\u041e\u043a\u043d\u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.label_insert_login.setText(QCoreApplication.translate("register_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d:", None))
        self.label_insert_pass.setText(QCoreApplication.translate("register_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_confirm_pass.setText(QCoreApplication.translate("register_window", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f:", None))
        self.register_btn.setText(QCoreApplication.translate("register_window", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

def run_window():

    window = QMainWindow()
    window_ui = Ui_register_window()
    window_ui.setupUi(window)
    window.show()

    app.exec()


