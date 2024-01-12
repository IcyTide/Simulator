from base.status import Status
from schools.yi_jin_jing.attribute import YiJinJing
from schools.yi_jin_jing.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.yi_jin_jing.skills import SKILLS
from schools.yi_jin_jing.buffs import BUFFS
from schools.yi_jin_jing.talents import TALENTS, TALENT_GAINS
from schools.yi_jin_jing.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.buffs["禅那"].increase(3)
    status.buffs["拿云"].increase(3)
    status.skills["二业依缘"].cast()


prepare = ''
priority = """
六合棍,
千斤坠(金刚日轮:stack=0),
千斤坠·无取(金刚日轮:stack=0|千斤坠·无取:duration<1),
千斤坠·无舍(金刚日轮:stack=0|千斤坠·无舍:duration<1),
拿云式(罗汉金身:stack>0),韦陀献杵(罗汉金身:stack>0),
摩诃无量(罗汉金身:duration<=1.5&禅那:stack=1),
守缺式(罗汉金身:duration<=1.5&禅那:stack<3),
捕风式(罗汉金身:duration<=1.5&禅那:stack<3),
普渡四方(罗汉金身:duration<=1.5&禅那:stack<3)"""
loop = """
罗汉金身,擒龙诀,横扫六合,守缺式(禅那:stack<3|拿云:stack=0),捕风式,守缺式,守缺式,捕风式,普渡四方,捉影式,守缺式,普渡四方,
罗汉金身,横扫六合,守缺式,捕风式,守缺式,守缺式,捕风式,普渡四方,守缺式,捉影式,捕风式,守缺式,
罗汉金身,横扫六合,守缺式,捕风式,守缺式,守缺式,捕风式,普渡四方,守缺式,捉影式,捕风式,守缺式
"""
