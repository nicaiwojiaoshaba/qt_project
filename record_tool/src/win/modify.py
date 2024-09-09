from PySide6.QtWidgets import QDialog
from ui.modify_ui import Ui_Dialog
from PySide6.QtGui import QIcon
from util.passwordEdit import PasswordEdit
from util.path import expand_source_root


class ModifyWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(ModifyWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置画面标题
        self.setWindowTitle("修改密码")
        # 设置图标
        self.setWindowIcon(QIcon(f"{expand_source_root('resource')}/user.png"))

        # 原密码
        self.original_edit = PasswordEdit()
        self.horizontalLayout_2.replaceWidget(self.original_temp, self.original_edit)
        self.original_temp.deleteLater()
        # 新密码
        self.new_edit = PasswordEdit()
        self.horizontalLayout_2.replaceWidget(self.new_temp, self.new_edit)
        self.new_temp.deleteLater()
        # 确认密码
        self.confirm_edit = PasswordEdit()
        self.horizontalLayout_2.replaceWidget(self.confirm_temp, self.confirm_edit)
        self.confirm_temp.deleteLater()
        self.modify_btn.clicked.connect(self.modify_btn_clicked)

    # 修改密码初始化方法
    def display(self):
        self.show()

    # 修改密码窗口关闭时触发
    def closeEvent(self, event):
        self.login_win.display()

    # 点击修改按钮
    def modify_btn_clicked(self):
        self.hide()
        self.login_win.display()
