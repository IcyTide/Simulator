from base.skill import Skill
from base.status import Status
from general.recipes import EmptyRecipe


class 云飞玉皇套装:
    def __call__(self, status: Status):
        status.skills["云飞玉皇"].skill_damage_addition += 102 / 1024


class 听雷套装:
    def __call__(self, status: Status):
        status.skills["听雷"].skill_damage_addition += 102 / 1024


class 器攻套装:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.buffs["器攻"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 夕照雷峰大橙武:
    def __call__(self, status: Status):
        status.skills["夕照雷峰"].skill_damage_addition += 51 / 1024


class 听雷大橙武:
    def __call__(self, status: Status):
        status.skills["听雷"].skill_damage_addition += 51 / 1024


class 橙武特效:
    @staticmethod
    def post_cast_effect(self: Skill):
        if not self.status.stacks["螭尘-冷却"]:
            self.status.buffs["螭尘"].trigger()

    def __call__(self, status: Status):
        for skill in status.skills.values():
            if skill.hit_with_cast:
                skill.post_hit_effect.append(self.post_cast_effect)
            elif skill.is_cast:
                skill.post_cast_effect.append(self.post_cast_effect)


class 云飞玉皇神兵:
    @staticmethod
    def post_cast_effect(self: Skill):
        self.status.skills["云飞玉皇·神兵"].cast()

    def __call__(self, status: Status):
        status.skills["云飞玉皇"].post_cast_effect.append(self.post_cast_effect)


class 五相斩:
    def __call__(self, status: Status):
        pass


EQUIP_GAINS_NAME = {
    '22035-1': "五相斩",
    "1920": "器攻4%双会套装",
    "818": "云飞玉皇10%套装",
    "4347": "听雷10%套装",
    "1536": "听雷5%橙武",
    "1537": "梦泉虎跑5%橙武",
    "1538": "听雷5%橙武",
    "1539": "夕照雷峰5%橙武",
    "2426": "橙武特效",
    "1942": "云飞玉皇·神兵"
}
EQUIP_GAINS = {
    '22035-1': 五相斩(),
    "1920": 器攻套装(),
    "818": 云飞玉皇套装(),
    "4347": 听雷套装(),
    "1536": EmptyRecipe(),
    "1537": EmptyRecipe(),
    "1538": 夕照雷峰大橙武(),
    "1539": 听雷大橙武(),
    "2426": 橙武特效(),
    "1937": 云飞玉皇神兵()
}
