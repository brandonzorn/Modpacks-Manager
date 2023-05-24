from modrinthmanager.parsers import CurseForge, Modrinth

CATALOGS = {0: Modrinth, 1: CurseForge}
USER_CATALOGS = [Modrinth, CurseForge]


def get_catalog(catalog_id):
    return CATALOGS.get(catalog_id)
