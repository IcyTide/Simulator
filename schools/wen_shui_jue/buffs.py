from base.buff import Buff, GainBuff, ExtendBuff, CountBuff, CDBuff, PlacementBuff, TriggerBuff, Energy
from general.buffs import 外功双会套装


class 器攻(外功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "器攻"


class 剑气(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑气"

        self.stack_max = 100


class 问水诀(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "问水诀"


class 山居剑意(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "山居剑意"

    def add(self):
        super().add()
        self.status.skills["断潮"].probability = 1
        for attr, value in self.status.attribute.primary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) - value)
        for attr, value in self.status.attribute.secondary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) + value)

    def remove(self):
        super().remove()
        self.status.skills["断潮"].probability = 717 / 1024
        for attr, value in self.status.attribute.secondary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) - value)
        for attr, value in self.status.attribute.primary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) + value)

    def gain(self, level, stack):
        super().gain(level, stack)
        for attr, value in self.status.attribute.primary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) - value)
        for attr, value in self.status.attribute.secondary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) + value)

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for attr, value in self.status.attribute.secondary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) - value)
        for attr, value in self.status.attribute.primary_weapon_attribute.items():
            setattr(self.status.attribute, attr, getattr(self.status.attribute, attr) + value)


class 莺鸣(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "莺鸣"

        self.duration = 16 * 8

        self.value = 0.2

    def add(self):
        super().add()
        self.status.buffs["剑气"].stack_max += 100
        self.status.buffs["剑气"].increase(135)
        self.status.attribute.physical_critical_strike_gain += self.value

    def remove(self):
        super().remove()
        self.status.buffs["剑气"].stack_max -= 100
        self.status.attribute.physical_critical_strike_gain -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.value


class 云栖松剑气回复(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "云栖松剑气回复"


class 岱宗(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "岱宗"

        self.duration = 16 * 15

        self.stack_max = 3

        self.value = 82 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_power_gain += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_power_gain -= self.value * stack


class 夜雨(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "夜雨"

        self.duration = 16 * 5

    def add(self):
        super().add()
        self.status.skills["云飞玉皇"].surplus_level = 4
        self.status.skills["云飞玉皇"].direct = True

    def remove(self):
        super().remove()
        self.status.skills["云飞玉皇"].surplus_level = 1
        self.status.skills["云飞玉皇"].direct = False


class 九溪弥烟_持续(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "九溪弥烟-持续"


class 凤鸣(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凤鸣"

        self.stack_add = 2
        self.stack_max = 2

        self.duration = 16 * 10

        self.values = [0.15, 154 / 1024]

        self.gain_group = ["夕照雷峰", "云飞玉皇", "云飞玉皇-额外"]

    def add(self):
        super().add()
        self.status.skills["夕照雷峰"].skill_critical_strike += self.values[0]
        self.status.skills["云飞玉皇"].skill_critical_strike += self.values[0]

    def remove(self):
        super().remove()
        self.status.skills["夕照雷峰"].skill_critical_strike -= self.values[0]
        self.status.skills["云飞玉皇"].skill_critical_strike -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["夕照雷峰"].skill_critical_strike += self.values[0]
        self.status.skills["云飞玉皇"].skill_critical_strike += self.values[0]
        self.status.skills["云飞玉皇-额外"].skill_critical_strike += self.values[0]
        self.status.skills["夕照雷峰"].skill_damage_addition += self.values[1]
        self.status.skills["云飞玉皇"].skill_damage_addition += self.values[1]
        self.status.skills["云飞玉皇-额外"].skill_damage_addition += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["夕照雷峰"].skill_critical_strike -= self.values[0]
        self.status.skills["云飞玉皇"].skill_critical_strike -= self.values[0]
        self.status.skills["云飞玉皇-额外"].skill_critical_strike -= self.values[0]
        self.status.skills["夕照雷峰"].skill_damage_addition -= self.values[1]
        self.status.skills["云飞玉皇"].skill_damage_addition -= self.values[1]
        self.status.skills["云飞玉皇-额外"].skill_damage_addition -= self.values[1]


class 造化(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "造化"

        self.duration = 16 * 10

        self.values = [102 / 1024, 154 / 1024]

        self.gain_group = ["夕照雷峰", "云飞玉皇", "云飞玉皇-额外"]

    def add(self):
        super().add()
        self.status.skills["夕照雷峰"].cost -= 2
        self.status.skills["云飞玉皇"].cost -= 2

    def remove(self):
        super().remove()
        self.status.skills["夕照雷峰"].cost += 2
        self.status.skills["云飞玉皇"].cost += 2

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["夕照雷峰"].skill_damage_addition += self.values[level - 1]
        self.status.skills["云飞玉皇"].skill_damage_addition += self.values[level - 1]
        self.status.skills["云飞玉皇-额外"].skill_damage_addition += self.values[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["夕照雷峰"].skill_damage_addition -= self.values[level - 1]
        self.status.skills["云飞玉皇"].skill_damage_addition -= self.values[level - 1]
        self.status.skills["云飞玉皇-额外"].skill_damage_addition -= self.values[level - 1]


class 层云(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "层云"

        self.duration = 128

        self.values = [72 / 1024, 143 / 1024, 215 / 1024, 287 / 1024, 358 / 1024]

        self.gain_group = ["风来吴山-持续"]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["风来吴山-持续"].skill_damage_addition += self.values[level - 1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["风来吴山-持续"].skill_damage_addition -= self.values[level - 1]


class 风来吴山_持续(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "风来吴山-持续"


class 惊雷(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "惊雷"

        self.duration = 10 * 16


class 雾锁(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "雾锁"

        self.duration = 80

        self.value = 614 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_shield_ignore += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_shield_ignore -= self.value


class 碧归(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "碧归"

        self.stack_max = 4

        self.duration = 16 * 9

        self.value = 307 / 1024

        self.gain_group = ["夕照雷峰", "云飞玉皇", "云飞玉皇-额外"]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.skills["夕照雷峰"].skill_damage_addition += self.value
        self.status.skills["云飞玉皇"].skill_damage_addition += self.value
        self.status.skills["云飞玉皇-额外"].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.skills["夕照雷峰"].skill_damage_addition -= self.value
        self.status.skills["云飞玉皇"].skill_damage_addition -= self.value
        self.status.skills["云飞玉皇-额外"].skill_damage_addition -= self.value


class 碧归_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "碧归-计数"

        self.duration = 24

        self.stack_max = 2

    def add(self):
        super().add()
        if self.status.stacks[self.name] == self.stack_max:
            self.status.buffs["碧归"].trigger()
            self.clear()


class 如风(ExtendBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "如风"

        self.duration_add = 16 * 5
        self.duration = 16 * 10

        self.value = 82 / 1024

    def add(self):
        super().add()
        self.status.attribute.haste_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.haste_gain -= self.value


class 飞来(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞来"

        self.value = 30 / 1024 * 5

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_power_gain -= self.value


class 闻踪(GainBuff, ExtendBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "闻踪"

        self.duration_add = 8 * 5
        self.duration = 0
        self.values = [0.1, 410 / 1024]

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.values[0]

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.values[0]

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.values[0]
        self.status.skills["断潮"].skill_damage_addition += self.values[1]

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.values[0]
        self.status.skills["断潮"].skill_damage_addition -= self.values[1]


class 螭尘(TriggerBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "螭尘"

        self.probability = 31 / 1024

    @property
    def condition(self):
        return not self.status.stacks["螭尘-冷却"]

    def add(self):
        super().add()
        self.status.skills["云飞玉皇"].reset()
        self.status.skills["夕照雷峰"].direct = True
        self.status.skills["云飞玉皇"].direct = True
        self.status.buffs["螭尘-冷却"].trigger()

    def remove(self):
        super().remove()

        self.status.skills["夕照雷峰"].direct = False
        self.status.skills["云飞玉皇"].direct = False


class 螭尘_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "螭尘-冷却"

        self.duration = 30 * 16


BUFFS = [
    器攻, 剑气, 问水诀, 山居剑意, 莺鸣, 云栖松剑气回复,
    岱宗, 夜雨, 九溪弥烟_持续, 凤鸣, 造化, 层云, 风来吴山_持续, 惊雷, 雾锁, 碧归, 碧归_计数, 如风, 飞来, 闻踪,
]
