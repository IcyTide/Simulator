from base.status import Status
from schools.yi_jin_jing.attribute import YiJinJing
from schools.yi_jin_jing.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.yi_jin_jing.skills import SKILLS
from schools.yi_jin_jing.buffs import BUFFS
from schools.yi_jin_jing.talents import TALENTS, TALENT_GAINS
from schools.yi_jin_jing.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.buffs["禅那"].increase(3)
    status.skills["二业依缘"].cast()


prepare = ''
priority = ''
loop = ''
