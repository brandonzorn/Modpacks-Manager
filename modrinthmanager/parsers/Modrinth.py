from modrinthmanager.consts.items import ModrinthItems
from modrinthmanager.consts.urls import URL_MODRINTH_API, MODRINTH_HEADERS
from modrinthmanager.items.mod_items import Mod, ModVersion
from modrinthmanager.items.other_items import RequestForm
from modrinthmanager.parsers.Parser import Parser
from modrinthmanager.utils.net import get_html


class Modrinth(Parser):
    CATALOG_NAME = "Modrinth"
    CATALOG_ID = 0
    ITEMS = ModrinthItems
    _HEADERS = MODRINTH_HEADERS

    @classmethod
    def get_mod(cls, mod: Mod):
        url = f'{URL_MODRINTH_API}/project/{mod.mod_id}'
        response = get_html(url, headers=cls._HEADERS, content_type='json')
        if response:
            mod.icon_url = response.get('icon_url')
        return mod

    @classmethod
    def search(cls, req_form: RequestForm):
        facets = []
        if req_form.version:
            facets.append(f'["versions:{req_form.version}"]')
        if req_form.loader:
            facets.append(f'["categories:{req_form.loader}"]')
        params = {"facets": f'[{", ".join(facets)}]' if facets else None,
                  'query': req_form.search, 'offset': (req_form.page - 1) * 10}
        url = f'{URL_MODRINTH_API}/search'
        response = get_html(url, params=params, headers=cls._HEADERS, content_type='json')
        mods = []
        if response:
            for mod_data in response['hits']:
                mod = Mod(mod_data['project_id'], Modrinth.CATALOG_ID, mod_data['title'])
                mod.description = mod_data['description']
                mod.icon_url = mod_data['icon_url']
                mods.append(mod)
        return mods

    @classmethod
    def get_versions(cls, mod: Mod, modpack=None):
        params = {}
        if modpack:
            params = {"loaders": f'["{modpack.modloader}"]', "game_versions": f'["{modpack.version}"]'}
        url = f'{URL_MODRINTH_API}/project/{mod.mod_id}/version'
        response = get_html(url, params=params, headers=cls._HEADERS, content_type='json')
        versions = []
        if response:
            for version_data in response:
                version = ModVersion(None, version_data["name"], version_data["version_number"],
                                     version_data["loaders"][0], version_data['files'][0]["url"])
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
