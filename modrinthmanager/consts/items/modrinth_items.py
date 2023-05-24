from modrinthmanager.consts.items.parser_items import ParserItems


class ModrinthItems(ParserItems):
    LOADERS = [
        {'value': 'forge', 'name': 'Forge'},
        {'value': 'fabric', 'name': 'Cauldron'},
        {'value': 'quilt', 'name': 'LiteLoader'}
    ]
