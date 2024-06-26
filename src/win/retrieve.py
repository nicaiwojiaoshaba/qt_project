from PySide6.QtWidgets import QDialog
from ui.retrieve_ui import Ui_Dialog
from win import modify


class retrieveWindow(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(retrieveWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("找回密码")
        self.confirm_btn.clicked.connect(self.show_modify_window)
        self.modify = modify.modifyWindow(self)

    def display(self, login):
        self._loginWindowFlag = True
        self.login = login
        self.showNormal()

    def show_modify_window(self):
        self._loginWindowFlag = False
        self.modify.display(self.login, self)

    # 忘记密码窗口关闭时触发
    def closeEvent(self, event):
        if self._loginWindowFlag:
            self.login.show()
            self.login.login_btn.setFocus()
