import requests

from modrinthmanager.items.mod_items import Mod, ModVersion

URL_MODRINTH_API = "https://api.modrinth.com/v2"
MODRINTH_HEADERS = {"User-Agent": "ModrinthManager"}


class Modrinth:
    @staticmethod
    def search(params: dict):
        response = requests.get(f'{URL_MODRINTH_API}/search', params=params, headers=MODRINTH_HEADERS)
        mods = []
        if response.status_code == 200 and response.json():
            for mod_data in response.json()['hits']:
                mod = Mod(mod_data['project_id'], mod_data['title'])
                mod.description = mod_data['description']
                mod.icon_url = mod_data['icon_url']
                mods.append(mod)
        return mods

    @staticmethod
    def get_versions(mod: Mod):
        params = {"loaders": '["fabric"]', "game_versions": '["1.19.4"]'}
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
