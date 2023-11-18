import json

import gradio as gr

from ui.constant import SUPPORT_CLASS, MAJOR_FOODS, MINOR_FOODS, MAJOR_POTIONS, MINOR_POTIONS, WEAPON_ENCHANTS, SPREADS, \
    SNACKS, WINES


def top_script(equipments, detail, top_components, equip_components, consumable_components):
    def update_class_name(class_name):
        if not class_name:
            return
        class_attr = SUPPORT_CLASS[class_name]
        equip_updates = []
        for equip in equipments:
            equipment = equipments[equip]
            choices = list(equipment[(equipment['kind'].isin([class_attr['kind'], class_attr['major']])) & (
                equipment['school'].isin(["精简", "通用", class_attr['school']]))].index)
            equip_updates.append(gr.update(choices=[""] + choices, value="", visible=True))
        consumable_updates = [
            gr.Dropdown(choices=[""] + MAJOR_FOODS[class_attr['major']], value=""),
            gr.Dropdown(choices=[""] + MINOR_FOODS[class_attr['kind']] + MINOR_FOODS["通用"], value=""),
            gr.Dropdown(choices=[""] + MAJOR_POTIONS[class_attr['major']], value=""),
            gr.Dropdown(choices=[""] + MINOR_POTIONS[class_attr['kind']] + MINOR_POTIONS["通用"], value=""),
            gr.Dropdown(choices=[""] + WEAPON_ENCHANTS[class_attr['kind']], value=""),
            gr.Dropdown(choices=[""] + SNACKS[class_attr['kind']] + SNACKS["通用"], value=""),
            gr.Dropdown(choices=[""] + WINES[class_attr['major']] + WINES["通用"], value=""),
            None,
            None,
            gr.Dropdown(choices=[""] + SPREADS[class_attr['major']] + SPREADS[class_attr['kind']], value=""),
            None
        ]
        return gr.update(visible=True), gr.update(value=class_attr), *equip_updates, *consumable_updates

    top_components['class_name'].input(
        update_class_name, top_components['class_name'],
        [detail, top_components['class_attr'],
         *[equip_component['equip_name'] for equip_component in equip_components['equips'].values()],
         *consumable_components['consumables'].values()])
