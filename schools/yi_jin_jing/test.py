from base.simulator import Simulator
from base.target import Target
from schools.yi_jin_jing import (YiJinJing, SKILLS, BUFFS, TALENTS, TALENT_GAINS, RECIPES, RECIPE_GAINS,
                                 prepare, priority, loop, initiation)
from utils.analyze import analyze_details


def main():
    duration = 300

    attribute = YiJinJing()
    attribute.spirit_base += 10000
    attribute.surplus += 10000
    attribute.strain_base += 30000
    attribute.haste_base += 5200
    attribute.magical_attack_power_base += 20000
    attribute.magical_critical_strike_base += 10000
    attribute.magical_overcome_base += 25000

    gains = ([TALENT_GAINS[talents[0]] for talents in TALENTS]
             + [RECIPE_GAINS[recipe] for recipes in RECIPES.values() for recipe in recipes[:4]])
    simulator = Simulator(attribute, SKILLS, BUFFS, gains, Target(), duration,
                          prepare=prepare, priority=priority, loop=loop, initiation=initiation, verbose=True)
    counts = simulator()
    dps, details, summary, gradients = analyze_details(1, simulator, counts)
    print(details)


if __name__ == '__main__':
    main()
