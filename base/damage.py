from dataclasses import dataclass

from base.skill import Skill


@dataclass
class Damage:
    skill: Skill

