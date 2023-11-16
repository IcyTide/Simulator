import gradio as gr

from ui.constant import ATTR_TYPE_TRANSLATE, CONSUMABLES


def gain_script(gain_components):
    def consumable_dropdown_update(consumable_type):
        def inner(consumable_name, consumables_attrs):
            if consumable_name:
                consumables_attrs[consumable_type] = {"name": consumable_name, "attrs": CONSUMABLES[consumable_name]}
            else:
                consumables_attrs.pop(consumable_type)
            return consumables_attrs

        return inner

    def consumable_checkbox_update(consumable_type):
        def inner(consumable_name, consumables_attrs):
            if consumable_name:
                consumables_attrs[consumable_type] = {"name": consumable_name, "attrs": CONSUMABLES[consumable_name[0]]}
            else:
                consumables_attrs.pop(consumable_type)

            return consumables_attrs

        return inner

    def update_attr(consumables_attrs):
        attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}
        name_texts = []
        for consumable_type, consumable_attr in consumables_attrs.items():
            name_texts.append(f"{consumable_type}: {consumable_attr['name']}")
            for attr, value in consumable_attr['attrs'].items():
                attrs[attr] += value

        attr_texts = [f"{ATTR_TYPE_TRANSLATE[k]}: {v}" for k, v in attrs.items() if v]
        return "\n".join(name_texts), "\n".join(attr_texts), attrs

    for consumable, component in gain_components['consumables'].items():
        if isinstance(component, gr.Dropdown):
            component.input(
                consumable_dropdown_update(consumable),
                [component, gain_components['consumable_attrs']],
                gain_components['consumable_attrs']
            ).then(
                update_attr,
                gain_components['consumable_attrs'],
                [gain_components['consumable_names'], gain_components['attrs'], gain_components['attr_state']]
            )
        elif isinstance(component, gr.CheckboxGroup):
            component.input(
                consumable_checkbox_update(consumable),
                [component, gain_components['consumable_attrs']],
                gain_components['consumable_attrs']
            ).then(
                update_attr,
                gain_components['consumable_attrs'],
                [gain_components['consumable_names'], gain_components['attrs'], gain_components['attr_state']]
            )
