from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow
from data.ui.main_window import Ui_MainWindow
from modrinthmanager.widgets.mod_search import ModSearch
from modrinthmanager.widgets.modpacks import ModpacksWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))

        self.search_wid = ModSearch()
        self.modpacks_wid = ModpacksWidget()

        self.ui.btn_main.clicked.connect(lambda: self.change_widget(self.search_wid))
        self.ui.btn_library.clicked.connect(lambda: self.change_widget(self.modpacks_wid))

        self.change_widget(self.search_wid)
        self.show()

    def change_widget(self, widget):
        if self.ui.top_item.currentWidget() == widget:
            return
        widget.setup()
        if self.ui.top_item.currentWidget():
            self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(widget)
        self.ui.top_item.setCurrentWidget(widget)
