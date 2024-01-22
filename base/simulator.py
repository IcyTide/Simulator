import math
from collections import Counter

from utils.regex import parse_expression

from base.constant import FRAME_PER_SECOND
from base.status import Status


class Simulator:
    def __init__(self, attribute, skills, buffs, gains, target, duration,
                 prepare=None, priority=None, loop=None, initiation=None, gap=0, verbose=False):

        if verbose:
            self.record = self.record_verbose

        self.duration = duration

        self.actions = []
        self.events = []
        self.damages = Counter()
        self.status = Status(attribute, target, skills, buffs,
                             self.damages, self.events, self.duration * FRAME_PER_SECOND, verbose)

        for gain in gains:
            gain(self.status)

        self.initiation = initiation

        self.prepare = parse_expression(self.status, prepare)
        self.priority = parse_expression(self.status, priority)
        self.loop = parse_expression(self.status, loop)

        self.current_loop = self.prepare if self.prepare else self.loop.copy()
        if not self.current_loop:
            self.loop_simulate = self.priority_simulate

        if gap:
            self.gap = gap
        else:
            self.gap = FRAME_PER_SECOND

    @staticmethod
    def record(skill):
        skill.cast()

    def record_verbose(self, skill):
        skill.cast()
        self.actions.append((self.status.current_frame, skill.name))

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
                self.current_loop = self.loop.copy()
            skill, condition = self.current_loop[0]

    def simulate(self):
        while self.status.total_frame > self.status.current_frame:
            self.priority_simulate()
            self.loop_simulate()
            gap = min(self.status.gcd_group.min(),
                      self.status.cds.min(),
                      self.status.intervals.min(),
                      self.status.durations.min(),
                      self.status.total_frame - self.status.current_frame, self.gap)
            self.status.timer(math.ceil(gap))

    def __call__(self, seed=82):
        self.status.set_dice(seed)
        self.initiation(self.status)
        self.simulate()
        return self.damages
