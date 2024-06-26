from PySide6.QtWidgets import QDialog
from ui.modify_ui import Ui_Dialog
from util.passwordEdit import PasswordEdit


class modifyWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(modifyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("修改密码")
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

    def display(self, login, retrieve):
        self.login = login
        self.retrieve = retrieve
        self.retrieve.close()
        self.showNormal()

    # 修改密码窗口关闭时触发
    def closeEvent(self, event):
        self.login.show()
        self.login.login_btn.setFocus()
