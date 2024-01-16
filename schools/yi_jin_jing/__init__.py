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
罗汉金身,
擒龙诀(禅那:stack=0),
千斤坠·无取(金刚日轮:stack=0|千斤坠·无取:duration<0.75),
千斤坠·无舍(金刚日轮:stack=0|千斤坠·无舍:duration<0.75),
千斤坠·无取(禅那:stack<2&金刚日轮:duration<=5.5&拿云式:cd>=0.75),
千斤坠·无舍(禅那:stack<2&金刚日轮:duration<=5.5&拿云式:cd>=0.75),
千斤坠·无取(禅那:stack=2&金刚日轮:duration<=5.5&拿云式:cd<0.75),
千斤坠·无舍(禅那:stack=2&金刚日轮:duration<=5.5&拿云式:cd<0.75),
横扫六合(罗汉金身:duration>9),
拿云式,韦陀献杵,
千斤坠(金刚日轮:stack=0|禅那:stack<3),
守缺式(守缺式:energy=3&禅那:stack<3),
捕风式(禅那:stack<3),
摩诃无量(禅那:stack=1),
守缺式(禅那:stack<3),
普渡四方"""
loop = ''
