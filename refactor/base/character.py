from dataclasses import dataclass
from typing import List

from base.attribute import Attribute


@dataclass
class Self:
    name: str

    attribute: Attribute

    casting: bool
    channeling: bool

    mana: int
    energy: int
    power: int

    buffs: dict
    talents: dict
    recipes: dict


class Target:
    name: str

    attribute: Attribute

