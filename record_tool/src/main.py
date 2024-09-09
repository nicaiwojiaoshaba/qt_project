import sys
from PySide6.QtWidgets import QApplication
# https://github.com/5yutan5/PyQtDarkTheme
# python -m qdarktheme.widget_gallery
import qdarktheme
from util.path import expand_source_root
# 追加环境变量
sys.path.append(str(expand_source_root()))
sys.path.append(str(expand_source_root("resource")))

from win.login import LoginWindow
from win.register import RegisterWindow
from win.retrieve import RetrieveWindow
from win.modify import ModifyWindow
from win.tool import ToolWindow


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    login_win = LoginWindow()
    # 注册画面
    login_win.register_win = RegisterWindow()
    # 找回密码画面
    login_win.retrieve_win = RetrieveWindow()
    # 修改密码画面
    login_win.modify_win = ModifyWindow()
    login_win.tool_win = ToolWindow()
    # 注册画面引用登录
    login_win.register_win.login_win = login_win
    # 找回密码画面引用登录
    login_win.retrieve_win.login_win = login_win
    # 找回密码画面引用修改画面
    login_win.retrieve_win.modify_win = login_win.modify_win
    # 修改画面引用登录
    login_win.modify_win.login_win = login_win
    # 显示登录画面
    login_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
