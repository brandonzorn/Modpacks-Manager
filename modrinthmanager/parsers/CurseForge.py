import requests

from modrinthmanager.consts.items import CurseforgeItems
from modrinthmanager.consts.urls import URL_CURSEFORGE_API, CURSEFORGE_HEADERS
from modrinthmanager.items.mod_items import Mod, ModVersion
from modrinthmanager.items.other_items import RequestForm
from modrinthmanager.parsers.Parser import Parser


class CurseForge(Parser):
    CATALOG_NAME = "CurseForge"
    CATALOG_ID = 1
    ITEMS = CurseforgeItems

    @staticmethod
    def search(req_form: RequestForm):
        params = {'gameId': '432', 'classId': '6', 'searchFilter': req_form.search,
                  'sortField': '1', 'sortOrder': "desc",
                  'modLoaderType': req_form.loader, 'gameVersion': req_form.version, 'index': 50 * (req_form.page - 1)}
        response = requests.get(f'{URL_CURSEFORGE_API}/v1/mods/search', params=params, headers=CURSEFORGE_HEADERS)
        mods = []
        if response.status_code == 200 and response.json():
            for mod_data in response.json()['data']:
                mod = Mod(mod_data['id'], CurseForge.CATALOG_ID, mod_data['name'])
                mod.description = mod_data['summary']
                mod.icon_url = mod_data['logo']['thumbnailUrl']
                mods.append(mod)
        return mods

    @staticmethod
    def _match_modloader(modloader: str):
        modloaders = {"Any": 0, "Forge": 1, "Cauldron": 2, "LiteLoader": 3, "Fabric": 4, "Quilt": 5}
        return modloaders[modloader.capitalize()]

    @staticmethod
    def get_versions(mod: Mod, modpack=None):
        params = {}
        if modpack:
            params = {"modLoaderType": f'{CurseForge._match_modloader(modpack.modloader)}',
                      "gameVersion": f"{modpack.version}"}
        response = requests.get(f'{URL_CURSEFORGE_API}/v1/mods/{mod.mod_id}/files',
                                params=params, headers=CURSEFORGE_HEADERS)
        versions = []
        if response.status_code == 200 and response.json():
            for version_data in response.json()['data']:
                version = ModVersion(version_data['id'], version_data['displayName'], None, None,
                                     version_data['downloadUrl'])
                versions.append(version)
        return versions

    @staticmethod
    def get_version(version: ModVersion):
        response = requests.get(version.version_url, headers=CURSEFORGE_HEADERS)
        if response.status_code == 200:
            return response.content

    @staticmethod
    def get_preview(mod: Mod):
        response = requests.get(mod.icon_url, headers=CURSEFORGE_HEADERS)
        if response.status_code == 200:
            return response.content
