from sortedcontainers import SortedDict

from base import Timeline
from base.skill import Skill


class Simulator:
    def __init__(self, agent, target, skills, buffs, priority):
        self.agent = agent
        self.target = target

        self.skills = skills
        self.buffs = buffs
        self.priority = priority

        self.timeline = Timeline()

        self.remain_time = 180

    @property
    def status(self):
        return [buff.current_stack for buff in self.buffs]

    @property
    def actions(self):
        return [skill.available for skill in self.skills]

    def next(self):
        pass

    def record(self, **kwargs):
        print(f"{self.remain_time} {kwargs}")
