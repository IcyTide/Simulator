import copy
import math
import time

from base.constant import FRAME_PER_SECOND
from base.status import Status

import random

random.seed(82)


class Simulator:
    def __init__(self, attribute, skills, buffs, gains, target, duration=300,
                 prepare_list=None, priority=None, loop=None):
        if prepare_list is None:
            prepare_list = []
        if priority is None:
            priority = []
        if loop is None:
            loop = []

        self.duration = duration
        self.frames_duration = self.duration * FRAME_PER_SECOND

        self.action_seq = []
        self.event_seq = []
        self.status = Status(attribute, target,
                             [skill() for skill in skills],
                             [buff() for buff in buffs],
                             self.event_seq, self.frames_duration)

        for gain in gains:
            gain(self.status)

        self.prepare_list = [
            (self.status.skills[e[0]], e[1]) if isinstance(e, tuple) else (self.status.skills[e], self.empty_condition)
            for e in prepare_list]
        self.priority = [
            (self.status.skills[e[0]], e[1]) if isinstance(e, tuple) else (self.status.skills[e], self.empty_condition)
            for e in priority]
        self.loop = [
            (self.status.skills[e[0]], e[1]) if isinstance(e, tuple) else (self.status.skills[e], self.empty_condition)
            for e in loop]

        self.current_loop = copy.copy(self.prepare_list) if self.prepare_list else self.loop

    @staticmethod
    def empty_condition(arg):
        return True

    def priority_simulate(self):
        for skill, condition in self.priority:
            if skill.available and condition(self.status):
                self.action_seq.append((self.status.current_frame, skill.name))
                skill.cast()

    def loop_simulate(self):
        skill, condition = self.current_loop[0]

        while skill.available and condition(self.status):
            self.action_seq.append((self.status.current_frame, skill.name))
            skill.cast()
            self.current_loop.pop(0)
            if not self.current_loop:
                self.current_loop = copy.copy(self.loop)
            skill, condition = self.current_loop[0]

    def simulate(self):
        self.status.init()
        while self.status.current_frame < self.frames_duration:
            self.priority_simulate()
            self.loop_simulate()
            gap = min(min(self.status.gcd_group.values(), default=FRAME_PER_SECOND),
                      min(self.status.cds.values(), default=FRAME_PER_SECOND),
                      min(self.status.intervals.values(), default=FRAME_PER_SECOND),
                      min(self.status.durations.values(), default=FRAME_PER_SECOND))
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
        self.summary()
