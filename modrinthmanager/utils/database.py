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
        (mod_id STRING PRIMARY KEY ON CONFLICT REPLACE NOT NULL, modpack INTEGER NOT NULL)
            """)
        self.__con.commit()

    @with_lock_thread(lock)
    def add_mod(self, mod: Mod):
        self.__cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?);",
                           (mod.id, mod.mod_id, 0, mod.name, mod.description))
        self.__con.commit()

    @with_lock_thread(lock)
    def add_mangas(self, mods: list[Mod]):
        for mod in mods:
            self.__cur.execute("INSERT INTO manga VALUES(?, ?, ?, ?, ?);",
                               (mod.id, mod.mod_id, 0, mod.name, mod.description))
        self.__con.commit()

    def get_manga(self, manga_id: str):
        x = self.__cur.execute(f"SELECT * FROM mods WHERE id = '{manga_id}'").fetchone()
        content_id = x[1]
        catalog_id = x[2]
        name = x[3]
        mod = Mod(content_id, name)
        mod.description = x[5]
        return mod

    @with_lock_thread(lock)
    def add_manga_library(self, mod: Mod, lib_list):
        self.__cur.execute(f"INSERT INTO library VALUES(?, ?);", (mod.id, lib_list.value))
        self.__con.commit()

    # @with_lock_thread(lock)
    # def get_manga_library(self, lib_list) -> list[Mod]:
    #     a = self.__cur.execute(f"SELECT manga_id FROM library WHERE list = '{lib_list.value}';").fetchall()
    #     mangas = []
    #     for i in a[::-1]:
    #         mangas.append(self.get_manga(i[0]))
    #     return mangas

   #  @with_lock_thread(lock)
   #  def get_manga_library_list(self, mod: Mod) -> LibList:
   #      a = self.__cur.execute(f"SELECT list FROM library WHERE manga_id = '{mod.id}';").fetchone()
   #      return LibList(a[0])

    @with_lock_thread(lock)
    def check_manga_library(self, mod: Mod) -> bool:
        a = self.__cur.execute(f"SELECT list FROM library WHERE manga_id = '{mod.id}';").fetchone()
        return bool(a)

    @with_lock_thread(lock)
    def rem_manga_library(self, mod: Mod):
        self.__cur.execute(f"DELETE FROM library WHERE manga_id = '{mod.id}';")
        self.__con.commit()
