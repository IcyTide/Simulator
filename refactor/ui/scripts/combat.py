from base.simulator import Simulator
from base.target import Target


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
        init_attr_texts = [f"{name}: {getattr(attribute, attr)}" for attr, name in display_attrs.items()]
        gains = sum([team_gains, talent_gains, recipe_gains], [])
        simulator = Simulator(attribute, class_attr['skills'], class_attr['buffs'], gains,
                              Target(target_level), duration)
        gain_attr_texts = [f"{name}: {getattr(attribute, attr)}" for attr, name in display_attrs.items()]
        return "\n".join(init_attr_texts), "\n".join(gain_attr_texts), simulator

    combat_components['attribute_button'].click(
        build_attr,
        [combat_components['class_attr'], combat_components['target_level'], combat_components['duration'],
         equip_components['attr_state'], consumable_components['attr_state'],
         gain_components['gain_state'], talent_components['gain_state'], recipe_components['gain_state']],
        [combat_components['init_attribute'], combat_components['gain_attribute'], combat_components['simulator']])

