from general.consumables import CONSUMABLES
from gr.constant import ATTR_TYPE_TRANSLATE


def consumable_script(consumable_components):
    def update_consumable(consumable_type):
        def inner(consumables_attrs, consumable_name):
            if consumable_name:
                if isinstance(consumable_name, list):
                    consumables_attrs[consumable_type] = {"name": consumable_name[0],
                                                          "attrs": CONSUMABLES[consumable_type]}
                else:
                    consumables_attrs[consumable_type] = {"name": consumable_name,
                                                          "attrs": CONSUMABLES[consumable_name]}
            else:
                consumables_attrs[consumable_type] = {}

            return consumables_attrs

        return inner

    def update_attr(consumables_attrs):
        attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}
        name_texts = []
        for consumable_type, consumable_attr in consumables_attrs.items():
            if not consumable_attr:
                continue
            for attr, value in consumable_attr['attrs'].items():
                attrs[attr] += value
            name_texts.append(f"{consumable_type}: {consumable_attr['name']}")

        attr_texts = [f"{ATTR_TYPE_TRANSLATE[k]}: {v}" for k, v in attrs.items() if v]
        return "\n".join(name_texts), "\n".join(attr_texts), attrs

    for consumable, component in consumable_components['consumables'].items():
        component.input(
            update_consumable(consumable),
            [consumable_components['consumable_attrs'], component],
            consumable_components['consumable_attrs']
        ).then(
            update_attr,
            consumable_components['consumable_attrs'],
            [consumable_components['consumable_names'], consumable_components['attrs'],
             consumable_components['attr_state']]
        )
