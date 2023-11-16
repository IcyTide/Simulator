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


def han_ru_lei(status: Status):
    status.attribute.physical_attack_power_gain += 51 / 1024


def po_feng(value):
    def inner(status: Status):
        status.attribute.target.physical_shield_base -= value

    return inner


def cheng_long_jian(status: Status):
    status.attribute.target.physical_shield_gain -= 102 / 1024


def hao_ling_san_jun(value):
    def outer(stack):
        duration = 30

        def inner(status: Status):
            status.attribute.strain_base += value * stack * duration * FRAME_PER_SECOND / status.total_frame
            status.attribute.strain_base += value * 0.5 * stack * duration * FRAME_PER_SECOND / status.total_frame

        return inner

    return outer


def ji_lei(rate):
    value = 205 / 1024

    def inner(status: Status):
        status.attribute.physical_attack_power_gain += value * rate
        status.attribute.physical_overcome_gain += value * rate

    return inner


""" 少林 """


def li_di_cheng_fo(rate):
    value = 30 * 5 / 1024

    def inner(status: Status):
        pass

    return inner


def she_shen_hong_fa(value):
    def outer(stack, rate):
        def inner(status: Status):
            status.attribute.strain_base += value * stack * rate

        return inner

    return outer


""" 万花 """


def qiu_su(status: Status):
    status.attribute.target.physical_vulnerable = 61 / 1024


def luo_zi_wu_hui(rate):
    value = 51 / 1024

    def inner(status: Status):
        status.attribute.physical_critical_power_gain += value * rate

    return inner


""" 纯阳 """


def sui_xing_chen(status: Status):
    status.attribute.physical_critical_power_gain += 10 / 1024


def po_cang_qiong(status: Status):
    pass


""" 藏剑 """


def jian_feng_bai_duan(rate):
    def inner(status: Status):
        status.attribute.weapon_damage_gain += 1 * rate

    return inner


""" 五毒 """


def shan_you():
    def inner(status: Status):
        status.attribute.cd_reduction += 0.06

    return inner


def xian_wang_gu_ding(rate):
    value = 123 / 1024

    def inner(status: Status):
        status.attribute.damage_addition += value * rate

    return inner


""" 明教 """


def jie_huo(status: Status):
    status.attribute.target.physical_vulnerable = 51 / 1024


def lie_ri(status: Status):
    pass


def chao_sheng_yan(value):
    def outer(stack, rate):
        def inner(status: Status):
            status.attribute.strain_base += value * stack * rate

        return inner

    return outer


def sheng_yu_ming_xin(stack, rate):
    value = TANK_GAIN_BASE * 1.5

    def inner(status: Status):
        status.attribute.strain_base += value * stack * rate

    return inner


""" 丐帮 """


def jiu_zhong_xian(status: Status):
    status.attribute.physical_critical_strike_gain += 0.1


""" 苍云 """


def xu_ruo(status: Status):
    status.attribute.target.physical_shield_gain -= 51 / 1024


def zhen_fen(value):
    def outer(stack, rate):
        def inner(status: Status):
            status.attribute.physical_overcome_base += value * stack * rate

        return inner

    return outer


def han_xiao_qian_jun(rate):
    value = 204 / 1024

    def inner(status: Status):
        status.attribute.physical_overcome_gain += value * rate

    return inner


""" 长歌 """


def zhuang_zhou_meng(value):
    def outer(rate, stack):
        def inner(status: Status):
            status.attribute.strain_base += value * stack * rate

        return inner

    return outer


""" 霸刀 """


def shu_kuang(rate):
    value = 307 / 1024

    def inner(status: Status):
        status.attribute.physical_attack_power_gain += value * rate

    return inner


""" 药宗 """


def piao_huang(rate):
    def inner(status: Status):
        pass

    return inner


def pei_wu(rate):
    value = 10 * 5 / 1024

    def inner(status: Status):
        status.attribute.all_major_gain += value * rate

    return inner
