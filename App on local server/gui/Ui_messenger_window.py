# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messenger_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from datetime import datetime

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Slot)
from PySide6.QtGui import (QAction)
from PySide6.QtWidgets import (QLabel, QLineEdit, QListWidget, QListWidgetItem, QMenu,
                               QMenuBar, QPushButton, QVBoxLayout,
                               QWidget, QMainWindow)

from data.messages import Message
from data.users_data import DataUsersManager

import requests
import json
import config

db = DataUsersManager()


class Ui_Messenger_window(object):
    def session(self,login_json):
        login = json.loads(login_json)
        self.session = login
        self.users = json.loads(requests.get(f'http://{config.host}:{config.port}/users').json())

    def setupUi(self, Messenger_window):
        if not Messenger_window.objectName():
            Messenger_window.setObjectName(u"Messenger_window")
        Messenger_window.resize(600, 456)

        self.centralwidget = QWidget(Messenger_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 15, 0, 0)
        self.userList_label = QLabel(self.verticalLayoutWidget)
        self.userList_label.setObjectName(u"userList_label")

        self.verticalLayout.addWidget(self.userList_label)

        self.users_ListWidget = QListWidget(self.verticalLayoutWidget)
        for _ in range(len(self.users)):
            QListWidgetItem(self.users_ListWidget)
        self.users_ListWidget.setObjectName(u"users_ListWidget")

        self.verticalLayout.addWidget(self.users_ListWidget)

        self.chat_label = QLabel(self.verticalLayoutWidget)
        self.chat_label.setObjectName(u"chat_label")

        self.verticalLayout.addWidget(self.chat_label)

        self.chat_view = QListWidget(self.verticalLayoutWidget)
        self.chat_view.setObjectName(u"chat_view")

        self.verticalLayout.addWidget(self.chat_view)

        self.textedit_line = QLineEdit(self.verticalLayoutWidget)
        self.textedit_line.setObjectName(u"textedit_line")

        self.verticalLayout.addWidget(self.textedit_line)

        self.send_btn = QPushButton(self.verticalLayoutWidget)
        self.send_btn.setObjectName(u"send_btn")

        self.verticalLayout.addWidget(self.send_btn)

        Messenger_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Messenger_window)

        QMetaObject.connectSlotsByName(Messenger_window)


        self.users_ListWidget.itemDoubleClicked.connect(self.open_messages)
        self.send_btn.clicked.connect(self.send_message)


    @Slot()
    def open_messages(self):
        self.chat_view.clear()
        current_row = self.users_ListWidget.selectionModel().currentIndex().row()
        user = self.users_ListWidget.item(current_row).text()
        if user == self.session:
            pass
        else:
            request = requests.get(f'http://{config.host}:{config.port}/users/{self.session}/{user}')
            db_messages = json.loads(request.json())
            for index, message in enumerate(db_messages):
                QListWidgetItem(self.chat_view)
                qlistwidgetitem = self.chat_view.item(index)
                qlistwidgetitem.setText(QCoreApplication.translate("Messenger_window", f"{message[3][:19]}, {message[1]}: {message[0]}", None));

    @Slot()
    def send_message(self):
        current_row = self.users_ListWidget.selectionModel().currentIndex().row()
        user_out = self.users_ListWidget.item(current_row).text()
        message = Message(self.textedit_line.text(), str(self.session), user_out, str(datetime.now()))
        data = {
            'text': message.text,
            'author': message.author,
            'receiver': message.receiver,
            'date': message.date
        }
        if message.text != '':
            request = requests.post(f'http://{config.host}:{config.port}/users/{self.session}/{user_out}/send', data=data)
            self.textedit_line.setText('')
            self.open_messages()

    def retranslateUi(self, Messenger_window):
        Messenger_window.setWindowTitle(QCoreApplication.translate("Messenger_window", f"Messenger - {self.session}", None))
        self.userList_label.setText(QCoreApplication.translate("Messenger_window", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439:", None))

        __sortingEnabled = self.users_ListWidget.isSortingEnabled()
        self.users_ListWidget.setSortingEnabled(False)
        for index, user in enumerate(self.users):
            QListWidgetItem(self.users_ListWidget)
            qlistwidgetitem = self.users_ListWidget.item(index)
            qlistwidgetitem.setText(QCoreApplication.translate("Messenger_window", "{}".format(user), None));
        self.users_ListWidget.setSortingEnabled(__sortingEnabled)

        self.chat_label.setText(QCoreApplication.translate("Messenger_window", u"\u041e\u043a\u043d\u043e \u0434\u0438\u0430\u043b\u043e\u0433\u0430 \u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c:", None))
        self.textedit_line.setInputMask("")
        self.textedit_line.setText("")
        self.textedit_line.setPlaceholderText(QCoreApplication.translate("Messenger_window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f...", None))
        self.send_btn.setText(QCoreApplication.translate("Messenger_window", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.send_btn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        # retranslateUi

#
def run_messenger(login):

    window = QMainWindow()
    window_ui = Ui_Messenger_window()
    window_ui.session(login)
    window_ui.setupUi(window)

    window.show()

    app.exec()




