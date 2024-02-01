from base.buff import Buff, GainBuff, DotBuff, CountBuff, CDBuff, PlacementBuff, Energy
from general.buffs import 内功双会套装


class 佛吼(内功双会套装):
    def __init__(self, status):
        super().__init__(status)
        self.name = "佛吼"


class 神机(Energy):
    def __init__(self, status):
        super().__init__(status)
        self.name = "神机"

        self.stack_max = 100


class 气魄(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "气魄"

        self.duration = 20 * 16
        self.stack_max = 5

        self.value = 20 / 1024

        self.gain_attribute = "attack_power"

    def add(self):
        super().add()
        self.status.attribute.spunk_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.spunk_gain -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.spunk_gain += self.value * stack
        self.status.attribute.strength_gain += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.spunk_gain -= self.value * stack
        self.status.attribute.strength_gain -= self.value * stack


class 天女散花_伤害(PlacementBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天女散花-伤害"


class 化血(DotBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化血"


class 千机变(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "千机变"

    def add(self):
        super().add()
        self.status.skills["连弩"].cast()

    def remove(self):
        super().remove()
        self.status.skills["连弩"].post_cast()


class 暗藏杀机_一(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗藏杀机-一"

        self.duration = 60 * 16

    def add(self):
        super().add()
        self.status.buffs["暗藏杀机-计数"].trigger()

    def remove(self):
        super().remove()
        self.status.buffs["暗藏杀机-计数"].consume()


class 暗藏杀机_二(暗藏杀机_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗藏杀机-二"


class 暗藏杀机_三(暗藏杀机_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗藏杀机-三"


class 暗藏杀机_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "暗藏杀机-计数"

        self.stack_max = 3


class 天绝地灭_冷却(CDBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-冷却"

        self.duration = 40


class 天绝地灭_计数(CountBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-计数"

        self.stack_max = 5

        self.skill_list = []


class 天绝地灭_持续_一(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-持续-一"

        self.duration = 17 * 16 + 10

    def add(self):
        super().add()
        self.status.buffs["天绝地灭-计数"].trigger()
        self.status.buffs["天绝地灭-计数"].skill_list.append(self.name)

    def remove(self):
        super().remove()
        self.status.buffs["天绝地灭-计数"].consume()
        self.status.buffs["天绝地灭-计数"].skill_list.remove(self.name)


class 天绝地灭_持续_二(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-持续-二"


class 天绝地灭_持续_三(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-持续-三"


class 扬威(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "扬威"

        self.duration = 15 * 16

        self.value = 512 / 1024

        self.gain_attribute = "attack_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_attack_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_attack_power_gain -= self.value


class 鬼斧弹药(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "鬼斧弹药"

        self.duration = 1920
        self.stack_max = 50


class 心无旁骛(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "心无旁骛"

        self.duration = 10 * 16

        self.sub_buffs = ["心无旁骛-会心", "心无旁骛-会效"]

    def add(self):
        super().add()
        self.status.skills["神机回复"].gain = 20

    def remove(self):
        super().remove()
        self.status.skills["神机回复"].gain = 10


class 心无旁骛_会心(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "心无旁骛-会心"

        self.value = 0.15

        self.gain_attribute = "critical_strike"

    def add(self):
        super().add()
        self.status.attribute.physical_critical_strike_gain += self.value

    def remove(self):
        super().remove()
        self.status.attribute.physical_critical_strike_gain -= self.value

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_strike_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_strike_gain -= self.value


class 心无旁骛_会效(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "心无旁骛-会效"

        self.value = 300 / 1024

        self.gain_attribute = "critical_power"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.physical_critical_power_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.physical_critical_power_gain -= self.value


class 血影留痕(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "血影留痕"

        self.duration = 48


class 天风汲雨(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天风汲雨"

        self.duration = 64


class 弩心(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "弩心"

        self.duration = 96
        self.value = 154 / 1024

        self.gain_attribute = "overcome"


    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_overcome_gain += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_overcome_gain -= self.value


class 擘两分星_内功伤害(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "擘两分星-内功伤害"

        self.value = 205 / 1024

        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.magical_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.magical_damage_addition -= self.value


class 擘两分星_陷阱伤害(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "擘两分星-陷阱伤害"

        self.value = 103 / 1024

        self.gain_skills = ["天绝地灭-伤害", "血影留痕-天绝地灭", "天风汲雨", "图穷匕见", "血影留痕-图穷匕见"]
        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition += self.value


class 流星赶月_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流星赶月-冷却"

        self.duration = 8 * 16


class 聚精凝神(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "聚精凝神"

        self.value = 204 / 1024

    def add(self):
        super().add()
        self.status.attribute.haste_gain += self.value
        self.status.buffs["天绝地灭-冷却"].duration -= 1

    def remove(self):
        super().remove()
        self.status.attribute.haste_gain -= self.value
        self.status.buffs["天绝地灭-冷却"].duration += 1


class 杀机断魂_千机变(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "杀机断魂-千机变"

        self.value = 103 / 1024
        self.stack_max = 5

        self.gain_skills = ["连弩"]
        self.gain_attribute = "damage_addition"

    def gain(self, level, stack):
        super().gain(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition += self.value * stack

    def revoke(self, level, stack):
        super().revoke(level, stack)
        for skill in self.gain_skills:
            self.status.skills[skill].skill_damage_addition -= self.value * stack


class 杀机断魂_天绝地灭(杀机断魂_千机变):
    def __init__(self, status):
        super().__init__(status)
        self.name = "杀机断魂-天绝地灭"

        self.value = 206 / 1024
        self.stack_max = 3

        self.gain_skills = ["天绝地灭-伤害", "血影留痕-天绝地灭", "天风汲雨"]
        self.gain_attribute = "damage_addition"


class 杀机断魂_暗藏杀机(杀机断魂_千机变):
    def __init__(self, status):
        super().__init__(status)
        self.name = "杀机断魂-暗藏杀机"

        self.value = 309 / 1024

        self.gain_skills = ["图穷匕见", "血影留痕-图穷匕见"]
        self.gain_attribute = "damage_addition"


class 催寒(GainBuff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "催寒"

        self.stack_add = 2
        self.stack_max = 2

        self.value = 410 / 1024

    def gain(self, level, stack):
        super().gain(level, stack)
        self.status.attribute.all_shield_ignore += self.value

    def revoke(self, level, stack):
        super().revoke(level, stack)
        self.status.attribute.all_shield_ignore -= self.value


class 诡鉴冥微_一(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诡鉴冥微-一"

        self.duration = 40 * 16

    def remove(self):
        super().remove()
        self.status.skills["天绝地灭-诡鉴-一"].post_cast()
        self.status.buffs["天绝地灭-诡鉴-一"].clear()


class 诡鉴冥微_二(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诡鉴冥微-二"

        self.duration = 40 * 16

    def remove(self):
        super().remove()
        self.status.skills["天绝地灭-诡鉴-二"].post_cast()
        self.status.buffs["天绝地灭-诡鉴-二"].clear()


class 天绝地灭_诡鉴_一(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-诡鉴-一"

    def remove(self):
        super().remove()
        self.status.buffs["诡鉴冥微-冷却-一"].trigger()


class 天绝地灭_诡鉴_二(天绝地灭_持续_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "天绝地灭-诡鉴-二"

    def remove(self):
        super().remove()
        self.status.buffs["诡鉴冥微-冷却-一"].trigger()


class 诡鉴冥微_冷却_一(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诡鉴冥微-冷却-一"

        self.duration = 10 * 16


class 诡鉴冥微_冷却_二(诡鉴冥微_冷却_一):
    def __init__(self, status):
        super().__init__(status)
        self.name = "诡鉴冥微-冷却-二"


BUFFS = [佛吼, 神机, 气魄, 天女散花_伤害, 化血, 千机变, 暗藏杀机_一, 暗藏杀机_二, 暗藏杀机_三, 暗藏杀机_计数, 天绝地灭_冷却,
         天绝地灭_计数, 天绝地灭_持续_一, 天绝地灭_持续_二, 天绝地灭_持续_三, 扬威, 鬼斧弹药, 心无旁骛, 心无旁骛_会心, 心无旁骛_会效,
         血影留痕, 天风汲雨, 弩心, 擘两分星_内功伤害, 擘两分星_陷阱伤害, 流星赶月_冷却, 聚精凝神, 杀机断魂_千机变, 杀机断魂_天绝地灭,
         杀机断魂_暗藏杀机, 催寒, 诡鉴冥微_一, 诡鉴冥微_二, 天绝地灭_诡鉴_一, 天绝地灭_诡鉴_二, 诡鉴冥微_冷却_一, 诡鉴冥微_冷却_二]
