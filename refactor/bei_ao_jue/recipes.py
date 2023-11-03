from base.status import Status


def lei_zou_feng_qie_5_damage(status: Status):
    status.skills["雷走风切"].skill_damage_addition += 0.05


def lei_zou_feng_qie_4_damage(status: Status):
    status.skills["雷走风切"].skill_damage_addition += 0.04


def lei_zou_feng_qie_3_damage(status: Status):
    status.skills["雷走风切"].skill_damage_addition += 0.03


def lei_zou_feng_qie_4_critical(status: Status):
    status.skills["雷走风切"].skill_critical_strike += 0.04


def lei_zou_feng_qie_3_critical(status: Status):
    status.skills["雷走风切"].skill_critical_strike += 0.03


def lei_zou_feng_qie_2_critical(status: Status):
    status.skills["雷走风切"].skill_critical_strike += 0.02


def po_fu_chen_zhou_5_damage(status: Status):
    status.skills["破釜沉舟"].skill_damage_addition += 0.05


def po_fu_chen_zhou_4_damage(status: Status):
    status.skills["破釜沉舟"].skill_damage_addition += 0.04


def po_fu_chen_zhou_3_damage(status: Status):
    status.skills["破釜沉舟"].skill_damage_addition += 0.03


def po_fu_chen_zhou_4_critical(status: Status):
    status.skills["破釜沉舟"].skill_critical_strike += 0.04


def po_fu_chen_zhou_3_critical(status: Status):
    status.skills["破釜沉舟"].skill_critical_strike += 0.03


def po_fu_chen_zhou_2_critical(status: Status):
    status.skills["破釜沉舟"].skill_critical_strike += 0.02


def shang_jiang_jun_yin_4_damage(status: Status):
    status.skills["上将军印"].skill_damage_addition += 0.04
    status.skills["见尘"].skill_damage_addition += 0.04


def shang_jiang_jun_yin_3_damage(status: Status):
    status.skills["上将军印"].skill_damage_addition += 0.03
    status.skills["见尘"].skill_damage_addition += 0.03


def shang_jiang_jun_yin_2_damage(status: Status):
    status.skills["上将军印"].skill_damage_addition += 0.02
    status.skills["见尘"].skill_damage_addition += 0.02


def shang_jiang_jun_yin_4_critical(status: Status):
    status.skills["上将军印"].skill_critical_strike += 0.04


def shang_jiang_jun_yin_3_critical(status: Status):
    status.skills["上将军印"].skill_critical_strike += 0.03


def shang_jiang_jun_yin_2_critical(status: Status):
    status.skills["上将军印"].skill_critical_strike += 0.02


def qin_long_liu_zhan_5_damage(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].skill_damage_addition += 0.05


def qin_long_liu_zhan_4_damage(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].skill_damage_addition += 0.04


def qin_long_liu_zhan_3_damage(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].skill_damage_addition += 0.03


def qin_long_liu_zhan_4_critical(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].skill_critical_strike += 0.04


def qin_long_liu_zhan_3_critical(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].skill_critical_strike += 0.03


def qin_long_liu_zhan_2_critical(status: Status):
    related_skills = ["惊燕式", "逐鹰式"]
    for skill in related_skills:
        status.skills[skill].skill_critical_strike += 0.02


def dao_xiao_feng_yin_5_damage(status: Status):
    status.skills["刀啸风吟"].skill_damage_addition += 0.05


def dao_xiao_feng_yin_4_damage(status: Status):
    status.skills["刀啸风吟"].skill_damage_addition += 0.04


def dao_xiao_feng_yin_4_critical(status: Status):
    status.skills["刀啸风吟"].skill_critical_strike += 0.04


def dao_xiao_feng_yin_3_critical(status: Status):
    status.skills["刀啸风吟"].skill_critical_strike += 0.03


def dao_xiao_feng_yin_2_critical(status: Status):
    status.skills["刀啸风吟"].skill_critical_strike += 0.02


recipes = [
    lei_zou_feng_qie_5_damage, lei_zou_feng_qie_4_damage, lei_zou_feng_qie_3_damage, lei_zou_feng_qie_4_critical,
    shang_jiang_jun_yin_4_damage, shang_jiang_jun_yin_3_damage, shang_jiang_jun_yin_2_damage,
    shang_jiang_jun_yin_4_critical,
    po_fu_chen_zhou_5_damage, po_fu_chen_zhou_4_damage, po_fu_chen_zhou_3_damage, po_fu_chen_zhou_4_critical,
    qin_long_liu_zhan_5_damage, qin_long_liu_zhan_4_damage, qin_long_liu_zhan_4_critical,
    dao_xiao_feng_yin_5_damage, dao_xiao_feng_yin_4_damage, dao_xiao_feng_yin_4_critical
]
