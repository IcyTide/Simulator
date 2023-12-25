from base.status import Status


class 九音惊弦阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 50 / 1024
        status.attribute.magical_critical_strike_gain += 0.03
        status.attribute.magical_critical_power_gain += 51 / 1024
        status.attribute.magical_overcome_gain += self.core_rate * 307 / 1024
        status.attribute.magical_attack_power_gain += self.rate * 50 / 1024


class 七绝逍遥阵:
    def __init__(self, rate, core_rate):
        pass

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 51 / 1024
        status.attribute.magical_overcome_gain += 300 / 1024


class 卫公折冲阵:
    def __init__(self, rate, core_rate):
        self.stack = 5
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.physical_overcome_gain += 200 / 1024
        status.attribute.strength_gain += self.core_rate * self.stack * 10 / 1024
        status.attribute.physical_attack_power_gain += self.rate * 51 / 1024


class 天鼓雷音阵:
    def __init__(self, rate, core_rate):
        self.stack = 5
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 51 / 1024
        status.attribute.strain_gain += 20 / 1024
        status.attribute.magical_overcome_gain += 102 / 1024
        status.attribute.magical_attack_power_gain += self.rate * self.stack * 21 / 1024


class 北斗七星阵:
    def __init__(self, rate, core_rate):
        self.stack = 5
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_critical_power_gain += 150 / 1024
        status.attribute.physical_critical_strike_gain += self.rate * 0.01 * self.stack


class 九宫八卦阵:
    def __init__(self, rate, core_rate):
        self.stack = 5
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.magical_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.magical_critical_power_gain += 154 / 1024
        status.attribute.magical_critical_strike_gain += self.rate * 0.01 * self.stack


class 依山观澜阵:
    def __init__(self, rate, core_rate):
        pass

    def __call__(self, status: Status):
        status.attribute.agility_gain += 30 / 1024
        status.attribute.physical_attack_power_gain += 51 / 1024
        status.attribute.physical_critical_power_gain += 204 / 1024


class 万蛊噬心阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 51 / 1024
        status.attribute.magical_critical_strike_gain += 0.03
        status.attribute.magical_critical_power_gain += 102 / 1024
        status.attribute.magical_attack_power_gain += self.core_rate * 51 / 1024
        status.attribute.magical_overcome_gain += self.rate * 102 / 1024


class 流星赶月阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.strength_gain += 30 / 1024
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_overcome_gain += 205 / 1024
        status.attribute.physical_critical_strike_gain += self.rate * 0.05


class 千机百变阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.all_shield_ignore += 20 / 1024
        status.attribute.all_critical_power_gain += 150 / 1024
        status.attribute.all_critical_strike_gain += self.rate * 0.05


class 炎威破魔阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 51 / 1024
        status.attribute.magical_critical_strike_gain += 0.03
        status.attribute.magical_critical_power_gain += self.core_rate * 200 / 1024
        status.attribute.magical_critical_strike_gain += self.rate * 0.1


class 降龙伏虎阵:
    def __init__(self, rate, core_rate):
        self.stack = 5
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.physical_overcome_gain += 102 / 1024
        status.attribute.physical_overcome_gain += self.core_rate * 306 / 1024
        status.attribute.physical_overcome_base += self.rate * 770 * self.stack


class 锋凌横绝阵:
    def __init__(self, rate, core_rate):
        self.stack = 5
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_overcome_gain += self.core_rate * 153 / 1024
        status.attribute.physical_critical_power_gain += self.rate * 20 / 1024 * self.stack


class 万籁金弦阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.magical_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.magical_attack_power_gain += 102 / 1024
        status.attribute.magical_critical_power_gain += self.core_rate * 205 / 1024
        status.attribute.magical_critical_strike_gain += self.rate * 0.05


class 霜岚洗锋阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_overcome_gain += 102 / 1024
        status.attribute.all_critical_strike_gain += self.rate * 0.05


class 墟海引归阵:
    def __init__(self, rate, core_rate):
        self.core_rate = core_rate

    def __call__(self, status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.physical_attack_power_gain += 102 / 1024
        status.attribute.physical_attack_power_gain += self.core_rate * 102 / 1024
        status.attribute.physical_overcome_gain += 102 / 1024


class 龙皇雪风阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.physical_critical_power_gain += 154 / 1024
        status.attribute.physical_attack_power_gain += self.rate * 102 / 1024


class 九星游年阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

        self.values = [102, 92, 82, 71, 61, 51, 41, 31, 20, 10]

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 51 / 1024
        status.attribute.strain_gain += 20 / 1024
        status.attribute.magical_critical_power_gain += 100 / 1024
        status.attribute.magical_critical_power_gain += self.core_rate * sum(self.values) / len(self.values) / 1024
        status.attribute.damage_addition += self.rate * 0.5 * 154 / 1024


class 乱暮浊茵阵:
    def __init__(self, rate, core_rate):
        pass

    def __call__(self, status: Status):
        status.attribute.magical_attack_power_gain += 51 / 1024
        status.attribute.damage_addition += 31 / 1024
        status.attribute.all_critical_strike_gain += 0.03


class 横云破锋阵:
    def __init__(self, rate, core_rate):
        pass

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.surplus += 1516
        status.attribute.physical_overcome_gain += 256 / 1024


class 苍梧引灵阵:
    def __init__(self, rate, core_rate):
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def __call__(self, status: Status):
        status.attribute.all_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.damage_addition += 62 / 1024
        status.attribute.all_critical_power_gain += self.rate * 150 / 1024


FORMATIONS = {
    "": ["千机百变阵", "苍梧引灵阵"],
    "外功": [
        "卫公折冲阵", "北斗七星阵", "依山观澜阵", "流星赶月阵", "降龙伏虎阵", "锋凌横绝阵", "霜岚洗锋阵", "墟海引归阵",
        "龙皇雪风阵", "横云破锋阵"
    ],
    "内功": [
        "九音惊弦阵", "七绝逍遥阵", "天鼓雷音阵", "九宫八卦阵", "万蛊噬心阵", "炎威破魔阵", "万籁金弦阵", "九星游年阵",
        "乱暮浊茵阵"
    ]
}
FORMATION_GAIN_NAMES = {
    "九音惊弦阵": "九音惊弦阵(5%内攻3%内会5%内功会效/5%内攻)",
    "七绝逍遥阵": "七绝逍遥阵(5%内攻30%内破)",
    "卫公折冲阵": "卫公折冲阵(5%外攻20%外破/5%外攻)",
    "天鼓雷音阵": "天鼓雷音阵(5%内攻2%无双10%内破/5*2%内攻)",
    "北斗七星阵": "北斗七星阵(3%外会2%无双15%外功会效/5*1%外会)",
    "九宫八卦阵": "九宫八卦阵(3%内会2%无双15%内功会效/5*1%内会)",
    "依山观澜阵": "依山观澜阵(3%身法5%外攻20%外攻会效)",
    "万蛊噬心阵": "万蛊噬心阵(5%内攻3%内会10%内功会效/10%内破)",
    "流星赶月阵": "流星赶月阵(3%力道2%无双20%外破/5%外会)",
    "千机百变阵": "千机百变阵(5%内攻5%无视15%会效/5%会心)",
    "炎威破魔阵": "炎威破魔阵(5%内攻3%内会/10%内会)",
    "降龙伏虎阵": "降龙伏虎阵(5%外攻10%外破/5*770外破)",
    "锋凌横绝阵": "锋凌横绝阵(3%外会2%无双/5*2%外功会效)",
    "万籁金弦阵": "万籁金弦阵(3%内会2%无双10%内攻/5*1%内会",
    "霜岚洗锋阵": "霜岚洗锋阵(5%外攻2%无双10%外破/5%会心)",
    "墟海引归阵": "墟海引归阵(3%外会10%外攻10%外破)",
    "龙皇雪风阵": "龙皇雪风阵(3%外会5%外攻15%外功会效/10%外攻)",
    "九星游年阵": "九星游年阵(5%内攻2%无双10%内功会效/15%伤害增加)",
    "乱暮浊茵阵": "乱暮浊茵阵(5%内攻3%伤害增加3%会心)",
    "横云破锋阵": "横云破锋阵(5%外攻1516破招25%外破)",
    "苍梧引灵阵": "苍梧引灵阵(3%会心2%无双6%伤害增加/15%会效)",
}

FORMATION_GAINS = {
    "九音惊弦阵": 九音惊弦阵,
    "七绝逍遥阵": 七绝逍遥阵,
    "卫公折冲阵": 卫公折冲阵,
    "天鼓雷音阵": 天鼓雷音阵,
    "北斗七星阵": 北斗七星阵,
    "九宫八卦阵": 九宫八卦阵,
    "依山观澜阵": 依山观澜阵,
    "万蛊噬心阵": 万蛊噬心阵,
    "流星赶月阵": 流星赶月阵,
    "千机百变阵": 千机百变阵,
    "炎威破魔阵": 炎威破魔阵,
    "降龙伏虎阵": 降龙伏虎阵,
    "锋凌横绝阵": 锋凌横绝阵,
    "万籁金弦阵": 万籁金弦阵,
    "霜岚洗锋阵": 霜岚洗锋阵,
    "墟海引归阵": 墟海引归阵,
    "龙皇雪风阵": 龙皇雪风阵,
    "九星游年阵": 九星游年阵,
    "乱暮浊茵阵": 乱暮浊茵阵,
    "横云破锋阵": 横云破锋阵,
    "苍梧引灵阵": 苍梧引灵阵,
}
