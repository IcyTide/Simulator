from abstract import melee
from badao.skills import *
from constants import FLOAT_POINT


# 1
def longxi_talent():
    jingyan_skill.overdraw = 6


# 2
def guihan_talent():
    shangjiang_skill.cd -= 10


# 3
def yangguan_talent():
    shangjiang_skill.k_b += 0.2
    shangjiang_skill.ignore_defense += 0.2
    jianchen_dot.k_b += 0.2


def minggu_talent():
    pofu_skill.k_b += 0.2
    pofu_counter.ignore_defense += 0.5
    # pofu_counter.k_b += 0.2
    pofu_skill.ignore_defense += 0.5


# 4
def shuangtian_talent():
    shangjiang_skill.increasing_k_c += 0.15


def huajiao_talent():
    zuizhan_skill.cd += 10
    zuizhan_skill.cast_time += 1.5
    zuizhan_skill.increasing_k_b += 0.25


# 5
hanfeng_effect = Effect("含风", duration=18, max_layers=2)


def hanfeng_talent(critical_strike=0.04, critical_effect=0.04, k=0.04):
    def hanfeng_apply(skills, attribute):
        attribute.physical_critical_strike_gain += critical_strike
        attribute.physical_critical_effect_gain += critical_effect
        for skill in skills:
            if skill in hanfeng_list:
                skill.k_b += k

    def hanfeng_revoke(skills, attribute):
        attribute.physical_critical_strike_gain -= critical_strike
        attribute.physical_critical_effect_gain -= critical_effect
        for skill in skills:
            if skill in hanfeng_list:
                skill.k_b -= k

    hanfeng_effect.apply = hanfeng_apply
    hanfeng_effect.revoke = hanfeng_revoke


# 6
JIANCHEN_DELAY = 0.5
jianchen_dot = Skill("见尘", base_damage=75.7, attack_power_cof=0.4125,
                     duration=shangjiang_skill.cast_time + 2 * JIANCHEN_DELAY)
jianchen_dot.periods = [
    round(jianchen_dot.duration - JIANCHEN_DELAY - sum(shangjiang_skill.periods[:i + 1]), FLOAT_POINT) for i in
    range(shangjiang_skill.times)]


def jianchen_talent():
    pass


# 7
def fenjiang_talent():
    shangjiang_skill.cast_time += 0.4
    shangjiang_skill.periods += [0.2, 0.2]
    jianchen_dot.duration = shangjiang_skill.cast_time + 2 * JIANCHEN_DELAY
    jianchen_dot.periods = [
        round(jianchen_dot.duration - JIANCHEN_DELAY - sum(shangjiang_skill.periods[:i + 1]), FLOAT_POINT) for i in
        range(shangjiang_skill.times)]


zhanfen_effect = Effect("斩纷", duration=16)


def zhanfen_talent(attack_power=0.15):
    zuizhan_skill.direct = True

    def zhanfen_apply(skills, attribute):
        attribute.physical_attack_power_gain += attack_power

    def zhanfen_revoke(skills, attribute):
        attribute.physical_attack_power_gain -= attack_power

    zhanfen_effect.apply = zhanfen_apply
    zhanfen_effect.revoke = zhanfen_revoke


# 8
def xinghuo_talent():
    pass


def juehe_talent():
    pofu_skill.overdraw = 1
    pofu_skill.k_b += 0.3


# 9
jinghong_skill = Skill("惊鸿", base_damage=46, attack_power_cof=1.25)


def jinghong_talent(cd_reduce=3, critical_strike=0.1, critical_effect=0.2):
    pofu_skill.cd -= cd_reduce
    pofu_skill.critical_strike += critical_strike
    pofu_skill.critical_effect += critical_effect


def chuge_talent():
    pass


linjiang_skill = Skill("临江", base_damage=122, attack_power_cof=0.2375)


def linjiang_talent():
    pass


JUEQI_RATE = 0.3
jueqi_skill = Skill("绝期", base_damage=57.5, attack_power_cof=0.75, )


# 10
def jueqi_talent(k=0.7):
    naoxumi_dot.k_b += k


yangdao_skill = Skill("扬刀激尘", base_damage=318.5, weapon_damage_cof=2, attack_power_cof=4.3876, gcd=True, cd=15)
yangdao_dot = Skill("扬刀激尘-持续", base_damage=260, weapon_damage_cof=0, attack_power_cof=1.1, period=1,
                    duration=5)


def yangdao_talent():
    pass


ZHONGYAN_RATE = 0.3


# 11
def zhongyan_talent():
    pass


def lifeng_talent():
    zuizhan_skill.cast_time = 2.19
    zuizhan_skill.period = 0.31
    zuizhan_skill.k_b += 0.25


# 12
xiangqi_pre_effect = Effect("降麒式-前置", max_layers=6)
xiangqi_ready_effect = Effect("降麒式-就绪", duration=15)
xiangqi_effect = Effect("降麒式", duration=15)
xiangqi_skill = Skill("降麒式")
xiangqi_dot = Skill("降麒式-持续", base_damage=52.5, weapon_damage_cof=1, attack_power_cof=0.75, duration=15, period=1)


def xiangqi_talent(cd_reduce=2, k=0.2):
    qinlongliuzhan_skill.cd -= cd_reduce

    def xiangqi_apply(skills, attribute):
        attribute.k_b += k

    def xiangqi_revoke(skills, attribute):
        attribute.k_b -= k

    xiangqi_effect.apply = xiangqi_apply
    xiangqi_effect.revoke = xiangqi_revoke


xinjing_effect = Effect("心镜", duration=15)


def xinjing_talent(critical_strike=0.2, critical_effect=0.2):
    jianbi_dot.duration += 5
    jianbi_dot.max_duration += 5

    def xinjing_apply(skills, attribute):
        for skill in skills:
            if skill in jinping_list:
                skill.critical_strike += critical_strike
                skill.critical_effect += critical_effect

    def xinjing_revoke(skills, attribute):
        for skill in skills:
            if skill in jinping_list:
                skill.critical_strike -= critical_strike
                skill.critical_effect -= critical_effect

    xinjing_effect.apply = xinjing_apply
    xinjing_effect.revoke = xinjing_revoke


linjiang_list = [xiangqi_skill, pofu_skill, shangjiang_skill]
hanfeng_list = jinping_list + [jianbi_dot]
jueqi_list = chenshen_list + jinping_list + zhuwu_list + [jianbi_dot, melee, jinghong_skill, xiangqi_dot]
divine_list = jueqi_list