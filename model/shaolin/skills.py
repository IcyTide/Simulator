from abstract import Skill, Counter, Effect

counter = Counter(name="破招", counter_cof=7.8086492308)


def tanpo_effect_apply(skills, attribute):
    attribute.k_counter -= 0.03


def tanpo_effect_revoke(skills, attribute):
    attribute.k_counter += 0.03


tanpo_effect = Effect(name="贪破", max_layers=10, apply=tanpo_effect_apply, revoke=tanpo_effect_revoke)

pudu_skill = Skill(name="普渡四方", base_damage=163.5, attack_power_cof=0.973958333, gcd=True)
pudu_weapon_skill = Skill(name="普渡四方-外功", weapon_damage_cof=1)


def pudu_effect_apply(skills, attribute):
    for skill in skills:
        if skill in pudu_list:
            skill.k_d += 0.04


def pudu_effect_revoke(skills, attribute):
    for skill in skills:
        if skill in pudu_list:
            skill.k_d -= 0.04


pudu_effect = Effect(name="普渡", duration=18, max_layers=2, apply=pudu_effect_apply, revoke=pudu_effect_revoke)

weituo_skill = Skill(name="韦陀献杵", base_damage=179, attack_power_cof=1.916666667, gcd=True)
weotuo_weapon_skill = Skill(name="韦陀献杵-外功", weapon_damage_cof=2)
hengsao_skill = Skill(name="横扫六合", base_damage=75, attack_power_cof=1.25, weapon_damage_cof=1, gcd=True, cd=12)
hengsao_weapon_skill = Skill(name="韦陀献杵-外功", weapon_damage_cof=2)
hengsao_dot = Skill(name="横扫六合-持续", base_damage=45, attack_power_cof=0.119791667, duration=12, period=2,
                    snapshot=True)

bufeng_skill = Skill(name="捕风式", base_damage=63, attack_power_cof=0.2739, gcd=True, cd=6)
bufeng_effect = Effect(name="捕风式", duration=30)
zhuoying_skill = Skill(name="捉影式", cd=20)
nayun_skill = Skill(name="拿云式", base_damage=258.5, attack_power_cof=2.182291667, gcd=True)
shouque_skill = Skill(name="守缺式", base_damage=144.5, attack_power_cof=1.432291667, gcd=True, cd=7, charge=3)

luohan_skill = Skill(name="罗汉金身", cd=20)


def luohan_effect_apply(skills, attribute):
    attribute.magical_overcome_gain += 0.3


def luohan_effect_revoke(skills, attribute):
    attribute.magical_overcome_gain -= 0.3


luohan_effect = Effect(name="罗汉金身", duration=20)

erye_skill = Skill(name="二业依缘", cd=45)


def fumo_effect_apply(skills, attribute):
    attribute.k_b += 0.1


def fumo_effect_revoke(skills, attribute):
    attribute.k_b -= 0.1


fumo_effect = Effect(name="伏魔", apply=fumo_effect_apply, revoke=fumo_effect_revoke)
jiasha_effect = Effect(name="袈裟")

qianjin_skill = Skill(name="千斤坠", attack_power_cof=0.083333333, gcd=True, cd=25)
qinlong_skill = Skill(name="擒龙诀", cd=60)


def qinlong_effect_apply(skills, attribute):
    attribute.magical_attack_power_gain += 0.2


def qinlong_effect_revoke(skills, attribute):
    attribute.magical_attack_power_gain -= 0.2


qinlong_effect = Effect(name="擒龙诀", duration=15.1, apply=qinlong_effect_apply, revoke=qinlong_effect_revoke)

channa_gain_list = [pudu_skill, hengsao_skill, weituo_skill, bufeng_skill, zhuoying_skill, shouque_skill, nayun_skill,
                    qianjin_skill]
channa_lost_list = [weituo_skill, nayun_skill, luohan_skill]
tanpo_list = [bufeng_skill, zhuoying_skill, shouque_skill, nayun_skill]
tanpo_break_list = [pudu_skill, hengsao_skill, weituo_skill, qianjin_skill]
pudu_list = [pudu_skill, hengsao_skill, weituo_skill, bufeng_skill, zhuoying_skill, shouque_skill, nayun_skill]
