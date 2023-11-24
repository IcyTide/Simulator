import math
import time

from base.constant import FRAME_PER_SECOND
from base.status import Status

import random


class Simulator:
    def __init__(self, attribute, skills, buffs, gains, target, duration,
                 prepare=None, priority=None, loop=None, seed=82, verbose=False):

        if verbose:
            random.seed(seed)
            self.record = self.record_verbose

        self.duration = duration

        self.actions = []
        self.events = []
        self.damages = {}
        self.status = Status(attribute, target, [skill() for skill in skills], [buff() for buff in buffs],
                             self.damages, self.events, self.duration * FRAME_PER_SECOND, verbose)

        for gain in gains:
            gain(self.status)

        self.prepare = [
            (self.status.skills[e[0]], e[1]) if isinstance(e, tuple) else (self.status.skills[e], self.empty_condition)
            for e in prepare]
        self.priority = [
            (self.status.skills[e[0]], e[1]) if isinstance(e, tuple) else (self.status.skills[e], self.empty_condition)
            for e in priority]
        self.loop = [
            (self.status.skills[e[0]], e[1]) if isinstance(e, tuple) else (self.status.skills[e], self.empty_condition)
            for e in loop]

        self.current_loop = self.prepare if self.prepare else self.loop

    @staticmethod
    def empty_condition(arg):
        return True

    @staticmethod
    def record(skill):
        skill.cast()

    def record_verbose(self, skill):
        skill.cast()
        self.actions.append((self.status.current_frame, skill.name))

    def priority_simulate(self):
        for skill, condition in self.priority:
            if skill.available and condition(self.status):
                skill.cast()

    def loop_simulate(self):
        skill, condition = self.current_loop[0]

        while skill.available and condition(self.status):
            skill.cast()
            self.actions.append((self.status.current_frame, skill.name))
            self.current_loop.pop(0)
            if not self.current_loop:
                self.current_loop = self.loop.copy()
            skill, condition = self.current_loop[0]

    def simulate(self):
        while self.status.total_frame > self.status.current_frame:
            self.priority_simulate()
            self.loop_simulate()
            gap = min(min(self.status.gcd_group.values(), default=FRAME_PER_SECOND),
                      min(self.status.cds.values(), default=FRAME_PER_SECOND),
                      min(self.status.intervals.values(), default=FRAME_PER_SECOND),
                      min(self.status.durations.values(), default=FRAME_PER_SECOND),
                      self.status.total_frame - self.status.current_frame)
            self.status.timer(math.ceil(gap))

    def __call__(self):
        start_time = time.time()
        self.simulate()
        print(f"finish simulation with {time.time() - start_time}")
        return self.damages
