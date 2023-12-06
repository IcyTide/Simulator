from base.skill import Skill
from base.status import Status


class 刀啸风吟套装:
    def __call__(self, status: Status):
        status.skills["刀啸风吟"].skill_damage_addition += 102 / 1024


class 上将军印套装:
    def __call__(self, status: Status):
        status.skills["上将军印"].skill_damage_addition += 102 / 1024
        status.skills["见尘"].skill_damage_addition += 102 / 1024


class 朔气套装:
    @staticmethod
    def critical_set_post_hit(self: Skill):
        self.status.buffs["朔气"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_cast and skill.is_hit:
                skill.post_hit_effect.append(self.critical_set_post_hit)


class 刀啸风吟大橙武:
    def __call__(self, status: Status):
        status.skills["刀啸风吟"].skill_damage_addition += 51 / 1024


class 项王击鼎大橙武:
    def __call__(self, status: Status):
        pass


class 橙武特效:
    @staticmethod
    def divine_post_cast(self: Skill):
        self.status.buffs["沉夜重雪"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.is_cast:
                skill.post_cast_effect.append(self.divine_post_cast)


class 上将军印神兵:
    @staticmethod
    def divine_post_cast(self: Skill):
        self.status.skills["上将军印·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["上将军印"].post_cast_effect.append(self.divine_post_cast)


class 五相斩:
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
    '22035-1': 五相斩(),
    "1925": 朔气套装(),
    "4290": 刀啸风吟套装(),
    "4291": 上将军印套装(),
    "4294": 刀啸风吟大橙武(),
    "4295": 项王击鼎大橙武(),
    "2430": 橙武特效(),
    "1942": 上将军印神兵()
}
