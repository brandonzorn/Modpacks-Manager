import os.path
from typing import Callable

import platformdirs
from PySide6.QtCore import QThreadPool, QRunnable, Slot, Signal, QObject
from PySide6.QtGui import QPixmap

from modrinthmanager.consts.app import APP_NAME
from modrinthmanager.consts.files import Styles
from modrinthmanager.items.mod_items import Mod, ModVersion
from modrinthmanager.parsers.Modrinth import Modrinth


def save_version(mod: Mod, version: ModVersion, content):
    path = f'Downloads/{mod.get_name()}'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f"{path}/{mod.get_name()} {version.version}.jar", 'wb') as ver:
        ver.write(content)


def get_file(path, file_name):
    path = f'{platformdirs.user_data_dir()}/{APP_NAME}/{path}/{file_name}'
    return path


def check_file_exists(path, file_name):
    return os.path.exists(f'{platformdirs.user_data_dir()}/{APP_NAME}/{path}/{file_name}')


def save_file(path, file_name, file_content):
    path = f'{platformdirs.user_data_dir()}/{APP_NAME}/{path}'
    if not os.path.exists(f'{path}/{file_name}'):
        os.makedirs(path, exist_ok=True)
        if file_content:
            if isinstance(file_content, str):
                file_content = bytes(file_content, encoding='utf8')
            with open(f'{path}/{file_name}', 'wb') as f:
                f.write(file_content)


def get_mod_preview(mod: Mod) -> QPixmap:
    path = f'images/{"Modrinth"}/mods/{mod.mod_id}'
    if not check_file_exists(path, 'preview.jpg'):
        save_file(path, 'preview.jpg', Modrinth.get_preview(mod))
    return QPixmap(get_file(path, 'preview.jpg'))


def get_ui_style(style: str):
    dark = Styles.Dark
    light = Styles.Light
    themes = {"Dark": dark, "Light": light}
    return themes[style]


class Signals(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()


class Worker(QRunnable):
    def __init__(self, target: Callable, args=(), kwargs=None, *, callback=None, locker=None):
        super(Worker, self).__init__()
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._locker = locker
        self.signals = Signals()
        if callback:
            self.signals.finished.connect(callback)

    @Slot()
    def run(self):
        if self._locker:
            while not self._locker.tryLock():
                pass
            self._target(*self._args, **self._kwargs)
            self._locker.unlock()
        else:
            self._target(*self._args, **self._kwargs)
        self.signals.finished.emit()

    def start(self, pool=None):
        if pool is None:
            pool = QThreadPool.globalInstance()
        if pool.activeThreadCount() == pool.maxThreadCount():
            return
        pool.start(self)
