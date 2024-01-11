from base.skill import Skill
from base.status import Status


class 韦陀献杵套装:
    def __call__(self, status: Status):
        status.skills["韦陀献杵"].skill_damage_addition += 102 / 1024
        status.skills["韦陀献杵-外功"].skill_damage_addition += 102 / 1024


class 拿云式套装:
    def __call__(self, status: Status):
        status.skills["拿云式"].skill_damage_addition += 102 / 1024


class 佛吼套装:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["佛吼"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 普渡四方大橙武:
    def __call__(self, status: Status):
        status.skills["普渡四方"].skill_damage_addition += 51 / 1024
        status.skills["普渡四方_外功"].skill_damage_addition += 51 / 1024


class 守缺式大橙武:
    def __call__(self, status: Status):
        status.skills["守缺式"].skill_damage_addition += 51 / 1024


class 橙武特效:
    @staticmethod
    def post_cast_effect(self: Skill):
        if not self.status.stacks["桑莲妙境-冷却"]:
            self.status.buffs["桑莲妙境"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 守缺式神兵:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["守缺式·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["守缺式"].post_cast_effect.append(self.post_cast_effect)


EQUIP_GAINS_NAME = {
    "1911": "佛吼4%双会套装",
    "818": "韦陀献杵10%套装",
    "1147": "拿云式10%套装",
    "1512": "普渡四方5%橙武",
    "1513": "守缺式5%橙武",
    "2410": "橙武特效",
    "1928": "守缺式·神兵"
}
EQUIP_GAINS = {
    "1911": 佛吼套装(),
    "818": 韦陀献杵套装(),
    "1147": 拿云式套装(),
    "1512": 普渡四方大橙武(),
    "1513": 守缺式大橙武,
    "2410": 橙武特效(),
    "1928": 守缺式神兵()
}
