from base.skill import Skill
from base.status import Status


class 孤锋破浪套装:
    def __call__(self, status: Status):
        status.skills["孤锋破浪"].skill_damage_addition += 102 / 1024


class 朔气套装:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["朔气"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 孤锋破浪大橙武:
    def __call__(self, status: Status):
        status.skills["孤锋破浪"].skill_damage_addition += 51 / 1024


class 沧浪三叠大橙武:
    def __call__(self, status: Status):
        status.skills["沧浪三叠·一"].skill_damage_addition += 51 / 1024
        status.skills["沧浪三叠·二"].skill_damage_addition += 51 / 1024
        status.skills["沧浪三叠·三"].skill_damage_addition += 51 / 1024


class 橙武特效:
    @staticmethod
    def post_cast_effect(self: Skill):
        if not self.status.stacks["绝地天通刀-冷却"]:
            self.status.buffs["绝地天通刀"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["绝地天通刀"]:
            self.reset()
            self.status.skills["背水沉舟-持续"].cast()

    def __call__(self, status: Status):
        # for skill in status.skills.values():
        #     if skill.hit_with_cast:
        #         skill.post_hit_effect.append(self.post_cast_effect)
        #     elif skill.is_cast:
        #         skill.post_cast_effect.append(self.post_cast_effect)
        # status.skills["孤锋破浪"].post_hit_effect.append(self.post_hit_effect)
        pass


class 行云式神兵:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["行云式·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["行云式"].post_cast_effect.append(self.post_cast_effect)


EQUIP_GAINS_NAME = {
    "1925": "朔气4%双会套装",
    "3188": "孤锋破浪10%套装",
    "3186": "孤锋破浪5%橙武",
    "3187": "沧浪三叠5%橙武",
    "2391": "橙武特效",
    "2392": "行云式·神兵"
}
EQUIP_GAINS = {
    "1925": 朔气套装(),
    "3188": 孤锋破浪套装(),
    "3186": 孤锋破浪大橙武(),
    "3187": 沧浪三叠大橙武(),
    "2391": 橙武特效(),
    "2392": 行云式神兵()
}
