from base.simulator import Simulator
from base.target import Target


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
    def build_attr(class_attr, target_level, duration,
                   equip_attr, consumable_attr, team_gains, talent_gains, recipe_gains):
        attribute = class_attr['attribute']()
        display_attrs = class_attr['display_attrs']
        for attr, value in equip_attr.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        for attr, value in consumable_attr.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        init_attr_text = display_attr(attribute, display_attrs)
        gains = sum([team_gains, talent_gains, recipe_gains], [])
        simulator = Simulator(attribute, class_attr['skills'], class_attr['buffs'], gains, Target(target_level),
                              duration, *class_attr['simulator'].values())
        gain_attr_text = display_attr(attribute, display_attrs)
        return init_attr_text, gain_attr_text, simulator

    def simulate(simulator):
        actions, events = simulator()
        actions_texts = [f"{action[0]}: {action[1]}" for action in actions]
        event_texts = [f"{event[0]}: {event[1]} {event[2]} {event[3]}" for event in events]
        return "\n".join(actions_texts), "\n".join(event_texts)

    combat_components['simulate'].click(
        build_attr,
        [combat_components['class_attr'], combat_components['target_level'], combat_components['duration'],
         equip_components['attr_state'], consumable_components['attr_state'],
         gain_components['gain_state'], talent_components['gain_state'], recipe_components['gain_state']],
        [combat_components['init_attribute'], combat_components['gain_attribute'], combat_components['simulator']]
    ).then(
        simulate, combat_components['simulator'], [combat_components['actions'], combat_components['events']]
    )
