from typing import Dict

from tools.regex import camel_to_snake


class BaseSetting:
    _aliases: Dict[str, str] = {}

    def __getattr__(self, item):
        if item in self._aliases:
            item = self._aliases[item]
        else:
            item = camel_to_snake(item)
        if item in dir(self):
            return getattr(self, item)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def __setattr__(self, key, value):
        key = camel_to_snake(key)
        super().__setattr__(key, value)