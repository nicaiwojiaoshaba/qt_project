from PySide6.QtWidgets import QLineEdit, QStyle
from PySide6.QtGui import QIcon, QAction


class PasswordEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设定lineEdit为password类型
        self.setEchoMode(QLineEdit.Password)
        # 定义图标
        self.passWordIcon = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogIgnoreButton), "showPassword", self)
        # 将图标添加到lineEdit中
        self.addAction(self.passWordIcon, QLineEdit.TrailingPosition)
        # 设置图标点击事件
        self.passWordIcon.triggered.connect(self.show_password)

    # 密码框图标切换
    def show_password(self):
        if self.echoMode() == QLineEdit.Password:
            self.setEchoMode(QLineEdit.Normal)
            self.passWordIcon.setIcon(QIcon(":/resource/showPass.png"))
        else:
            self.setEchoMode(QLineEdit.Password)
            self.passWordIcon.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DialogIgnoreButton))
