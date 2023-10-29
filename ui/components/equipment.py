import json

import gradio as gr

from constant import ATTR_MAP, ATTR_TYPE_MAP, POSITION_MAP, MAX_EMBED_NUMBER, MAX_EMBED_LEVEL


def get_equip_name(row):
    name = row['Name']
    attrs = " ".join([ATTR_MAP[attr] for attr in ATTR_MAP if attr in row['_Attrs']])
    level = row['Level']
    return f"{name} ({attrs})  {level}"


def build_equipment():
    equips = []
    strengths = []
    embeds = []
    enchants = []
    for label, equip in POSITION_MAP.items():
        equipments = json.load(open(f"assets/{equip}.json", encoding="utf-8"))
        with gr.Row():
            equip_dropdown = gr.Dropdown(choices=[(get_equip_name(row), row)
                                                  for row in equipments],
                                         label=label, scale=6)
            equips.append(equip_dropdown)
            strengths_dropdown = gr.Dropdown(choices=[], label="精炼", visible=False, scale=2)
            strengths.append(strengths_dropdown)
            embed_dropdowns = []
            for _ in range(MAX_EMBED_NUMBER):
                embed_dropdowns.append(
                    gr.Dropdown(choices=list(range(1, MAX_EMBED_LEVEL + 1)), value=MAX_EMBED_LEVEL,
                                visible=False)
                )
                embeds.append(embed_dropdowns)

            def equip_dropdown_func(e):
                embed_updates = []
                for i in range(MAX_EMBED_NUMBER):
                    embed_attr = e[f'_DiamondAttributeID{i + 1}']
                    if embed_attr:
                        embed_updates.append(gr.update(label=ATTR_TYPE_MAP[embed_attr[0]], visible=True))
                    else:
                        embed_updates.append(gr.update(visible=False))
                max_strength = int(e['MaxStrengthLevel'])
                return gr.update(choices=list(range(1, max_strength + 1)), value=max_strength,
                                 visible=True), *embed_updates

            equip_dropdown.input(equip_dropdown_func, equip_dropdown, [strengths_dropdown, *embed_dropdowns])
