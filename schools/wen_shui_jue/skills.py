from base.constant import PHYSICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, PHYSICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import Melee, CastingSkill, PhysicalDamage, ActionSkill, PlacementSkill, TriggerSkill, LoopSkill, \
    ChargingSkill, apply_haste

"""
    Base Skills
"""


class 三柴剑法(Melee):
    def __init__(self, status):
        super().__init__(status)
        self.name = "三柴剑法"

        self.gcd_index = self.name
        self.gcd_base = 24

        self.skill_damage_addition = 205 / 1024

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].increase(5)

    @property
    def condition(self):
        return self.status.stacks["问水诀"]


class 四季剑法(Melee):
    @property
    def attack_power_cof(self):
        return self._attack_power_cof * apply_haste(self.haste, 32) / 32

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        self._attack_power_cof = attack_power_cof

    def __init__(self, status):
        super().__init__(status)
        self.name = "四季剑法"

        self.gcd_index = self.name
        self.cd_base = 2 * 16

        self.skill_damage_addition = 205 / 1024

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].increase(5)

    @property
    def condition(self):
        return self.status.stacks["山居剑意"]


class 啸日(CastingSkill, ChargingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "啸日"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name
        self.gcd_base = 16

        self.cd_base = 12 * 16
        self.energy = 2

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["山居剑意"]:
            self.status.buffs["山居剑意"].clear()
            self.status.buffs["问水诀"].trigger()
        else:
            self.status.buffs["问水诀"].clear()
            self.status.buffs["山居剑意"].trigger()


class 剑气衰减(LoopSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑气衰减"

        self.interval_base = 16

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].decrease(2)


class 断潮(TriggerSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "断潮"
        self.probability = 1
        self.damage_base = int(144 * 0.95)
        self.damage_rand = int(144 * 0.1)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 1.1 * 1.1 * 1.1 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 听雷(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "听雷"

        self.damage_base = int(280 / 2)
        self.damage_rand = int(22 / 2)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(144 * 1.1 * 1.15 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def critical_hit(self):
        super().critical_hit()
        self.status.skills["断潮"].cast()

    def post_hit(self):
        super().post_hit()
        if self.status.stacks["问水诀"]:
            self.status.buffs["剑气"].increase(20)


class 破(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.is_cast = False
        self.is_hit = False

        self.surplus_cof = [
            SURPLUS_COF(1024 * 1024 * (0.616 - 1)),
            SURPLUS_COF(1024 * 1024 * (0.1 - 1)),
            SURPLUS_COF(1024 * 1024 * (0.8 - 1)),
            SURPLUS_COF(1024 * 1024 * (0.7392 - 1))
        ]


class 夕照雷峰(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "夕照雷峰"

        self.interval_base = 24

        self.damage_base = int(801 * 0.25)
        self.damage_rand = int(80 * 0.25)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(180 * 1.1 * 1.15 * 1.1 * 1.1 * 1.15 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)

        self.cost = 15

    @property
    def condition(self):
        return self.status.stacks["山居剑意"] and self.status.stacks["剑气"] > self.cost

    def pre_hit(self):
        super().pre_hit()
        self.status.buffs["剑气"].decrease(self.cost)

    def critical_hit(self):
        super().critical_hit()
        self.status.skills["断潮"].cast()

    def pre_cast(self):
        super().pre_cast()
        self.status.intervals["剑气衰减"] = 32

    def post_hit(self):
        super().post_hit()
        self.status.skills["破"].cast(2)


class 云飞玉皇(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云飞玉皇"

        self.interval_base = 32
        self.cd_base = 4 * 16

        self.damage_base = int(770 * 0.35)
        self.damage_rand = int(72 * 0.35)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(200 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)

        self.cost = 15
        self.surplus_level = 1

    @property
    def condition(self):
        return self.status.stacks["山居剑意"] and self.status.stacks["剑气"] > self.cost

    def critical_hit(self):
        super().critical_hit()
        self.status.skills["断潮"].cast()

    def pre_cast(self):
        super().pre_cast()
        self.status.intervals["剑气衰减"] = 32

    def post_hit(self):
        super().post_hit()
        self.status.skills["破"].cast(self.surplus_level)
        self.status.skills["云飞玉皇-额外"].cast()
        self.status.buffs["剑气"].decrease(self.cost)


class 云飞玉皇_额外(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云飞玉皇-额外"

        self.damage_base = int(688 * 0.35)
        self.damage_rand = int(72 * 0.35)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(40 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 风来吴山_引导(ActionSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "风来吴山-引导"

        self.interval_list = [8] * 10
        self.damage_base = int(252 / 2)
        self.damage_rand = int(10 / 2)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 1.2 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 风来吴山(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.is_cast = False
        self.is_hit = False

        self.name = "风来吴山"

        self.cd_base = 90 * 16

        self.sub_skill = "风来吴山-引导"

        self.cost = 50

    @property
    def condition(self):
        return self.status.stacks["山居剑意"] and self.status.stacks["剑气"] > self.cost

    def post_cast(self):
        super().post_cast()
        self.status.skills[self.sub_skill].cast()


class 九溪弥烟(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "九溪弥烟"

        self.damage_base = 78
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(48 * 1.1)

    @property
    def condition(self):
        return self.status.stacks["问水诀"]

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].increase(5)


class 玉虹贯日(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玉虹贯日"

        self.gcd_index = 1
        self.gcd_base = 0

        self.cd_base = 15 * 16

    @property
    def condition(self):
        return self.status.stacks["问水诀"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["剑气"].increase(20)


class 黄龙吐翠(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "黄龙吐翠"

        self.gcd_index = 1
        self.gcd_base = 0

        self.cd_base = 8 * 16

        self.damage_base = int(349 / 3)
        self.damage_rand = int(37 / 3)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(112)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["问水诀"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["剑气"].increase(25)


class 莺鸣柳(CastingSkill, ChargingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "莺鸣柳"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name
        self.gcd_base = 16

        self.energy = 3
        self.cd_base = 90 * 16

    def post_cast(self):
        super().post_cast()
        self.status.buffs["莺鸣"].trigger()


class 云栖松(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云栖松"

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 70 * 16


class 云栖松剑气回复(PlacementSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云栖松剑气回复"

        self.interval_list = [16] * 8

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].increase(5)


"""
    Talent Skills
"""


class 云飞玉皇_岱宗(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云飞玉皇·岱宗"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 300
        self.damage_rand = 35
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(300 * 1.2)


class 九溪弥烟_持续(PlacementSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "九溪弥烟-持续"

        self.interval_list = [16] * 24

        self.damage_base = 61
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(48 * 1.1 * 2 * 1.3 * 0.34 * 1.15 * 1.1 * 1.25)


class 风来吴山_持续(PlacementSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "风来吴山-持续"

        self.interval_list = [8] * 16

        self.damage_base = int(252 / 2)
        self.damage_rand = int(10 / 2)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 0.7 * 1.3 * 1.2 * 1.1)

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].increase(5)
        if self.status.intervals[self.name]:
            self.status.buffs["层云"].clear()
            self.status.buffs["层云"].trigger(min(self.status.ticks[self.name], 5))

    def post_cast(self):
        super().post_cast()
        self.status.buffs["层云"].clear()


class 惊雷(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "惊雷"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 31
        self.damage_rand = 6
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(80 * 1.2 * 1.1 * 1.2 * 1.1)


class 飞来(PlacementSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞来"

        self.interval_list = [16] * 10

    def post_hit(self):
        super().post_hit()
        self.status.buffs["剑气"].increase(2 * 5)
        self.status.buffs["闻踪"].trigger()


class 飞来闻踪(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞来闻踪"

        self.activate = False

        self.is_cast = False
        self.is_hit = False

        self.cd_base = 45 * 16

    @property
    def condition(self):
        return self.status.stacks["山居剑意"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["飞来"].cast()


SKILLS_MAP = {
    "通用": [三柴剑法, 四季剑法, 断潮, 破, 剑气衰减],
    "君子风": [啸日, 听雷],
    "秀水剑法": [九溪弥烟, 玉虹贯日, 黄龙吐翠],
    "灵峰剑式": [夕照雷峰, 云飞玉皇, 云飞玉皇_额外, 风来吴山, 风来吴山_引导],
    "西子情": [莺鸣柳, 云栖松, 云栖松剑气回复],
    "奇穴": [云飞玉皇_岱宗, 九溪弥烟_持续, 风来吴山_持续, 惊雷, 飞来, 飞来闻踪],
}
SKILLS = sum(SKILLS_MAP.values(), [])
