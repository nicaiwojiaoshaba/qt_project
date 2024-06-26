# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QDialog, QStyle
from ui.login_ui import Ui_Dialog
from win import register, retrieve
from util.passwordEdit import PasswordEdit


class LoginWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置登录窗口名
        self.setWindowTitle("登录")
        # 设置登录窗口图标
        window_icon = self.conversion_icon(QStyle.StandardPixmap.SP_FileDialogInfoView)
        self.setWindowIcon(window_icon)
        # 初始化带有按钮的密码框
        self.password_edit = PasswordEdit()
        # 替换模板密码框 verticalLayout_2为密码框父元素
        self.verticalLayout_2.replaceWidget(self.password_temp, self.password_edit)
        # 删除模板密码框
        self.password_temp.deleteLater()
        # 注册账号页面实例
        self.register = register.registerWindow(self)
        self.register_btn.clicked.connect(self.show_register_window)
        # 找回密码页面实例
        self.retrieve = retrieve.retrieveWindow(self)
        # 设置找回密码按钮
        self.retrieve_btn.setFlat(True)
        self.retrieve_btn.clicked.connect(self.show_retrieve_window)

    # 图标转换
    def conversion_icon(self, icon):
        return self.style().standardIcon(icon)

    # 显示注册窗口
    def show_register_window(self):
        self.register.display(self)
        self.hide()

    # 显示找回密码窗口
    def show_retrieve_window(self):
        self.retrieve.display(self)
        self.hide()

    # 初始化方法
    def display(self):
        self.showNormal()
