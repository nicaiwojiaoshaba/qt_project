# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
        Dialog.resize(390, 383)
        Dialog.setMaximumSize(QSize(390, 383))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 18pt \"Yu Gothic UI\";")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.username_label = QLabel(self.widget)
        self.username_label.setObjectName(u"username_label")

        self.horizontalLayout_3.addWidget(self.username_label)

        self.username_edit = QLineEdit(self.widget)
        self.username_edit.setObjectName(u"username_edit")
        self.username_edit.setMaximumSize(QSize(272, 16777215))

        self.horizontalLayout_3.addWidget(self.username_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_5 = QSpacerItem(68, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.checkMessage_username = QLabel(self.widget)
        self.checkMessage_username.setObjectName(u"checkMessage_username")
        self.checkMessage_username.setMaximumSize(QSize(287, 10))

        self.horizontalLayout_11.addWidget(self.checkMessage_username)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.password_label = QLabel(self.widget)
        self.password_label.setObjectName(u"password_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        self.password_label.setMaximumSize(QSize(81, 16777215))

        self.horizontalLayout_12.addWidget(self.password_label)

        self.password_temp = QLineEdit(self.widget)
        self.password_temp.setObjectName(u"password_temp")
        self.password_temp.setMaximumSize(QSize(272, 16777215))
        self.password_temp.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_12.addWidget(self.password_temp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_6 = QSpacerItem(68, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.checkMessage_password = QLabel(self.widget)
        self.checkMessage_password.setObjectName(u"checkMessage_password")
        self.checkMessage_password.setMaximumSize(QSize(287, 10))

        self.horizontalLayout_13.addWidget(self.checkMessage_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.confirm_label = QLabel(self.widget)
        self.confirm_label.setObjectName(u"confirm_label")
        sizePolicy.setHeightForWidth(self.confirm_label.sizePolicy().hasHeightForWidth())
        self.confirm_label.setSizePolicy(sizePolicy)
        self.confirm_label.setMinimumSize(QSize(68, 0))
        self.confirm_label.setMaximumSize(QSize(76, 16777215))

        self.horizontalLayout_14.addWidget(self.confirm_label)

        self.confirm_temp = QLineEdit(self.widget)
        self.confirm_temp.setObjectName(u"confirm_temp")
        self.confirm_temp.setMaximumSize(QSize(272, 16777215))
        self.confirm_temp.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_14.addWidget(self.confirm_temp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_7 = QSpacerItem(68, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.checkMessage_confirm = QLabel(self.widget)
        self.checkMessage_confirm.setObjectName(u"checkMessage_confirm")
        self.checkMessage_confirm.setMaximumSize(QSize(287, 10))

        self.horizontalLayout_15.addWidget(self.checkMessage_confirm)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.question1_label = QLabel(self.widget)
        self.question1_label.setObjectName(u"question1_label")

        self.horizontalLayout_16.addWidget(self.question1_label)

        self.question1_edit = QLineEdit(self.widget)
        self.question1_edit.setObjectName(u"question1_edit")
        self.question1_edit.setMaximumSize(QSize(287, 16777215))

        self.horizontalLayout_16.addWidget(self.question1_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.verticalSpacer = QSpacerItem(354, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.question2_label = QLabel(self.widget)
        self.question2_label.setObjectName(u"question2_label")

        self.horizontalLayout_17.addWidget(self.question2_label)

        self.question2_edit = QLineEdit(self.widget)
        self.question2_edit.setObjectName(u"question2_edit")
        self.question2_edit.setMaximumSize(QSize(287, 16777215))

        self.horizontalLayout_17.addWidget(self.question2_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_8 = QSpacerItem(70, 14, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)

        self.tip = QLabel(self.widget)
        self.tip.setObjectName(u"tip")
        self.tip.setMaximumSize(QSize(287, 14))
        self.tip.setStyleSheet(u"color:rgb(255, 0, 0);\n"
"font: 8pt \"Yu Gothic UI\";")

        self.horizontalLayout_18.addWidget(self.tip)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u6ce8\u518c", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d\uff1a", None))
        self.username_edit.setPlaceholderText("")
        self.checkMessage_username.setText("")
        self.password_label.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\uff1a", None))
        self.checkMessage_password.setText("")
        self.confirm_label.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.confirm_temp.setText("")
        self.checkMessage_confirm.setText("")
        self.question1_label.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u4fdd(\u59d3\u540d)\uff1a", None))
        self.question2_label.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u4fdd(\u5de5\u53f7)\uff1a", None))
        self.tip.setText(QCoreApplication.translate("Dialog", u"  *\u5bc6\u4fdd\u95ee\u9898\u7528\u4e8e\u5bc6\u7801\u627e\u56de,\u8bf7\u5982\u5b9e\u586b\u5199", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
    # retranslateUi

