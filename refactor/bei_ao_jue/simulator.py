import copy

from base.simulator import Simulator
from base.status import Status
from bei_ao_jue.attribute import get_attribute

from bei_ao_jue.skills import skills
from bei_ao_jue.buffs import buffs
from bei_ao_jue.talents import talents
from bei_ao_jue.recipes import recipes
from bei_ao_jue.gains import gains


def wait_gcd(status: Status):
    return not status.gcd_group[0]


def wait_pofu(status: Status):
    return "破釜沉舟" not in status.cds


prepare_list = ["雪絮金屏", "刀啸风吟", "坚壁清野", "松烟竹雾", "闹须弥", "秀明尘身", "破釜沉舟"]
priority = ["霜风刀法", "雷走风切"]
loop = ["上将军印", "破釜沉舟", ("雪絮金屏", wait_gcd), "刀啸风吟", "松烟竹雾", "擒龙六斩", "秀明尘身",
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


def call(lst):

    simulator = Simulator(get_attribute(), copy.deepcopy(skills), copy.deepcopy(buffs),
                          copy.deepcopy(talents), copy.deepcopy(recipes), copy.deepcopy(gains),
                          prepare_list=prepare_list, loop=loop, priority=priority, duration=180)

    simulator()
    lst.append(simulator.status.total_damage)


if __name__ == '__main__':
    results = list()
    for _ in range(1):
        call(results)
    print(results)
