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

    def _add(self):
        self.status.stacks[self.name] += 1
        for effect in self.add_effect:
            effect(self)

    def _remove(self):
        self.status.stacks[self.name] -= 1
        for effect in self.remove_effect:
            effect(self)

        if not self.status.stacks[self.name]:
            self.status.durations.pop(self.name)

    def cast(self, level=1):
        self.level = level

        self.pre_cast()

    def pre_cast(self):
        stack = min(self.stack_max - self.status.stacks[self.name], self.stack_add)

        # self.status.durations[self.name] = min(self.duration_max, self.status.durations[self.name] + self.duration)
        self.status.durations[self.name] = min(self.duration_max, self.duration)

        for _ in range(stack):
            self._add()

    def consume(self, stack=None):
        if stack is None:
            stack = self.stack_remove

        stack = min(stack, self.status.stacks[self.name])

        for _ in range(stack):
            self._remove()

    def post_cast(self):
        for _ in range(self.status.stacks[self.name]):
            self._remove()


class TriggerBuff(Buff):
    probability: float = 1

    def cast(self, level=1):
        if self.roll < self.probability:
            super().cast()


class DotBuff(Buff):
    def pre_cast(self):
        stack = min(self.stack_max - self.status.stacks[self.name], self.stack_add)

        # self.status.durations[self.name] = min(self.duration_max, self.status.durations[self.name] + self.duration)
        skill = self.status.skills[self.name]
        if interval := self.status.intervals[self.name]:
            self.status.durations[self.name] = interval - skill.interval + skill.duration
        else:
            self.status.durations[self.name] = skill.duration

        for _ in range(stack):
            self._add()


class PlacementBuff(Buff):
    def pre_cast(self):
        stack = min(self.stack_max - self.status.stacks[self.name], self.stack_add)

        self.status.durations[self.name] = self.status.skills[self.name].duration

        for _ in range(stack):
            self._add()


class GainBuff(Buff):
    def _add(self):
        super()._add()
        self.status.gains[self.name] = (self.level, self.status.stacks[self.name])

    def _remove(self):
        super()._remove()
        if stack := self.status.stacks[self.name]:
            self.status.gains[self.name] = (self.level, stack)
        else:
            self.status.gains.pop(self.name)

    def add(self, level, stack):
        pass

    def remove(self, level, stack):
        pass


class CDBuff(Buff):
    pass


class CountBuff(Buff):
    pass
