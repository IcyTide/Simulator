import json

import gradio as gr
import pandas as pd

from ui.constant import *


def get_special_enchant(row, position):
    for k, v in SPECIAL_ENCHANT_MAP[position].items():
        if row['level'] > k:
            return [v]
    return []


def build_equipment():
    attr_state = gr.State()
    gain_state = gr.State()
    equips_attr = gr.JSON({}, visible=False)

    equipments = {k: pd.DataFrame.from_dict(v, orient='index') for k, v in
                  json.load(open(EQUIPMENTS_DIR, encoding='utf-8')).items()}
    enchants = {
        k: pd.DataFrame.from_dict(v, orient='index').sort_values("score", ascending=False) if v else pd.DataFrame()
        for k, v in json.load(open(ENCHANTS_DIR, encoding='utf-8')).items()
    }

    stones = pd.read_json(STONES_DIR, orient='index')

    equip_components = {"equips_attr": equips_attr, "attr_state": attr_state, "gain_state": gain_state}
    with gr.Column(scale=7):
        for label, equip in POSITION_TRANSLATE.items():
            equip_components[equip] = {}
            equip_sub = equip_components[equip]
            equip_attr = gr.JSON({}, visible=False)
            equip_sub["equip_attr"] = equip_attr

            with gr.Tab(label=label):
                with gr.Row():
                    with gr.Column(scale=7):
                        with gr.Row():
                            equip_name = gr.Dropdown(choices=[""] + list(equipments[equip].index),
                                                     label="装备", value="", scale=6)
                            equip_sub["equip_name"] = equip_name
                            strength_level = gr.Dropdown(choices=list(range(MAX_STRENGTH_LEVEL + 1)), label="精炼",
                                                         visible=False, scale=4)
                            equip_sub["strength_level"] = strength_level

                        with gr.Row():
                            enchant_name = gr.Dropdown(choices=[""] + list(enchants[equip].index), label="附魔",
                                                       value="", visible=False, scale=6)
                            equip_sub["enchant_name"] = enchant_name
                            special_enchant = gr.CheckboxGroup(choices=["大附魔"], visible=False, label="大附魔",
                                                               scale=4)
                            equip_sub["special_enchant"] = special_enchant

                        embed_levels = []
                        with gr.Row():
                            for i in range(MAX_EMBED_ATTR):
                                embed_level = gr.Dropdown(choices=list(range(MAX_EMBED_LEVEL + 1)), visible=False)
                                embed_levels.append(embed_level)

                        equip_sub["embed_levels"] = embed_levels

                        with gr.Group(visible=False) as stone_group:
                            with gr.Row():
                                stone_level = gr.Dropdown(choices=list(range(1, MAX_STONE_LEVEL + 1)),
                                                          label="五彩石等级", value=MAX_STONE_LEVEL, scale=4)
                                equip_sub['stone_level'] = stone_level
                                stone_name = gr.Dropdown(
                                    choices=[""] + list(stones[stones['level'] == MAX_STONE_LEVEL].index),
                                    label="五彩石", value="", scale=6)

                                equip_sub['stone_name'] = stone_name
                            stone_attrs = []
                            with gr.Row():
                                for i in range(MAX_EMBED_ATTR):
                                    stone = gr.Textbox(visible=False)
                                    stone_attrs.append(stone)
                        equip_sub['stone_group'] = stone_group
                        equip_sub["stone_attrs"] = stone_attrs

                    with gr.Column(scale=3, min_width=200):
                        base_attrs = gr.Textbox(label="基本属性", visible=False)
                        equip_sub["base_attrs"] = base_attrs
                        magic_attrs = gr.Textbox(label="精炼属性", visible=False)
                        equip_sub["magic_attrs"] = magic_attrs
                        embed_attrs = gr.Textbox(label="镶嵌属性", visible=False)
                        equip_sub["embed_attrs"] = embed_attrs
                        enchant_attrs = gr.Textbox(label="附魔属性", visible=False)
                        equip_sub["enchant_attrs"] = enchant_attrs

    with gr.Column(scale=3):
        with gr.Row():
            with gr.Column(min_width=150):
                equip_attrs = gr.Textbox(label="装备属性")
                equip_components["equip_attrs"] = equip_attrs
                equip_gains = gr.Textbox(label="装备效果")
                equip_components["equip_gains"] = equip_gains

    equip_names = gr.Textbox(label="当前配装", scale=7)
    equip_components["equip_names"] = equip_names

    return equipments, enchants, stones, equip_components
