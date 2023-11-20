from base.status import Status


def ao_xue_zhan_yi(rate):
    def inner(status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.physical_overcome_gain += 200 / 1024
        status.attribute.physical_attack_power_gain += rate * 51 / 1024

    return inner


def tai_xu_jian_yi(rate):
    stack = 5

    def inner(status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_critical_power_gain += 150 / 1024
        status.attribute.physical_critical_strike_gain += rate * 0.01 * stack

    return inner


def wen_shui_jue(rate):
    def inner(status: Status):
        status.attribute.agility_gain += 30 / 1024
        status.attribute.physical_attack_power_gain += 51 / 1024
        status.attribute.physical_critical_power_gain += 204 / 1024

    return inner


def jing_yu_jue(rate):
    def inner(status: Status):
        status.attribute.strength_gain += 30 / 1024
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_overcome_gain += 205 / 1024
        status.attribute.physical_critical_strike_gain += rate * 0.05

    return inner


def tian_luo_gui_dao(rate):
    def inner(status: Status):
        status.attribute.all_shield_ignore += 20 / 1024
        status.attribute.all_critical_power_gain += 150 / 1024
        status.attribute.all_critical_strike_gain += rate * 0.05

    return inner


def xiao_chen_jue(rate):
    stack = 5

    def inner(status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.physical_overcome_gain += 102 / 1024
        status.attribute.physical_overcome_base += rate * 770 * stack

    return inner


def fen_shan_jing(rate):
    stack = 5

    def inner(status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_critical_power_gain += rate * 20 / 1024 * stack

    return inner


def bei_ao_jue(rate):
    def inner(status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.strain_gain += 20 / 1024
        status.attribute.physical_overcome_gain += 102 / 1024
        status.attribute.all_critical_strike_gain += rate * 0.05

    return inner


def ling_hai_jue(rate):
    def inner(status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.physical_attack_power_gain += 102 / 1024
        status.attribute.physical_overcome_gain += 102 / 1024

    return inner


def yin_long_jue(rate):
    def inner(status: Status):
        status.attribute.physical_critical_strike_gain += 0.03
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.physical_critical_power_gain += 154 / 1024
        status.attribute.physical_attack_power_gain += rate * 102 / 1024

    return inner


def gu_feng_jue(rate):
    def inner(status: Status):
        status.attribute.physical_attack_power_gain += 50 / 1024
        status.attribute.surplus += 1516
        status.attribute.physical_overcome_gain += 256 / 1024

    return inner


def shan_hai_xin_jue(rate):
    def inner(status: Status):
        status.attribute.all_critical_strike_gain += 0.03
        status.attribute.strain_gain += 20 / 1024
        status.attribute.damage_addition += 62 / 1024
        status.attribute.all_critical_power_gain += rate * 150 / 1024

    return inner


FORMATIONS = {
    "通用": ["千机百变阵", "苍梧引灵阵"],
    "外功": [
        "卫公折冲阵", "北斗七星阵", "依山观澜阵", "流星赶月阵", "降龙伏虎阵", "锋凌横绝阵", "霜岚洗锋阵", "墟海引归阵",
        "龙皇雪风阵", "横云破锋阵"
    ]
}
FORMATION_GAIN_NAMES = {
    "千机百变阵": "千机百变阵(5%内攻5%无视15%会效/5%会心)",
    "苍梧引灵阵": "苍梧引灵阵(3%会心2%无双6%伤害增加/15%会效)",

    "卫公折冲阵": "卫公折冲阵(5%外攻20%外破/5%外攻)",
    "北斗七星阵": "北斗七星阵(3%外会2%无双15%外功会效/5*1%外会)",
    "依山观澜阵": "依山观澜阵(3%身法5%外攻20%外攻会效)",
    "流星赶月阵": "流星赶月阵(3%力道2%无双20%外破/5%外会)",
    "降龙伏虎阵": "降龙伏虎阵(5%外攻10%外破/5*770外破)",
    "锋凌横绝阵": "锋凌横绝阵(3%外会2%无双/5*2%外功会效)",
    "霜岚洗锋阵": "霜岚洗锋阵(5%外攻2%无双10%外破/5%会心)",
    "墟海引归阵": "墟海引归阵(3%外会10%外攻10%外破)",
    "龙皇雪风阵": "龙皇雪风阵(3%外会5%外攻15%外功会效/10%外攻)",
    "横云破锋阵": "横云破锋阵(5%外攻1516破招25%外破)",
}

FORMATION_GAINS = {
    "千机百变阵": tian_luo_gui_dao,
    "苍梧引灵阵": shan_hai_xin_jue,

    "卫公折冲阵": ao_xue_zhan_yi,
    "北斗七星阵": tai_xu_jian_yi,
    "依山观澜阵": wen_shui_jue,
    "流星赶月阵": jing_yu_jue,
    "降龙伏虎阵": xiao_chen_jue,
    "锋凌横绝阵": fen_shan_jing,
    "霜岚洗锋阵": bei_ao_jue,
    "墟海引归阵": ling_hai_jue,
    "龙皇雪风阵": yin_long_jue,
    "横云破锋阵": gu_feng_jue
}
