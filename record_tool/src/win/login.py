# -*- coding: utf-8 -*-
import os
import json

from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QIcon
from ui.login_ui import Ui_Dialog
from util.passwordEdit import PasswordEdit
from util.config import user_info_path, resource_path, user_info_file, default_user_info_file
from util.checkPassword import checkPassword
from util.logger import LOG, LEVEL


# 登录窗口
class LoginWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置登录窗口名
        self.setWindowTitle("登录")
        # 设置登录窗口图标
        self.setWindowIcon(QIcon(f"{resource_path}/main.png"))
        # 初始化带有按钮的密码框
        self.password_edit = PasswordEdit("password_edit", "密码:")
        # 替换模板密码框 verticalLayout_2为密码框父元素
        self.verticalLayout_2.replaceWidget(self.password_temp, self.password_edit)
        # 删除模板密码框
        self.password_temp.deleteLater()
        self.setTabOrder(self.username_edit, self.password_edit)
        # 注册按钮事件绑定
        self.register_btn.clicked.connect(self.register_btn_clicked)
        # 设置修改密码按钮
        self.modify_btn.setFlat(True)
        self.modify_btn.clicked.connect(self.modify_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.check_default_user()

    # 点击登录按钮
    def login_btn_clicked(self):
        if os.path.exists(user_info_path):
            with open(user_info_file, "r", encoding="utf-8") as f:
                user_info = json.load(f)
                if self.username_edit.text() in user_info.keys():
                    check_password = user_info[self.username_edit.text()]["password"]
                    # 检查输入密码是否正确
                    if checkPassword(self.password_edit.text(), check_password):
                        # 如果勾选记住密码，则保存用户名和密码
                        if self.checkBox.isChecked():
                            default_user_info = {"username": self.username_edit.text(), "password": self.password_edit.text()}
                        # 如果未勾选记住密码，则只保存用户名
                        else:
                            default_user_info = {"username": self.username_edit.text()}
                        with open(default_user_info_file, "w", encoding="utf-8") as f:
                            json.dump(default_user_info, f, indent=4, ensure_ascii=False)
                        LOG(LEVEL.INFO, self.label.text(), f"用户<{self.username_edit.text()}>登录成功")
                        msg_box = QMessageBox.information(self, "提示", "登录成功")
                        if msg_box == QMessageBox.Ok:
                            self.hide()
                            self.tool_win.display()
                    else:
                        QMessageBox.warning(self, "提示", "密码错误，请重新输入")
                        LOG(LEVEL.WARNING, self.label.text(), "密码错误，请重新输入")
                else:
                    QMessageBox.warning(self, "提示", "该用户未注册，请先注册账号")
                    LOG(LEVEL.WARNING, self.label.text(), f"用户<{self.username_edit.text()}>未注册，请先注册账号")
        else:
            LOG(LEVEL.ERROR, self.label.text(), "用户信息文件不存在")
            QMessageBox.warning(self, "提示", "该用户未注册，请先注册账号")

    # 显示注册账号窗口
    def register_btn_clicked(self):
        self.hide()
        self.register_win.display()
        self.register_win.activateWindow()
        self.register_win.raise_()

    # 显示修改密码窗口
    def modify_btn_clicked(self):
        self.hide()
        self.modify_win.display(self.username_edit.text())
        self.modify_win.activateWindow()
        self.modify_win.raise_()

    # 登录画面初始化
    def display(self, user_name="", password=""):
        if user_name:
            self.username_edit.setText(user_name)
        if password:
            self.password_edit.setText(password)
        self.show()
        self.login_btn.setFocus()

    # 检查默认用户
    def check_default_user(self):
        # 检查默认用户信息文件是否存在
        if os.path.exists(default_user_info_file):
            # 读取默认用户信息文件内容
            with open(default_user_info_file, "r", encoding="utf-8") as f:
                default_user_info = json.load(f)
            # 如果默认用户信息文件中存在用户名，则自动填充
            self.username_edit.setText(default_user_info["username"])
            # 如果默认用户信息文件中存在密码，则自动填充
            if "password" in default_user_info:
                self.password_edit.setText(default_user_info["password"])
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
