from base.status import Status
from schools.fen_ying_sheng_jue.attribute import FenYingShengJue
from schools.fen_ying_sheng_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from schools.fen_ying_sheng_jue.skills import SKILLS
from schools.fen_ying_sheng_jue.buffs import BUFFS
from schools.fen_ying_sheng_jue.talents import TALENTS, TALENT_GAINS
from schools.fen_ying_sheng_jue.recipes import RECIPES, RECIPE_GAINS


def initiation(status: Status):
    status.buffs["日灵"].increase(100)
    status.buffs["月灵"].increase(100)
    status.buffs["日月同辉"].trigger()


prepare = """
净世破魔击,净世破魔击,驱夜断愁,烈日斩,暗尘弥散(悬象著明:cd=0),悬象著明,生死劫,诛邪镇魔,
驱夜断愁,银月斩,净世破魔击,诛邪镇魔,净世破魔击,诛邪镇魔,
驱夜断愁,净世破魔击,诛邪镇魔,银月斩,烈日斩,净世破魔击,银月斩,光明相,生死劫,
诛邪镇魔,净世破魔击,驱夜断愁,烈日斩,净世破魔击,诛邪镇魔,净世破魔击,净世破魔击
"""
priority = ""
loop = """
银月斩,诛邪镇魔,烈日斩,赤日轮,银月斩,净世破魔击,烈日斩,生死劫,
银月斩,诛邪镇魔,烈日斩,赤日轮,银月斩,净世破魔击,烈日斩,净世破魔击,诛邪镇魔,银月斩,
净世破魔击,驱夜断愁,暗尘弥散(悬象著明:cd=0),悬象著明,生死劫,诛邪镇魔,
驱夜断愁,银月斩,净世破魔击,诛邪镇魔,净世破魔击,诛邪镇魔,
驱夜断愁,净世破魔击,诛邪镇魔,银月斩,烈日斩,净世破魔击,银月斩,生死劫,
诛邪镇魔,驱夜断愁,烈日斩,净世破魔击,银月斩,净世破魔击,诛邪镇魔,烈日斩,净世破魔击,净世破魔击,
银月斩,诛邪镇魔,烈日斩,赤日轮,银月斩,净世破魔击,烈日斩,生死劫,
银月斩,诛邪镇魔,烈日斩,赤日轮,银月斩,净世破魔击,烈日斩,净世破魔击,诛邪镇魔,银月斩,
净世破魔击,驱夜断愁,暗尘弥散(悬象著明:cd=0),悬象著明,生死劫,诛邪镇魔,
驱夜断愁,银月斩,净世破魔击,诛邪镇魔,净世破魔击,诛邪镇魔,
驱夜断愁,净世破魔击,诛邪镇魔,银月斩,烈日斩,净世破魔击,银月斩,光明相,生死劫,
诛邪镇魔,净世破魔击,驱夜断愁,烈日斩,净世破魔击,银月斩,净世破魔击,诛邪镇魔,净世破魔击,净世破魔击
"""
