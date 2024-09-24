import json
import os
import bcrypt

from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox
from PySide6.QtGui import QIcon
from ui.register_ui import Ui_Dialog
from util.passwordEdit import PasswordEdit
from util.config import user_info_path, user_info_file, resource_path
from util.logger import LOG, LEVEL
from util.inputValidator import inputValidator


class RegisterWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置画面标题
        self.setWindowTitle("注册")
        # 设置图标
        self.setWindowIcon(QIcon(f"{resource_path}/main.png"))
        # 初始化带有按钮的密码框
        self.password_edit = PasswordEdit("password_edit")
        # 替换模板密码框 verticalLayout_2为密码框父元素
        self.verticalLayout_2.replaceWidget(self.password_temp, self.password_edit)
        # 删除模板密码框
        self.password_temp.deleteLater()
        # 设定新密码框宽度
        self.password_edit.setFixedWidth(272)
        # 初始化带有按钮的确认密码框
        self.confirm_edit = PasswordEdit("confirm_edit")
        # 替换模板确认密码框 verticalLayout_2为确认密码框父元素
        self.verticalLayout_2.replaceWidget(self.confirm_temp, self.confirm_edit)
        # 删除模板确认密码框
        self.confirm_temp.deleteLater()
        # 设定新确认密码框宽度
        self.confirm_edit.setFixedWidth(272)
        # 设置tab切换控件的顺序
        self.setTabOrder(self.username_edit, self.password_edit)
        self.setTabOrder(self.password_edit, self.confirm_edit)
        self.setTabOrder(self.confirm_edit, self.security_name_edit)
        # 绑定注册按钮点击事件
        self.register_btn.clicked.connect(self.register_btn_clicked)
        self.username_edit.textChanged.connect(lambda: self.input_line_change(self.username_edit))
        self.password_edit.textChanged.connect(lambda: self.input_line_change(self.password_edit))
        self.confirm_edit.textChanged.connect(lambda: self.input_line_change(self.confirm_edit))
        self.security_name_edit.textChanged.connect(lambda: self.input_line_change(self.security_name_edit))
        self.security_number_edit.textChanged.connect(lambda: self.input_line_change(self.security_number_edit))

    # 注册画面初始化
    def display(self):
        self.show()
        LOG(LEVEL.INFO, self.label.text(), "注册画面初始化成功")

    # 焦点事件
    def input_line_change(self, line_name):
        if line_name.text():
            line_name.setStyleSheet("")

    # 窗口关闭时还原控件
    def initialize_controls(self):
        all_input_lines = self.findChildren(QLineEdit)
        for input_line in all_input_lines:
            input_line.setText("")
            input_line.setStyleSheet("")
        self.username_edit.setFocus()

    # 注册窗口关闭时触发
    def closeEvent(self, event):
        self.initialize_controls()
        self.login_win.display()
        LOG(LEVEL.INFO, self.label.text(), "注册窗口关闭,登录窗口启动")

    # 注册按钮点击事件
    def register_btn_clicked(self):
        validate_flg = 0
        # 取得所有输入框控件对象
        all_input_lines = self.findChildren(QLineEdit)
        # 校验所有输入框
        for input_line in all_input_lines:
            validate_flg += inputValidator(input_line)
        # 所有输入框都输入了值，则进行注册
        if validate_flg == 0:
            # 创建用户信息目录
            os.makedirs(os.path.dirname(user_info_path), exist_ok=True)
            if not os.path.exists(user_info_file):
                with open(user_info_file, "w", encoding="utf-8") as file:
                    LOG(LEVEL.INFO, self.label.text(), "用户信息文件不存在，创建用户信息文件")
            # 读取用户信息文件
            with open(user_info_file, "r+", encoding="utf-8") as file:
                # 如果文件为空，则创建空字典
                if not file.read().strip():
                    data = {}
                # 如果文件不为空，则读取文件内容
                else:
                    try:
                        file.seek(0)
                        data = json.load(file)
                    except json.decoder.JSONDecodeError:
                        LOG(LEVEL.ERROR, self.label.text(), "用户信息文件格式错误")
                # 校验用户名是否已存在
                if self.username_edit.text() in data.keys():
                    return QMessageBox.warning(self, "警告", "用户名已存在")
                # 校验两次输入的密码是否一致
                elif self.password_edit.text() != self.confirm_edit.text():
                    return QMessageBox.warning(self, "警告", "两次输入密码必须相同")
                # 校验通过
                else:
                    user_name = self.username_edit.text()
                    password = self.password_edit.text()
                    # bcrypt加密
                    hash_pasword = bcrypt.hashpw((self.password_edit.text().encode("utf-8")), bcrypt.gensalt())
                    security_name = self.security_name_edit.text()
                    security_number = self.security_number_edit.text()
                    # 将用户信息写入文件
                    user_info = {
                        user_name: {
                            "password": hash_pasword.decode("utf-8"),
                            "security_name": security_name,
                            "security_number": security_number,
                        }
                    }
                    # 将用户信息追加入文件
                    data.update(user_info)
                    file.seek(0)
                    json.dump(data, file, ensure_ascii=False, indent=4)
                    file.truncate()
                    LOG(LEVEL.INFO, self.label.text(), f"用户<{user_name}>注册成功")
                msg_box = QMessageBox.information(self, "信息", "新用户注册成功")
                if msg_box == QMessageBox.Ok:
                    self.initialize_controls()
                    self.hide()
                    self.login_win.display(user_name, password)
                    LOG(LEVEL.INFO, self.label.text(), "注册成功，跳转到登录界面")
        else:
            LOG(LEVEL.ERROR, self.label.text(), "用户注册画面的输入信息校验失败")
