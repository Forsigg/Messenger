# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authentification.ui'
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
    QPushButton, QSizePolicy, QWidget, QDialog)

from Ui_auth_false_dialog import run_dialog as dialog_auth_false
from Ui_pass_not_conf import run_dialog as dialog_pass_not_conf
from Ui_register_window import run_window as register_window
from data.users_data import DataUsersManager
from Ui_messenger_window import run_messenger

class Ui_authentification(object):
    def setupUi(self, authentification):
        if not authentification.objectName():
            authentification.setObjectName(u"authentification")
        authentification.resize(400, 400)
        authentification.setStyleSheet(u"")
        self.centralwidget = QWidget(authentification)
        self.centralwidget.setObjectName(u"centralwidget")
        self.login_edit = QLineEdit(self.centralwidget)
        self.login_edit.setObjectName(u"login_edit")
        self.login_edit.setGeometry(QRect(50, 150, 300, 30))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(10)
        self.login_edit.setFont(font)
        self.login_edit.setMaxLength(30)
        self.login_edit.setClearButtonEnabled(False)
        self.password_edit = QLineEdit(self.centralwidget)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setGeometry(QRect(50, 240, 300, 30))
        self.password_edit.setFont(font)
        self.password_edit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.label_login = QLabel(self.centralwidget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(50, 120, 141, 20))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_login.setFont(font1)
        self.label_login.setTextFormat(Qt.PlainText)
        self.label_login.setAlignment(Qt.AlignCenter)
        self.label_login.setMargin(0)
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(50, 210, 151, 20))
        self.label_password.setFont(font1)
        self.label_password.setTextFormat(Qt.PlainText)
        self.label_password.setAlignment(Qt.AlignCenter)
        self.label_password.setMargin(0)
        self.label_auth_window = QLabel(self.centralwidget)
        self.label_auth_window.setObjectName(u"label_auth_window")
        self.label_auth_window.setGeometry(QRect(90, 30, 200, 30))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_auth_window.setFont(font2)
        self.label_auth_window.setAlignment(Qt.AlignCenter)
        self.enter_btn = QPushButton(self.centralwidget)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setGeometry(QRect(50, 300, 85, 30))
        self.enter_btn_2 = QPushButton(self.centralwidget)
        self.enter_btn_2.setObjectName(u"enter_btn_2")
        self.enter_btn_2.setGeometry(QRect(270, 300, 85, 30))
        authentification.setCentralWidget(self.centralwidget)

        self.retranslateUi(authentification)

        QMetaObject.connectSlotsByName(authentification)


        # signals for buttons
        self.enter_btn.clicked.connect(self.dialog_in_auth)
        self.enter_btn_2.clicked.connect(self.register_window)

    @Slot()
    def dialog_in_auth(self):
        db = DataUsersManager()
        if not db.user_in_base(self.login_edit.text()):
            dialog_auth_false()
        elif not db.is_right_password(self.login_edit.text(), self.password_edit.text()):
            dialog_pass_not_conf()
        else:
            self.session = {'login': self.login_edit.text()}
            QWidget.close()



    @Slot()
    def register_window(self):
        register_window()


    def retranslateUi(self, authentification):
        authentification.setWindowTitle(QCoreApplication.translate("authentification", u"Messenger", None))
        self.login_edit.setInputMask("")
        self.password_edit.setInputMask("")
        self.label_login.setText(QCoreApplication.translate("authentification", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d:", None))
        self.label_password.setText(QCoreApplication.translate("authentification", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_auth_window.setText(QCoreApplication.translate("authentification", u"\u041e\u043a\u043d\u043e \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.enter_btn.setText(QCoreApplication.translate("authentification", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.enter_btn_2.setText(QCoreApplication.translate("authentification", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi


if __name__ == '__main__':
    app = QApplication()

    window = QMainWindow()
    ui_window = Ui_authentification()
    ui_window.setupUi(window)
    window.show()

    sys.exit(app.exec())

