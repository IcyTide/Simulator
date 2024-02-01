from base.constant import PHYSICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, PHYSICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import Melee, CastingSkill, ChargingSkill, TriggerSkill, DotSkill, PlacementSkill, PhysicalDamage

"""
    Base Skills
"""


class 云刀(Melee):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云刀"

        self.gcd_index = self.name
        self.gcd_base = 24


class 破(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.is_cast = False
        self.is_hit = False

        self.surplus_cof = SURPLUS_COF(1024 * 1024 * (0.48 - 1))


class 识破(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "识破"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = self.name

    @property
    def condition(self):
        return self.status.stacks["身形"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["身形"].consume()
        self.status.buffs["识破"].trigger()


class 避实击虚(TriggerSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "避实击虚"

        self.is_cast = False
        self.is_hit = False

        self.probability = 0

        self.damage_base = [35, 42, 45, 50, 55, 60]
        self.damage_rand = 5
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(80),
            PHYSICAL_ATTACK_POWER_COF(100 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(120 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(160 * 0.8),
            PHYSICAL_ATTACK_POWER_COF(160),
            PHYSICAL_ATTACK_POWER_COF(200),
        ]
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 行云式(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式"

        self.is_cast = False
        self.is_hit = False

    def post_cast(self):
        super().post_cast()
        self.status.buffs["锐意"].increase(5)
        if self.status.stacks["行云式"] == 2:
            self.status.skills["行云式·三"].cast()
        elif self.status.stacks["行云式"] == 1:
            self.status.skills["行云式·二"].cast()
        else:
            self.status.skills["行云式·一"].cast()
        self.status.skills["避实击虚"].cast()


class 行云式_一(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式·一"

        self.damage_base = [180, int(180 * 1.2), int(180 * 1.5)][0]
        self.damage_rand = [15, int(15 * 1.2), int(15 * 1.5)][0]
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(135 * 1.5),
            PHYSICAL_ATTACK_POWER_COF(159 * 1.5),
            PHYSICAL_ATTACK_POWER_COF(190 * 1.5 * 1.5)
        ][0]
        self.weapon_damage_cof = [
            WEAPON_DAMAGE_COF(1024),
            WEAPON_DAMAGE_COF(1536),
            WEAPON_DAMAGE_COF(2048)
        ][0]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["行云式"].trigger()


class 行云式_二(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式·二"

        self.damage_base = [180, int(180 * 1.2), int(180 * 1.5)][1]
        self.damage_rand = [15, int(15 * 1.2), int(15 * 1.5)][1]
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(135 * 1.5),
            PHYSICAL_ATTACK_POWER_COF(159 * 1.5),
            PHYSICAL_ATTACK_POWER_COF(190 * 1.5 * 1.5)
        ][1]
        self.weapon_damage_cof = [
            WEAPON_DAMAGE_COF(1024),
            WEAPON_DAMAGE_COF(1536),
            WEAPON_DAMAGE_COF(2048)
        ][1]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["行云式"].trigger()


class 行云式_三(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式·三"

        self.damage_base = [180, int(180 * 1.2), int(180 * 1.5)][2]
        self.damage_rand = [15, int(15 * 1.2), int(15 * 1.5)][2]
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(135 * 1.5),
            PHYSICAL_ATTACK_POWER_COF(159 * 1.5),
            PHYSICAL_ATTACK_POWER_COF(190 * 1.5 * 1.5)
        ][2]
        self.weapon_damage_cof = [
            WEAPON_DAMAGE_COF(1024),
            WEAPON_DAMAGE_COF(1536),
            WEAPON_DAMAGE_COF(2048)
        ][2]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["行云式"].clear()


class 停云式(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "停云式"

        self.cd_base = 12 * 16

        self.damage_base = 405
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(240 * 1.5 * 0.9)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)

    @property
    def condition(self):
        return self.status.stacks["单手持刀"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["锐意"].increase(10)
        self.status.skills["避实击虚"].cast()


class 决云式(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "决云式"

        self.cd_base = 20 * 16

        self.damage_base = int(160 * 1.25)
        self.damage_rand = int(15 * 1.25)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(188)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["单手持刀"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["锐意"].increase(25)
        if self.status.stacks["识破"]:
            self.status.buffs["识破"].consume()
            self.status.buffs["破绽"].trigger()
            self.status.buffs["锐意"].increase(10)
        self.status.skills["避实击虚"].cast()


class 断云式(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "断云式"

        self.damage_base = int(115 * 1.5)
        self.damage_rand = int(15 * 1.5)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(380 * 0.9)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)

    @property
    def condition(self):
        return self.status.stacks["锐意"] == 100 and self.status.stacks["单手持刀"]

    def set_gcd(self):
        self.status.gcd_group[0] = self.gcd
        self.status.gcd_group[1] = self.gcd

    def post_cast(self):
        super().post_cast()
        self.status.skills["断云式-额外"].cast()
        self.status.skills["避实击虚"].cast()
        self.status.buffs["锐意"].clear()
        self.status.buffs["双手持刀"].trigger()


class 断云式_额外(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "断云式-额外"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = int(115 * 1.5 * 0.4)
        self.damage_rand = int(15 * 1.5 * 0.4)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(380 * 0.9 * 0.4)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)


class 沧浪三叠(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沧浪三叠"

        self.is_cast = False
        self.is_hit = False

        self.gcd_index = 1

    @property
    def condition(self):
        return self.status.stacks["双手持刀"]

    def post_cast(self):
        super().post_cast()
        if self.status.stacks["沧浪三叠"] == 2:
            self.status.skills["沧浪三叠·三"].cast()
        elif self.status.stacks["沧浪三叠"] == 1:
            self.status.skills["沧浪三叠·二"].cast()
        else:
            self.status.skills["沧浪三叠·一"].cast()
        self.status.skills["避实击虚"].cast()


class 沧浪三叠_一(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沧浪三叠·一"

        self.damage_base = [int(255 * 0.8), int(255 * 1.05), int(255 * 1.15)][0]
        self.damage_rand = [int(20 * 0.8), int(20 * 1.05), int(20 * 1.15)][0]
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(230 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(255 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(290 * 0.9)
        ][0]
        self.weapon_damage_cof = [
            WEAPON_DAMAGE_COF(2048),
            WEAPON_DAMAGE_COF(2560),
            WEAPON_DAMAGE_COF(3072)
        ][0]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["沧浪三叠"].trigger()


class 沧浪三叠_二(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沧浪三叠·二"

        self.damage_base = [int(255 * 0.8), int(255 * 1.05), int(255 * 1.15)][1]
        self.damage_rand = [int(20 * 0.8), int(20 * 1.05), int(20 * 1.15)][1]
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(230 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(255 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(290 * 0.9)
        ][1]
        self.weapon_damage_cof = [
            WEAPON_DAMAGE_COF(2048),
            WEAPON_DAMAGE_COF(2560),
            WEAPON_DAMAGE_COF(3072)
        ][1]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["沧浪三叠"].trigger()


class 沧浪三叠_三(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "沧浪三叠·三"

        self.damage_base = [int(255 * 0.8), int(255 * 1.05), int(255 * 1.15)][2]
        self.damage_rand = [int(20 * 0.8), int(20 * 1.05), int(20 * 1.15)][2]
        self.attack_power_cof = [
            PHYSICAL_ATTACK_POWER_COF(230 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(255 * 0.9),
            PHYSICAL_ATTACK_POWER_COF(290 * 0.9)
        ][2]
        self.weapon_damage_cof = [
            WEAPON_DAMAGE_COF(2048),
            WEAPON_DAMAGE_COF(2560),
            WEAPON_DAMAGE_COF(3072)
        ][2]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["沧浪三叠"].clear()


class 横云断浪(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "横云断浪"

        self.cd_base = 12 * 16

        self.gcd_index = self.name

        self.damage_base = int(1203 * 0.6)
        self.damage_rand = int(1473 * 0.1 * 0.6)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(450 * 0.8)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(3072)

    @property
    def condition(self):
        return self.status.stacks["双手持刀"]

    def set_gcd(self):
        self.status.gcd_group[1] = self.gcd

    def post_cast(self):
        super().post_cast()
        for _ in range(self.status.stacks["破绽"]):
            self.status.skills["流血"].cast()
        self.status.skills["避实击虚"].cast()


class 流血(DotSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流血"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 3

        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(200, self.interval_base)


class 孤锋破浪(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "孤锋破浪"

        self.is_cast = False
        self.hit_with_cast = True

        self.gcd_index = 1

        self.damage_base = 290 * 5
        self.damage_rand = 15 * 5
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(650 * 0.9 * 0.85 * 0.9 * 1.1)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(3072)

    @property
    def condition(self):
        return self.status.stacks["双手持刀"]

    def post_hit(self):
        super().post_hit()
        self.status.skills["避实击虚"].cast()
        self.status.skills["破"].cast()

    def post_cast(self):
        super().post_cast()
        self.status.buffs["单手持刀"].trigger()


class 留客雨(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "留客雨"

        self.cd_base = 6 * 16

        self.gcd_index = self.name

        self.damage_base = int(160 * 1.1)
        self.damage_rand = int(15 * 1.1)
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(200)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["单手持刀"]

    def post_cast(self):
        super().post_cast()
        self.status.gcd_group[0] = max(0, self.status.gcd_group[0] - 16)
        self.status.skills["避实击虚"].cast()


class 触石雨(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "触石雨"

        self.cd_base = 30 * 16

        self.gcd_index = self.name

        self.damage_base = 180
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(200)

    @property
    def condition(self):
        return self.status.stacks["单手持刀"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["避实击虚"].cast()


class 驰风八步(CastingSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "驰风八步"

        self.cd_base = 30 * 16

        self.gcd_index = self.name

        self.damage_base = 25
        self.damage_rand = 5
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(45)

    def post_cast(self):
        super().post_cast()
        self.status.skills["避实击虚"].cast()


class 游风飘踪(CastingSkill, ChargingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "游风飘踪"

        self.energy = 2
        self.cd_base = 50 * 16 - 7 * 16

        self.gcd_index = self.name


class 灭影追风(CastingSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "灭影追风"

        self.cd_base = 20 * 16
        self.gcd_index = self.name

    def post_cast(self):
        super().post_cast()
        self.status.buffs["灭影追风"].trigger()


"""
    Talent Skills
"""


class 界破(PlacementSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "界破"

        self.is_cast = False
        self.is_hit = False

        self.interval_list = [32]

        self.damage_base = 160
        self.damage_rand = 317
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(350 * 1.1)


class 潋风_携刃(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "潋风·携刃"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 78
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(150 * 1.1)

    def post_cast(self):
        super().post_cast()
        self.status.buffs["锐意"].increase(5)
        self.status.skills["留客雨"].reset()


class 潋风_拓锋(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "潋风·拓锋"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 78
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(300 * 1.1)


class 截辕(PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "截辕"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 77
        self.damage_rand = 25
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(340 * 0.75)

    def post_cast(self):
        super().post_cast()
        self.status.skills["截辕-持续"].cast()


class 截辕_持续(DotSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "截辕-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 32
        self.tick_base = 6

        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(450, self.interval_base)


class 行云式_神兵(TriggerSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "行云式·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 102 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(60)


class 背水沉舟_持续(DotSkill, PhysicalDamage):
    def __init__(self, status):
        super().__init__(status)
        self.name = "背水沉舟-持续"

        self.is_cast = False
        self.is_hit = False

        self.interval_base = 3 * 16
        self.tick_base = 6

        self.damage_base = 1
        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(380, self.interval_base)


SKILLS_MAP = {
    "通用": [云刀, 破, 识破, 避实击虚, 行云式_神兵],
    "流云势法": [行云式, 行云式_一, 行云式_二, 行云式_三, 停云式, 决云式, 断云式, 断云式_额外],
    "破浪三式": [沧浪三叠, 沧浪三叠_一, 沧浪三叠_二, 沧浪三叠_三, 横云断浪, 流血, 孤锋破浪],
    "骤雨劲": [留客雨, 触石雨],
    "游风步": [驰风八步, 游风飘踪, 灭影追风],
    "奇穴": [界破, 潋风_携刃, 潋风_拓锋, 截辕, 截辕_持续],
}
SKILLS = sum(SKILLS_MAP.values(), [])
