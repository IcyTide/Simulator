import copy
import time

from base.constant import FRAME_PER_SECOND
from base.status import Status

import random
random.seed(82)


class Simulator:
    def __init__(self, attribute, skills, buffs, talents, recipes, gains,
                 prepare_list=None, priority=None, loop=None, duration=300):
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
        self.status = Status(attribute, skills, buffs, self.event_seq)
        for skill in skills:
            skill.status = self.status

        for buff in buffs:
            buff.status = self.status

        for talent in talents:
            talent(self.status)

        for recipe in recipes:
            recipe(self.status)

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
    def empty_condition(s):
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

    # def loop_simulate(self):
    #     skill, condition = self.current_loop.pop(0)
    #
    #     while not skill.available or not condition(self.status):
    #         self.status.timer()
    #         if self.status.current_time >= self.duration:
    #             return
    #
    #     self.action_seq.append((self.status.current_time, skill.name))
    #     skill.cast()
    #
    #     if not self.current_loop:
    #         self.current_loop = copy.copy(self.loop)

    def simulate(self):
        while self.status.current_frame < self.frames_duration:
            self.priority_simulate()
            self.loop_simulate()
            self.status.timer()

    def summary(self):
        total = {}
        for event in self.event_seq:
            if event[1] not in total:
                total[event[1]] = [0, 0]
            total[event[1]][0] += 1
            total[event[1]][1] += event[-1]

        for k, v in total.items():
            print(f"{k} - {v[0]} - {v[1]} - {round(float(v[1] / self.status.total_damage) * 100, 2)}")

        self.status.total_damage = self.status.total_damage / self.duration
        if self.status.attribute.grad_attrs:
            self.status.total_damage.backward()

            for name in self.status.attribute.grad_attrs:
                print(f"{name}: {getattr(self.status.attribute, name).grad * self.status.attribute.grad_scale[name]}")

    def __call__(self, *args, **kwargs):
        # print("start simulate")
        start_time = time.time()
        self.simulate()
        print(f"finish with {time.time() - start_time}")
        self.summary()

        # for e in self.event_seq:
        #     print(round(e[0] / self.scale, 2), e[1], e[3] + 1)
