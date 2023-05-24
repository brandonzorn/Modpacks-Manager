from typing import Any


class SortItem:
    def __init__(self, value: Any, name: str):
        self.value = value
        self.name = name

    def get_name(self):
        return self.name


class Loader(SortItem):
    def __init__(self, value: Any, name: str):
        super().__init__(value, name)


class Order:
    def __init__(self, value: Any, name: str):
        super().__init__(value, name)
