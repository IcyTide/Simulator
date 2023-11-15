from base.constant import FRAME_PER_SECOND, TANK_GAIN_BASE, HEALER_GAIN_BASE
from base.status import Status

""" Tank/Healer """


def han_ru_lei(status: Status):
    status.attribute.physical_attack_power_gain += 51 / 1024


def xiu_qi(status: Status):
    status.attribute.all_major_base += 244


def po_feng(status: Status):
    status.attribute.target.physical_shield_base -= 1150


def jing_feng(status: Status):
    status.attribute.target.physical_shield_base -= 1397


def xu_ruo(status: Status):
    status.attribute.target.physical_shield_gain -= 51 / 1024


def jie_huo(status: Status):
    status.attribute.target.physical_vulnerable += 51 / 1024


def qiu_su(status: Status):
    status.attribute.target.physical_vulnerable += 61 / 1024


def hao_ling_san_jun(stack):
    duration = 30
    value = TANK_GAIN_BASE

    def inner(status: Status):
        status.attribute.strain_base += value * stack * duration * FRAME_PER_SECOND / status.total_frame
        status.attribute.strain_base += value * 0.5 * stack * duration * FRAME_PER_SECOND / status.total_frame

    return inner


def li_di_cheng_fo(rate):
    value = 30 * 5 / 1024

    def inner(status: Status):
        pass

    return inner


def luo_zi_wu_hui(rate):
    value = 0.051

    def inner(status: Status):
        status.attribute.physical_critical_power_gain += value * rate

    return inner


def she_shen_hong_fa(stack, rate):
    value = TANK_GAIN_BASE

    def inner(status: Status):
        status.attribute.strain_base += value * stack * rate

    return inner


def chao_sheng_yan(stack, rate):
    value = TANK_GAIN_BASE

    def inner(status: Status):
        status.attribute.strain_base += value * stack * rate

    return inner


def sheng_yu_ming_xin(stack, rate):
    value = TANK_GAIN_BASE * 1.5

    def inner(status: Status):
        status.attribute.strain_base += value * stack * rate

    return inner


def zhen_fen(stack, rate):
    value = HEALER_GAIN_BASE

    def inner(status: Status):
        status.attribute.physical_overcome_base += value * stack * rate

    return inner


def han_xiao_qian_jun(rate):
    value = 204 / 1024

    def inner(status: Status):
        status.attribute.physical_overcome_gain += value * rate

    return inner


def zuo_xuan_you_zhuan(stack):
    value = HEALER_GAIN_BASE * 0.9

    def inner(status: Status):
        status.attribute.surplus += value * stack

    return inner


def xian_wang_gu_ding(rate):
    value = 123 / 1024

    def inner(status: Status):
        status.attribute.damage_addition += value * rate

    return inner


def zhuang_zhou_meng(rate, stack):
    value = HEALER_GAIN_BASE

    def inner(status: Status):
        status.attribute.strain_base += value * stack * rate

    return inner


def piao_huang(rate):
    def inner(status: Status):
        pass

    return inner


def pei_wu(rate):
    value = 10 * 5 / 1024

    def inner(status: Status):
        status.attribute.all_major_gain += value * rate

    return inner


""" DPS Gains """


def sui_xing_chen(status: Status):
    status.attribute.physical_critical_power_gain += 0.1


def jiu_zhong_xian(status: Status):
    status.attribute.physical_critical_strike_gain += 0.1


def jian_feng_bai_duan(rate):
    def inner(status: Status):
        status.attribute.weapon_damage_gain += 1 * rate

    return inner


def shan_you():
    def inner(status: Status):
        status.attribute.cd_reduction += 0.06

    return inner


def ji_lei(rate):
    value = 205 / 1024

    def inner(status: Status):
        status.attribute.physical_attack_power_gain += value * rate
        status.attribute.physical_overcome_gain += value * rate

    return inner


def shu_kuang(rate):
    value = 307 / 1024

    def inner(status: Status):
        status.attribute.physical_attack_power_gain += value * rate

    return inner
