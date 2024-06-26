# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 309)
        Dialog.setMaximumSize(QSize(420, 309))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 18pt \"Yu Gothic UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_12 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.username_edit = QLineEdit(self.widget)
        self.username_edit.setObjectName(u"username_edit")
        self.username_edit.setEnabled(True)
        self.username_edit.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.username_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.password_temp = QLineEdit(self.widget)
        self.password_temp.setObjectName(u"password_temp")
        self.password_temp.setStyleSheet(u"")
        self.password_temp.setEchoMode(QLineEdit.Password)
        self.password_temp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.password_temp)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"border-bottom-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.retrieve_btn = QPushButton(self.widget)
        self.retrieve_btn.setObjectName(u"retrieve_btn")
        self.retrieve_btn.setStyleSheet(u"font: 9pt \"Yu Gothic UI\";\n"
"text-decoration: underline;\n"
"color:rgb(88, 197, 255);")

        self.horizontalLayout_2.addWidget(self.retrieve_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_btn = QPushButton(self.widget)
        self.login_btn.setObjectName(u"login_btn")

        self.horizontalLayout.addWidget(self.login_btn)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.register_btn = QPushButton(self.widget)
        self.register_btn.setObjectName(u"register_btn")

        self.horizontalLayout.addWidget(self.register_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        QWidget.setTabOrder(self.username_edit, self.password_temp)
        QWidget.setTabOrder(self.password_temp, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.login_btn)
        QWidget.setTabOrder(self.login_btn, self.register_btn)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u767b\u5f55", None))
        self.username_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d:", None))
        self.password_temp.setText("")
        self.password_temp.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801:", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.retrieve_btn.setText(QCoreApplication.translate("Dialog", u"\u627e\u56de\u5bc6\u7801?", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.register_btn.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
    # retranslateUi

