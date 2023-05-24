from PySide6.QtCore import Slot, QThreadPool
from PySide6.QtWidgets import QWidget, QRadioButton

from data.ui.mod_search import Ui_Form
from modrinthmanager.dialogs.ModInfo import ModInfo
from modrinthmanager.items.mod_items import Mod
from modrinthmanager.items.other_items import RequestForm
from modrinthmanager.parsers import CurseForge, Modrinth
from modrinthmanager.utils.catalog_manager import USER_CATALOGS, get_catalog
from modrinthmanager.utils.threads import Thread
from modrinthmanager.widgets.mod_item import ModItem


class ModSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.items_list.doubleClicked.connect(self.open_mod_info)
        self.ui.prev_btn.clicked.connect(self.turn_page_prev)
        self.ui.next_btn.clicked.connect(self.turn_page_next)
        self.ui.catalogs_btn.clicked.connect(
            lambda: self.ui.catalogs_frame.setVisible(not self.ui.catalogs_frame.isVisible()))
        self.ui.catalogs_list.doubleClicked.connect(
            lambda: self.change_catalog(self.ui.catalogs_list.currentIndex().row()))
        self.ui.catalogs_frame.setVisible(False)
        self.info = None
        self.mods: list[Mod] = []

        self.req_params = RequestForm()

        self.mod_thread_pool = QThreadPool()
        self.order_items = {}
        self.loader_items = {}
        self.catalog = None

        self._get_content_thread = Thread(target=self._get_content, callback=self.update_content)

    def setup(self):
        if not self.catalog:
            self.ui.catalogs_frame.hide()
            self.ui.catalogs_list.clear()
            self.ui.catalogs_list.addItems([i.CATALOG_NAME for i in USER_CATALOGS])
            self.change_catalog(0)
        else:
            self.get_content()

    def setup_catalogs(self):
        self.change_catalog(0)

    def change_catalog(self, index: int):
        self.catalog = USER_CATALOGS[index]
        self.setup_filters()
        self.get_content()

    @Slot()
    def search(self):
        self.get_content()

    @Slot()
    def turn_page_next(self):
        if self.req_params.page == 999:
            return
        self.req_params.page += 1
        self.get_content()

    @Slot()
    def turn_page_prev(self):
        if self.req_params.page == 1:
            return
        self.req_params.page -= 1
        self.get_content()

    def update_page(self):
        self.ui.page_lbl.setText(f"{'Page'} {self.req_params.page}")

    def get_content(self):
        self.update_page()
        self._get_content_thread.terminate()
        self._get_content_thread.wait()
        self.ui.items_list.clear()
        self._get_content_thread.start()

    def _get_content(self):
        self.req_params.version = self.ui.version_line.text()
        self.req_params.loader = self.get_cur_loader()
        self.req_params.loaders = self.get_cur_loader()
        self.req_params.search = self.ui.search_line.text()
        self.mods = self.catalog.search(self.req_params)
        self.mod_thread_pool.setMaxThreadCount(len(self.mods))

    def update_content(self):
        for mod in self.mods:
            item = ModItem(mod, self.mod_thread_pool)
            self.ui.items_list.addItem(item)

    def open_mod_info(self):
        mod = self.mods[self.ui.items_list.currentIndex().row()]
        info = ModInfo(get_catalog(mod.catalog_id).get_mod(mod), self)
        info.exec()

    def setup_filters(self):
        self.clear_filters()
        for i in self.catalog.get_loaders():
            item = QRadioButton(i.get_name())
            if not self.loader_items:
                item.setChecked(True)
            self.ui.modloader_grid.addWidget(item)
            self.loader_items.update({item: i})
        self.ui.modloader_frame.setVisible(bool(self.loader_items))

    def clear_filters(self):
        [item.deleteLater() for item in self.loader_items]
        self.loader_items.clear()

    def get_cur_loader(self):
        for i in self.loader_items:
            if i.isChecked():
                return self.loader_items[i].value
