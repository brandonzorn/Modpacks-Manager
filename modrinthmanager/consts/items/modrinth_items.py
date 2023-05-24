from modrinthmanager.consts.items.parser_items import ParserItems


class ModrinthItems(ParserItems):
    LOADERS = [
        {'value': None, 'name': 'Any'},
        {'value': 'forge', 'name': 'Forge'},
        {'value': 'fabric', 'name': 'Fabric'},
        {'value': 'quilt', 'name': 'Quilt'}
    ]
