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
        for effect in self.add_effect:
            effect(self)

    def remove(self):
        for effect in self.remove_effect:
            effect(self)

    def trigger(self):
        if not self.activate:
            return
        if not self.condition:
            return
        if self.roll >= self.probability:
            return

        self.refresh()

    def refresh(self):
        stack = min(self.stack_max - self.status.stacks[self.name], self.stack_add)

        self.status.stacks[self.name] += stack

        for _ in range(stack):
            self.add()

        if self.is_dot:
            if self.name in self.status.intervals:
                skill = self.status.skills[self.name]
                duration = skill.duration - skill.interval
                self.status.durations[self.name] = duration
            else:
                self.status.durations[self.name] = self.status.skills[self.name].duration
        else:
            self.status.durations[self.name] = min(self.duration_max, self.duration)

    def consume(self, stack=None):
        if not (current_stack := self.status.stacks[self.name]):
            return

        if not stack:
            stack = self.stack_remove

        stack = min(current_stack, stack)

        for _ in range(stack):
            self.remove()

        self.status.stacks[self.name] -= stack
        if not self.status.stacks[self.name]:
            self.status.durations.pop(self.name)

    def clear(self):
        for _ in range(self.status.stacks[self.name]):
            self.remove()

        self.status.stacks[self.name] = 0
        if self.name in self.status.durations:
            self.status.durations.pop(self.name)
