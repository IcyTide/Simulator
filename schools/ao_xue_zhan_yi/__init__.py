from base.status import Status
from schools.ao_xue_zhan_yi.attribute import AoXueZhanYi
from schools.ao_xue_zhan_yi.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.ao_xue_zhan_yi.skills import SKILLS
from schools.ao_xue_zhan_yi.buffs import BUFFS
from schools.ao_xue_zhan_yi.talents import TALENTS, TALENT_GAINS
from schools.ao_xue_zhan_yi.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.buffs["战意"].increase(5)


prepare = ''
priority = """
下马(牧云:duration<1.5|渊:cd=0&龙牙:cd>0.75),
突(牧云:duration<1.5),
渊(牧云:duration>10),
撼如雷(渊:duration=10),
任驰骋(渊:duration=10),
断魂刺(战意:stack=2),
龙吟(流血:duration<1.5),
龙牙(战意:stack=5),
灭(战意:stack=2),
龙吟(战意:stack<4),
穿云(战意:stack!=4)
"""
loop = ''
