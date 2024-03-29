from base.status import Status
from schools.bing_xin_jue.attribute import BingXinJue
from schools.bing_xin_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.bing_xin_jue.skills import SKILLS
from schools.bing_xin_jue.buffs import BUFFS
from schools.bing_xin_jue.talents import TALENTS, TALENT_GAINS
from schools.bing_xin_jue.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    for _ in range(10):
        status.buffs["剑舞"].trigger()
    status.skills["名动四方"].cast()


prepare = '江海凝光,玳弦急曲,玳弦急曲'
priority = '连环双刀,心鼓弦(繁音急节:stack=0&广陵月:stack=0),繁音急节(钗燕-计数:stack=2|凝华:stack=6),剑影留痕(化冰:stack>0),广陵月(流玉:stack>0)'
loop = '江海凝光,剑破虚空,玳弦急曲,江海凝光,剑气长江,玳弦急曲,江海凝光,剑气长江,玳弦急曲'
