from base.constant import PHYSICAL_ATTACK_POWER_COF, WEAPON_DAMAGE_COF, PHYSICAL_DOT_ATTACK_POWER_COF, SURPLUS_COF
from base.skill import PhysicalSkill, Skill

"""
    Base Skills
"""


class 霜风刀法(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "霜风刀法"

        self.gcd_index = self.name

        self.damage_base = 1

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(16)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)


class 秀明尘身(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "秀明尘身"

        self.is_hit = False

        self.gcd_base = 0
        self.gcd_index = self.name
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["秀明尘身"].trigger()
        self.status.buffs["松烟竹雾"].clear()
        self.status.buffs["雪絮金屏"].clear()


class 松烟竹雾(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "松烟竹雾"

        self.is_hit = False

        self.gcd_base = 0
        self.gcd_index = self.name
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["秀明尘身"].clear()
        self.status.buffs["松烟竹雾"].trigger()
        self.status.buffs["雪絮金屏"].clear()


class 雪絮金屏(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "雪絮金屏"

        self.is_hit = False

        self.gcd_base = 0
        self.gcd_index = self.name
        self.cd_base = 3 * 16

    @property
    def condition(self):
        return not self.status.stacks[self.name]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["秀明尘身"].clear()
        self.status.buffs["松烟竹雾"].clear()
        self.status.buffs["雪絮金屏"].trigger()


class 破(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 1
        self.level_params = {
            "surplus_cof": [SURPLUS_COF(1024 * 1024 * (n - 1)) for n in (0.1375, 0.275, 0.875)]
        }


class 雷走风切(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "雷走风切"

        self.gcd_index = self.name
        self.cd_base = 16 * 16

        self.damage_base = 175
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(224 * 0.8 * 0.7)

    @property
    def condition(self):
        return not self.status.stacks["雪絮金屏"]


class 上将军印(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "上将军印"

        self.hit_with_cast = True

        self.cd_base = 18 * 16
        self.interval_list = [4, 6, 6, 6, 6]

        self.damage_base = 300
        self.damage_rand = 15
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 0.9 * 1.1 * 1.05)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]


class 破釜沉舟(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "破釜沉舟"

        self.is_overdraw = True

        self.cd_base = 9 * 16
        self.energy = 2

        self.damage_base = 350
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(400 * 0.9 * 0.95 * 1.1 * 1.15)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(2048)

    @property
    def condition(self):
        return self.status.stacks["秀明尘身"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["破"].cast(3)
        if self.status.stacks["沉夜重雪"]:
            self.recharge()
            self.status.skills["背水沉舟-持续"].cast()


class 闹须弥_持续(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "闹须弥-持续"

        self.is_cast = False
        self.is_hit = False

        self.is_snapshot = True

        self.count_base = 8
        self.interval_base = 48

        self.damage_base = 1
        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(280, self.interval_base)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["闹须弥-持续"].trigger()


class 闹须弥(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "闹须弥"

        self.is_hit = False

        self.cd_base = 25 * 16

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def pre_cast(self):
        super().pre_cast()
        self.status.skills["闹须弥-持续"].cast()


class 擒龙六斩(Skill):
    related_skills = ["逐鹰式"]

    def __init__(self, status):
        super().__init__(status)
        self.name = "擒龙六斩"

        self.cd_base = 10 * 16

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def recharge(self):
        super().recharge()
        for skill in self.related_skills:
            self.status.skills[skill].activate = False

    def post_cast(self):
        super().post_cast()
        self.status.skills["惊燕式"].cast()


class 惊燕式(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "惊燕式"

        self.interval_list = [3, 7]

        self.damage_base = 80
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(64 * 1.3 * 1.2)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def post_hit(self):
        self.attack_power_cof_gain += 0.25
        super().post_hit()

    def post_cast(self):
        super().post_cast()
        self.attack_power_cof_gain -= 0.25 * self.count
        self.status.skills["破"].cast(2)
        self.status.skills["逐鹰式"].activate = True


class 逐鹰式(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "逐鹰式"

        self.activate = False

        self.interval_list = [4, 6]

        self.damage_base = 80
        self.damage_rand = 10
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(64 * 1.3 * 1.2)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    @property
    def condition(self):
        return self.status.skills['擒龙六斩'].available

    def pre_cast(self):
        super().pre_cast()
        self.status.cds["擒龙六斩"] += self.status.skills["擒龙六斩"].cd
        self.status.energies["擒龙六斩"] -= 1

    def post_hit(self):
        self.attack_power_cof_gain += 0.5
        super().post_hit()

    def post_cast(self):
        super().post_cast()
        self.attack_power_cof_gain -= 0.5 * self.count
        self.status.skills["破"].cast(2)
        self.activate = False


class 坚壁清野_持续(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "坚壁清野-持续"

        self.is_cast = False
        self.hit_with_cast = True

        self.interval_list = [16] * 10

        self.damage_base = 250
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(160 * 1.1)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["坚壁清野-持续"].trigger()


class 坚壁清野(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "坚壁清野"

        self.cd_base = 30 * 16

        self.damage_base = 430
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(288 * 1.2 * 0.7 * 1.1)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["坚壁清野-持续"].cast()


class 刀啸风吟(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "刀啸风吟"

        self.interval_base = 24

        self.damage_base = 250
        self.damage_rand = 20

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(256 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05)

    @property
    def condition(self):
        return self.status.stacks["雪絮金屏"]

    def post_cast(self):
        super().post_cast()
        self.status.skills["破"].cast(1)


"""
    Talent Skills
"""


class 见尘(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "见尘"

        self.is_cast = False
        self.is_hit = False

        self.interval_list = [5, 6, 6, 6, 6]

        self.damage_base = int(100 * 1.45 * 0.5)
        self.damage_rand = int(10 * 1.45 * 0.5)

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(60 * 1.45 * 1.1 * 0.7)
        # self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024 * 1.45 * 0.25)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["见尘"].trigger()


class 楚歌(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "楚歌"

        self.is_cast = False
        self.is_hit = False

        self.damage_base = 55
        self.damage_rand = 5
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(1200 * 0.8)


class 绝期(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "绝期"

        self.is_cast = False
        self.is_hit = False

        self.probability = 306 / 1024

        self.damage_base = 250
        self.damage_rand = 20
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(120)

    def post_cast(self):
        super().post_cast()
        self.status.skills["闹须弥-持续"].cast()


class 降麒式(Skill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式"

        self.activate = False

        self.gcd_base = 0

    @property
    def condition(self):
        return self.status.stacks["松烟竹雾"]

    def post_cast(self):
        super().post_cast()
        self.status.buffs["降麒式-计数"].clear()
        self.status.buffs["降麒式-就绪"].clear()
        self.status.buffs["降麒式"].trigger()
        self.status.skills["降麒式-持续"].cast()


class 降麒式_持续(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "降麒式-持续"

        self.is_cast = False
        self.hit_with_cast = True

        self.interval_list = [16] * 15

        self.damage_base = 50
        self.damage_rand = 5

        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(60 * 2)
        self.weapon_damage_cof = WEAPON_DAMAGE_COF(1024)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["降麒式-持续"].trigger()


class 上将军印_神兵(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "上将军印·神兵"

        self.is_cast = False
        self.is_hit = False

        self.probability = 102 / 1024

        self.damage_base = 20
        self.damage_rand = 2
        self.attack_power_cof = PHYSICAL_ATTACK_POWER_COF(25)


class 背水沉舟_持续(PhysicalSkill):
    def __init__(self, status):
        super().__init__(status)
        self.name = "背水沉舟-持续"

        self.is_cast = False
        self.is_hit = False

        self.is_stack = True
        self.is_snapshot = True

        self.interval_base = 3 * 16
        self.count_base = 6

        self.damage_base = 1
        self.attack_power_cof = PHYSICAL_DOT_ATTACK_POWER_COF(380, self.interval_base)

    def pre_cast(self):
        super().pre_cast()
        self.status.buffs["背水沉舟-持续"].trigger()


SKILLS_MAP = {
    "通用": [霜风刀法, 破],
    "殷雷腿": [雷走风切],
    "秀明尘身": [秀明尘身, 上将军印, 破釜沉舟],
    "松烟竹雾": [松烟竹雾, 闹须弥, 闹须弥_持续, 擒龙六斩, 惊燕式, 逐鹰式],
    "雪絮金屏": [雪絮金屏, 刀啸风吟, 坚壁清野_持续, 坚壁清野],
    "奇穴": [见尘, 楚歌, 绝期, 降麒式, 降麒式_持续],
}
SKILLS = sum(SKILLS_MAP.values(), [])
