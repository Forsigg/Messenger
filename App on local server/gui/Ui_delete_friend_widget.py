# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_friend_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Delete_friend(object):
    def setupUi(self, Delete_friend):
        if not Delete_friend.objectName():
            Delete_friend.setObjectName(u"Delete_friend")
        Delete_friend.resize(400, 129)
        self.verticalLayoutWidget = QWidget(Delete_friend)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 371, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.friend_login_label = QLabel(self.verticalLayoutWidget)
        self.friend_login_label.setObjectName(u"friend_login_label")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(10)
        font.setBold(True)
        self.friend_login_label.setFont(font)
        self.friend_login_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.friend_login_label)

        self.friend_login_editline = QLineEdit(self.verticalLayoutWidget)
        self.friend_login_editline.setObjectName(u"friend_login_editline")

        self.verticalLayout.addWidget(self.friend_login_editline)

        self.delete_friend_btn = QPushButton(self.verticalLayoutWidget)
        self.delete_friend_btn.setObjectName(u"delete_friend_btn")

        self.verticalLayout.addWidget(self.delete_friend_btn)


        self.retranslateUi(Delete_friend)

        QMetaObject.connectSlotsByName(Delete_friend)
    # setupUi

    def retranslateUi(self, Delete_friend):
        Delete_friend.setWindowTitle(QCoreApplication.translate("Delete_friend", u"Messenger Delete Friend", None))
        self.friend_login_label.setText(QCoreApplication.translate("Delete_friend", u"\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.friend_login_editline.setInputMask("")
        self.friend_login_editline.setText("")
        self.friend_login_editline.setPlaceholderText(QCoreApplication.translate("Delete_friend", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f...", None))
        self.delete_friend_btn.setText(QCoreApplication.translate("Delete_friend", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 \u0434\u0440\u0443\u0437\u0435\u0439", None))
    # retranslateUi

