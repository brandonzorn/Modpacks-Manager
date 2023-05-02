from PySide6.QtWidgets import QWidget, QListWidgetItem

from data.ui.mod_search import Ui_Form
from modrinthmanager.dialogs.ModInfo import ModInfo
from modrinthmanager.items.mod_items import Mod
from modrinthmanager.parsers.Modrinth import Modrinth


class ModSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.items_list.doubleClicked.connect(self.open_mod_info)
        self.info = None
        self.mods: list[Mod] = []

    def search(self):
        self.ui.items_list.clear()
        params = {'query': self.ui.search_line.text(), "facets": '[["categories:fabric"], ["versions:1.19.4"]]'}
        self.mods = Modrinth.search(params)
        for mod in self.mods:
            item = QListWidgetItem(mod.get_name())
            self.ui.items_list.addItem(item)

    def open_mod_info(self):
        self.info = ModInfo(self.mods[self.ui.items_list.currentIndex().row()])
        self.info.show()
