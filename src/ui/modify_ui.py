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
        Dialog.resize(380, 281)
        Dialog.setMaximumSize(QSize(381, 281))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 18pt \"Yu Gothic UI\";")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.original_label = QLabel(self.widget)
        self.original_label.setObjectName(u"original_label")

        self.verticalLayout_2.addWidget(self.original_label)

        self.new_label = QLabel(self.widget)
        self.new_label.setObjectName(u"new_label")

        self.verticalLayout_2.addWidget(self.new_label)

        self.confirm_label = QLabel(self.widget)
        self.confirm_label.setObjectName(u"confirm_label")

        self.verticalLayout_2.addWidget(self.confirm_label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.original_temp = QLineEdit(self.widget)
        self.original_temp.setObjectName(u"original_temp")
        self.original_temp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.original_temp)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.new_temp = QLineEdit(self.widget)
        self.new_temp.setObjectName(u"new_temp")
        self.new_temp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.new_temp)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.confirm_temp = QLineEdit(self.widget)
        self.confirm_temp.setObjectName(u"confirm_temp")
        self.confirm_temp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.confirm_temp)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.modify_btn = QPushButton(self.widget)
        self.modify_btn.setObjectName(u"modify_btn")
        self.modify_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_4.addWidget(self.modify_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5bc6\u7801", None))
        self.original_label.setText(QCoreApplication.translate("Dialog", u"\u539f\u5bc6\u7801:", None))
        self.new_label.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5bc6\u7801:", None))
        self.confirm_label.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4\u5bc6\u7801:", None))
        self.modify_btn.setText(QCoreApplication.translate("Dialog", u"\u4fee\u6539", None))
    # retranslateUi

