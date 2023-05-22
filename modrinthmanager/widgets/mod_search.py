from PySide6.QtWidgets import QWidget, QListWidgetItem

from data.ui.mod_search import Ui_Form
from modrinthmanager.dialogs.ModInfo import ModInfo
from modrinthmanager.items.mod_items import Mod
from modrinthmanager.parsers.Modrinth import Modrinth
from modrinthmanager.utils.utils import get_mod_preview


class ModSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.items_list.doubleClicked.connect(self.open_mod_info)
        self.info = None
        self.mods: list[Mod] = []

    def setup(self):
        self.search()

    def search(self):
        self.ui.items_list.clear()
        version = self.ui.version_line.text()
        mod_loader = self.ui.modloader_line.text()
        facets = []
        if version:
            facets.append(f'["versions:{version}"]')
        if mod_loader:
            facets.append(f'["categories:{mod_loader}"]')
        params = {'query': self.ui.search_line.text(),
                  "facets": f'[{", ".join(facets)}]' if facets else None}
        self.mods = Modrinth.search(params)
        for mod in self.mods:
            item = QListWidgetItem(mod.get_name())
            item.setIcon(get_mod_preview(mod))
            self.ui.items_list.addItem(item)

    def open_mod_info(self):
        self.info = ModInfo(self.mods[self.ui.items_list.currentIndex().row()])
        self.info.show()
