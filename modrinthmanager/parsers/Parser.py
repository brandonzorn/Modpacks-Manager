from modrinthmanager.items import Loader, Order


class Parser:
    CATALOG_NAME = None
    CATALOG_ID = None
    ITEMS = None

    @classmethod
    def get_loaders(cls) -> list[Loader]:
        loaders = [Loader(i['value'], i['name']) for i in cls.ITEMS.LOADERS]
        return loaders

    @classmethod
    def get_orders(cls) -> list[Order]:
        orders = [Order(i['value'], i['name']) for i in cls.ITEMS.ORDERS]
        return orders
