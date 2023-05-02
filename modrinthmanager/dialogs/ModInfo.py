from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QDialog, QListWidgetItem

from data.ui.mod_info import Ui_Dialog
from modrinthmanager.items.mod_items import Mod
from modrinthmanager.parsers.Modrinth import Modrinth
from modrinthmanager.utils.utils import save_version, get_mod_preview


class ModInfo(QDialog):
    def __init__(self, mod: Mod):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.name_lbl.setText(mod.get_name())
        self.ui.description_text.setText(mod.description)
        self.ui.items_list.doubleClicked.connect(self.download)
        self.mod_pixmap = None
        self.mod = mod
        self.versions = []
        self.set_icon()
        self.get_versions()

    def resizeEvent(self, a0):
        self.update_manga_preview()

    def update_manga_preview(self):
        self.ui.icon_lbl.clear()
        if not self.mod_pixmap:
            self.mod_pixmap = get_mod_preview(self.mod)
        image_size = QSize(self.width() // 5, self.height() // 2)
        pixmap = self.mod_pixmap.scaled(image_size, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
        self.ui.icon_lbl.setPixmap(pixmap)

    def get_versions(self):
        self.versions = Modrinth.get_versions(self.mod)
        for version in self.versions:
            item = QListWidgetItem(version.get_name())
            self.ui.items_list.addItem(item)

    def set_icon(self):
        self.ui.icon_lbl.setPixmap(get_mod_preview(self.mod))

    def download(self):
        version = self.versions[self.ui.items_list.currentIndex().row()]
        save_version(self.mod, version, Modrinth.get_version(version))
