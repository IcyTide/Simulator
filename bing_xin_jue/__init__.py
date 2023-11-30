from base.status import Status
from bing_xin_jue.attribute import BingXinJue
from bing_xin_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from bing_xin_jue.talents import TALENTS, TALENT_GAINS
from bing_xin_jue.recipes import RECIPES, RECIPE_GAINS
from bing_xin_jue.skills import SKILLS
from bing_xin_jue.buffs import BUFFS


def hua_bing(status: Status):
    return not status.stacks["化冰"]


def fan_yin_ji_jie(status: Status):
    return status.stacks["钗燕·计数"] == 2 or status.stacks["凝华"] == 6


def guang_ling_yue(status: Status):
    return status.stacks["流玉"]


prepare = [
    "江海凝光", "玳弦急曲", "玳弦急曲", "江海凝光", "剑气长江", "玳弦急曲"
]
priority = [
    "名动四方", ("心鼓弦", hua_bing), ("繁音急节", fan_yin_ji_jie), ("广陵月", guang_ling_yue), "剑影留痕"
]
loop = [
    "江海凝光", "剑气长江", "玳弦急曲",
    # "江海凝光", "剑破虚空", "玳弦急曲",
    "江海凝光", "剑气长江", "玳弦急曲",
]
