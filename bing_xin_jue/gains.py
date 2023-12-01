from base.skill import Skill
from base.status import Status


class DaiXianJiQuSetGain:
    def __call__(self, status: Status):
        status.skills["玳弦急曲"].skill_damage_addition += 102 / 1024


class CriticalSetGain:
    @staticmethod
    def critical_set_post_cast(self: Skill):
        self.status.buffs["嗔怒"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_cast:
                skill.post_cast_effect.append(self.critical_set_post_cast)


class DaiXianJiQuDivineGain:
    def __call__(self, status: Status):
        status.skills["玳弦急曲"].skill_damage_addition += 51 / 1024


class JiangHaiNingGuangDivineGain:
    def __call__(self, status: Status):
        status.skills["江海凝光"].skill_damage_addition += 51 / 1024


class DivineEffect:
    @staticmethod
    def divine_post_cast(self: Skill):
        self.status.buffs["飞霜绛露"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_cast:
                skill.post_cast_effect.append(self.divine_post_cast)


class JianPoXuKongDivineEffect:
    @staticmethod
    def divine_post_cast(self: Skill):
        self.status.skills["剑破虚空·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["剑破虚空"].post_cast_effect.append(self.divine_post_cast)


EQUIP_GAINS_NAME = {
    "1916": "嗔怒4%双会套装",
    "1547": "玳弦急曲10%套装",
    "1524": "玳弦急曲5%橙武",
    "1525": "江海凝光5%橙武",
    "2416": "橙武特效",
    "1930": "剑破虚空·神兵"
}
EQUIP_GAINS = {
    "1916": CriticalSetGain(),
    "1547": DaiXianJiQuSetGain(),
    "1524": DaiXianJiQuDivineGain,
    "1525": JiangHaiNingGuangDivineGain,
    "2416": DivineEffect(),
    "1930": JianPoXuKongDivineEffect()
}
