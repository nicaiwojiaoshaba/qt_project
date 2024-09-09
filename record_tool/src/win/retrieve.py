from PySide6.QtWidgets import QDialog
from ui.retrieve_ui import Ui_Dialog
from PySide6.QtGui import QIcon
from util.path import expand_source_root


class RetrieveWindow(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(RetrieveWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置画面标题
        self.setWindowTitle("找回密码")
        # 设置图标
        self.setWindowIcon(QIcon(f"{expand_source_root('resource')}/user.png"))
        # 绑定确认按钮事件
        self.confirm_btn.clicked.connect(self.confirm_btn_clicked)

    # 找回密码初始化方法
    def display(self):
        self.show()

    # 点击确认按钮时触发
    def confirm_btn_clicked(self):
        self.hide()
        self.modify_win.display()

    # 忘记密码窗口关闭时触发
    def closeEvent(self, event):
        # if self._loginWindowFlag:
        self.login_win.display()
