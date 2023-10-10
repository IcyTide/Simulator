from shaolin.skills import pudu_skill, weituo_skill, hengsao_skill, hengsao_dot, bufeng_skill, shouque_skill, \
    nayun_skill
from shaolin.talents import xiangmo_weituo_skill, xiangmo_nayun_skill, zhongchen_effect


def pudu_recipe(k, cd):
    pudu_skill.k_b += k
    pudu_skill.cd -= cd


def weituo_recipe(k, c=0):
    weituo_skill.k_b += k
    weituo_skill.critical_strike += c
    xiangmo_weituo_skill.k_b += k
    xiangmo_weituo_skill.critical_strike += c


def hengsao_recipe(k, duration):
    hengsao_skill.k_b += k
    hengsao_dot.duration += duration
    hengsao_dot.max_duration += duration
    zhongchen_effect.duration += duration
    zhongchen_effect.max_duration += duration


def bufeng_recipe(k, cd):
    bufeng_skill.cd -= cd
    bufeng_skill.k_b += k


def shouque_recipe(k, c):
    shouque_skill.k_b += k
    shouque_skill.critical_strike += c


def nayun_recipe(k):
    nayun_skill.k_b += k
    xiangmo_nayun_skill.k_b += k


