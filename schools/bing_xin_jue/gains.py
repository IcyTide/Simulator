from base.skill import Skill
from base.status import Status


class 玳弦急曲套装:
    def __call__(self, status: Status):
        status.skills["玳弦急曲"].skill_damage_addition += 102 / 1024
        status.skills["玳弦急曲-新妆"].skill_damage_addition += 102 / 1024


class 嗔怒套装:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["嗔怒"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 玳弦急曲大橙武:
    def __call__(self, status: Status):
        status.skills["玳弦急曲"].skill_damage_addition += 51 / 1024


class 江海凝光大橙武:
    def __call__(self, status: Status):
        status.skills["江海凝光"].skill_damage_addition += 51 / 1024


class 橙武特效:
    @staticmethod
    def post_cast_effect(self: Skill):
        if not self.status.stacks["飞霜绛露-冷却"]:
            self.status.buffs["飞霜绛露"].trigger()

    @staticmethod
    def post_hit_effect(self: Skill):
        if self.status.stacks["飞霜绛露"]:
            self.reset()
            self.status.skills["气吞长江-持续"].cast()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)

        status.skills["剑气长江"].post_hit_effect.append(self.post_hit_effect)


class 剑破虚空神兵:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["剑破虚空·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["剑破虚空"].post_cast_effect.append(self.post_cast_effect)


EQUIP_GAINS_NAME = {
    "1916": "嗔怒4%双会套装",
    "1547": "玳弦急曲10%套装",
    "1524": "玳弦急曲5%橙武",
    "1525": "江海凝光5%橙武",
    "2416": "橙武特效",
    "1930": "剑破虚空·神兵"
}
EQUIP_GAINS = {
    "1916": 嗔怒套装(),
    "1547": 玳弦急曲套装(),
    "1524": 玳弦急曲大橙武(),
    "1525": 江海凝光大橙武,
    "2416": 橙武特效(),
    "1930": 剑破虚空神兵()
}
