from base.attribute import Attribute, Target
from base.simulator import Simulator
from base.status import Status
from bei_ao_jue.buffs import buffs
from bei_ao_jue.skills import skills
from bei_ao_jue.talents import talents


def wait(status: Status):
    return not status.gcd_group[0]


prepare_list = ["雪絮金屏", "刀啸风吟", "坚壁清野", "松烟竹雾", "闹须弥", "秀明尘身", "破釜沉舟"]
priority = ["霜风刀法", "雷走风切", "降麒式"]
loop = ["上将军印", "破釜沉舟", ("雪絮金屏", wait), "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身",
        "上将军印", "破釜沉舟", "破釜沉舟", ("松烟竹雾", wait), "擒龙六斩", "秀明尘身",
        "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身", "破釜沉舟",

        "上将军印", "破釜沉舟", ("松烟竹雾", wait), "擒龙六斩", "雪絮金屏", "坚壁清野", "秀明尘身",
        "上将军印", "破釜沉舟", "破釜沉舟", ("松烟竹雾", wait), "擒龙六斩", "秀明尘身",
        "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身", "破釜沉舟",

        "上将军印", "破釜沉舟", ("松烟竹雾", wait), "擒龙六斩", "逐鹰式", "秀明尘身",
        "上将军印", "破釜沉舟", ("雪絮金屏", wait), "坚壁清野", "秀明尘身", "破釜沉舟",
        "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身", "破釜沉舟",

        "上将军印", "破釜沉舟", ("雪絮金屏", wait), "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身",
        "上将军印", "破釜沉舟", "破釜沉舟", ("松烟竹雾", wait), "擒龙六斩", "秀明尘身",
        "上将军印", "雪絮金屏", "坚壁清野", "松烟竹雾", "擒龙六斩", "秀明尘身", "破釜沉舟",
        ]

if __name__ == '__main__':
    simulator = Simulator(Attribute(Target(), haste_base=300), skills, buffs, talents,
                          prepare_list=prepare_list, loop=loop)

    simulator()
