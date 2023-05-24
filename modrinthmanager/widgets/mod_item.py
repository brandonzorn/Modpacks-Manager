from PySide6.QtWidgets import QListWidgetItem

from modrinthmanager.items import Mod
from modrinthmanager.utils.utils import get_mod_preview, Worker


class ModItem(QListWidgetItem):
    def __init__(self, mod: Mod, pool=None):
        super().__init__(mod.get_name())
        self.mod = mod
        self.mod_pixmap = None
        self._pool = pool
        self.update_image()

    def get_image(self):
        self.mod_pixmap = get_mod_preview(self.mod)

    def set_image(self):
        self.setIcon(self.mod_pixmap)

    def update_image(self):
        Worker(target=self.get_image, callback=self.set_image).start(self._pool)