# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tool.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(263, 74)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sessions_btn = QPushButton(self.centralwidget)
        self.sessions_btn.setObjectName(u"sessions_btn")
        icon = QIcon()
        icon.addFile(u":/resource/session.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sessions_btn.setIcon(icon)
        self.sessions_btn.setIconSize(QSize(48, 48))
        self.sessions_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.sessions_btn)

        self.links_btn = QPushButton(self.centralwidget)
        self.links_btn.setObjectName(u"links_btn")
        icon1 = QIcon()
        icon1.addFile(u":/resource/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.links_btn.setIcon(icon1)
        self.links_btn.setIconSize(QSize(32, 32))
        self.links_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.links_btn)

        self.plugins_btn = QPushButton(self.centralwidget)
        self.plugins_btn.setObjectName(u"plugins_btn")
        icon2 = QIcon()
        icon2.addFile(u":/resource/plugins.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plugins_btn.setIcon(icon2)
        self.plugins_btn.setIconSize(QSize(32, 32))
        self.plugins_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.plugins_btn)

        self.horizontalSpacer = QSpacerItem(76, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sessions_btn.setText("")
        self.links_btn.setText("")
        self.plugins_btn.setText("")
    # retranslateUi

