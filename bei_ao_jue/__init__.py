from base.status import Status
from bei_ao_jue.attribute import BeiAoJue
from bei_ao_jue.gains import EQUIP_GAINS_NAME, EQUIP_GAINS
from bei_ao_jue.talents import TALENTS, TALENT_GAINS
from bei_ao_jue.recipes import RECIPES, RECIPE_GAINS
from bei_ao_jue.skills import SKILLS
from bei_ao_jue.buffs import BUFFS


def wait_gcd(status: Status):
    return not status.gcd_group.get(0)


def wait_pofu(status: Status):
    return "破釜沉舟" not in status.cds


prepare = ["雪絮金屏", "刀啸风吟", "坚壁清野", "松烟竹雾", "闹须弥", "秀明尘身", "破釜沉舟"]
priority = ["霜风刀法", "雷走风切"]
loop = [
    "上将军印", "破釜沉舟", ("雪絮金屏", wait_gcd), "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身",
    "上将军印", "破釜沉舟", "破釜沉舟", ("松烟竹雾", wait_gcd), "擒龙六斩", "秀明尘身",
    "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身", "破釜沉舟",

    "上将军印", "破釜沉舟", ("松烟竹雾", wait_gcd), "擒龙六斩", "雪絮金屏", "坚壁清野", "秀明尘身",
    "上将军印", "破釜沉舟", "破釜沉舟", ("松烟竹雾", wait_gcd), "擒龙六斩", "秀明尘身",
    "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", ("降麒式", wait_pofu), "秀明尘身", "破釜沉舟",

    "上将军印", "破釜沉舟", ("松烟竹雾", wait_gcd), "擒龙六斩", "逐鹰式", "秀明尘身",
    "上将军印", "破釜沉舟", ("雪絮金屏", wait_gcd), "坚壁清野", "秀明尘身", "破釜沉舟",
    "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身", "破釜沉舟",

    "上将军印", "破釜沉舟", ("雪絮金屏", wait_gcd), "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身",
    "上将军印", "破釜沉舟", "破釜沉舟", ("松烟竹雾", wait_gcd), "擒龙六斩", "秀明尘身",
    "上将军印", "雪絮金屏", "坚壁清野", "松烟竹雾", "擒龙六斩", ("降麒式", wait_pofu), "秀明尘身", "破釜沉舟",
]
