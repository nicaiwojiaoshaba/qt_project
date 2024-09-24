import json

from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from ui.retrieve_ui import Ui_Dialog
from PySide6.QtGui import QIcon
from util.logger import LOG, LEVEL

from util.inputValidator import inputValidator
from util.config import resource_path, user_info_file


class RetrieveWindow(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(RetrieveWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置画面标题
        self.setWindowTitle("找回密码")
        # 设置图标
        self.setWindowIcon(QIcon(f"{resource_path}/main.png"))
        # 绑定确认按钮事件
        self.confirm_btn.clicked.connect(self.confirm_btn_clicked)

    # 找回密码初始化方法
    def display(self, username):
        self.username_edit.setText(username)
        self.show()
        self.confirm_btn.setFocus()

    # 窗口关闭时还原控件
    def initialize_controls(self):
        all_input_lines = self.findChildren(QLineEdit)
        for input_line in all_input_lines:
            input_line.setText("")
            input_line.setStyleSheet("")
        self.confirm_btn.setFocus()

    # 点击确认按钮时触发
    def confirm_btn_clicked(self):
        validate_flg = 0
        # 检查入力框是否都输入了内容
        all_input_lines = self.findChildren(QLineEdit)
        for line in all_input_lines:
            validate_flg += inputValidator(line)
        # 输入内容校验
        if validate_flg == 0:
            # 读取用户信息
            with open(user_info_file, "r", encoding="utf-8") as f:
                user_info = json.load(f)
                user_name = self.username_edit.text()
                # 检查用户是否存在
                if user_name in user_info:
                    # 检查密保问题(姓名)是否正确
                    if self.question1_edit.text() == user_info[user_name]["security_name"]:
                        # 检查密保问题(工号)是否正确
                        if self.question2_edit.text() == user_info[user_name]["security_number"]:
                            LOG(LEVEL.INFO, self.label.text(), f"用户<{user_name}>密保验证通过")
                            msg_box = QMessageBox.information(self, "提示", "密保验证通过")
                            if msg_box == QMessageBox.Ok:
                                self.initialize_controls()
                                self.hide()
                                self.modify_win.display(user_name, True)
                        else:
                            LOG(LEVEL.ERROR, self.label.text(), f"用户<{user_name}>工号验证失败")
                            QMessageBox.warning(self, "警告", "工号验证失败")
                    else:
                        print(self.label.text())
                        LOG(LEVEL.ERROR, self.label.text(), f"用户<{user_name}>姓名验证失败")
                        QMessageBox.warning(self, "警告", "姓名验证失败")
                else:
                    LOG(LEVEL.ERROR, self.label.text(), f"用户<{user_name}>不存在")
                    QMessageBox.warning(self, "警告", f"用户<{user_name}>不存在")

    # 找回密码窗口关闭时触发
    def closeEvent(self, event):
        self.initialize_controls()
        self.login_win.display()
