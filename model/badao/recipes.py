from badao.skills import shangjiang_skill, pofu_skill, daoxiao_skill, qinlong_list, zuizhan_skill
from badao.talents import jianchen_dot


def shangjiang_recipe(k, c):
    shangjiang_skill.k_b += k
    shangjiang_skill.critical_strike += c
    jianchen_dot.k_b += k
    jianchen_dot.critical_strike += c


def pofu_recipe(k, c):
    pofu_skill.k_b += k
    pofu_skill.critical_strike += c


def daoxiao_recipe(k, c):
    daoxiao_skill.k_b += k
    daoxiao_skill.critical_strike += c


def qinlong_recipe(k, c):
    for skill in qinlong_list:
        skill.k_b += k
        skill.critical_strike += c


def zuizhan_recipe(k, c):
    zuizhan_skill.k_b += k
    zuizhan_skill.critical_strike += c