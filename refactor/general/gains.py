from base.constant import FRAME_PER_SECOND, TANK_GAIN_BASE
from base.skill import Skill
from base.status import Status

""" Permanent gain """


def han_ru_lei(status: Status):
    status.attribute.physical_attack_power_gain += 0.1


def po_feng(status: Status):
    status.attribute.target.physical_shield_base -= 1150


def jing_feng(status: Status):
    status.attribute.target.physical_shield_base -= 1397


def xiu_qi(status: Status):
    status.attribute.all_major_base += 244


def jie_huo(status: Status):
    status.attribute.target.physical_vulnerable += 0.05


def qiu_su(status: Status):
    status.attribute.target.physical_vulnerable += 0.06


def jiu_zhong_xian(status: Status):
    status.attribute.physical_critical_strike_gain += 0.1


def sui_xing_chen(status: Status):
    status.attribute.physical_critical_power_gain += 0.1


def zuo_xuan_you_zhuan(stack):
    value = 54

    def inner(status: Status):
        status.attribute.surplus += value * stack

    return inner


def zhen_fen(stack):
    value = 60

    def inner(status: Status):
        status.attribute.physical_overcome_base += value * stack

    return inner


def hao_ling_san_jun(stack):
    duration = 30
    value = TANK_GAIN_BASE

    def inner(status: Status):
        status.attribute.strain_base += value * stack * duration * FRAME_PER_SECOND / status.total_frame
        status.attribute.strain_base += value * 0.5 * stack * duration * FRAME_PER_SECOND / status.total_frame

    return inner


""" Periodic Gains """


def ji_lei(num):
    value = 0.2
    duration = 6
    cd = 30

    def inner(status: Status):
        rate = min(1, num * duration / cd)
        status.attribute.physical_attack_power_gain += value * rate
        status.attribute.physical_overcome_gain += value * rate

    return inner


def jian_feng_bai_duan(rate):
    def inner(status: Status):
        status.attribute.weapon_damage_gain += 1 * rate

    return inner


def shu_kuang(num, cd=50):
    duration = 12
    value = 0.3

    def inner(status: Status):
        rate = min(1, num * duration / cd)
        status.attribute.physical_attack_power_gain += value * rate

    return inner


def chao_sheng_yan(num, stack, cd=180):
    duration = 8
    value = TANK_GAIN_BASE

    def inner(status: Status):
        rate = min(1, num * duration / cd)
        status.attribute.strain_base += value * stack * rate

    return inner


def sheng_yu_ming_xin(num, stack, cd=180):
    duration = 8
    value = TANK_GAIN_BASE * 1.5

    def inner(status: Status):
        rate = min(1, num * duration / cd)
        status.attribute.strain_base += value * stack * rate

    return inner


def she_shen_hong_fa(num, stack):
    duration = 20
    cd = 40
    value = TANK_GAIN_BASE

    def inner(status: Status):
        rate = min(1, num * duration / cd)
        status.attribute.strain_base += value * stack * rate

    return inner


def han_xiao_qian_jun(num):
    duration = 15
    cd = 30
    value = 0.2

    def inner(status: Status):
        rate = min(1, num * duration / cd)
        status.attribute.physical_overcome_gain += value * rate

    return inner


def xian_wang_gu_ding(num):
    duration = 25
    cd = 120

    def inner(status: Status):
        rate = min(1, num * duration * cd)
        status.attribute.damage_addition += 0.12 * rate

    return inner


def mei_hua_san_nong(rate, stack):
    value = 60

    def inner(status: Status):
        status.attribute.strain_base += value * stack * rate

    return inner


def piao_huang(rate):
    def inner(status: Status):
        pass

    return inner


def shan_you():
    def inner(status: Status):
        status.attribute.cd_reduction += 0.08

    return inner


def pei_wu(rate):
    value = 0.05

    def inner(status: Status):
        status.attribute.all_major_gain += value * rate

    return inner


""" Weapon Enchant """


def physical_attack_power_enchant(status: Status):
    status.attribute.physical_attack_power_base += 1


def weapon_damage_enchant(status: Status):
    status.attribute.weapon_damage_base += 1


""" Spread """


def physical_spread(status: Status):
    status.attribute.physical_attack_power_base += 1
    status.attribute.all_critical_strike_base += 1
    status.attribute.surplus += 1


def tong_ze_spread():
    pass


def boiled_fish_spread(status: Status):
    status.attribute.surplus += 1
    status.attribute.strain_base += 1


def streamed_fish_spread(status: Status):
    status.attribute.strain_gain += 1


""" Major Food """


def strength_food(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Minor Food """


def surplus_food(value):
    def inner(status: Status):
        status.attribute.surplus += value

    return inner


def haste_food(value):
    def inner(status: Status):
        status.attribute.haste_base += value

    return inner


def physical_attack_power_food(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


def physical_critical_strike_food(value):
    def inner(status: Status):
        status.attribute.physical_critical_strike_base += value

    return inner


def physical_overcome_food(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value

    return inner


""" Major Potion """


def strength_potion(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Minor Potion """


def surplus_potion(value):
    def inner(status: Status):
        status.attribute.surplus += value

    return inner


def haste_potion(value):
    def inner(status: Status):
        status.attribute.haste_base += value

    return inner


def physical_attack_power_potion(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


def physical_critical_strike_potion(value):
    def inner(status: Status):
        status.attribute.physical_critical_strike_base += value

    return inner


def physical_overcome_potion(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value

    return inner


""" Wine """


def strength_wine(value):
    def inner(status: Status):
        status.attribute.strength_base += value

    return inner


""" Snack """

""" Equipment Gains """


def water_weapon_gain(value):
    def inner(status: Status):
        status.buffs["水特效"].value = value

        def water_weapon_post_hit(self: Skill):
            self.status.buffs["水特效"].trigger()

        for skill in status.skills.values():
            if skill.is_hit:
                skill.post_hit_effect.append(water_weapon_post_hit)

    return inner


def wind_pendant_gain(value):
    def inner(status: Status):
        status.buffs["风特效"].value = value

    return inner


def special_enchant_hat_gain(value):
    def inner(status: Status):
        status.attribute.physical_overcome_base += value

    return inner


def special_enchant_jacket_gain(value):
    def inner(status: Status):
        status.attribute.physical_attack_power_base += value

    return inner


def special_enchant_belt_gain(status: Status):
    def enchant_belt_post_hit(self: Skill):
        if not self.status.stacks["大附魔腰"]:
            self.status.skills["大附魔腰"].cast()

    for skill in status.skills.values():
        if skill.damage_base:
            skill.post_hit_effect.append(enchant_belt_post_hit)


def special_enchant_wrist_gain(status: Status):
    def enchant_wrist_post_hit(self: Skill):
        if not self.status.stacks["大附魔手"]:
            self.status.skills["昆吾·弦刃"].cast()

    for skill in status.skills.values():
        if skill.damage_base:
            skill.post_hit_effect.append(enchant_wrist_post_hit)


def special_enchant_shoes_gain(status: Status):
    def enchant_wrist_critical_hit(self: Skill):
        if not self.status.stacks["大附魔脚"]:
            self.status.skills["刃凌"].cast()

    for skill in status.skills.values():
        if skill.damage_base:
            skill.critical_hit_effect.append(enchant_wrist_critical_hit)
