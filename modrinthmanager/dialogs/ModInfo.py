from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtWidgets import QDialog, QListWidgetItem

from data.ui.mod_info import Ui_Dialog
from modrinthmanager.items.mod_items import Mod, Modpack
from modrinthmanager.parsers.Modrinth import Modrinth
from modrinthmanager.utils import Database
from modrinthmanager.utils.utils import save_version, get_mod_preview, check_version_exists


class ModInfo(QDialog):
    def __init__(self, mod: Mod):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.items_list.doubleClicked.connect(self.download)
        self.ui.add_btn.clicked.connect(self.change_favourite)

        self.db = Database()
        self.mod_pixmap = None
        self.mod = mod
        self.db.add_mod(self.mod)
        self.versions = []

        self.set_info()
        self.get_versions()

    def resizeEvent(self, a0):
        self.update_manga_preview()

    def set_info(self):
        if self.db.check_mod_modpack(self.mod):
            self.ui.add_btn.setChecked(True)
        else:
            self.ui.add_btn.setChecked(False)

        self.ui.name_lbl.setText(self.mod.get_name())
        self.ui.description_text.setText(self.mod.description)

        self.ui.icon_lbl.setPixmap(get_mod_preview(self.mod))

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

    def download(self):
        modpack = Modpack(self.mod.get_name(), '1.19.2', 'Fabric', [])
        version = self.versions[self.ui.items_list.currentIndex().row()]
        if not check_version_exists(modpack, version):
            save_version(modpack, version, Modrinth.get_version(version))

    @Slot()
    def change_favourite(self):
        if self.db.check_mod_modpack(self.mod):
            self.db.rem_mod_modpack(self.mod)
        else:
            self.db.add_mod_modpack(self.mod)
