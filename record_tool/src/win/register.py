from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui.register_ui import Ui_Dialog
from util.passwordEdit import PasswordEdit
from util.path import expand_source_root


class RegisterWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置画面标题
        self.setWindowTitle("注册")
        # 设置图标
        self.setWindowIcon(QIcon(f"{expand_source_root('resource')}/user.png"))
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
        # 绑定注册按钮点击事件
        self.register_btn.clicked.connect(self.register_btn_clicked)

    # 注册画面初始化
    def display(self):
        self.show()

    # 注册窗口关闭时触发
    def closeEvent(self, event):
        self.login_win.display()

    # 注册按钮点击事件
    def register_btn_clicked(self):
        self.hide()
        self.login_win.display()
