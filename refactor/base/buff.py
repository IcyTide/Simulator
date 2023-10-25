from dataclasses import dataclass

from base.status import Status, Snapshot


@dataclass
class Buff:
    name: str = None
    status: Status = None
    activate: bool = True

    duration: int = 0
    duration_max: int = 0

    stack_add: int = 1
    stack_remove: int = 1
    stack_max: int = 1

    add_effect: list = None
    remove_effect: list = None

    snapshot: Snapshot = None

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

    def add(self):
        for effect in self.add_effect:
            effect(self)

    def remove(self):
        for effect in self.remove_effect:
            effect(self)

    def refresh(self, stack=None, duration=None):
        if stack is None:
            stack = self.stack_add
        if duration is None:
            duration = self.duration_max

        stack = min(self.stack_max - self.status.stacks[self.name], stack)
        self.status.stacks[self.name] += stack

        for _ in range(stack):
            self.add()

        self.status.durations[self.name] = min(self.duration_max, duration)

    def consume(self, stack=None):
        if stack is None:
            stack = self.stack_remove
        stack = min(stack, self.status.stacks[self.name])
        self.status.stacks[self.name] -= stack
        for _ in range(stack):
            self.remove()
        if not self.status.stacks[self.name]:
            self.status.durations.pop(self.name)

    def expire(self):
        for _ in range(self.status.stacks[self.name]):
            self.remove()

        self.status.stacks[self.name] = 0

        if self.name in self.status.durations:
            self.status.durations.pop(self.name)
