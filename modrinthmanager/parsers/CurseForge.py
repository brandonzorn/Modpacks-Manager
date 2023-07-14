from modrinthmanager.consts.items import CurseforgeItems
from modrinthmanager.consts.urls import URL_CURSEFORGE_API, CURSEFORGE_HEADERS
from modrinthmanager.items.mod_items import Mod, ModVersion
from modrinthmanager.items.other_items import RequestForm
from modrinthmanager.parsers.Parser import Parser
from modrinthmanager.utils.net import get_html


class CurseForge(Parser):
    CATALOG_NAME = "CurseForge"
    CATALOG_ID = 1
    ITEMS = CurseforgeItems
    _HEADERS = CURSEFORGE_HEADERS

    @classmethod
    def get_mod(cls, mod: Mod):
        url = f'{URL_CURSEFORGE_API}/v1/mods/{mod.mod_id}'
        response = get_html(url, headers=cls._HEADERS, content_type='json')
        if response:
            mod_data = response['data']
            mod.icon_url = mod_data['logo']['thumbnailUrl']
        return mod

    @classmethod
    def search(cls, req_form: RequestForm):
        params = {'gameId': '432', 'classId': '6', 'searchFilter': req_form.search,
                  'sortField': '1', 'sortOrder': "desc",
                  'modLoaderType': req_form.loader, 'gameVersion': req_form.version, 'index': 50 * (req_form.page - 1)}
        url = f'{URL_CURSEFORGE_API}/v1/mods/search'
        response = get_html(url, params=params, headers=CURSEFORGE_HEADERS, content_type='json')
        mods = []
        if response:
            for mod_data in response['data']:
                mod = Mod(mod_data['id'], CurseForge.CATALOG_ID, mod_data['name'])
                mod.description = mod_data['summary']
                mod.icon_url = mod_data['logo']['thumbnailUrl']
                mods.append(mod)
        return mods

    @staticmethod
    def _match_modloader(modloader: str):
        modloaders = {"Any": 0, "Forge": 1, "Cauldron": 2, "LiteLoader": 3, "Fabric": 4, "Quilt": 5}
        return modloaders[modloader.capitalize()]

    @classmethod
    def get_versions(cls, mod: Mod, modpack=None):
        params = {}
        if modpack:
            params = {"modLoaderType": f'{CurseForge._match_modloader(modpack.modloader)}',
                      "gameVersion": f"{modpack.version}"}
        url = f'{URL_CURSEFORGE_API}/v1/mods/{mod.mod_id}/files'
        response = get_html(url, params=params, headers=cls._HEADERS, content_type='json')
        versions = []
        if response:
            for version_data in response['data']:
                version = ModVersion(version_data['id'], version_data['displayName'], None, None,
                                     version_data['downloadUrl'])
                versions.append(version)
        return versions

    @classmethod
    def get_version(cls, version: ModVersion):
        url = version.version_url
        response = get_html(url, headers=cls._HEADERS, content_type='content')
        if response:
            return response

    @classmethod
    def get_preview(cls, mod: Mod):
        url = mod.icon_url
        response = get_html(url, headers=cls._HEADERS, content_type='content')
        if response:
            return response
