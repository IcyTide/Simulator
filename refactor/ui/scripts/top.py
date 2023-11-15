import json

import gradio as gr

from ui.constant import SUPPORT_CLASS


def top_script(equipments, top_components, equipments_components):
    def update_class_name(class_name):
        class_attr = SUPPORT_CLASS[class_name]
        equip_updates = []
        for equip in equipments:
            equipment = equipments[equip]
            choices = list(equipment[(equipment['kind'].isin([class_attr['kind'], class_attr['major']])) & (
                equipment['school'].isin(["精简", "通用", class_attr['school']]))].index)
            equip_updates.append(gr.update(choices=[""] + choices, value="", visible=True))
        return gr.update(value=class_attr), *equip_updates

    top_components['class_name'].input(update_class_name, top_components['class_name'],
                                       [top_components['class_attr'],
                                        *[equipments_components[equip]['equip_name'] for equip in equipments]])
