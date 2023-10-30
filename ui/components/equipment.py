import json
import os

import gradio as gr

from constant import *


def get_equip_name(row):
    name = row['Name']
    attrs = " ".join([ATTR_MAP[attr] for attr in ATTR_MAP if attr in row['_Attrs']])
    level = row['Level']
    return f"{name} ({attrs})  {level}"


def get_enchant_name(row):
    if not row:
        return ""
    name = row['Name']
    attr = row['AttriName']
    return f"{name} {attr}"


def get_base_attr(row):
    attrs = {}
    for i in range(MAX_BASE_ATTR):
        if not (attr_type := row[f'Base{i + 1}Type']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = (int(row[f'Base{i + 1}Max']) + int(row[f'Base{i + 1}Min'])) / 2
    return attrs


def get_magic_attr(row):
    attrs = {}
    for i in range(MAX_MAGIC_ATTR):
        if not (attr := row[f'_Magic{i + 1}Type']):
            break
        attr = attr['attr']
        if attr[0] not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr[0]]] = (int(attr[1]) + int(attr[2])) / 2
    return attrs


def get_embed_attr(row):
    attrs = {}
    for i in range(MAX_EMBED_ATTR):
        if not (attr := row[f'_DiamondAttributeID{i + 1}']):
            break
        if attr[0] not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr[0]]] = (int(attr[1]) + int(attr[2])) / 2
    return attrs


def get_enchant_attr(row):
    attrs = {}
    for i in range(MAX_ENCHANT_ATTR):
        if not (attr_type := row[f'Attribute{i + 1}ID']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = (int(row[f'Attribute{i + 1}Value1']) + int(
            row[f'Attribute{i + 1}Value2'])) / 2
    return attrs


def aggregate(*args):
    result = {}
    for arg in args:
        for k, v in arg.items():
            if k not in result:
                result[k] = 0
            result[k] += v
    return result


def build_equipment():
    final_attrs = []

    with gr.Row():
        with gr.Column(scale=5):
            for label, equip in POSITION_TRANSLATE.items():
                equipments = {get_equip_name(row): row for row in
                              json.load(open(os.path.join(EQUIPMENTS_DIR, f"{equip}.json"), encoding="utf-8"))}
                enchants = {get_enchant_name(row): row for row in
                            json.load(open(os.path.join(ENCHANTS_DIR, f"{equip}.json"), encoding="utf-8"))}
                with gr.Accordion(open=False, label=label) as equip_accordion:
                    with gr.Row():
                        with gr.Column(scale=8):
                            with gr.Row():
                                equipment_dropdown = gr.Dropdown(
                                    choices=list(equipments), label="装备")
                                strengths_level = gr.Number(minimum=0, maximum=MAX_STRENGTH_LEVEL, label="精炼",
                                                            value=MAX_STRENGTH_LEVEL, visible=False)

                            with gr.Row():
                                enchant_dropdown = gr.Dropdown(
                                    choices=list(enchants), label="附魔",
                                    visible=False)

                            with gr.Row():
                                embed_levels = []
                                for i in range(MAX_EMBED_ATTR):
                                    embed_level = gr.Number(minimum=0, maximum=MAX_EMBED_LEVEL, label=f"镶嵌-{i + 1}",
                                                            value=MAX_EMBED_LEVEL, visible=False)
                                    embed_levels.append(embed_level)

                        with gr.Column(scale=2, min_width=200):
                            base_box = gr.Textbox(label="基本属性", visible=False)
                            magic_box = gr.Textbox(label="精炼属性", visible=False)
                            embed_box = gr.Textbox(label="镶嵌属性", visible=False)
                            enchant_box = gr.Textbox(label="附魔属性", visible=False)

                    base_attr_base = gr.JSON(value={}, visible=False)
                    magic_attr_base = gr.JSON(value={}, visible=False)
                    embed_attr_base = gr.JSON(value={}, visible=False)

                    magic_attr_gain = gr.JSON(value={}, visible=False)
                    embed_attr_gain = gr.JSON(value={}, visible=False)
                    enchant_attr_gain = gr.JSON(value={}, visible=False)

                    final_attr = gr.JSON(value={}, visible=False)
                    final_attrs.append(final_attr)

                    def equipment_dropdown_func(name, equipment_map):
                        def inner(equip_name, enchant_name):
                            equip_row = equipment_map[equip_name]
                            base_attrs = get_base_attr(equip_row)
                            magic_attrs = get_magic_attr(equip_row)
                            embed_attrs = get_embed_attr(equip_row)

                            max_strength = int(equip_row['MaxStrengthLevel'])

                            embed_updates = []
                            for i in range(MAX_EMBED_ATTR):
                                if i < len(embed_attrs):
                                    embed_updates.append(gr.update(visible=True))
                                else:
                                    embed_updates.append(gr.update(visible=False))
                            return base_attrs, magic_attrs, embed_attrs, gr.update(visible=True), gr.update(
                                label=f"{name} {equip_name}/{enchant_name}"), gr.update(
                                maximum=max_strength,
                                value=max_strength,
                                visible=True), *embed_updates

                        return inner

                    equipment_dropdown.input(equipment_dropdown_func(label, equipments),
                                             [equipment_dropdown, enchant_dropdown],
                                             [base_attr_base, magic_attr_base, embed_attr_base, enchant_dropdown,
                                              equip_accordion, strengths_level, *embed_levels]
                                             )

                    def enchant_dropdown_func(name, enchant_map):
                        def inner(equip_name, enchant_name):
                            enchant_row = enchant_map[enchant_name]
                            enchant_attrs = get_enchant_attr(enchant_row)
                            return enchant_attrs, gr.update(
                                label=f"{name} {equip_name}/{enchant_name}")

                        return inner

                    enchant_dropdown.input(enchant_dropdown_func(label, enchants),
                                           [equipment_dropdown, enchant_dropdown],
                                           [enchant_attr_gain, equip_accordion])

                    def strength_gain_func(magic_base, level):
                        strength_cof = STRENGTH_COF(level)
                        magic_gain = {k: round(strength_cof * v) for k, v in magic_base.items()}
                        return magic_gain

                    strengths_level.change(strength_gain_func, [magic_attr_base, strengths_level], magic_attr_gain)
                    magic_attr_base.change(strength_gain_func, [magic_attr_base, strengths_level], magic_attr_gain)

                    def embed_gain_func(embed, *levels):
                        embed_gain = {}
                        for i, (k, v) in enumerate(embed.items()):
                            embed_cof = EMBED_COF(levels[i])
                            embed_gain[k] = round(embed_cof * v)
                        return embed_gain

                    for i, embed_level in enumerate(embed_levels):
                        embed_level.change(embed_gain_func,
                                           [embed_attr_base, *embed_levels], embed_attr_gain)
                    embed_attr_base.change(embed_gain_func,
                                           [embed_attr_base, *embed_levels], embed_attr_gain)

                    def base_box_func(base, magic_base, magic_gain, embed, enchant):
                        base_text = "\n".join([f"{v}: {base[k]}" for k, v in ATTR_TYPE_TRANSLATE.items() if k in base])
                        final = aggregate(base, magic_base, magic_gain, embed, enchant)
                        if base_text:
                            return gr.update(value=base_text, visible=True), final
                        else:
                            return gr.update(visible=False), final

                    base_attr_base.change(base_box_func,
                                          [base_attr_base, magic_attr_base, magic_attr_gain, embed_attr_gain,
                                           enchant_attr_gain],
                                          [base_box, final_attr])

                    def magic_box_func(base, magic_base, magic_gain, embed, enchant):
                        magic_text = "\n".join(
                            [f"{v}: {magic_base[k]}(+{magic_gain[k]})" for k, v in ATTR_TYPE_TRANSLATE.items() if
                             k in magic_base])
                        final = aggregate(base, magic_base, magic_gain, embed, enchant)
                        if magic_text:
                            return gr.update(value=magic_text, visible=True), final
                        else:
                            return gr.update(visible=False), final

                    magic_attr_gain.change(magic_box_func,
                                           [base_attr_base, magic_attr_base, magic_attr_gain, embed_attr_gain,
                                            enchant_attr_gain],
                                           [magic_box, final_attr])

                    def embed_box_func(base, magic_base, magic_gain, embed, enchant):
                        embed_text = "\n".join(
                            [f"{v}: {embed[k]}" for k, v in ATTR_TYPE_TRANSLATE.items() if k in embed])
                        final = aggregate(base, magic_base, magic_gain, embed, enchant)
                        if embed_text:
                            return gr.update(value=embed_text, visible=True), final
                        else:
                            return gr.update(visible=False), final

                    embed_attr_gain.change(embed_box_func,
                                           [base_attr_base, magic_attr_base, magic_attr_gain, embed_attr_gain,
                                            enchant_attr_gain],
                                           [embed_box, final_attr])

                    def enchant_box_func(base, magic_base, magic_gain, embed, enchant):
                        enchant_text = "\n".join(
                            [f"{v}: {enchant[k]}" for k, v in ATTR_TYPE_TRANSLATE.items() if k in enchant])
                        final = aggregate(base, magic_base, magic_gain, embed, enchant)
                        if enchant_text:
                            return gr.update(value=enchant_text, visible=True), final
                        else:
                            return gr.update(visible=False), final

                    enchant_attr_gain.change(enchant_box_func,
                                             [base_attr_base, magic_attr_base, magic_attr_gain, embed_attr_gain,
                                              enchant_attr_gain],
                                             [enchant_box, final_attr])

        with gr.Column(scale=5):
            equip_box = gr.Textbox(label="装备属性")
            equip_attr = gr.JSON(visible=False)

            base_attr = gr.JSON(value={}, visible=False)
            consumable_attr = gr.JSON(value={}, visible=False)

            def equip_attr_func(*attrs):
                return aggregate(*attrs)

            for final_attr in final_attrs:
                final_attr.change(equip_attr_func, final_attrs, equip_attr)

            def equip_box_func(attr):
                return "\n".join([f"{v}: {attr[k]}" for k, v in ATTR_TYPE_TRANSLATE.items() if k in attr])

            equip_attr.change(equip_box_func, equip_attr, equip_box)
