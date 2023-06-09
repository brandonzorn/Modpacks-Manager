import requests

from modrinthmanager.consts.items import ModrinthItems
from modrinthmanager.consts.urls import URL_MODRINTH_API, MODRINTH_HEADERS
from modrinthmanager.items.mod_items import Mod, ModVersion
from modrinthmanager.items.other_items import RequestForm
from modrinthmanager.parsers.Parser import Parser


class Modrinth(Parser):
    CATALOG_NAME = "Modrinth"
    CATALOG_ID = 0
    ITEMS = ModrinthItems

    @staticmethod
    def get_mod(mod: Mod):
        response = requests.get(f'{URL_MODRINTH_API}/project/{mod.mod_id}', headers=MODRINTH_HEADERS)
        if response.status_code == 200 and response.json():
            mod_data = response.json()
            mod.icon_url = mod_data.get('icon_url')
        return mod

    @staticmethod
    def search(req_form: RequestForm):
        facets = []
        if req_form.version:
            facets.append(f'["versions:{req_form.version}"]')
        if req_form.loader:
            facets.append(f'["categories:{req_form.loader}"]')
        params = {"facets": f'[{", ".join(facets)}]' if facets else None,
                  'query': req_form.search, 'offset': (req_form.page - 1) * 10}
        response = requests.get(f'{URL_MODRINTH_API}/search', params=params, headers=MODRINTH_HEADERS)
        mods = []
        if response.status_code == 200 and response.json():
            for mod_data in response.json()['hits']:
                mod = Mod(mod_data['project_id'], Modrinth.CATALOG_ID, mod_data['title'])
                mod.description = mod_data['description']
                mod.icon_url = mod_data['icon_url']
                mods.append(mod)
        return mods

    @staticmethod
    def get_versions(mod: Mod, modpack=None):
        params = {}
        if modpack:
            params = {"loaders": f'["{modpack.modloader}"]', "game_versions": f'["{modpack.version}"]'}
        response = requests.get(f'{URL_MODRINTH_API}/project/{mod.mod_id}/version',
                                params=params, headers=MODRINTH_HEADERS)
        versions = []
        if response.status_code == 200 and response.json():
            for version_data in response.json():
                version = ModVersion(None, version_data["name"], version_data["version_number"],
                                     version_data["loaders"][0], version_data['files'][0]["url"])
                versions.append(version)
        return versions

    @staticmethod
    def get_version(version: ModVersion):
        response = requests.get(version.version_url, headers=MODRINTH_HEADERS)
        if response.status_code == 200:
            return response.content

    @staticmethod
    def get_preview(mod: Mod):
        response = requests.get(mod.icon_url, headers=MODRINTH_HEADERS)
        if response.status_code == 200:
            return response.content
