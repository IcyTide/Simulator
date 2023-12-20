from base.status import Status
from schools.bing_xin_jue.attribute import BingXinJue
from schools.bing_xin_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.bing_xin_jue.skills import SKILLS
from schools.bing_xin_jue.buffs import BUFFS
from schools.bing_xin_jue.talents import TALENTS, TALENT_GAINS
from schools.bing_xin_jue.recipes import RECIPES, RECIPE_GAINS


def hua_bing(status: Status):
    return not status.stacks["繁音急节"] and not status.stacks["广陵月"]


def fan_yin_ji_jie(status: Status):
    return status.stacks["钗燕-计数"] == 2 or status.stacks["凝华"] == 6


def guang_ling_yue(status: Status):
    return status.stacks["流玉"]


prepare = '江海凝光,玳弦急曲,玳弦急曲'
priority = '名动四方,连环双刀,心鼓弦(繁音急节:stack=0&广陵月:stack=0),繁音急节(钗燕-计数:stack=2|凝华:stack=6),剑影留痕,广陵月(流玉:stack>0)'
loop = '江海凝光,剑破虚空,玳弦急曲,江海凝光,剑气长江,玳弦急曲,江海凝光,剑气长江,玳弦急曲'
