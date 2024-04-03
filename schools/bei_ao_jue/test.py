from base.simulator import Simulator
from base.target import Target
from qt.scripts.combat import detail_content
from schools.bei_ao_jue import (BeiAoJue, SKILLS, BUFFS, TALENT_GAINS, RECIPES, RECIPE_GAINS, priority, initiation)
from utils.analyze import analyze_details
from utils.simulate import simulate_concurrent

# talents = ["龙息", "虎踞", "沧雪", "冥鼓", "霜天", "含风", "逐鹿", "百战", "掠关", "楚歌", "绝期", "重烟", "降麒式"]
# prepare = ",".join(["雪絮金屏", "刀啸风吟", "松烟竹雾", "闹须弥", "秀明尘身"])
# loop = ",".join([
#     "破釜沉舟", "松烟竹雾", "擒龙六斩", "秀明尘身", "项王击鼎", "雪絮金屏(刀啸风吟:cd=0)", "刀啸风吟", "松烟竹雾", "擒龙六斩", "逐鹰式",
#     "秀明尘身", "上将军印", "破釜沉舟", "破釜沉舟", "项王击鼎",
#     "破釜沉舟", "松烟竹雾", "擒龙六斩", "秀明尘身", "项王击鼎", "雪絮金屏(刀啸风吟:cd=0)", "刀啸风吟", "松烟竹雾", "擒龙六斩", "逐鹰式", "降麒式(刀啸风吟:cd=0)",
#     "秀明尘身", "上将军印", "破釜沉舟", "破釜沉舟", "项王击鼎",
# ])
talents = ["龙息", "虎踞", "归酣", "冥鼓", "霜天", "含风", "见尘", "分疆", "掠关", "楚歌", "绝期", "重烟", "降麒式"]
prepare = ",".join(["雪絮金屏", "刀啸风吟", "松烟竹雾", "闹须弥", "秀明尘身"])
# loop = ",".join([
#     "上将军印", "破釜沉舟", "项王击鼎",
#     "上将军印", "破釜沉舟", "破釜沉舟", "松烟竹雾", "擒龙六斩", "秀明尘身",
#     "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "逐鹰式", "秀明尘身",
#     "上将军印", "破釜沉舟", "项王击鼎",
#     "上将军印", "破釜沉舟", "破釜沉舟", "松烟竹雾", "擒龙六斩", "秀明尘身",
#     "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "逐鹰式", "降麒式(上将军印:cd=0)", "秀明尘身",
# ])
loop = ",".join([
    "破釜沉舟", "上将军印", "破釜沉舟", "项王击鼎",
    "上将军印", "破釜沉舟", "破釜沉舟", "松烟竹雾", "擒龙六斩", "秀明尘身",
    "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "逐鹰式", "秀明尘身",
    "上将军印", "破釜沉舟", "项王击鼎",
    "上将军印", "破釜沉舟", "松烟竹雾", "擒龙六斩", "逐鹰式", "秀明尘身",
    "上将军印", "雪絮金屏", "刀啸风吟", "松烟竹雾", "擒龙六斩", "降麒式(破釜沉舟:cd=0)", "秀明尘身",
])


def main():
    duration = 180

    attribute = BeiAoJue()
    attribute.strength_base += 10000
    attribute.surplus += 20000
    attribute.strain_base += 20000
    attribute.haste_base += 300
    attribute.physical_attack_power_base += 20000
    attribute.physical_critical_strike_base += 20000
    attribute.physical_overcome_base += 20000

    gains = ([TALENT_GAINS[talent] for talent in talents]
             + [RECIPE_GAINS[recipe] for recipes in RECIPES.values() for recipe in recipes[:4]])

    simulator = Simulator(attribute, SKILLS, BUFFS, gains, Target(), duration,
                          prepare=prepare, priority=priority, loop=loop, initiation=initiation, verbose=True)
    # counts = simulate_concurrent(10000, simulator)
    counts = simulator()
    dps, details, summary, gradients = analyze_details(
        1, simulator, counts
    )
    detail_content(details)
    print(details)
    import pandas as pd
    df = pd.DataFrame(summary, columns=["技能", "等级", "倍数", "次数", "增益(增益,等级,层数)"])
    df.to_excel("result.xlsx")


if __name__ == '__main__':
    main()
