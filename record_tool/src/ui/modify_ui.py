# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(349, 321)
        Dialog.setMaximumSize(QSize(381, 321))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 311, 284))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 18pt \"Yu Gothic UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.username_edit = QLineEdit(self.widget1)
        self.username_edit.setObjectName(u"username_edit")

        self.verticalLayout_2.addWidget(self.username_edit)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.original_temp = QLineEdit(self.widget1)
        self.original_temp.setObjectName(u"original_temp")
        self.original_temp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.original_temp)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.new_temp = QLineEdit(self.widget1)
        self.new_temp.setObjectName(u"new_temp")
        self.new_temp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.new_temp)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.confirm_temp = QLineEdit(self.widget1)
        self.confirm_temp.setObjectName(u"confirm_temp")
        self.confirm_temp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.confirm_temp)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.modify_btn = QPushButton(self.widget1)
        self.modify_btn.setObjectName(u"modify_btn")
        self.modify_btn.setMinimumSize(QSize(90, 0))

        self.verticalLayout_2.addWidget(self.modify_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.retrieve_btn = QPushButton(self.widget1)
        self.retrieve_btn.setObjectName(u"retrieve_btn")
        self.retrieve_btn.setStyleSheet(u"font: 9pt \"Yu Gothic UI\";\n"
"text-decoration: underline;\n"
"color:rgb(88, 197, 255);")

        self.horizontalLayout.addWidget(self.retrieve_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5bc6\u7801", None))
        self.username_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d:", None))
        self.modify_btn.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539", None))
        self.retrieve_btn.setText(QCoreApplication.translate("Dialog", u"\u627e\u56de\u5bc6\u7801", None))
    # retranslateUi

