from base.constant import FRAME_PER_SECOND
from base.status import Status

""" 七秀 """


class XiuQi:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.all_major_base += self.value


class ZuoXuanYouZhuan:
    class Inner:
        def __init__(self, value, stack):
            self.value = value
            self.stack = stack

        def __call__(self, status: Status):
            status.attribute.surplus += self.value * self.stack

    def __init__(self, value):
        self.value = value

    def __call__(self, stack):
        return self.Inner(self.value, stack)


""" 天策 """


class HanRuLei:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_attack_power_gain += self.value


class PoFeng:
    class Inner:
        def __init__(self, value):
            self.value = value

        def __call__(self, status: Status):
            status.target.physical_shield_base -= self.value

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __call__(self, name):
        if name.startswith("破风"):
            return self.Inner(self.value1)
        elif name.startswith("劲风"):
            return self.Inner(self.value2)
        else:
            raise ValueError


class ChengLongJian:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.target.physical_shield_gain -= self.value


class HaoLingSanJun:
    class Inner:
        def __init__(self, duration, value, stack):
            self.duration = duration
            self.value = value
            self.stack = stack

        def __call__(self, status: Status):
            rate = self.duration * FRAME_PER_SECOND / status.total_frame
            status.attribute.strain_base += self.value * self.stack * rate
            status.attribute.strain_base += self.value / 2 * self.stack * rate

    def __init__(self, value):
        self.duration = 30
        self.value = value

    def __call__(self, stack):
        return self.Inner(self.duration, self.value, stack)


class JiLei:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.physical_attack_power_gain += self.value * self.rate
            status.attribute.physical_overcome_gain += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


""" 少林 """


class LiDiChengFo:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.target.magical_shield_gain -= self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


class SheShenHongFa:
    class Inner:
        def __init__(self, value, stack, rate):
            self.value = value
            self.stack = stack
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.strain_base += self.value * self.stack * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, stack, rate):
        return self.Inner(self.value, stack, rate)


""" 万花 """


class QiuSu:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.target.all_vulnerable = self.value


class JiaoSu:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.all_critical_power_gain += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


""" 纯阳 """


class SuiXingChen:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_critical_power_gain += self.value


class PoCangQiong:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.magical_critical_power_gain += self.value


""" 藏剑 """


class JianFengBaiDuan:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.weapon_damage_gain += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


""" 五毒 """


class ShanYou:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.cd_reduction += self.value


class XianWangGuDing:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.damage_addition += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


""" 明教 """


class JieHuo:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        if not status.target.physical_vulnerable:
            status.target.all_vulnerable = self.value


class LieRi:

    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.target.magical_vulnerable += self.value


class ChaoShengYan:
    class Inner:
        def __init__(self, value, stack, rate):
            self.value = value
            self.stack = stack
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.strain_base += self.value * self.stack * self.rate

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __call__(self, name, stack, rate):
        if name.startswith("朝圣言"):
            return self.Inner(self.value1, stack, rate)
        elif name.startswith("圣浴明心"):
            return self.Inner(self.value2, stack, rate)
        else:
            raise ValueError


""" 丐帮 """


class JiuZhongXian:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.attribute.physical_critical_strike_gain += self.value


""" 苍云 """


class XuRuo:
    def __init__(self, value):
        self.value = value

    def __call__(self, status: Status):
        status.target.physical_shield_gain -= self.value


class ZhenFen:
    class Inner:
        def __init__(self, value, stack, rate):
            self.value = value
            self.stack = stack
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.physical_overcome_base += self.value * self.stack * self.rate
            status.attribute.magical_overcome_base += self.value * self.stack * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, stack, rate):
        return self.Inner(self.value, stack, rate)


class HanXiaoQianJun:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.physical_overcome_gain += self.value * self.rate
            status.attribute.magical_overcome_gain += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


""" 长歌 """


class ZhuangZhouMeng:
    class Inner:
        def __init__(self, value, stack, rate):
            self.value = value
            self.stack = stack
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.strain_base += self.value * self.stack * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, stack, rate):
        return self.Inner(self.value, stack, rate)


""" 霸刀 """


class ShuKuang:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.physical_attack_power_gain += self.value * self.rate
            status.attribute.magical_attack_power_gain += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


""" 药宗 """


class PiaoHuang:
    class Inner:
        def __init__(self, rate):
            self.rate = rate

        def __call__(self, status: Status):
            pass

    def __call__(self, rate):
        return self.Inner(rate)


class PeiWu:
    class Inner:
        def __init__(self, value, rate):
            self.value = value
            self.rate = rate

        def __call__(self, status: Status):
            status.attribute.all_major_gain += self.value * self.rate

    def __init__(self, value):
        self.value = value

    def __call__(self, rate):
        return self.Inner(self.value, rate)


TEAM_GAINS_NUMBER = {
    "袖气": 244,
    "左旋右转": 54,

    "撼如雷": 51 / 1024,
    "破风": 1150,
    "劲风": 1397,
    "乘龙箭": 102 / 1024,
    "号令三军": 470,
    "激雷": 205 / 1024,

    "立地成佛": 30 * 5 / 1024,
    "舍身弘法": 470,

    "秋肃": 61 / 1024,
    "皎素": 51 / 1024,

    "碎星辰": 100 / 1024,
    "破苍穹": 100 / 1024,

    "剑锋百锻": 1,

    "善友": 0.06,
    "仙王蛊鼎": 123 / 1024,

    "戒火": 21 / 1024,
    "烈日": 51 / 1024,
    "朝圣言": 470,
    "圣浴明心": 705,

    "酒中仙": 0.1,

    "虚弱": 51 / 1024,
    "寒啸千军": 204 / 1024,
    "振奋": 60,

    "庄周梦": 60,

    "疏狂": 307 / 1024,

    "配伍": 10 * 5 / 1024,
}
TEAM_GAINS_NAME = {
    "袖气": f"{TEAM_GAINS_NUMBER['袖气']}全属性",
    "左旋右转": f"左旋右转({TEAM_GAINS_NUMBER['左旋右转']}破招)",

    "撼如雷": f"{round(TEAM_GAINS_NUMBER['撼如雷'] * 100)}%外攻",
    "破风": "破风",
    "破风(基础)": f"破风(-{TEAM_GAINS_NUMBER['破风']}外防)",
    "破风(劲风)": f"劲风(-{TEAM_GAINS_NUMBER['劲风']}外防)",
    "乘龙箭": f"{-round(TEAM_GAINS_NUMBER['乘龙箭'] * 100)}%外防",
    "号令三军": f"号令三军({TEAM_GAINS_NUMBER['号令三军']}无双)",
    "激雷": f"激雷({round(TEAM_GAINS_NUMBER['激雷'] * 100)}%外攻/外破)",

    "立地成佛": f"立地成佛(-{round(TEAM_GAINS_NUMBER['立地成佛'] * 100)}%内防)",
    "舍身弘法": f"舍身弘法({TEAM_GAINS_NUMBER['舍身弘法']}无双)",

    "秋肃": f"{round(TEAM_GAINS_NUMBER['秋肃'] * 100)}%全易伤",
    "皎素": f"皎素{round(TEAM_GAINS_NUMBER['皎素'] * 100)}%全会效",

    "碎星辰": f"{round(TEAM_GAINS_NUMBER['碎星辰'] * 100)}%外功会效",
    "破苍穹": f"{round(TEAM_GAINS_NUMBER['破苍穹'] * 100)}%内功会效",

    "剑锋百锻": f"剑锋百锻{round(TEAM_GAINS_NUMBER['剑锋百锻'] * 100)}%武伤",

    "善友": f"{round(TEAM_GAINS_NUMBER['善友'] * 100)}%调息加速",
    "仙王蛊鼎": f"仙王蛊鼎({round(TEAM_GAINS_NUMBER['仙王蛊鼎'] * 100)}%伤害加成)",

    "戒火": f"{round(TEAM_GAINS_NUMBER['戒火'] * 100)}%全易伤",
    "烈日": f"{round(TEAM_GAINS_NUMBER['烈日'] * 100)}%阴性/阳性易伤",
    "朝圣言": "朝圣言",
    "朝圣言(基础)": f"朝圣言({TEAM_GAINS_NUMBER['朝圣言']}无双)",
    "朝圣言(圣浴明心)": f"圣浴明心({TEAM_GAINS_NUMBER['圣浴明心']}无双)",

    "酒中仙": f"{round(TEAM_GAINS_NUMBER['酒中仙'] * 100)}%外会",

    "虚弱": f"{-round(TEAM_GAINS_NUMBER['虚弱'] * 100)}%外防",
    "寒啸千军": f"寒啸千军({round(TEAM_GAINS_NUMBER['寒啸千军'] * 100)}%破防)",
    "振奋": f"振奋({TEAM_GAINS_NUMBER['振奋']}破防)",

    "庄周梦": f"庄周梦({TEAM_GAINS_NUMBER['庄周梦']}无双)",

    "疏狂": f"疏狂({round(TEAM_GAINS_NUMBER['疏狂'] * 100)}%攻击)",

    "飘黄": f"飘黄(额外伤害)",
    "配伍": f"配伍({round(TEAM_GAINS_NUMBER['配伍'] * 100)}%全属性)",
}
TEAM_GAINS = {
    "袖气": XiuQi(TEAM_GAINS_NUMBER["袖气"]),
    "左旋右转": ZuoXuanYouZhuan(TEAM_GAINS_NUMBER["左旋右转"]),

    "撼如雷": HanRuLei(TEAM_GAINS_NUMBER["撼如雷"]),
    "破风": PoFeng(TEAM_GAINS_NUMBER["破风"], TEAM_GAINS_NUMBER["劲风"]),
    "乘龙箭": ChengLongJian(TEAM_GAINS_NUMBER["乘龙箭"]),
    "号令三军": HaoLingSanJun(TEAM_GAINS_NUMBER["号令三军"]),
    "激雷": JiLei(TEAM_GAINS_NUMBER["激雷"]),

    "立地成佛": LiDiChengFo(TEAM_GAINS_NUMBER["立地成佛"]),
    "舍身弘法": SheShenHongFa(TEAM_GAINS_NUMBER["舍身弘法"]),

    "秋肃": QiuSu(TEAM_GAINS_NUMBER["秋肃"]),
    "皎素": JiaoSu(TEAM_GAINS_NUMBER["皎素"]),

    "碎星辰": SuiXingChen(TEAM_GAINS_NUMBER["碎星辰"]),
    "破苍穹": PoCangQiong(TEAM_GAINS_NUMBER["破苍穹"]),

    "剑锋百锻": JianFengBaiDuan(TEAM_GAINS_NUMBER["破苍穹"]),

    "善友": ShanYou(TEAM_GAINS_NUMBER["善友"]),
    "仙王蛊鼎": XianWangGuDing(TEAM_GAINS_NUMBER["仙王蛊鼎"]),

    "戒火": JieHuo(TEAM_GAINS_NUMBER["戒火"]),
    "烈日": LieRi(TEAM_GAINS_NUMBER["烈日"]),
    "朝圣言": ChaoShengYan(TEAM_GAINS_NUMBER["朝圣言"], TEAM_GAINS_NUMBER["圣浴明心"]),

    "酒中仙": JiuZhongXian(TEAM_GAINS_NUMBER["酒中仙"]),

    "虚弱": XuRuo(TEAM_GAINS_NUMBER["虚弱"]),
    "寒啸千军": HanXiaoQianJun(TEAM_GAINS_NUMBER["寒啸千军"]),
    "振奋": ZhenFen(TEAM_GAINS_NUMBER["振奋"]),

    "庄周梦": ZhuangZhouMeng(TEAM_GAINS_NUMBER["庄周梦"]),

    "疏狂": ShuKuang(TEAM_GAINS_NUMBER["疏狂"]),

    "飘黄": PiaoHuang(),
    "配伍": PeiWu(TEAM_GAINS_NUMBER["配伍"]),
}
