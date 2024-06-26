from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui.register_ui import Ui_Dialog
from util.passwordEdit import PasswordEdit


class registerWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(registerWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("注册")
        # 设置任务栏图标
        self.setWindowIcon(QIcon("plugins.png"))
        # 初始化带有按钮的密码框
        self.password_edit = PasswordEdit()
        # 替换模板密码框 verticalLayout_2为密码框父元素
        self.verticalLayout_2.replaceWidget(self.password_temp, self.password_edit)
        # 删除模板密码框
        self.password_temp.deleteLater()
        # 设定新密码框宽度
        self.password_edit.setFixedWidth(272)
        # 初始化带有按钮的确认密码框
        self.confirm_edit = PasswordEdit()
        # 替换模板确认密码框 verticalLayout_2为确认密码框父元素
        self.verticalLayout_2.replaceWidget(self.confirm_temp, self.confirm_edit)
        # 删除模板确认密码框
        self.confirm_temp.deleteLater()
        # 设定新确认密码框宽度
        self.confirm_edit.setFixedWidth(272)

    def display(self, login):
        self.login = login
        self.showNormal()

    # 注册窗口关闭时触发
    def closeEvent(self, event):
        self.login.show()
