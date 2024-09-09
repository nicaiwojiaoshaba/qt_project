from PySide6.QtWidgets import QMainWindow
from ui.tool_ui import Ui_MainWindow
from PySide6.QtGui import QIcon
from util.path import expand_source_root


class ToolWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ToolWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("工具")
        self.setWindowIcon(QIcon(f"{expand_source_root('resource')}/tool.png"))
        # self.__signal_slot()

    def display(self):
        self.show()

    # def __signal_slot(self):
    #     self.sessions_btn.clicked.connect(self.__session.display)
    #     self.links_btn.clicked.connect(self.__links.display)
    #     self.plugins_btn.clicked.connect(self.__plugins.display)
