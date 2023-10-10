from abstract import Effect, Skill
from shaolin.skills import pudu_effect, hengsao_skill, hengsao_dot, shouque_skill, luohan_effect, weituo_skill, \
    nayun_skill, erye_skill, bufeng_skill, qianjin_skill, pudu_skill, zhuoying_skill, qinlong_skill


# 1
def mingfa_talent():
    pudu_effect.max_layers = 3


def bingxin_talent():
    pass


bingxin_list = [bufeng_skill, shouque_skill, zhuoying_skill]
nayun_effect = Effect(name="拿云", max_layers=3)


# 2
def huanshen_talent():
    hengsao_skill.k_c += 0.65
    hengsao_dot.k_c += 0.65


def shanxin_talent():
    pass


# 3
shenyi_effect = Effect(name="身意", duration=2)


def shenyi_talent():
    shouque_skill.critical_strike += 0.1
    shouque_skill.critical_effect += 0.1

    def shenyi_effect_apply(skills, attribute):
        attribute.magical_critical_strike_gain += 0.05
        attribute.magical_critical_effect_gain += 0.05

    def shenyi_effect_revoke(skills, attribute):
        attribute.magical_critical_strike_gain -= 0.05
        attribute.magical_critical_effect_gain -= 0.05

    shenyi_effect.apply = shenyi_effect_apply
    shenyi_effect.revoke = shenyi_effect_revoke


def fenyun_wuqu_effect_apply(skills, attribute):
    for skill in skills:
        if skill is qianjin_skill:
            skill.gcd = False


def fenyun_wuqu_effect_revoke(skills, attribute):
    for skill in skills:
        if skill is qianjin_skill:
            skill.gcd = True


def fenyun_wushe_effect_apply(skills, attribute):
    for skill in skills:
        if skill is qianjin_skill:
            skill.gcd = False


def fenyun_wushe_effect_revoke(skills, attribute):
    for skill in skills:
        if skill is qianjin_skill:
            skill.gcd = True


fenyun_wuqu_effect = Effect(name="纷纭-无取", duration=9, apply=fenyun_wuqu_effect_apply,
                            revoke=fenyun_wuqu_effect_revoke)
fenyun_wushe_effect = Effect(name="纷纭-无舍", duration=9, apply=fenyun_wushe_effect_apply,
                             revoke=fenyun_wushe_effect_revoke)


def fenyun_talent():
    pass


# 4
suodi_skill = Skill(name="缩地", base_damage=407.5, attack_power_cof=0.833333333)
suodi_effect = Effect(name="缩地")
suodi_list = [pudu_skill, hengsao_skill, weituo_skill, bufeng_skill, nayun_skill, shouque_skill, qianjin_skill]


def suodi_talent():
    pass


# 5
xiangmo_weituo_skill = Skill(name="降魔-韦陀献杵", base_damage=6, attack_power_cof=0.453125)
xiangmo_nayun_skill = Skill(name="降魔-拿云式", base_damage=26, attack_power_cof=0.520833333)


def xiangmo_talent():
    pass


# 6
def jingang_talent():
    def luohan_effect_apply(skills, attribute):
        attribute.magical_overcome_gain += 0.3
        attribute.magical_attack_power_gain += 0.3

    def luohan_effect_revoke(skills, attribute):
        attribute.magical_overcome_gain -= 0.3
        attribute.magical_attack_power_gain -= 0.3

    luohan_effect.apply = luohan_effect_apply
    luohan_effect.revoke = luohan_effect_revoke


def xizhu_talent():

    qinlong_skill.cd = 25
    qinlong_skill.charge = 3
    qinlong_skill.duration = 9.1
    qinlong_skill.max_duration = 9.1


# 7
def jingguo_talent():
    pass


jingguo_list = [pudu_skill, hengsao_skill, weituo_skill, bufeng_skill, nayun_skill, shouque_skill, qianjin_skill]

# 8
sansheng_effect = Effect(name="三生", max_layers=3)


def sansheng_talent():
    def sansheng_effect_apply(skills, attribute):
        attribute.magical_attack_power_gain += 0.08

    def sansheng_effect_revoke(skills, attribute):
        attribute.magical_attack_power_gain -= 0.08

    sansheng_effect.apply = sansheng_effect_apply
    sansheng_effect.revoke = sansheng_effect_revoke


def wowen_effect():
    hengsao_skill.critical_strike += 0.01
    hengsao_skill.critical_effect += 0.02
    hengsao_skill.cd -= 3
    hengsao_dot.critical_strike += 0.01
    hengsao_dot.critical_effect += 0.02


def hengsao_dot_effect_apply(skills, attribute):
    for skill in skills:
        if skill is hengsao_dot:
            skill.attack_power_cof += 0.119791667


def hengsao_dot_effect_revoke(skills, attribute):
    for skill in skills:
        if skill is hengsao_dot:
            hengsao_dot.attack_power_cof -= 0.119791667


hengsao_dot_effect = Effect("横扫六合-持续", duration=hengsao_dot.duration, max_layers=3,
                            apply=hengsao_dot_effect_apply,
                            revoke=hengsao_dot_effect_revoke)

# 9
zhongchen_effect = Effect(name="众嗔", duration=hengsao_dot.duration)
zhongchen_list = [shouque_skill, weituo_skill, nayun_skill]


def zhongchen_talent():
    def zhongchen_effect_apply(skills, attribute):
        for skill in skills:
            if skill in zhongchen_list:
                skill.k_c += 0.2

    def zhongchen_effect_revoke(skills, attribute):
        for skill in skills:
            if skill in zhongchen_list:
                skill.k_c -= 0.2

    zhongchen_effect.apply = zhongchen_effect_apply
    zhongchen_effect.revoke = zhongchen_effect_revoke


# 10
def huaxiang_talent():
    weituo_skill.ignore_defense += 0.6
    nayun_skill.ignore_defense += 0.6
    shouque_skill.ignore_defense += 0.6


# 11
foguo_skill = Skill(name="佛果", base_damage=127.5, attack_power_cof=0.953125, cd=1)
foguo_list = [pudu_skill, hengsao_skill, weituo_skill, bufeng_skill, nayun_skill, shouque_skill]


def foguo_talent():
    pass


rilun_effect = Effect(name="金刚日轮", duration=18, max_duration=18)
longzhao_skill = Skill(name="金刚龙爪功", attack_power_cof=1.5625)
longzhao_list = [bufeng_skill, shouque_skill, nayun_skill]
rilun_skill = Skill(name="金刚日轮", base_damage=29.5, attack_power_cof=2.5, ignore_defense=0.65)
rilun_list = [pudu_skill, hengsao_skill]


def rilun_talent():
    def rilun_effect_apply(skills, attribute):
        attribute.magical_critical_strike_gain += 0.06
        attribute.magical_critical_effect_gain += 0.06

    def rilun_effect_revoke(skills, attribute):
        attribute.magical_critical_strike_gain -= 0.06
        attribute.magical_critical_effect_gain -= 0.06

    rilun_effect.apply = rilun_effect_apply
    rilun_effect.revoke = rilun_effect_revoke


# 12
yeyin_pre_effect = Effect(name="业因-前置", layer=4, max_layers=4)
yeyin_effect = Effect(name="业因", max_layers=4)
yeyin_shouque_effect = Effect(name="业因-守缺", max_layers=4)
yeyin_hengsao_effect = Effect(name="业因-横扫", max_layers=4)
zhuyin_shouque_effect = Effect(name="主因-守缺")
zhuyin_hengsao_effect = Effect(name="主因-横扫")
guobao_shouque_skill = Skill(name="果报-守缺", attack_power_cof=3.125)
guobao_hengsao_skill = Skill(name="果报-横扫", attack_power_cof=2.083333333)
guobao_effect = Effect(name="果报", max_layers=4)
yeyin_map = {
    shouque_skill: yeyin_shouque_effect,
    hengsao_skill: yeyin_hengsao_effect
}
zhuyin_map = {
    yeyin_shouque_effect: zhuyin_shouque_effect,
    yeyin_hengsao_effect: zhuyin_hengsao_effect
}
guobao_map = {
    zhuyin_shouque_effect: guobao_shouque_skill,
    zhuyin_hengsao_effect: guobao_hengsao_skill
}
guobao_list = [weituo_skill, nayun_skill]


def yeyin_talent():
    erye_skill.cd = 45
