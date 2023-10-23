from sortedcontainers import SortedDict

from base import Timeline
from base.skill import Skill
from base.status import Status


class Simulator:
    def __init__(self, status: Status):
        self.status = status
        self.priority = priority

        self.timeline = Timeline()

        self.remain_time = 180

