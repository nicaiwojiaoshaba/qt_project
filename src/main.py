import sys

from PySide6.QtWidgets import QApplication
# https://github.com/5yutan5/PyQtDarkTheme
# python -m qdarktheme.widget_gallery
import qdarktheme
from util.path import expand_source_root

# 追加环境变量
sys.path.append(str(expand_source_root()))
sys.path.append(str(expand_source_root("resource")))

# from win.login import LoginWindow
from win.tool import ToolWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    # main_window = LoginWindow()
    main_window = ToolWindow()
    main_window.display()
    sys.exit(app.exec())
