import random
from dataclasses import dataclass

from base.status import Status


@dataclass
class Buff:
    status: Status
    name: str = None
    activate: bool = True

    is_dot: bool = False

    level: int = 1

    duration: int = 3600 * 16
    duration_add: int = 0
    duration_max: int = 3600 * 16

    stack_add: int = 1
    stack_remove: int = 1
    stack_max: int = 1

    def __post_init__(self):
        self.add_effect = []
        self.remove_effect = []

    @property
    def roll(self):
        return random.random()

    def set_duration(self):
        # self.status.durations[self.name] = min(self.duration_max, self.status.durations[self.name] + self.duration)
        self.status.durations[self.name] = self.duration_max

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

    def extend(self):
        if duration := self.status.durations[self.name]:
            self.status.durations[self.name] = max(self.duration_max, duration + self.duration_add)

    def trigger(self, level=1, stack=None):
        self.level = level

        if stack is None:
            stack = self.stack_add

        self.set_duration()

        stack = min(stack, self.stack_max - self.status.stacks[self.name])

        for _ in range(stack):
            self.add()

    def consume(self, stack=None):
        if stack is None:
            stack = self.stack_remove

        stack = min(stack, self.status.stacks[self.name])

        for _ in range(stack):
            self.remove()

    def clear(self):
        for _ in range(self.status.stacks[self.name]):
            self.remove()


class TriggerBuff(Buff):
    probability: float = 1

    def trigger(self, level=1, stack=None):
        if self.roll < self.probability:
            super().trigger(level, stack)


class ExtendBuff(Buff):
    def set_duration(self):
        self.status.durations[self.name] += self.duration_add


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
    gain_effect: list = []
    revoke_effect: list = []

    def add(self):
        super().add()
        self.status.gains[self.name] = (self.level, self.status.stacks[self.name])

    def remove(self):
        super().remove()
        if stack := self.status.stacks[self.name]:
            self.status.gains[self.name] = (self.level, stack)
        else:
            self.status.gains.pop(self.name)

    def gain(self, level, stack):
        for effect in self.gain_effect:
            effect(self, level, stack)

    def revoke(self, level, stack):
        for effect in self.revoke_effect:
            effect(self, level, stack)


class Energy(Buff):
    increase_effect: list = []
    decrease_effect: list = []

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
