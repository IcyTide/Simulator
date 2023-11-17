import gradio as gr

from ui.constant import ATTR_TYPE_TRANSLATE, CONSUMABLES, TEAM_GAINS, TEAM_GAINS_NAME


def gain_script(gain_components):
    def consumable_dropdown_update(consumable_type):
        def inner(consumables_attrs, consumable_name):
            if consumable_name:
                consumables_attrs[consumable_type] = {"name": consumable_name, "attrs": CONSUMABLES[consumable_name]}
            else:
                consumables_attrs.pop(consumable_type)
            return consumables_attrs

        return inner

    def consumable_checkbox_update(consumable_type):
        def inner(consumables_attrs, consumable_name):
            if consumable_name:
                consumables_attrs[consumable_type] = {"name": consumable_name[0], "attrs": CONSUMABLES[consumable_type]}
            else:
                consumables_attrs.pop(consumable_type)

            return consumables_attrs

        return inner

    def update_attr(consumables_attrs):
        attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}
        name_texts = []
        for consumable_type, consumable_attr in consumables_attrs.items():
            for attr, value in consumable_attr['attrs'].items():
                attrs[attr] += value
            name_texts.append(f"{consumable_type}: {consumable_attr['name']}")

        attr_texts = [f"{ATTR_TYPE_TRANSLATE[k]}: {v}" for k, v in attrs.items() if v]
        return "\n".join(name_texts), "\n".join(attr_texts), attrs

    for consumable, component in gain_components['consumables'].items():
        if isinstance(component, gr.Dropdown):
            component.input(
                consumable_dropdown_update(consumable),
                [gain_components['consumable_attrs'], component],
                gain_components['consumable_attrs']
            ).then(
                update_attr,
                gain_components['consumable_attrs'],
                [gain_components['consumable_names'], gain_components['attrs'], gain_components['attr_state']]
            )
        elif isinstance(component, gr.CheckboxGroup):
            component.input(
                consumable_checkbox_update(consumable),
                [gain_components['consumable_attrs'], component],
                gain_components['consumable_attrs']
            ).then(
                update_attr,
                gain_components['consumable_attrs'],
                [gain_components['consumable_names'], gain_components['attrs'], gain_components['attr_state']]
            )

    def team_gain_params_update(team_gain_type, *team_gain_keys):
        def inner(team_gains, *team_gain_values):
            if all(team_gain_values):
                team_gains[team_gain_type] = {
                    "param": "\t".join([f"{k}{v}" for k, v in zip(team_gain_keys, team_gain_values)]),
                    "gain": TEAM_GAINS[team_gain_type](*team_gain_values)}
            else:
                team_gains.pop(team_gain_type)
            return team_gains

        return inner

    def team_gain_checkbox_update(team_gain_type):
        def inner(team_gains, team_gain):
            if team_gain:
                team_gains[team_gain_type] = {"gain": TEAM_GAINS[team_gain_type]}
            else:
                team_gains.pop(team_gain_type)

            return team_gains

        return inner

    def update_gain(team_gains):
        gains = []
        name_texts = []
        for team_gain_type, team_gain in team_gains.items():
            gains.append(team_gain['gain'])
            if param := team_gain.get('param'):
                name_texts.append(f"{TEAM_GAINS_NAME[team_gain_type]}: {param}")
            else:
                name_texts.append(f"{team_gain_type}: {TEAM_GAINS_NAME[team_gain_type]}")

        return "\n".join(name_texts), gains

    for team, component in gain_components['teams'].items():
        if isinstance(component, dict):
            for sub_component in component.values():
                sub_component.input(
                    team_gain_params_update(team, *component.keys()),
                    [gain_components['team_gains'], *component.values()],
                    gain_components['team_gains'],
                    trigger_mode="multiple"
                ).then(
                    update_gain,
                    gain_components['team_gains'],
                    [gain_components['team_gain_names'], gain_components['gain_state']],
                    trigger_mode="multiple"
                )
        elif isinstance(component, gr.CheckboxGroup):
            component.input(
                team_gain_checkbox_update(team),
                [gain_components['team_gains'], component],
                gain_components['team_gains']
            ).then(
                update_gain,
                gain_components['team_gains'],
                [gain_components['team_gain_names'], gain_components['gain_state']]
            )
