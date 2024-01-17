import random
from dataclasses import dataclass

from base.status import Status


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

    dice: random.Random = None

    def __post_init__(self):
        self.add_effect = []
        self.remove_effect = []

        self.dice = random.Random(82)

    @property
    def roll(self):
        return random.random()

    def set_duration(self):
        # self.status.durations[self.name] = min(self.duration_max, self.status.durations[self.name] + self.duration)
        self.status.durations[self.name] = self.duration

    def add(self, stack: int):
        stack = min(stack, self.stack_max - self.status.stacks[self.name])
        if not stack:
            return
        
        self.status.stacks[self.name] += stack
        for _ in range(stack):
            for effect in self.add_effect:
                effect(self)

    def remove(self, stack: int):
        stack = min(stack, self.status.stacks[self.name])
        if not stack:
            return
        
        self.status.stacks[self.name] -= stack
        for _ in range(stack):
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

        self.add(stack)

    def consume(self, stack=None):
        if stack is None:
            stack = self.stack_remove

        self.remove(stack)

    def clear(self):
        self.remove(self.status.stacks[self.name])


class TriggerBuff(Buff):
    probability: float = 1

    def trigger(self, level=1, stack=None):
        if self.roll < self.probability:
            super().trigger(level, stack)


class ExtendBuff(Buff):
    duration_add: int = 0
    duration_max: int = 3600 * 16

    def extend(self):
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
        self.gain_group = [""]

    def add(self, stack):
        super().add(stack)
        for gain_index in self.gain_group:
            self.status.gains[gain_index][self.name] = (self.level, self.status.stacks[self.name])

    def remove(self, stack):
        super().remove(stack)
        if stack := self.status.stacks[self.name]:
            for gain_index in self.gain_group:
                self.status.gains[gain_index][self.name] = (self.level, stack)
        else:
            for gain_index in self.gain_group:
                self.status.gains[gain_index].pop(self.name)

    def gain(self, level, stack):
        for effect in self.gain_effect:
            effect(self, level, stack)

    def revoke(self, level, stack):
        for effect in self.revoke_effect:
            effect(self, level, stack)


class SnapshotBuff(GainBuff):
    def add(self, stack):
        super().add(stack)
        for gain_index in self.gain_group:
            self.status.snapshots[gain_index][self.name] = (self.level, self.status.stacks[self.name])

    def remove(self, stack):
        super().remove(stack)
        if stack := self.status.stacks[self.name]:
            for gain_index in self.gain_group:
                self.status.snapshots[gain_index][self.name] = (self.level, stack)
        else:
            for gain_index in self.gain_group:
                self.status.snapshots[gain_index].pop(self.name)


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


class CDBuff(Buff):
    pass


class CountBuff(Buff):
    pass
