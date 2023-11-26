from base.simulator import Simulator
from base.target import Target
from general.buffs import BUFFS
from general.skills import SKILLS
from ui.constant import ATTR_TYPE_TRANSLATE
from utils.simulate import simulate_delta


def display_attr(attribute, display_attrs):
    texts = []
    for attr, name in display_attrs.items():
        value = getattr(attribute, attr)
        if isinstance(value, int):
            texts.append(f"{name}: {value}")
        else:
            texts.append(f"{name}: {round(value * 100, 2)}%")
    return "\n".join(texts)


def combat_script(combat_components,
                  equip_components, consumable_components,
                  gain_components, talent_components, recipe_components):
    def build_attr(class_attr, equip_attr, consumable_attr, target_level, duration,
                   equip_gains, team_gains, talent_gains, recipe_gains):
        attribute = class_attr['attribute']()
        display_attrs = class_attr['display_attrs']
        for attr, value in equip_attr.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        for attr, value in consumable_attr.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        init_attr_text = display_attr(attribute, display_attrs)
        gains = sum([equip_gains, team_gains, talent_gains, recipe_gains], [])
        simulator = Simulator(attribute, SKILLS + class_attr['skills'], BUFFS + class_attr['buffs'], gains,
                              Target(target_level), duration, *class_attr['simulator'].values())
        gain_attr_text = display_attr(attribute, display_attrs)
        return init_attr_text, gain_attr_text, simulator

    def build_summary(class_attr, iteration, simulator):
        dps, details, gradients = simulate_delta(
            class_attr['damage'], class_attr['attribute'], iteration, simulator
        )
        total_damage = dps * simulator.duration
        summary_texts = []
        for skill, detail in details.items():
            count = detail['hit'] + detail['critical']
            summary_texts.append(f"{skill}:\t次数{count}\t"
                                 f"\t命中{detail['hit']}/{round(detail['hit'] / count * 100, 2)}%\t"
                                 f"\t会心{detail['critical']}/{round(detail['critical'] / count * 100, 2)}%\t"
                                 f"\t伤害{detail['damage']}/{round(detail['damage'] / total_damage * 100, 2)}%")
        gradient_texts = [f"{ATTR_TYPE_TRANSLATE[k]}:\t{round(v[0], 2)}/{round(v[1], 4)}" for k, v in gradients.items()]
        return dps, "\n".join(summary_texts), "\n".join(gradient_texts)

    combat_components['simulate'].click(
        build_attr,
        [combat_components['class_attr'], equip_components['attr_state'], consumable_components['attr_state'],
         combat_components['target_level'], combat_components['duration'],
         equip_components['gain_state'], gain_components['gain_state'],
         talent_components['gain_state'], recipe_components['gain_state']],
        [combat_components['init_attribute'], combat_components['gain_attribute'], combat_components['simulator']]
    ).then(
        build_summary,
        [combat_components['class_attr'], combat_components['iteration'], combat_components['simulator']],
        [combat_components['dps'], combat_components['summary'], combat_components['gradient']]
    )
