from modrinthmanager.consts.items.parser_items import ParserItems


class CurseforgeItems(ParserItems):
    ORDERS = [
        {'value': 1, 'name': 'Featured'},
        {'value': 2, 'name': 'Popularity'},
        {'value': 3, 'name': 'LastUpdated'},
        {'value': 4, 'name': 'Name'},
        {'value': 5, 'name': 'Author'},
        {'value': 6, 'name': 'TotalDownloads'},
        {'value': 7, 'name': 'Category'}
    ]

    LOADERS = [
        {'value': 0, 'name': 'Any'},
        {'value': 1, 'name': 'Forge'},
        {'value': 2, 'name': 'Cauldron'},
        {'value': 3, 'name': 'LiteLoader'},
        {'value': 4, 'name': 'Fabric'},
        {'value': 5, 'name': 'Quilt'}
    ]
