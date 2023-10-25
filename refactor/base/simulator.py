import copy

from base.status import Status


class Simulator:
    def __init__(self, attribute, skills, buffs, talents, prepare_list=None,
                 priority=None, loop=None, duration=3600 * 24):
        self.prepare_list = prepare_list if prepare_list else []
        self.priority = priority if priority else []
        self.loop = loop if loop else []

        self.duration = duration

        self.action_seq = []
        self.event_seq = []
        self.status = Status(attribute, skills, buffs, self.event_seq)
        for skill in skills:
            skill.status = self.status

        for buff in buffs:
            buff.status = self.status

        for talent in talents:
            talent(self.status)

    def epoch_prepare(self):
        for skill in self.prepare_list:
            skill = self.status.skills[skill]
            while not skill.available:
                self.status.timer()

            self.action_seq.append((self.status.current_time / 16, skill.name))
            skill.cast()

    @staticmethod
    def empty_condition(s):
        return True

    def priority_simulate(self):
        for skill in self.priority:
            if isinstance(skill, tuple):
                skill, condition = skill
            else:
                condition = self.empty_condition
            skill = self.status.skills[skill]
            if skill.available and condition(self.status):
                self.action_seq.append((self.status.current_time / 16, skill.name))
                skill.cast()

    def loop_simulate(self):
        loop_list = copy.copy(self.loop)
        if self.prepare_list:
            self.epoch_prepare()

        while self.status.current_time < self.duration:
            self.priority_simulate()
            if isinstance(skill := loop_list.pop(0), tuple):
                skill, condition = skill
            else:
                condition = self.empty_condition

            skill = self.status.skills[skill]
            while not skill.available or not condition(self.status):
                self.status.timer()

            self.action_seq.append((self.status.current_time / 16, skill.name))
            skill.cast()

            if not loop_list:
                loop_list = copy.copy(self.loop)

    def __call__(self, *args, **kwargs):
        if self.loop:
            self.loop_simulate()
            for e in self.action_seq:
                print(e)
