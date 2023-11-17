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
            status.attribute.target.physical_shield_base -= value

        return inner

    return outer


def cheng_long_jian(value):
    def inner(status: Status):
        status.attribute.target.physical_shield_gain -= value

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
        status.attribute.target.physical_vulnerable = value

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
        status.attribute.target.physical_vulnerable = value

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
        status.attribute.target.physical_shield_gain -= value

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
