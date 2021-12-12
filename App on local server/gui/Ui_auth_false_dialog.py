# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aithentification_false_dialog.ui'
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

class Ui_authentification_false_dialog(object):
    def setupUi(self, authentification_false_dialog):
        if not authentification_false_dialog.objectName():
            authentification_false_dialog.setObjectName(u"authentification_false_dialog")
        authentification_false_dialog.resize(400, 81)
        self.OK_btn = QDialogButtonBox(authentification_false_dialog)
        self.OK_btn.setObjectName(u"OK_btn")
        self.OK_btn.setGeometry(QRect(30, 40, 341, 32))
        self.OK_btn.setOrientation(Qt.Horizontal)
        self.OK_btn.setStandardButtons(QDialogButtonBox.Ok)
        self.OK_btn.setCenterButtons(True)
        self.dialoglabel = QLabel(authentification_false_dialog)
        self.dialoglabel.setObjectName(u"dialoglabel")
        self.dialoglabel.setGeometry(QRect(20, 10, 350, 20))
        font = QFont()
        font.setPointSize(9)
        self.dialoglabel.setFont(font)
        self.dialoglabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(authentification_false_dialog)
        self.OK_btn.accepted.connect(authentification_false_dialog.accept)
        self.OK_btn.rejected.connect(authentification_false_dialog.reject)

        QMetaObject.connectSlotsByName(authentification_false_dialog)
    # setupUi

    def retranslateUi(self, authentification_false_dialog):
        authentification_false_dialog.setWindowTitle(QCoreApplication.translate("authentification_false_dialog", u"Dialog", None))
        self.dialoglabel.setText(QCoreApplication.translate("authentification_false_dialog", u"\u041d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u0432\u0432\u0435\u0434\u0435\u043d \u043b\u043e\u0433\u0438\u043d \u0438/\u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c. \u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0441\u043d\u043e\u0432\u0430", None))
    # retranslateUi

def run_dialog():
    dialog = QDialog()
    dialog_ui = Ui_authentification_false_dialog()
    dialog_ui.setupUi(dialog)
    dialog.exec()