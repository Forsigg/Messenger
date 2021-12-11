# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_friend_widget.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

from data.users_data.datafriendmanager import DataFriendsManager
from data.users_data.datausersmanager import DataUsersManager


class Ui_Add_friend(object):
    def setupUi(self, Add_friend):
        if not Add_friend.objectName():
            Add_friend.setObjectName(u"Add_friend")
        Add_friend.resize(400, 129)
        self.verticalLayoutWidget = QWidget(Add_friend)
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

        self.add_friend_btn = QPushButton(self.verticalLayoutWidget)
        self.add_friend_btn.setObjectName(u"add_friend_btn")

        self.verticalLayout.addWidget(self.add_friend_btn)


        self.retranslateUi(Add_friend)

        QMetaObject.connectSlotsByName(Add_friend)

        self.add_friend_btn.clicked.connect(self.METH)

    @Slot()
    def register(self):
        db_friend = DataFriendsManager()
        db_user = DataUsersManager()
        friend = self.friend_login_editline.text()
        if not db_user.user_in_base(friend):
            pass # добавить "ТАКОГО ПОЛЬЗОВАТЕЛЯ НЕ СУЩЕСТВУЕТ"
        else:
            db_friend.add_one()




    def retranslateUi(self, Add_friend):
        Add_friend.setWindowTitle(QCoreApplication.translate("Add_friend", u"Messenger Add Friend", None))
        self.friend_login_label.setText(QCoreApplication.translate("Add_friend", u"\u041b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.friend_login_editline.setInputMask("")
        self.friend_login_editline.setText("")
        self.friend_login_editline.setPlaceholderText(QCoreApplication.translate("Add_friend", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f...", None))
        self.add_friend_btn.setText(QCoreApplication.translate("Add_friend", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0434\u0440\u0443\u0437\u044c\u044f", None))
    # retranslateUi

def run_widget():
    app = QApplication()
    widget = QWidget()
    widget_ui = Ui_Add_friend()
    widget_ui.setupUi(widget)

    widget.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    run_widget()
