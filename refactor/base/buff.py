import random
from dataclasses import dataclass

from base.status import Status


@dataclass
class Buff:
    name: str = None
    status: Status = None
    activate: bool = True

    is_dot: bool = False

    cd: int = 0
    probability: float = 0
    duration: int = 3600 * 16
    duration_max: int = 3600 * 16

    stack_add: int = 1
    stack_remove: int = 1
    stack_max: int = 1

    add_effect: list = None
    remove_effect: list = None

    def __post_init__(self):
        self.add_effect = []
        self.remove_effect = []
    # def extend(self, stack=None, duration=None):
    #     if stack is None:
    #         stack = self.stack_add
    #     if duration is None:
    #         duration = self.duration
    #     self.status.stacks[self] = min(self.stack_max, self.status.stacks[self] + stack)
    #     for _ in range(stack):
    #         self.add_effect()
    #     self.status.durations[self] = min(self.duration_max, self.status.durations[self] + duration)

    @property
    def condition(self):
        return True

    @property
    def roll(self):
        return random.random()

    def ready(self):
        self.activate = True

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
        if not self.probability or self.roll < self.probability:

            self.refresh()
            if self.cd:
                self.activate = False
                self.status.cds[self.name] = self.cd

    def refresh(self):
        if stack := self.status.stacks.get(self.name, 0):
            stack = min(self.stack_max - stack, self.stack_add)
        else:
            stack = self.stack_add
            self.status.stacks[self.name] = 0

        self.status.stacks[self.name] += stack

        for _ in range(stack):
            self.add()

        if self.is_dot:
            if self.name in self.status.intervals:
                duration = self.status.intervals[self.name].duration - self.status.intervals[self.name].interval
                self.status.durations[self.name] += duration
            else:
                self.status.durations[self.name] = self.status.skills[self.name].duration
        else:
            self.status.durations[self.name] = min(self.duration_max, self.duration)

    def consume(self):
        if stack := self.status.stacks.get(self.name, 0):
            stack = min(stack, self.stack_remove)

            self.status.stacks[self.name] -= stack

            for _ in range(stack):
                self.remove()

            if not self.status.stacks[self.name]:
                self.status.stacks.pop(self.name)
                self.status.durations.pop(self.name)

    def clear(self):
        if stack := self.status.stacks.get(self.name, 0):
            for _ in range(stack):
                self.remove()

            self.status.stacks.pop(self.name)

        if self.name in self.status.durations:
            self.status.durations.pop(self.name)
