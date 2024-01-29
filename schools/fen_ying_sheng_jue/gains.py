from base.skill import Skill
from base.status import Status


class 净世破魔击套装:
    def __call__(self, status: Status):
        for skill in ["净世破魔击·日", "净世破魔击·月", "诛邪镇魔-日", "诛邪镇魔-月"]:
            status.skills[skill].skill_damage_addition += 102 / 1024


class 明尊套装:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["明尊"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 驱夜断愁大橙武:
    def __call__(self, status: Status):
        status.skills["驱夜断愁"].skill_damage_addition += 51 / 1024


class 净世破魔击大橙武:
    def __call__(self, status: Status):
        for skill in ["净世破魔击·日", "净世破魔击·月", "诛邪镇魔-日", "诛邪镇魔-月"]:
            status.skills[skill].skill_damage_addition += 51 / 1024


class 橙武特效:
    @staticmethod
    def post_cast_effect(self: Skill):
        if not self.status.stacks["血月-冷却"]:
            self.status.buffs["血月"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 驱夜断愁神兵:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["驱夜断愁·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["驱夜断愁"].post_cast_effect.append(self.post_cast_effect)


EQUIP_GAINS_NAME = {
    "1922": "明尊4%双会套装",
    "948": "净世破魔击10%套装",
    "1542": "驱夜断愁5%橙武",
    "1543": "净世破魔击5%橙武",
    "2421": "橙武特效",
    "1938": "驱夜断愁·神兵"
}
EQUIP_GAINS = {
    "1922": 明尊套装(),
    "948": 净世破魔击套装(),
    "1542": 驱夜断愁大橙武(),
    "1543": 净世破魔击大橙武,
    "2421": 橙武特效(),
    "1938": 驱夜断愁神兵()
}
