from base.status import Status
from schools.tian_luo_gui_jian.attribute import TianLuoGuiJian
from schools.tian_luo_gui_jian.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.tian_luo_gui_jian.skills import SKILLS
from schools.tian_luo_gui_jian.buffs import BUFFS
from schools.tian_luo_gui_jian.talents import TALENTS, TALENT_GAINS
from schools.tian_luo_gui_jian.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.skills["神机回复"].cast()
    status.buffs["千机变"].trigger()
    status.buffs["暗藏杀机-一"].trigger()
    status.buffs["暗藏杀机-二"].trigger()
    status.buffs["神机"].increase(100)


prepare = """"""
priority = ""
loop = """
鬼斧神工,暗藏杀机,心无旁骛,天绝地灭,诡鉴冥微,天绝地灭,蚀肌弹,蚀肌弹,诡鉴冥微,天绝地灭
"""
