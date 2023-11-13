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
    probability: float = 1
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
        if self.roll >= self.probability:
            return

        self.refresh()
        if self.cd:
            self.activate = False
            self.status.cds[self.name] = self.cd

    def refresh(self):
        stack = min(self.stack_max - self.status.stacks[self.name], self.stack_add)

        self.status.stacks[self.name] += stack

        for _ in range(stack):
            self.add()

        if self.is_dot:
            if self.name in self.status.intervals:
                duration = self.status.skills[self.name].duration - self.status.skills[self.name].interval
                self.status.durations[self.name] = duration
            else:
                self.status.durations[self.name] = self.status.skills[self.name].duration
        else:
            self.status.durations[self.name] = min(self.duration_max, self.duration)

    def consume(self):
        stack = min(self.status.stacks[self.name], self.stack_remove)

        self.status.stacks[self.name] -= stack

        for _ in range(stack):
            self.remove()

        if not self.status.stacks[self.name]:
            self.status.durations.pop(self.name)

    def clear(self):
        for _ in range(self.status.stacks[self.name]):
            self.remove()

        self.status.stacks[self.name] = 0
        if self.name in self.status.durations:
            self.status.durations.pop(self.name)
