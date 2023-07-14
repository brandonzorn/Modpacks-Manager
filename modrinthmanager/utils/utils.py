import os.path

import platformdirs
from PySide6.QtGui import QPixmap

from modrinthmanager.consts.app import APP_NAME
from modrinthmanager.consts.files import Styles
from modrinthmanager.items.mod_items import Mod, ModVersion, Modpack
from modrinthmanager.utils.catalog_manager import get_catalog


def save_version(modpack: Modpack, version: ModVersion, content):
    path = f'Downloads/Test'
    if not os.path.exists(path):
        os.makedirs(path)
    filename = f"{modpack.name}"
    if version.version:
        filename += f" {version.version}"
    with open(f"{path}/{filename}.jar", 'wb') as ver:
        ver.write(content)


def check_version_exists(modpack: Modpack, version: ModVersion):
    path = f'Downloads/Test'
    return os.path.exists(f"{path}/{modpack.name} {version.version}.jar")


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
        save_file(path, 'preview.jpg', get_catalog(mod.catalog_id).get_preview(mod))
    return QPixmap(get_file(path, 'preview.jpg'))


def get_ui_style(style: str):
    dark = Styles.Dark
    light = Styles.Light
    themes = {"Dark": dark, "Light": light}
    return themes[style]
