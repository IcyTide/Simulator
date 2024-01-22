from base.status import Status
from schools.gu_feng_jue.attribute import GuFengJue
from schools.gu_feng_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.gu_feng_jue.skills import SKILLS
from schools.gu_feng_jue.buffs import BUFFS
from schools.gu_feng_jue.talents import TALENTS, TALENT_GAINS
from schools.gu_feng_jue.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.buffs["双手持刀"].trigger()


prepare = '游风飘踪,识破,孤锋破浪'
priority = '识破(身形:duration<=1),灭影追风(行云式:cd=0)'
loop = """
决云式,留客雨,行云式,行云式,留客雨,行云式,行云式,留客雨,行云式,行云式,留客雨,断云式,识破,横云断浪,沧浪三叠,沧浪三叠,沧浪三叠,孤锋破浪,
决云式,留客雨,行云式,行云式,留客雨,行云式,行云式,留客雨,行云式,行云式,留客雨,断云式,横云断浪,沧浪三叠,沧浪三叠,沧浪三叠,孤锋破浪,
决云式,留客雨,行云式,行云式,留客雨,行云式,行云式,留客雨,行云式,行云式,留客雨,断云式,横云断浪,沧浪三叠,沧浪三叠,沧浪三叠,游风飘踪(沧浪三叠:cd=0),识破,孤锋破浪
"""
