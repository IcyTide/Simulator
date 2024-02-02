import random
from dataclasses import dataclass

from base.status import Status, Gains


@dataclass
class Buff:
    status: Status
    name: str = None
    activate: bool = True

    level: int = 1

    duration: int = 3600 * 16

    stack_add: int = 1
    stack_remove: int = 1
    stack_max: int = 1

    def __post_init__(self):
        self.add_effect = []
        self.remove_effect = []
        self.clear_effect = []

        self.sub_buffs = []
        self.dice = random.Random(82)

    @property
    def roll(self):
        return random.random()

    def set_duration(self):
        # self.status.durations[self.name] = min(self.duration_max, self.status.durations[self.name] + self.duration)
        self.status.durations[self.name] = self.duration

    def add(self):
        self.status.stacks[self.name] += 1
        for effect in self.add_effect:
            effect(self)

    def remove(self):
        self.status.stacks[self.name] -= 1
        for effect in self.remove_effect:
            effect(self)

        if not self.status.stacks[self.name]:
            self.status.durations.pop(self.name)

    def trigger(self, level=1, stack=None):
        if not level:
            return
        self.level = level

        if stack is None:
            stack = self.stack_add

        self.set_duration()

        stack = min(stack, self.stack_max - self.status.stacks[self.name])

        for _ in range(stack):
            self.add()

        for buff in self.sub_buffs:
            self.status.buffs[buff].trigger()

    def consume(self, stack=None):
        if stack is None:
            stack = self.stack_remove

        stack = min(stack, self.status.stacks[self.name])

        for _ in range(stack):
            self.remove()

        for buff in self.sub_buffs:
            self.status.buffs[buff].consume()

    def clear(self):
        for _ in range(self.status.stacks[self.name]):
            self.remove()
        for effect in self.clear_effect:
            effect(self)
        for buff in self.sub_buffs:
            self.status.buffs[buff].clear()


class TriggerBuff(Buff):
    probability: float = 1

    def trigger(self, level=1, stack=None):
        if self.roll < self.probability:
            super().trigger(level, stack)


class ExtendBuff(Buff):
    duration_add: int = 0
    duration_max: int = 3600 * 16

    def set_duration(self):
        if duration := self.status.durations[self.name]:
            self.status.durations[self.name] = min(self.duration_max, duration + self.duration_add)
        elif self.duration:
            self.status.durations[self.name] = self.duration
        else:
            self.status.durations[self.name] += self.duration_add

    def extend(self):   # only extend if exists
        if duration := self.status.durations[self.name]:
            self.status.durations[self.name] = min(self.duration_max, duration + self.duration_add)


class DotBuff(Buff):
    def set_duration(self):
        skill = self.status.skills[self.name]
        if interval := self.status.intervals[self.name]:
            self.status.durations[self.name] = interval - skill.interval + skill.duration
        else:
            self.status.durations[self.name] = skill.duration


class PlacementBuff(Buff):
    def set_duration(self):
        self.status.durations[self.name] = self.status.skills[self.name].duration


class GainBuff(Buff):

    def __post_init__(self):
        super().__post_init__()
        self.gain_effect: list = []
        self.revoke_effect: list = []
        self.gain_skills = [""]
        self.gain_attribute = ""

    def add(self):
        super().add()
        for gain_skill in self.gain_skills:
            self.status.gains[self.gain_attribute][gain_skill][self.name] = (self.level, self.status.stacks[self.name])

    def remove(self):
        super().remove()
        if stack := self.status.stacks[self.name]:
            for gain_skill in self.gain_skills:
                self.status.gains[self.gain_attribute][gain_skill][self.name] = (self.level, stack)
        else:
            for gain_skill in self.gain_skills:
                self.status.gains[self.gain_attribute][gain_skill].pop(self.name)

    def gain(self, level, stack):
        for effect in self.gain_effect:
            effect(self, level, stack)

    def revoke(self, level, stack):
        for effect in self.revoke_effect:
            effect(self, level, stack)


class Energy(Buff):
    def __post_init__(self):
        super().__post_init__()
        self.increase_effect = []
        self.decrease_effect = []

    def increase(self, stack):
        self.set_duration()
        self.status.stacks[self.name] = min(self.status.stacks[self.name] + stack, self.stack_max)
        for effect in self.increase_effect:
            effect(self)

    def decrease(self, stack):
        self.set_duration()
        self.status.stacks[self.name] = max(self.status.stacks[self.name] - stack, 0)
        for effect in self.decrease_effect:
            effect(self)


class Pet(Buff):
    snapshot_attrs = ["attack_power", "critical_power", "overcome", "strain"]
    gains = []

    def add(self):
        super().add()
        self.gains = []
        for attr in self.snapshot_attrs:
            for buff, (level, stack) in (self.status.gains[attr][""] + self.status.gains[attr][self.name]).items():
                self.gains.append(Gains(buff, level, stack))


class CDBuff(Buff):
    pass


class CountBuff(Buff):
    pass
