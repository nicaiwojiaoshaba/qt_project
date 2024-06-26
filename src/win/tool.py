from PySide6.QtWidgets import QMainWindow
from ui.tool_ui import Ui_MainWindow


class ToolWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ToolWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("工具")
        # self.__signal_slot()

    def display(self):
        self.showNormal()

    # def __signal_slot(self):
    #     self.sessions_btn.clicked.connect(self.__session.display)
    #     self.links_btn.clicked.connect(self.__links.display)
    #     self.plugins_btn.clicked.connect(self.__plugins.display)
