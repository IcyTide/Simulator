from dataclasses import dataclass

from base import Timeline
from base.attribute import Attribute


@dataclass
class Agent:
    name: str

    timeline: Timeline

    casting: bool
    channeling: bool

    mana: int
    energy: int
    power: int

    talents: dict
    recipes: dict

    physical_shield_ignore_gain: int = 0
    magical_shield_ignore_gain: int = 0

    def update(self, gap):
        self.casting -= gap
        self.channeling -= gap


class Target:
    name: str

