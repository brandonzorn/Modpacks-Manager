from PySide6.QtWidgets import QMainWindow
from data.ui.main_window import Ui_MainWindow
from modrinthmanager.widgets.mod_search import ModSearch


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        window = ModSearch()
        self.ui.top_item.addWidget(window)
        self.show()