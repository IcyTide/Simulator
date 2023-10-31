import json
import os

import gradio as gr
import pandas as pd

from bei_ao_jue.attribute import BeiAoJue
from ui.constant import *


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


def build_equipment():
    stones = pd.read_json(open(STONES_DIR, encoding="utf-8"))
    with gr.Row():
        with gr.Column(scale=8):
            equipments_json = gr.JSON(value={}, visible=False)
            for label, equip in POSITION_TRANSLATE.items():
                equipments = {get_equip_name(row): row for row in
                              json.load(open(os.path.join(EQUIPMENTS_DIR, f"{equip}.json"), encoding="utf-8"))}
                enchants = {get_enchant_name(row): row for row in
                            json.load(open(os.path.join(ENCHANTS_DIR, f"{equip}.json"), encoding="utf-8"))}

                with gr.Accordion(open=False, label=label) as equip_accordion:
                    with gr.Row():
                        with gr.Column(scale=8):
                            with gr.Row():
                                equipment_dropdown = gr.Dropdown(choices=[""] + list(equipments), label="装备", value="")
                                strength_level = gr.Dropdown(choices=list(range(MAX_STRENGTH_LEVEL + 1)), label="精炼",
                                                             value=MAX_STRENGTH_LEVEL, visible=False)

                            with gr.Row():
                                enchant_dropdown = gr.Dropdown(choices=[""] + list(enchants), label="附魔", value="",
                                                               visible=False)

                                special_enchant_dropdown = gr.Checkbox(label="大附魔", visible=False)

                            with gr.Row():
                                embed_levels = []
                                for i in range(MAX_EMBED_ATTR):
                                    embed_level = gr.Dropdown(choices=list(range(MAX_EMBED_LEVEL + 1)),
                                                              label=f"镶嵌-{i + 1}", value=MAX_EMBED_LEVEL, visible=False)
                                    embed_levels.append(embed_level)

                            with gr.Group(visible=False) as stone_group:
                                with gr.Row():
                                    stone_level = gr.Dropdown(choices=list(range(MAX_STONE_LEVEL + 1)), label="五彩石等级",
                                                              value=MAX_STONE_LEVEL)
                                    stone_select = gr.Textbox(label="五彩石")
                                with gr.Row():
                                    stone_attrs = []
                                    for i in range(MAX_STONE_ATTR):
                                        if i:
                                            stone_attr = gr.Dropdown(choices=[""], label=f"五彩石属性{i + 1}", value="",
                                                                     visible=False)
                                        else:
                                            choices = [""] + [ATTR_TYPE_TRANSLATE[ATTR_TYPE_MAP[e]] for e in
                                                              stones[stones['stone_level'] == MAX_STONE_LEVEL][
                                                                  'Attribute1ID'].unique()]
                                            stone_attr = gr.Dropdown(choices=choices, label=f"五彩石属性{i + 1}",
                                                                     value="")
                                        stone_attrs.append(stone_attr)

                        with gr.Column(scale=2, min_width=200):
                            base_box = gr.Textbox(label="基本属性", visible=False)
                            magic_box = gr.Textbox(label="精炼属性", visible=False)
                            embed_box = gr.Textbox(label="镶嵌属性", visible=False)
                            enchant_box = gr.Textbox(label="附魔属性", visible=False)
                            stone_box = gr.Textbox(label="五彩石属性", visible=False)

                    # base_attr_base = gr.JSON(value={}, visible=False)
                    # magic_attr_base = gr.JSON(value={}, visible=False)
                    # embed_attr_base = gr.JSON(value={}, visible=False)
                    #
                    # magic_attr_gain = gr.JSON(value={}, visible=False)
                    # embed_attr_gain = gr.JSON(value={}, visible=False)
                    # enchant_attr_gain = gr.JSON(value={}, visible=False)
                    #
                    # final_attr = gr.JSON(value={}, visible=False)
                    # final_attrs.append(final_attr)
                    equipment_json = gr.JSON(value={"base": {}, "magic": {}, "embed": {}, "enchant": {}, "stone": {},
                                                    "equip_name": "", "enchant_name": "", "stone_name": "",
                                                    "strength_level": MAX_STRENGTH_LEVEL,
                                                    "embed_levels": [MAX_EMBED_LEVEL for _ in range(MAX_EMBED_ATTR)]},
                                             visible=False)

                    def equipment_dropdown_func(name, position, equipment_map, enchant_map):
                        def inner(equip_name, enchant_name, stone_name, equip_attr):
                            if not equip_name:
                                equip_attr["base"] = {}
                                equip_attr["magic"] = {}
                                equip_attr["embed"] = {}
                                equip_attr["enchant"] = {}
                                equip_attr["stone"] = {}
                                return equip_attr, gr.update(visible=False), gr.update(visible=False), gr.update(
                                    visible=False), gr.update(label=name), gr.update(visible=False), *[
                                    gr.update(visible=False) for _ in range(MAX_EMBED_ATTR)]

                            equip_row = equipment_map[equip_name]
                            equip_attr["base"] = get_base_attr(equip_row)
                            equip_attr["magic"] = get_magic_attr(equip_row)
                            equip_attr["embed"] = get_embed_attr(equip_row)
                            if enchant_name:
                                enchant_row = enchant_map[enchant_name]
                                equip_attr["enchant"] = get_enchant_attr(enchant_row)
                            else:
                                equip_attr["enchant"] = {}

                            max_strength = int(equip_row['MaxStrengthLevel'])
                            equip_attr["strength_level"] = max_strength

                            embed_updates = []
                            embed_attrs = [ATTR_TYPE_TRANSLATE[k] for k in equip_attr['embed']]
                            for k in range(MAX_EMBED_ATTR):
                                if k < len(equip_attr["embed"]):
                                    embed_updates.append(gr.update(label=f"镶嵌-{embed_attrs[k]}", visible=True))
                                else:
                                    embed_updates.append(gr.update(visible=False))

                            special_enchant_visible = position in SPECIAL_ENCHANT_POSITIONS
                            stone_visible = position in STONE_POSITIONS
                            return equip_attr, gr.update(visible=bool(enchant_map)), gr.update(
                                visible=special_enchant_visible), gr.update(visible=stone_visible), gr.update(
                                label=f"{name} {equip_name}\t{enchant_name}\t{stone_name}"), gr.update(
                                choices=list(range(max_strength + 1)), value=equip_attr["strength_level"],
                                visible=True), *embed_updates

                        return inner

                    equipment_dropdown.input(equipment_dropdown_func(label, equip, equipments, enchants),
                                             [equipment_dropdown, enchant_dropdown, stone_select, equipment_json],
                                             [equipment_json, enchant_dropdown, special_enchant_dropdown, stone_group,
                                              equip_accordion, strength_level, *embed_levels]
                                             )

                    def enchant_dropdown_func(name, enchant_map):
                        def inner(equip_name, enchant_name, stone_name, equip_attr):
                            if not enchant_name:
                                equip_attr["enchant"] = {}
                                return equip_attr, gr.update(label=name)
                            enchant_row = enchant_map[enchant_name]
                            equip_attr["enchant"] = get_enchant_attr(enchant_row)
                            return equip_attr, gr.update(
                                label=f"{name} {equip_name}\t{enchant_name}\t{stone_name}")

                        return inner

                    enchant_dropdown.input(enchant_dropdown_func(label, enchants),
                                           [equipment_dropdown, enchant_dropdown, stone_select, equipment_json],
                                           [equipment_json, equip_accordion])

                    def strength_level_func(equip_attr, level):
                        equip_attr["strength_level"] = level
                        return equip_attr

                    strength_level.change(strength_level_func, [equipment_json, strength_level], equipment_json)

                    def embed_level_func(k):
                        def inner(equip_attr, level):
                            equip_attr["embed_levels"][k] = level
                            return equip_attr

                        return inner

                    for i, embed_level in enumerate(embed_levels):
                        embed_level.change(embed_level_func(i), [equipment_json, embed_level], equipment_json)

                    def stone_attr_func(equip_attr, level, *attrs):
                        sub = stones[stones['stone_level'] == level]

                        name = ""
                        attr_updates = []
                        equip_attr["stone"] = {}

                        for n, attr in enumerate(attrs):
                            if not attr:
                                break
                            attr = ATTR_TYPE_REVERSE[ATTR_TYPE_TRANSLATE_REVERSE[attr]]

                            if attr in sub[f"Attribute{n + 1}ID"].unique():
                                sub = sub[sub[f"Attribute{n + 1}ID"] == attr]
                            else:
                                break

                            if len(sub) == 1:
                                name = sub.iloc[-1]['Name']
                            equip_attr["stone"][ATTR_TYPE_MAP[attr]] = sub.iloc[-1][
                                f"Attribute{n + 1}Value1"]
                            attr_updates.append(gr.update(visible=True))

                        if len(attr_updates) < MAX_STONE_ATTR:
                            sub_choices = [ATTR_TYPE_TRANSLATE[ATTR_TYPE_MAP[e]] for e in
                                           sub[f'Attribute{len(attr_updates) + 1}ID'].unique()]
                            attr_updates.append(
                                gr.update(choices=[""] + sub_choices, value="", visible=bool(sub_choices)))

                        for _ in range(len(attr_updates), MAX_STONE_ATTR):
                            attr_updates.append(gr.update(choices=[""], value="", visible=False))

                        return equip_attr, *attr_updates, gr.update(value=name)

                    stone_level.change(stone_attr_func, [equipment_json, stone_level, *stone_attrs],
                                       [equipment_json, *stone_attrs, stone_select])
                    for stone_attr in stone_attrs:
                        stone_attr.change(stone_attr_func, [equipment_json, stone_level, *stone_attrs],
                                          [equipment_json, *stone_attrs, stone_select])

                    def stone_select_func(name):
                        def inner(equip_name, enchant_name, stone_name):
                            return gr.update(label=f"{name} {equip_name}\t{enchant_name}\t{stone_name}")

                        return inner

                    stone_select.change(stone_select_func(label), [equipment_dropdown, enchant_dropdown, stone_select],
                                        equip_accordion)

                    def equip_attr_func(name):
                        def inner(equip_attr, equips_attr):
                            attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}

                            base_texts = []
                            for k, v in equip_attr['base'].items():
                                attrs[k] += v
                                base_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

                            strength_cof = STRENGTH_COF(equip_attr["strength_level"])
                            magic_texts = []
                            for k, v in equip_attr['magic'].items():
                                v_gain = round(v * strength_cof)
                                attrs[k] += v + v_gain
                                magic_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}(+{v_gain})")

                            embed_cof = [EMBED_COF(level) for level in equip_attr["embed_levels"]]
                            embed_texts = []
                            for n, (k, v) in enumerate(equip_attr['embed'].items()):
                                v = round(v * embed_cof[n])
                                attrs[k] += v
                                embed_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

                            enchant_texts = []
                            for k, v in equip_attr['enchant'].items():
                                attrs[k] += v
                                enchant_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

                            stone_texts = []
                            for k, v in equip_attr['stone'].items():
                                attrs[k] += v
                                stone_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

                            equips_attr[name] = attrs
                            return gr.update(value="\n".join(base_texts), visible=bool(base_texts)), gr.update(
                                value="\n".join(magic_texts), visible=bool(magic_texts)), gr.update(
                                value="\n".join(embed_texts), visible=bool(embed_texts)), gr.update(
                                value="\n".join(enchant_texts), visible=bool(enchant_texts)), gr.update(
                                value="\n".join(stone_texts), visible=bool(stone_texts)), equips_attr
                            json.dump()
                        return inner

                    equipment_json.change(equip_attr_func(label), [equipment_json, equipments_json],
                                          [base_box, magic_box, embed_box, enchant_box, stone_box, equipments_json])

        with gr.Column(scale=2, min_width=250):
            equip_box = gr.Textbox(label="装备属性")
        with gr.Column(scale=2, min_width=250):
            attr_box = gr.Textbox(label="角色属性")

            def equips_attr_func(equips_attr):
                attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}
                for equip_attr in equips_attr.values():
                    for k, v in equip_attr.items():
                        attrs[k] += v

                attribute = BeiAoJue(**attrs)
                attr_texts = []
                for k, v in ATTRIBUTE_MAP.items():
                    if attr := getattr(attribute, k):
                        if attr > 2:
                            attr = round(attr)
                        else:
                            attr = round(attr * 100, 2)
                        attr_texts.append(f"{v}: {attr}")

                return "\n".join([f"{ATTR_TYPE_TRANSLATE[k]}: {v}" for k, v in attrs.items() if v]), "\n".join(
                        attr_texts)

            equipments_json.change(equips_attr_func, equipments_json, [equip_box, attr_box])
