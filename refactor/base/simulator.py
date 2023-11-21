import copy
import math
import time

from base.constant import FRAME_PER_SECOND
from base.status import Status

import random

random.seed(82)


class Simulator:
    def __init__(self, attribute, skills, buffs, gains, target, duration=300,
                 prepare=None, priority=None, loop=None):
        if prepare is None:
            prepare = []
        if priority is None:
            priority = []
        if loop is None:
            loop = []

        self.duration = duration

        self.action_seq = []
        self.event_seq = []
        self.status = Status(attribute, target,
                             [skill() for skill in skills],
                             [buff() for buff in buffs],
                             self.event_seq, self.duration * FRAME_PER_SECOND)

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

        self.current_loop = copy.copy(self.prepare) if self.prepare else self.loop

    @staticmethod
    def empty_condition(arg):
        return True

    def record(self, skill):
        self.action_seq.append((self.status.current_frame, skill.name))
        skill.cast()

    def priority_simulate(self):
        for skill, condition in self.priority:
            if skill.available and condition(self.status):
                self.record(skill)

    def loop_simulate(self):
        skill, condition = self.current_loop[0]

        while skill.available and condition(self.status):
            self.record(skill)
            self.current_loop.pop(0)
            if not self.current_loop:
                self.current_loop = copy.copy(self.loop)
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

    def summary(self):
        total = {}
        total_damage = 0
        for event in self.event_seq:
            if event[1] not in total:
                total[event[1]] = [0, 0]
            total[event[1]][0] += 1
            total[event[1]][1] += event[-1]
            total_damage += event[-1]

        for k, v in total.items():
            print(f"{k} - {v[0]} - {v[1]} - {round(float(v[1] / total_damage) * 100, 2)}")
        print(total_damage / self.duration)

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.simulate()
        print(f"finish simulation with {time.time() - start_time}")
        return self.action_seq, self.event_seq
        # self.summary()
