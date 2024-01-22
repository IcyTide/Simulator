from base.simulator import Simulator
from base.target import Target
from schools.gu_feng_jue import (GuFengJue, SKILLS, BUFFS, TALENTS, TALENT_GAINS, RECIPES, RECIPE_GAINS,
                                 prepare, priority, loop, initiation)
from utils.analyze import analyze_details


def main():
    duration = 300

    attribute = GuFengJue()
    attribute.strength_base += 10000
    attribute.surplus += 10000
    attribute.strain_base += 10000
    attribute.haste_base += 5000
    attribute.physical_attack_power_base += 10000
    attribute.physical_critical_strike_base += 10000
    attribute.physical_overcome_base += 10000

    gains = ([TALENT_GAINS[talents[0]] for talents in TALENTS]
             + [RECIPE_GAINS[recipe] for recipes in RECIPES.values() for recipe in recipes[:4]])

    simulator = Simulator(attribute, SKILLS, BUFFS, gains, Target(), duration,
                          prepare=prepare, priority=priority, loop=loop, initiation=initiation, verbose=True)
    counts = simulator()
    dps, details, summary, gradients = analyze_details(
        1, simulator, counts
    )
    print(details)


if __name__ == '__main__':
    main()
