from base.skill import Skill
from base.status import Status


class 龙牙套装:
    def __call__(self, status: Status):
        status.skills["龙牙"].skill_damage_addition += 102 / 1024
        status.skills["龙牙-龙血"].skill_damage_addition += 102 / 1024


class 军啸套装:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["军啸"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 龙吟大橙武:
    def __call__(self, status: Status):
        status.skills["龙吟"].skill_damage_addition += 51 / 1024


class 穿云大橙武:
    def __call__(self, status: Status):
        status.skills["穿云"].skill_damage_addition += 51 / 1024


class 橙武特效:
    @staticmethod
    def post_cast_effect(self: Skill):
        if not self.status.stacks["旷野孤疆-冷却"]:
            self.status.buffs["旷野孤疆"].trigger()

    @staticmethod
    def post_hit_effect_1(self: Skill):
        if self.status.stacks["旷野孤疆"]:
            self.reset()

    @staticmethod
    def post_hit_effect_2(self: Skill):
        if self.status.stacks["旷野孤疆"]:
            self.status.skills["画角闻龙"].cast()
            self.status.buffs["战意"].increase(5)

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)
        status.skills["龙吟"].post_hit_effect(self.post_hit_effect_1)
        status.skills["龙牙"].post_hit_effect(self.post_hit_effect_2)


class 龙牙神兵:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["龙牙·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["龙牙"].post_cast_effect.append(self.post_cast_effect)


EQUIP_GAINS_NAME = {
    "1913": "朔气4%双会套装",
    "817": "龙牙10%套装",
    "1508": "龙吟5%橙武",
    "1509": "穿云5%橙武",
    "2424": "橙武特效",
    "1933": "龙牙·神兵"
}
EQUIP_GAINS = {
    "1913": 军啸套装(),
    "817": 龙牙套装(),
    "1508": 龙吟大橙武(),
    "1509": 穿云大橙武(),
    "2424": 橙武特效(),
    "1933": 龙牙神兵()
}
