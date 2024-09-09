# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui.login_ui import Ui_Dialog
from util.passwordEdit import PasswordEdit
from util.path import expand_source_root


# 登录窗口
class LoginWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置登录窗口名
        self.setWindowTitle("登录")
        # 设置登录窗口图标
        self.setWindowIcon(QIcon(f"{expand_source_root('resource')}/user.png"))
        # 初始化带有按钮的密码框
        self.password_edit = PasswordEdit()
        # 替换模板密码框 verticalLayout_2为密码框父元素
        self.verticalLayout_2.replaceWidget(self.password_temp, self.password_edit)
        # 删除模板密码框
        self.password_temp.deleteLater()
        # 注册账号页面实例
        # self.register = register.RegisterWindow(self)
        self.register_btn.clicked.connect(self.register_btn_clicked)
        # 设置找回密码按钮
        self.retrieve_btn.setFlat(True)
        self.retrieve_btn.clicked.connect(self.retrieve_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)

    # 显示工具窗口
    def login_btn_clicked(self):
        self.hide()
        self.tool_win.display()

    # 显示注册账号窗口
    def register_btn_clicked(self):
        self.hide()
        self.register_win.display()
        self.register_win.activateWindow()
        self.register_win.raise_()

    # 显示找回密码窗口
    def retrieve_btn_clicked(self):
        self.hide()
        self.retrieve_win.display()
        self.retrieve_win.activateWindow()
        self.retrieve_win.raise_()

    # 登录画面初始化
    def display(self):
        self.show()
        self.login_btn.setFocus()
