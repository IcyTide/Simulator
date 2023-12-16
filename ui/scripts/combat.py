from base.simulator import Simulator
from base.target import Target
from general.buffs import BUFFS
from general.skills import SKILLS
from ui.constant import ATTR_TYPE_TRANSLATE
from utils.simulate import simulate_delta

import gradio as gr


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
    def build_attr(school_attr, equip_attr, consumable_attr, target_level, duration, prepare, priority, loop,
                   equip_gains, team_gains, talent_gains, recipe_gains):
        attribute = school_attr['attribute']()
        display_attrs = school_attr['display_attrs']
        for attr, value in equip_attr.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        for attr, value in consumable_attr.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        init_attr_text = display_attr(attribute, display_attrs)
        gains = sum([equip_gains, team_gains, talent_gains, recipe_gains], [])
        simulator = Simulator(attribute, SKILLS[school_attr['kind']] + school_attr['skills'],
                              BUFFS + school_attr['buffs'],
                              gains, Target(target_level), duration, prepare, priority, loop, verbose=False)
        gain_attr_text = display_attr(attribute, display_attrs)
        return init_attr_text, gain_attr_text, simulator

    def build_summary(school_attr, iteration, simulator, delta_value):
        dps, details, gradients, delta_dps, delta_details, delta_gradients = simulate_delta(
            school_attr['attribute'], iteration, simulator, delta_value
        )
        total_damage = dps * simulator.duration
        summary_texts = []
        for skill, detail in details.items():
            count = round(detail['hit'] + detail['critical'], 2)
            summary_texts.append(
                f"{skill}:\t次数{count}\t"
                f"\t命中{detail['hit']}/{round(detail['hit'] / count * 100, 2)}%\t"
                f"\t会心{detail['critical']}/{round(detail['critical'] / count * 100, 2)}%\t"
                f"\t伤害{detail['damage']}/{round(detail['damage'] / total_damage * 100, 2)}%")
        gradient_texts = [f"{ATTR_TYPE_TRANSLATE[k]}:\t{round(v[0], 2)}/{round(v[1], 4)}" for k, v in gradients.items()]
        if delta_dps:
            total_damage = delta_dps * simulator.duration
            delta_summary_texts = []
            for skill, detail in delta_details.items():
                count = round(detail['hit'] + detail['critical'], 2)
                delta_summary_texts.append(
                    f"{skill}:\t次数{count}\t平均伤害\t{round(detail['damage'] / count, 2)}\t"
                    f"\t命中{detail['hit']}/{round(detail['hit'] / count * 100, 2)}%\t"
                    f"\t会心{detail['critical']}/{round(detail['critical'] / count * 100, 2)}%\t"
                    f"\t伤害{detail['damage']}/{round(detail['damage'] / total_damage * 100, 2)}%")
            delta_gradient_texts = [
                f"{ATTR_TYPE_TRANSLATE[k]}:\t{round(v[0], 2)}/{round(v[1], 4)}" for k, v in delta_gradients.items()]
            return (round(dps), "\n".join(summary_texts), "\n".join(gradient_texts),
                    gr.update(visible=True, value=round(delta_dps)),
                    gr.update(visible=True, value="\n".join(delta_summary_texts)),
                    gr.update(visible=True, value="\n".join(delta_gradient_texts)))
        return round(dps), "\n".join(summary_texts), "\n".join(gradient_texts), gr.update(visible=False), gr.update(
            visible=False), gr.update(visible=False)

    combat_components['simulate'].click(
        build_attr,
        [combat_components['school_attr'], equip_components['attr_state'], consumable_components['attr_state'],
         combat_components['target_level'], combat_components['duration'], *combat_components['sequences'].values(),
         equip_components['gain_state'], gain_components['gain_state'],
         talent_components['gain_state'], recipe_components['gain_state']],
        [combat_components['init_attribute'], combat_components['gain_attribute'], combat_components['simulator']]
    ).then(
        build_summary,
        [combat_components['school_attr'], combat_components['iteration'],
         combat_components['simulator'], combat_components['delta_value']],
        [combat_components['dps'], combat_components['summary'], combat_components['gradient'],
         combat_components['delta_dps'], combat_components['delta_summary'], combat_components['delta_gradient']]
    )
