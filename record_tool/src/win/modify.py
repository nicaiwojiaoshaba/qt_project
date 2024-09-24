import json
import bcrypt
import os

from PySide6.QtWidgets import QDialog, QLineEdit, QMessageBox
from ui.modify_ui import Ui_Dialog
from PySide6.QtGui import QIcon
from util.passwordEdit import PasswordEdit
from util.config import user_info_file, resource_path, default_user_info_file
from util.checkPassword import checkPassword
from util.logger import LOG, LEVEL
from util.inputValidator import inputValidator


class ModifyWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(ModifyWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置画面标题
        self.setWindowTitle("修改密码")
        # 设置图标
        self.setWindowIcon(QIcon(f"{resource_path}/main.png"))

        # 原密码
        self.original_edit = PasswordEdit("original_edit", "原密码:")
        self.verticalLayout_2.replaceWidget(self.original_temp, self.original_edit)
        self.original_temp.deleteLater()
        # 新密码
        self.new_edit = PasswordEdit("new_edit", "新密码:")
        self.verticalLayout_2.replaceWidget(self.new_temp, self.new_edit)
        self.new_temp.deleteLater()
        # 确认密码
        self.confirm_edit = PasswordEdit("confirm_edit", "确认密码:")
        self.verticalLayout_2.replaceWidget(self.confirm_temp, self.confirm_edit)
        self.confirm_temp.deleteLater()
        self.modify_btn.clicked.connect(self.modify_btn_clicked)
        # 设置tab切换控件的顺序
        self.setTabOrder(self.username_edit, self.original_edit)
        self.setTabOrder(self.original_edit, self.new_edit)
        self.setTabOrder(self.new_edit, self.confirm_edit)

        self.retrieve_btn.setFlat(True)
        self.retrieve_btn.clicked.connect(self.retrieve_btn_clicked)
        self.username_edit.textChanged.connect(lambda: self.input_line_change(self.username_edit))
        self.original_edit.textChanged.connect(lambda: self.input_line_change(self.original_edit))
        self.new_edit.textChanged.connect(lambda: self.input_line_change(self.new_edit))
        self.confirm_edit.textChanged.connect(lambda: self.input_line_change(self.confirm_edit))

    # 修改密码初始化方法
    def display(self, user_name="", retrieve_flg=False):
        self.initialize_controls()
        self.retrieve_flg = retrieve_flg
        if user_name:
            self.username_edit.setText(user_name)
        self.username_edit.setDisabled(retrieve_flg)
        self.original_edit.setDisabled(retrieve_flg)
        if self.retrieve_flg:
            self.username_edit.setStyleSheet("border: 1px solid grey; background-color: rgb(240, 240, 240);")
            self.original_edit.setStyleSheet("border: 1px solid grey; background-color: rgb(240, 240, 240);")
        else:
            self.username_edit.setStyleSheet("")
            self.original_edit.setStyleSheet("")
        self.show()
        self.modify_btn.setFocus()

    # 焦点事件
    def input_line_change(self, line_name):
        if line_name.text():
            line_name.setStyleSheet("")

    # 修改密码窗口关闭时触发
    def closeEvent(self, event):
        self.initialize_controls()
        self.login_win.display()
        LOG(LEVEL.INFO, self.label.text(), "修改密码窗口关闭,登录窗口启动")

    # 点击找回密码按钮
    def retrieve_btn_clicked(self):
        self.hide()
        self.retrieve_win.display(self.username_edit.text())
        self.retrieve_win.activateWindow()
        self.retrieve_win.raise_()

    # 窗口关闭时还原控件
    def initialize_controls(self):
        all_input_lines = self.findChildren(QLineEdit)
        for input_line in all_input_lines:
            input_line.setText("")
            input_line.setStyleSheet("")

    # 点击修改按钮
    def modify_btn_clicked(self):
        validate_flg = 0
        # 获取输入的用户名
        username = self.username_edit.text()
        # 获取输入的密码
        password = self.new_edit.text()
        # 获取确认密码
        confirm_password = self.confirm_edit.text()
        # 读取用户信息
        with open(user_info_file, "r") as f:
            user_info_list = json.load(f)
        if not self.retrieve_flg:
            # 取得所有入力框对象
            all_input_lines = self.findChildren(QLineEdit)
            # 验证所有入力框
            for input_line in all_input_lines:
                validate_flg += inputValidator(input_line)
            # 验证通过
            if validate_flg == 0:
                # 如果用户名在用户信息中存在
                if username in user_info_list:
                    # 原密码输入正确
                    if checkPassword(self.original_edit.text(), user_info_list[username]["password"]):
                        # 确认新密码和原密码不相同
                        if password != self.original_edit.text():
                            # 确认新密码和确认密码相同
                            if password != confirm_password:
                                QMessageBox.warning(self, "警告", "新密码与确认密码不一致")
                                LOG(LEVEL.WARNING, self.label.text(), "新密码与确认密码不一致")
                                return
                        else:
                            QMessageBox.warning(self, "警告", "新密码不能与原密码相同")
                            LOG(LEVEL.WARNING, self.label.text(), "新密码不能与原密码相同")
                            return
                    else:
                        QMessageBox.warning(self, "警告", "原密码输入错误")
                        LOG(LEVEL.WARNING, self.label.text(), "原密码输入错误")
                        return
                else:
                    QMessageBox.warning(self, "警告", "当前用户未注册")
                    LOG(LEVEL.ERROR, self.label.text(), f"当前用户{username}未注册")
                    return
            else:
                QMessageBox.warning(self, "警告", "修改密码画面的输入信息校验失败")
                LOG(LEVEL.WARNING, self.label.text(), "修改密码画面的输入信息校验失败")
                return
        else:
            validate_flg += inputValidator(self.new_edit)
            validate_flg += inputValidator(self.confirm_edit)
            if validate_flg == 0:
                if password != confirm_password:
                    QMessageBox.warning(self, "警告", "两次密码输入不相同")
                    LOG(LEVEL.WARNING, self.label.text(), "两次密码输入不相同")
                    return
        # 加密密码
        hash_pasword = bcrypt.hashpw((password.encode("utf-8")), bcrypt.gensalt())
        user_info_list[username]["password"] = hash_pasword.decode("utf-8")
        # 将修改后的用户信息 写入文件
        with open(user_info_file, "w") as f:
            json.dump(user_info_list, f, ensure_ascii=False, indent=4)
        LOG(LEVEL.INFO, self.label.text(), f"用户<{username}>修改密码成功")
        msg_box = QMessageBox.information(self, "提示", "修改密码成功")
        if msg_box == QMessageBox.Ok:
            self.initialize_controls()
            self.hide()
            self.login_win.display(username, password)

        # 判断默认用户是否存在
        if os.path.exists(default_user_info_file):
            with open(default_user_info_file, "r+") as f:
                default_user_info = json.load(f)
                # 如果默认用户名和输入的用户名相同
                if username == default_user_info["username"] and "password" in default_user_info:
                    # 修改默认用户密码
                    default_user_info["password"] = password
                    f.seek(0)
                    json.dump(default_user_info, f, ensure_ascii=False, indent=4)
                    f.truncate()
