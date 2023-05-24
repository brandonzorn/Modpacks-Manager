from enum import Enum, unique


class Mod:
    def __init__(self, mod_id, catalog_id: int, name):
        self.id = f'|{catalog_id}|_|{mod_id}|'
        self.mod_id = mod_id
        self.catalog_id = catalog_id
        self.name = name
        self.description = None
        self.icon_url = None

    def get_name(self):
        return self.name


class ModVersion:
    def __init__(self, version_id, name, version, mod_loader: str, version_url):
        self.version_id = version_id
        self.name = name
        self.version = version
        self.mod_loader = mod_loader
        self.version_url = version_url

    def get_name(self):
        return f'{self.name}'


class Modpack:
    def __init__(self, name, version, modloader, mods: list[Mod]):
        self.name = name
        self.version = version
        self.modloader = modloader
        self.mods = mods

    def get_name(self):
        return f"{self.name}-{self.modloader} {self.version}"


@unique
class ModLoaders(Enum):
    Any = 0
    Forge = 1
    Fabric = 4
    Quilt = 5
