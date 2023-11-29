from base.buff import Buff
from general.buffs import PhysicalCriticalSet


class ShuoQi(PhysicalCriticalSet):
    def __init__(self):
        super().__init__()
        self.name = "朔气"


class JianWu(Buff):
    def __init__(self):
        super().__init__()
        self.name = "剑舞"

        self.stack_add = 2
        self.stack_max = 10

        self.value = 31 / 1024

    def add(self):
        super().add()
        self.status.attribute.magical_attack_power_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.magical_attack_power_gain -= self.value


class JiQuDot(Buff):
    def __init__(self):
        super().__init__()
        self.name = "急曲·持续"

        self.is_dot = True

        self.stack_max = 3


class FanYinJiJie(Buff):
    def __init__(self):
        super().__init__()
        self.name = "繁音急节"

        self.duration = 20 * 16
        self.duration_max = 20 * 16

        self.value = 461 / 1024

    def add(self):
        super().add()
        self.status.attribute.magical_attack_power_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.magical_attack_power_gain -= self.value


class ZhenShang(Buff):
    def __init__(self):
        super().__init__()
        self.name = "枕上"

        self.duration = 16 * 15
        self.duration_max = 16 * 15
        self.stack_max = 5
        self.value = 10 / 1024

    def add(self):
        super().add()
        self.status.attribute.haste_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.haste_gain -= self.value


class GuangLingYue(Buff):
    def __init__(self):
        super().__init__()
        self.name = "广陵月"

        self.duration = 16 * 6
        self.duration_max = 16 * 6

    def add(self):
        super().add()
        self.status.skills["剑破虚空"].jian_wu = False

    def remove(self):
        super().remove()
        self.status.skills["剑破虚空"].jian_wu = True
        self.status.buffs["广陵月·会效"].clear()


class GuangLingYueCritical(Buff):
    def __init__(self):
        super().__init__()
        self.name = "广陵月·会效"

        self.duration = 16 * 6
        self.duration_max = 16 * 6
        self.stack_max = 10

        self.value = 20 / 1024

    def add(self):
        super().add()
        self.status.attribute.magical_critical_power_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.magical_critical_power_gain -= self.value


class LiuYu(Buff):
    def __init__(self):
        super().__init__()
        self.name = "流玉"

        self.duration = 16 * 5
        self.duration_max = 16 * 5

        self.value = 512 / 1024

    def add(self):
        super().add()
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value


class ChaiYanCount(Buff):
    def __init__(self):
        super().__init__()
        self.name = "钗燕·计数"

        self.stack_max = 3

        self.count_list = ["江海凝光·钗燕", "玳弦急曲·钗燕", "剑破虚空·钗燕", "剑气长江·钗燕", "剑影留痕·钗燕"]

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 3:
            self.clear()
            for buff in self.count_list:
                self.status.buffs[buff].clear()
            self.status.skills["钗燕"].cast()


class JiangHaiNingGuangChaiYan(Buff):
    def __init__(self):
        super().__init__()
        self.name = "江海凝光·钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕·计数"].trigger()


class DaiXianJiQuChaiYan(Buff):
    def __init__(self):
        super().__init__()
        self.name = "玳弦急曲·钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕·计数"].trigger()


class JianPoXuKongChaiYan(Buff):
    def __init__(self):
        super().__init__()
        self.name = "剑破虚空·钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕·计数"].trigger()


class JianQiChangJiangChaiYan(Buff):
    def __init__(self):
        super().__init__()
        self.name = "剑气长江·钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕·计数"].trigger()


class JianYingLiuHenChaiYan(Buff):
    def __init__(self):
        super().__init__()
        self.name = "剑影留痕·钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕·计数"].trigger()


class YingXiu(Buff):
    def __init__(self):
        super().__init__()
        self.name = "盈袖"

        self.duration = 20 * 16
        self.duration_max = 20 * 16

        self.value = 204 / 1024

    def add(self):
        super().add()
        self.status.attribute.haste_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.haste_gain -= self.value


class HuaBing(Buff):
    def __init__(self):
        super().__init__()
        self.name = "化冰"

        self.duration = 180 * 16
        self.duration_max = 180 * 16

        self.value = 164 / 1024

    def add(self):
        super().add()
        self.status.attribute.pve_addition += self.value

    def remove(self):
        super().remove()
        self.status.attribute.pve_addition -= self.value


class HuaBingCount(Buff):
    def __init__(self):
        super().__init__()
        self.name = "化冰·计数"

        self.duration = 16
        self.duration_max = 16
        self.stack_max = 3

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 3:
            self.clear()
            self.status.skills["化冰"].cast()


class YeTian(Buff):
    def __init__(self):
        super().__init__()
        self.name = "夜天"

        self.duration = 2 * 16
        self.duration_max = 2 * 16

        self.value = 102 / 1024

    def add(self):
        super().add()
        self.status.attribute.damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.attribute.damage_addition -= self.value


class JianShenWuWo(Buff):
    def __init__(self):
        super().__init__()
        self.name = "剑神无我"

        self.duration = 20 * 16
        self.duration_max = 20 * 16


class QiongXiaoCD(Buff):
    def __init__(self):
        super().__init__()
        self.name = "琼霄·冷却"

        self.duration = 20 * 16
        self.duration_max = 20 * 16


class NingHua(Buff):
    def __init__(self):
        super().__init__()
        self.name = "凝华"

        self.stack_add = 3
        self.stack_max = 9


class ShuangJiang15(Buff):
    def __init__(self):
        super().__init__()
        self.name = "霜降·15%"

        self.value = 154 / 1024

    def add(self):
        super().add()
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value


class ShuangJiang30(Buff):
    def __init__(self):
        super().__init__()
        self.name = "霜降·30%"

        self.value = 307 / 1024

    def add(self):
        super().add()
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value


class ShuangJiang45(Buff):
    def __init__(self):
        super().__init__()
        self.name = "霜降·45%"

        self.value = 461 / 1024

    def add(self):
        super().add()
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value


BUFFS = []
