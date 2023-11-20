from base.constant import FRAME_PER_SECOND
from base.status import Status

""" 七秀 """


def xiu_qi(value):
    def inner(status: Status):
        status.attribute.all_major_base += value

    return inner


def zuo_xuan_you_zhuan(value):
    def outer(stack):
        def inner(status: Status):
            status.attribute.surplus += value * stack

        return inner

    return outer


""" 天策 """


def han_ru_lei(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_gain += value

    return inner


def po_feng(value1, value2):
    def outer(name):
        if name.startswith("破风"):
            value = value1
        elif name.startswith("劲风"):
            value = value2
        else:
            raise ValueError

        def inner(status: Status):
            status.target.physical_shield_base -= value

        return inner

    return outer


def cheng_long_jian(value):
    def inner(status: Status):
        status.target.physical_shield_gain -= value

    return inner


def hao_ling_san_jun(value):
    def outer(stack):
        duration = 30

        def inner(status: Status):
            status.attribute.strain_base += value * stack * duration * FRAME_PER_SECOND / status.total_frame
            status.attribute.strain_base += value / 2 * stack * duration * FRAME_PER_SECOND / status.total_frame

        return inner

    return outer


def ji_lei(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.physical_attack_power_gain += value * rate
            status.attribute.physical_overcome_gain += value * rate

        return inner

    return outer


""" 少林 """


def li_di_cheng_fo(value):
    def outer(rate):
        def inner(status: Status):
            pass

        return inner

    return outer


def she_shen_hong_fa(value):
    def outer(stack, rate):
        def inner(status: Status):
            status.attribute.strain_base += value * stack * rate

        return inner

    return outer


""" 万花 """


def qiu_su(value):
    def inner(status: Status):
        status.target.physical_vulnerable = value

    return inner


def jiao_su(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.physical_critical_power_gain += value * rate

        return inner

    return outer


""" 纯阳 """


def sui_xing_chen(value):
    def inner(status: Status):
        status.attribute.physical_critical_power_gain += value

    return inner


def po_cang_qiong(value):
    def inner(status: Status):
        pass

    return inner


""" 藏剑 """


def jian_feng_bai_duan(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.weapon_damage_gain += value * rate

        return inner

    return outer


""" 五毒 """


def shan_you(value):
    def inner(status: Status):
        status.attribute.cd_reduction += value

    return inner


def xian_wang_gu_ding(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.damage_addition += value * rate

        return inner

    return outer


""" 明教 """


def jie_huo(value):
    def inner(status: Status):
        status.target.physical_vulnerable = value

    return inner


def lie_ri(value):
    def inner(status: Status):
        pass

    return inner


def chao_sheng_yan(value1, value2):
    def outer(name, stack, rate):
        if name.startswith("朝圣言"):
            value = value1
        elif name.startswith("圣浴明心"):
            value = value2
        else:
            raise ValueError

        def inner(status: Status):
            status.attribute.strain_base += value * stack * rate

        return inner

    return outer


""" 丐帮 """


def jiu_zhong_xian(value):
    def inner(status: Status):
        status.attribute.physical_critical_strike_gain += value

    return inner


""" 苍云 """


def xu_ruo(value):
    def inner(status: Status):
        status.target.physical_shield_gain -= value

    return inner


def zhen_fen(value):
    def outer(stack, rate):
        def inner(status: Status):
            status.attribute.physical_overcome_base += value * stack * rate

        return inner

    return outer


def han_xiao_qian_jun(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.physical_overcome_gain += value * rate

        return inner

    return outer


""" 长歌 """


def zhuang_zhou_meng(value):
    def outer(stack, rate):
        def inner(status: Status):
            status.attribute.strain_base += value * stack * rate

        return inner

    return outer


""" 霸刀 """


def shu_kuang(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.physical_attack_power_gain += value * rate

        return inner

    return outer


""" 药宗 """


def piao_huang(rate):
    def inner(status: Status):
        pass

    return inner


def pei_wu(value):
    def outer(rate):
        def inner(status: Status):
            status.attribute.all_major_gain += value * rate

        return inner

    return outer


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
    "袖气": xiu_qi(TEAM_GAINS_NUMBER["袖气"]),
    "左旋右转": zuo_xuan_you_zhuan(TEAM_GAINS_NUMBER["左旋右转"]),

    "撼如雷": han_ru_lei(TEAM_GAINS_NUMBER["撼如雷"]),
    "破风": po_feng(TEAM_GAINS_NUMBER["破风"], TEAM_GAINS_NUMBER["劲风"]),
    "乘龙箭": cheng_long_jian(TEAM_GAINS_NUMBER["乘龙箭"]),
    "号令三军": hao_ling_san_jun(TEAM_GAINS_NUMBER["号令三军"]),
    "激雷": ji_lei(TEAM_GAINS_NUMBER["激雷"]),

    "立地成佛": li_di_cheng_fo(TEAM_GAINS_NUMBER["立地成佛"]),
    "舍身弘法": she_shen_hong_fa(TEAM_GAINS_NUMBER["舍身弘法"]),

    "秋肃": qiu_su(TEAM_GAINS_NUMBER["秋肃"]),
    "皎素": jiao_su(TEAM_GAINS_NUMBER["皎素"]),

    "碎星辰": sui_xing_chen(TEAM_GAINS_NUMBER["碎星辰"]),
    "破苍穹": po_cang_qiong(TEAM_GAINS_NUMBER["破苍穹"]),

    "剑锋百锻": jian_feng_bai_duan(TEAM_GAINS_NUMBER["破苍穹"]),

    "善友": shan_you(TEAM_GAINS_NUMBER["善友"]),
    "仙王蛊鼎": xian_wang_gu_ding(TEAM_GAINS_NUMBER["仙王蛊鼎"]),

    "戒火": jie_huo(TEAM_GAINS_NUMBER["戒火"]),
    "烈日": lie_ri(TEAM_GAINS_NUMBER["烈日"]),
    "朝圣言": chao_sheng_yan(TEAM_GAINS_NUMBER["朝圣言"], TEAM_GAINS_NUMBER["圣浴明心"]),

    "酒中仙": jiu_zhong_xian(TEAM_GAINS_NUMBER["酒中仙"]),

    "虚弱": xu_ruo(TEAM_GAINS_NUMBER["虚弱"]),
    "寒啸千军": han_xiao_qian_jun(TEAM_GAINS_NUMBER["寒啸千军"]),
    "振奋": zhen_fen(TEAM_GAINS_NUMBER["振奋"]),

    "庄周梦": zhuang_zhou_meng(TEAM_GAINS_NUMBER["庄周梦"]),

    "疏狂": shu_kuang(TEAM_GAINS_NUMBER["疏狂"]),

    "飘黄": piao_huang,
    "配伍": pei_wu(TEAM_GAINS_NUMBER["配伍"]),
}
