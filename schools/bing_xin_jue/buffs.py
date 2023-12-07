from base.buff import Buff
from general.buffs import MagicalCriticalSet


class 嗔怒(MagicalCriticalSet):
    def __init__(self, status):
        super().__init__(status)
        self.name = "嗔怒"


class 剑舞(Buff):
    def __init__(self, status):
        super().__init__(status)
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


class 满堂(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "满堂"

        self.stack_add = 5
        self.stack_max = 5

        self.duration = 15 * 16
        self.duration_max = 15 * 16

        self.value1 = 0.08
        self.value2 = 21 / 1024

    def add(self):
        super().add()
        self.status.attribute.magical_critical_strike_gain += self.value1
        self.status.attribute.magical_critical_power_gain += self.value2

    def remove(self):
        super().remove()
        self.status.attribute.magical_critical_strike_gain -= self.value1
        self.status.attribute.magical_critical_power_gain -= self.value2


class 急曲_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "急曲-持续"

        self.is_dot = True

        self.stack_max = 3


class 繁音急节(Buff):
    def __init__(self, status):
        super().__init__(status)
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


class 枕上(Buff):
    def __init__(self, status):
        super().__init__(status)
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


class 广陵月(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月"

        self.duration = 16 * 6
        self.duration_max = 16 * 6

    def add(self):
        super().add()
        self.status.skills["剑破虚空"].jian_wu = False

    def remove(self):
        super().remove()
        self.status.skills["剑破虚空"].jian_wu = True
        self.status.buffs["广陵月-会效"].clear()


class 广陵月_会效(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "广陵月-会效"

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


class 流玉(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉"

        self.duration = 16 * 5
        self.duration_max = 16 * 5

        self.value = 512 / 1024

    def add(self):
        super().add()
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value
        self.status.skills["玳弦急曲-新妆"].skill_damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value
        self.status.skills["玳弦急曲-新妆"].skill_damage_addition -= self.value


class 流玉_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "流玉-持续"

        self.is_dot = True


class 钗燕_计数(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "钗燕-计数"

        self.stack_max = 3
        self.duration = 6 * 16
        self.duration_max = 6 * 16

        self.count_list = []

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 3:
            self.status.skills["钗燕"].cast()
            self.status.skills["急曲-持续"].cast()
            self.clear()

    def clear(self):
        super().clear()
        self.count_list = []

class 江海凝光_钗燕(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "江海凝光-钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕-计数"].trigger()


class 玳弦急曲_钗燕(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "玳弦急曲-钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕-计数"].trigger()


class 剑破虚空_钗燕(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑破虚空-钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕-计数"].trigger()


class 剑气长江_钗燕(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑气长江-钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕-计数"].trigger()


class 剑影留痕_钗燕(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑影留痕-钗燕"

    def add(self):
        super().add()
        self.status.buffs["钗燕-计数"].trigger()


class 盈袖(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "盈袖"

        self.duration = 20 * 16
        self.duration_max = 20 * 16

        self.value = 204 / 1024

    def add(self):
        super().add()
        self.status.attribute.extra_haste += self.value

    def remove(self):
        super().remove()
        self.status.attribute.extra_haste -= self.value


class 化冰(Buff):
    def __init__(self, status):
        super().__init__(status)
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


class 化冰_计数(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "化冰-计数"

        self.duration = 24
        self.duration_max = 24
        self.stack_max = 3

    @property
    def condition(self):
        return self.status.stacks["化冰"]

    def add(self):
        super().add()
        if self.status.stacks[self.name] == 3:
            self.status.skills["化冰"].cast()
            self.clear()


class 夜天(Buff):
    def __init__(self, status):
        super().__init__(status)
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


class 剑神无我(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "剑神无我"

        self.duration = 20 * 16
        self.duration_max = 20 * 16


class 琼霄_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "琼霄-冷却"

        self.duration = 20 * 16
        self.duration_max = 20 * 16


class 凝华(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "凝华"

        self.stack_add = 3
        self.stack_max = 9

        self.duration = 20 * 16
        self.duration_max = 20 * 16


class 霜降(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "霜降"

        self.value = 0
        self.level_params = {
            "value": [154 / 1024, 307 / 1024, 461 / 1024]
        }

    def add(self):
        super().add()
        self.status.skills["玳弦急曲"].skill_damage_addition += self.value

    def remove(self):
        super().remove()
        self.status.skills["玳弦急曲"].skill_damage_addition -= self.value


class 飞霜绛露(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞霜绛露"

        self.probability = 25 / 1024

    @property
    def condition(self):
        return not self.status.stacks["飞霜绛露-冷却"]

    def add(self):
        super().add()
        self.status.skills["剑气长江"].recharge()
        self.status.buffs["飞霜绛露-冷却"].trigger()


class 飞霜绛露_冷却(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "飞霜绛露-冷却"

        self.duration = 30 * 16
        self.duration_max = 30 * 16


class 气吞长江_持续(Buff):
    def __init__(self, status):
        super().__init__(status)
        self.name = "气吞长江-持续"

        self.is_dot = True

        self.stack_max = 3


BUFFS = [嗔怒, 剑舞, 满堂, 急曲_持续, 繁音急节, 枕上, 广陵月, 广陵月_会效, 流玉, 流玉_持续,
         钗燕_计数, 江海凝光_钗燕, 玳弦急曲_钗燕, 剑破虚空_钗燕, 剑气长江_钗燕,
         剑影留痕_钗燕, 盈袖, 化冰, 化冰_计数, 夜天, 剑神无我, 琼霄_冷却, 凝华,
         霜降, 飞霜绛露, 飞霜绛露_冷却, 气吞长江_持续]
