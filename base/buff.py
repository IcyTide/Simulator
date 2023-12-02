import random
from dataclasses import dataclass

from base.status import Status


@dataclass
class Buff:
    status: Status
    name: str = None
    activate: bool = True

    is_dot: bool = False

    probability: float = 1
    duration: int = 3600 * 16
    duration_max: int = 3600 * 16

    stack_add: int = 1
    stack_remove: int = 1
    stack_max: int = 1

    level_params: dict = None

    def __post_init__(self):
        self.add_effect = []
        self.remove_effect = []

    @property
    def condition(self):
        return True

    @property
    def roll(self):
        return random.random()

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

    def trigger(self, level=None):
        if not self.activate:
            return
        if not self.condition:
            return
        if self.roll >= self.probability:
            return

        if level:
            for attr, values in self.level_params.items():
                setattr(self, attr, values[level - 1])

        self.refresh()

    def refresh(self):
        stack = min(self.stack_max - self.status.stacks[self.name], self.stack_add)

        if self.is_dot:
            if self.name in self.status.intervals:
                skill = self.status.skills[self.name]
                self.status.durations[self.name] += skill.duration - skill.interval
            else:
                self.status.durations[self.name] = self.status.skills[self.name].duration
        else:
            self.status.durations[self.name] = min(self.duration_max, self.duration)

        for _ in range(stack):
            self.add()

    def consume(self, stack=None):
        if not stack:
            stack = self.stack_remove

        stack = min(stack, self.status.stacks[self.name])

        for _ in range(stack):
            self.remove()

    def clear(self):
        for _ in range(self.status.stacks[self.name]):
            self.remove()
