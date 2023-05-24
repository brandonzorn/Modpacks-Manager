import sqlite3
from threading import Lock

import platformdirs

from modrinthmanager.consts import APP_NAME
from modrinthmanager.items import Mod
from modrinthmanager.utils.decorators import with_lock_thread, singleton


@singleton
class Database:
    lock = Lock()

    def __init__(self):
        self.__con = sqlite3.connect(f'{platformdirs.user_data_dir()}/{APP_NAME}/data.db', check_same_thread=False)
        self.__cur = self.__con.cursor()
        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS mods (id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL,
        content_id STRING NOT NULL, catalog_id INTEGER NOT NULL, name STRING, description TEXT);
            """)
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS modpacks
        (mod_id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL, modpack STRING NOT NULL)
            """)
        self.__con.commit()

    @with_lock_thread(lock)
    def add_mod(self, mod: Mod):
        self.__cur.execute("INSERT INTO mods VALUES(?, ?, ?, ?, ?);",
                           (mod.id, mod.mod_id, mod.catalog_id, mod.name, mod.description))
        self.__con.commit()

    @with_lock_thread(lock)
    def add_mods(self, mods: list[Mod]):
        for mod in mods:
            self.__cur.execute("INSERT INTO mods VALUES(?, ?, ?, ?, ?);",
                               (mod.id, mod.mod_id, mod.catalog_id, mod.name, mod.description))
        self.__con.commit()

    def get_mod(self, mod_id: str):
        x = self.__cur.execute(f"SELECT * FROM mods WHERE id = '{mod_id}'").fetchone()
        content_id = x[1]
        catalog_id = x[2]
        name = x[3]
        mod = Mod(content_id, catalog_id, name)
        mod.description = x[4]
        return mod

    @with_lock_thread(lock)
    def add_mod_modpack(self, mod: Mod, modpack="Test"):
        self.__cur.execute(f"INSERT INTO modpacks VALUES(?, ?);", (mod.id, modpack))
        self.__con.commit()

    @with_lock_thread(lock)
    def get_mods_modpack(self, modpack="Test") -> list[Mod]:
        a = self.__cur.execute(f"SELECT mod_id FROM modpacks;").fetchall()
        mods = []
        for i in a[::-1]:
            mods.append(self.get_mod(i[0]))
        return mods

   #  @with_lock_thread(lock)
   #  def get_manga_library_list(self, mod: Mod) -> LibList:
   #      a = self.__cur.execute(f"SELECT list FROM modpacks WHERE manga_id = '{mod.id}';").fetchone()
   #      return LibList(a[0])

    @with_lock_thread(lock)
    def check_mod_modpack(self, mod: Mod) -> bool:
        a = self.__cur.execute(f"SELECT modpack FROM modpacks WHERE mod_id = '{mod.id}';").fetchone()
        return bool(a)

    @with_lock_thread(lock)
    def rem_mod_modpack(self, mod: Mod):
        self.__cur.execute(f"DELETE FROM modpacks WHERE mod_id = '{mod.id}';")
        self.__con.commit()
