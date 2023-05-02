from PySide6.QtWidgets import QDialog, QListWidgetItem

from data.ui.mod_info import Ui_Dialog
from modrinthmanager.items.mod_items import Mod
from modrinthmanager.parsers.Modrinth import Modrinth
from modrinthmanager.utils.utils import save_version


class ModInfo(QDialog):
    def __init__(self, mod: Mod):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.name_lbl.setText(mod.get_name())
        self.ui.description_text.setText(mod.description)
        self.ui.items_list.doubleClicked.connect(self.download)

        self.mod = mod
        self.versions = []

        self.get_versions()

    def get_versions(self):
        self.versions = Modrinth.get_versions(self.mod)
        for version in self.versions:
            item = QListWidgetItem(version.get_name())
            self.ui.items_list.addItem(item)

    def download(self):
        version = self.versions[self.ui.items_list.currentIndex().row()]
        save_version(self.mod, version, Modrinth.get_version(version))
