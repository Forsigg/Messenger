# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_not_confirm_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

class Ui_password_not_confirm_dialog(object):
    def setupUi(self, password_not_confirm_dialog):
        if not password_not_confirm_dialog.objectName():
            password_not_confirm_dialog.setObjectName(u"password_not_confirm_dialog")
        password_not_confirm_dialog.resize(400, 88)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(9)
        password_not_confirm_dialog.setFont(font)
        self.O_btn = QDialogButtonBox(password_not_confirm_dialog)
        self.O_btn.setObjectName(u"O_btn")
        self.O_btn.setGeometry(QRect(30, 40, 340, 30))
        self.O_btn.setOrientation(Qt.Horizontal)
        self.O_btn.setStandardButtons(QDialogButtonBox.Ok)
        self.O_btn.setCenterButtons(True)
        self.dialog_label = QLabel(password_not_confirm_dialog)
        self.dialog_label.setObjectName(u"dialog_label")
        self.dialog_label.setGeometry(QRect(20, 0, 361, 41))
        self.dialog_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(password_not_confirm_dialog)
        self.O_btn.accepted.connect(password_not_confirm_dialog.accept)
        self.O_btn.rejected.connect(password_not_confirm_dialog.reject)

        QMetaObject.connectSlotsByName(password_not_confirm_dialog)
    # setupUi

    def retranslateUi(self, password_not_confirm_dialog):
        password_not_confirm_dialog.setWindowTitle(QCoreApplication.translate("password_not_confirm_dialog", u"Dialog", None))
        self.dialog_label.setText(QCoreApplication.translate("password_not_confirm_dialog", u"\u041f\u0430\u0440\u043e\u043b\u0438 \u043d\u0435 \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0441\u043d\u043e\u0432\u0430.", None))
    # retranslateUi

def run_dialog():
    dialog = QDialog()
    dialog_ui = Ui_password_not_confirm_dialog()
    dialog_ui.setupUi(dialog)
    dialog.exec()