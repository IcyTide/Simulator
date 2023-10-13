from dataclasses import dataclass

from base import Timeline
from base.status import Status


@dataclass
class Buff:
    uid: int
    name: str

    timeline: Timeline

    skills: dict
    buffs: dict
    status: Status

    activate: bool = True

    cd: int = 0

    duration: int = 0
    duration_max: int = 0

    stack: int = 1
    stack_add: int = 1
    stack_remove: int = 1
    stack_max: int = 1

    current_cd: int = 0
    current_duration: int = 0
    current_stack: int = 0

    @property
    def condition(self):
        return True

    @property
    def ready(self):
        return self.activate and self.condition

    def insert(self):
        gaps = (e for e in (self.current_cd, self.current_duration) if e > 0)
        if gaps:
            self.timeline.set(min(gaps), self)

    def set_duration(self, duration):
        self.current_duration = max(duration, self.duration_max)
        if not self.current_duration:
            self.remove_stack(self.current_stack)

    def add_duration(self, duration):
        self.set_duration(self.current_duration + duration)

    def set_cd(self, cd):
        self.current_cd = max(cd, 0)

    def add_cd(self, cd):
        self.set_cd(self.cd + cd)

    def update(self, gap):
        self.set_duration(gap)
        self.set_cd(gap)
        self.insert()

    def set_stack(self, stack):
        self.current_stack = max(stack, self.stack_max)

        if not self.current_stack:
            self.set_duration(0)

    def add_effect(self):
        pass

    def add_stack(self, stack):
        stack_residual = max(stack, self.stack_max - self.current_stack)
        for _ in range(stack_residual):
            self.add_effect()
        self.set_stack(stack_residual)

    def remove_effect(self):
        pass

    def remove_stack(self, stack):
        stack_residual = min(stack, self.current_stack)
        for _ in range(stack_residual):
            self.remove_effect()
        self.set_stack(-stack_residual)

    def refresh(self, stack=stack_add, duration=duration):
        self.add_stack(stack)
        self.set_duration(duration)

    def consume(self, stack=stack_remove):
        self.remove_stack(stack)
