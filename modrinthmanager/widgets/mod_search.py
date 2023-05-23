from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QListWidgetItem

from data.ui.mod_search import Ui_Form
from modrinthmanager.dialogs.ModInfo import ModInfo
from modrinthmanager.items.mod_items import Mod
from modrinthmanager.parsers.Modrinth import Modrinth
from modrinthmanager.utils.threads import Thread
from modrinthmanager.utils.utils import get_mod_preview


class ModSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.items_list.doubleClicked.connect(self.open_mod_info)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.info = None
        self.mods: list[Mod] = []

        self.cur_page = 1

        self._get_content_thread = Thread(target=self._get_content, callback=self.update_content)

    def setup(self):
        self.get_content()

    @Slot()
    def search(self):
        self.get_content()

    @Slot()
    def turn_page_next(self):
        if self.cur_page == 999:
            return
        self.cur_page += 1
        self.get_content()

    @Slot()
    def turn_page_prev(self):
        if self.cur_page == 1:
            return
        self.cur_page -= 1
        self.get_content()

    def update_page(self):
        self.ui.page_lbl.setText(f"{'Page'} {self.cur_page}")

    def get_content(self):
        self.update_page()
        self._get_content_thread.terminate()
        self._get_content_thread.wait()
        self._get_content_thread.start()

    def _get_content(self):
        version = self.ui.version_line.text()
        mod_loader = self.ui.modloader_line.text()
        facets = []
        if version:
            facets.append(f'["versions:{version}"]')
        if mod_loader:
            facets.append(f'["categories:{mod_loader.lower()}"]')
        params = {'query': self.ui.search_line.text(), 'offset': (self.cur_page - 1) * 10,
                  "facets": f'[{", ".join(facets)}]' if facets else None}
        self.mods = Modrinth.search(params)

    def update_content(self):
        self.ui.items_list.clear()
        for mod in self.mods:
            item = QListWidgetItem(mod.get_name())
            item.setIcon(get_mod_preview(mod))
            self.ui.items_list.addItem(item)

    def open_mod_info(self):
        self.info = ModInfo(self.mods[self.ui.items_list.currentIndex().row()])
        self.info.show()
