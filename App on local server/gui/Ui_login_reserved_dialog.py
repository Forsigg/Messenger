# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_reserved_dialog.ui'
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

class Ui_login_reserved_dialog(object):
    def setupUi(self, login_reserved_dialog):
        if not login_reserved_dialog.objectName():
            login_reserved_dialog.setObjectName(u"login_reserved_dialog")
        login_reserved_dialog.resize(400, 95)
        self.OK_btn = QDialogButtonBox(login_reserved_dialog)
        self.OK_btn.setObjectName(u"OK_btn")
        self.OK_btn.setGeometry(QRect(30, 40, 341, 32))
        self.OK_btn.setOrientation(Qt.Horizontal)
        self.OK_btn.setStandardButtons(QDialogButtonBox.Ok)
        self.OK_btn.setCenterButtons(True)
        self.dialog_label = QLabel(login_reserved_dialog)
        self.dialog_label.setObjectName(u"dialog_label")
        self.dialog_label.setGeometry(QRect(10, 0, 361, 41))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(9)
        self.dialog_label.setFont(font)
        self.dialog_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(login_reserved_dialog)
        self.OK_btn.accepted.connect(login_reserved_dialog.accept)
        self.OK_btn.rejected.connect(login_reserved_dialog.reject)

        QMetaObject.connectSlotsByName(login_reserved_dialog)
    # setupUi

    def retranslateUi(self, login_reserved_dialog):
        login_reserved_dialog.setWindowTitle(QCoreApplication.translate("login_reserved_dialog", u"Dialog", None))
        self.dialog_label.setText(QCoreApplication.translate("login_reserved_dialog", u"\u0422\u0430\u043a\u043e\u0439 \u043b\u043e\u0433\u0438\u043d \u0443\u0436\u0435 \u0437\u0430\u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0441\u043d\u043e\u0432\u0430.", None))
    # retranslateUi


def run_dialog():
    dialog = QDialog()
    dialog_ui = Ui_login_reserved_dialog()
    dialog_ui.setupUi(dialog)
    dialog.exec()
