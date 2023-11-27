from base.skill import Skill
from base.status import Status


class DaoXiaoFengYinSetGain:
    def __call__(self, status: Status):
        status.skills["刀啸风吟"].skill_damage_addition += 0.1


class ShangJiangJunYinSetGain:
    def __call__(self, status: Status):
        status.skills["上将军印"].skill_damage_addition += 0.1
        status.skills["见尘"].skill_damage_addition += 0.1


class CriticalSetGain:
    @staticmethod
    def critical_set_post_cast(self: Skill):
        self.status.buffs["朔气"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(self.critical_set_post_cast)


class DaoXiaoFengYinDivineGain:
    def __call__(self, status: Status):
        status.skills["刀啸风吟"].skill_damage_addition += 0.05


class XiangWangJiDingDivineGain:
    def __call__(self, status: Status):
        pass


class DivineEffect:
    def __call__(self, status: Status):
        pass


class ShangJiangJunYinDivineEffect:
    def __call__(self, status: Status):
        pass


class WuXiangZhan:
    def __call__(self, status: Status):
        pass


EQUIP_GAINS_NAME = {
    '22035-1': "五相斩",
    "1925": "朔气4%双会套装",
    "4290": "刀啸风吟10%套装",
    "4291": "上将军印10%套装",
    "4294": "刀啸风吟5%橙武",
    "4295": "项王击鼎5%橙武",
    "2430": "橙武特效",
    "1942": "上将军印·神兵"
}
EQUIP_GAINS = {
    '22035-1': WuXiangZhan(),
    "1925": CriticalSetGain(),
    "4290": DaoXiaoFengYinSetGain(),
    "4291": ShangJiangJunYinSetGain(),
    "4294": DaoXiaoFengYinDivineGain(),
    "4295": XiangWangJiDingDivineGain(),
    "2430": DivineEffect(),
    "1942": ShangJiangJunYinDivineEffect()
}