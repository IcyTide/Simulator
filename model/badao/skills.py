from abstract import Skill, Counter, Effect
from constants import GCD

# Skill
divine_dot = Skill("divine-dot", base_damage=1, period=GCD * 2, duration=GCD * 12)


def divine_dot_effect_apply(skills, attribute):
    for skill in skills:
        if skill is divine_dot:
            divine_dot.attack_power_cof += 0.6


def divine_dot_effect_revoke(skills, attribute):
    for skill in skills:
        if skill is divine_dot:
            divine_dot.attack_power_cof -= 0.6


divine_dot_effect = Effect("divine-dot", duration=22, max_layers=3, apply=divine_dot_effect_apply,
                           revoke=divine_dot_effect_revoke)

xiangwang_skill = Skill("项王击鼎", base_damage=257.5, weapon_damage_cof=1, attack_power_cof=1.6312, gcd=True)
xiangwang_whirl_skill = Skill("项王击鼎-风车", base_damage=200, weapon_damage_cof=1, attack_power_cof=0.7875,
                              cast_time=2, period=0.5)

shangjiang_skill = Skill("上将军印", base_damage=307.5, weapon_damage_cof=1, attack_power_cof=0.9875, cast_time=1.7,
                         periods=[0, 0.35, 0.35, 0.5, 0.5], gcd=True, cd=18)
pofu_skill = Skill("破釜沉舟", base_damage=360, weapon_damage_cof=2, attack_power_cof=2.7, gcd=True, cd=9, overdraw=2)
pofu_counter = Counter("破釜沉舟-破招", counter_cof=11.543)
pofu_counter_effect = Effect("破釜沉舟-破招", duration=60, layer=2)
chenshen_effect = Effect("秀明尘身")

naoxumi_skill = Skill("闹须弥", gcd=True, cd=25)
naoxumi_dot = Skill("闹须弥-持续", base_damage=52, attack_power_cof=0.4375, period=GCD * 2,
                    duration=GCD * 16, snapshot=True)
jingyan_skill = Skill("惊燕式", base_damage=26, weapon_damage_cof=1, attack_power_cof=0.697, periods=[0, 1.43],
                      cast_time=0, gcd=True)
zhuying_skill = Skill("逐鹰式", base_damage=26, weapon_damage_cof=1, attack_power_cof=0.775, periods=[0, 1.43],
                      cast_time=GCD, gcd=True)
konghe_skill = Skill("控鹤式", base_damage=52, weapon_damage_cof=1, attack_power_cof=0.8937, periods=[0, 1.43],
                     cast_time=GCD, gcd=True)
qifeng_skill = Skill("起凤式", base_damage=52, weapon_damage_cof=1, attack_power_cof=1.05, periods=[0, 1.43],
                     cast_time=GCD, gcd=True)
tengjiao_skill = Skill("腾蛟式", base_damage=52, weapon_damage_cof=1, attack_power_cof=1.1657, periods=[0, 1.43],
                       cast_time=GCD, gcd=True)
qinlong_skill = Skill("擒龙式", base_damage=52, weapon_damage_cof=1, attack_power_cof=1.2437, periods=[0, 1.43],
                      cast_time=GCD, gcd=True, )
qinlongliuzhan_skill = Skill("擒龙六斩", cd=10, gcd=True)

qinlong_effect = Effect("擒龙六斩", duration=2, max_layers=5)

qinlong_counter = Counter("擒龙六斩-破招", counter_cof=3.6278)
zhuwu_effect = Effect("松烟竹雾")

zuizhan_skill = Skill("醉斩白蛇", base_damage=260, attack_power_cof=0.5437, cast_time=2, period=0.5, gcd=True,
                      cast=True)
daoxiao_skill = Skill("刀啸风吟", base_damage=260, attack_power_cof=2.5562, cast_time=GCD, gcd=True, cast=True)
daoxiao_counter = Counter("刀啸风吟-破招", counter_cof=1.8138)
jianbi_skill = Skill("坚壁清野", base_damage=440, attack_power_cof=1.6625, gcd=True, cd=30)
jianbi_dot = Skill("坚壁清野-持续", base_damage=260, attack_power_cof=1.1, period=1, duration=10)

jinping_effect = Effect("雪絮金屏")

chenshen_list = [xiangwang_skill, xiangwang_whirl_skill, shangjiang_skill, pofu_skill]
qinlong_list = [jingyan_skill, zhuying_skill, konghe_skill, qifeng_skill, tengjiao_skill, qinlong_skill]
zhuwu_list = [naoxumi_skill] + qinlong_list
jinping_list = [daoxiao_skill, zuizhan_skill, jianbi_skill]
