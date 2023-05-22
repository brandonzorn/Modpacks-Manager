from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QListWidgetItem
from data.ui.modpacks import Ui_Form
from modrinthmanager.items import Mod
from modrinthmanager.parsers.LocalLib import LocalLib
from modrinthmanager.parsers.Modrinth import Modrinth
from modrinthmanager.utils.utils import get_mod_preview, save_version


class ModpacksWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mods: list[Mod] = []
        self.catalog = LocalLib()
        self.ui.download.clicked.connect(self.download_all)

    def setup(self):
        self.update_content()

    def update_content(self):
        self.mods = self.catalog.search_mods()
        for mod in self.mods:
            item = QListWidgetItem(mod.get_name())
            item.setIcon(get_mod_preview(mod))
            self.ui.items_list.addItem(item)

    @Slot()
    def download_all(self):
        for mod in self.mods:
            version = Modrinth.get_versions(mod)[0]
            save_version(mod, version, Modrinth.get_version(version))
