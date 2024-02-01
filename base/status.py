from collections import defaultdict

from base import Monitor, monitor
from base.attribute import Attribute
from base.target import Target


class Status:
    def __init__(self, attribute: Attribute, target: Target,
                 skills: list, buffs: list, damages: dict, events: list, total_frame: int, verbose=False):
        if verbose:
            self.record = self.record_verbose

        self.attribute = attribute
        self.target = target

        self.gcd_group = Monitor(0)
        self.casting = False

        self.intervals = Monitor(0)
        self.ticks = Monitor(-1)

        self.skills = {}
        self.cds = Monitor(0)
        self.energies = Monitor(0)

        for skill in skills:
            skill = skill(self)
            self.skills[skill.name] = skill
            self.energies[skill.name] = skill.energy

        self.buffs = {}
        self.durations = Monitor(0)
        self.stacks = Monitor(0)
        self.gains = {
            "": defaultdict(monitor),
            "attack_power": defaultdict(monitor),
            "critical_strike": defaultdict(monitor),
            "critical_power": defaultdict(monitor),
            "overcome": defaultdict(monitor),
            "strain": defaultdict(monitor),
            "damage_addition": defaultdict(monitor)
        }

        for buff in buffs:
            buff = buff(self)
            self.buffs[buff.name] = buff
            self.stacks[buff.name] = 0

        self.total_frame = total_frame
        self.current_frame = 0
        self.damages = damages
        self.events = events

    def timer(self, gap=1):
        self.current_frame += gap

        for gcd_index in self.gcd_group - gap:
            self.gcd_group.pop(gcd_index)

        for buff in self.durations - gap:
            self.buffs[buff].clear()

        for skill in self.intervals - gap:
            self.skills[skill].hit()

        reduction_gap = gap * (1 + self.attribute.cd_reduction)
        for skill in self.cds - reduction_gap:
            self.skills[skill].recharge()

    def set_dice(self, seed):
        for skill in self.skills.values():
            skill.dice.seed(seed)
        for buff in self.buffs.values():
            buff.dice.seed(seed)

    def record_verbose(self, params):
        self.damages[params] += 1
        self.events.append((self.current_frame, params))

    def record(self, params):
        self.damages[params] += 1
