from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow
from data.ui.main_window import Ui_MainWindow
from modrinthmanager.widgets.mod_search import ModSearch


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        window = ModSearch()
        self.ui.top_item.addWidget(window)
        self.show()
