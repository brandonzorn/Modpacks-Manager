from modrinthmanager.items import Mod
from modrinthmanager.utils.database import Database


class LocalLib:
    catalog_name = 'LocalLib'

    def __init__(self):
        self.db: Database = Database()

    def search_mods(self) -> list[Mod]:
        mods = self.db.get_mods_modpack()
        return mods
