import gradio as gr
import pandas as pd

from bei_ao_jue.attribute import BeiAoJue
from ui.constant import *


def get_base_attr(row):
    attrs = {}
    for i in range(MAX_BASE_ATTR):
        if not (attr_type := row[f'Base{i + 1}Type']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Base{i + 1}Min'])
    return attrs


def get_magic_attr(row):
    attrs, gains = {}, []
    for i in range(MAX_MAGIC_ATTR):
        if not (attr := row[f'_Magic{i + 1}Type']):
            break
        attr = attr['attr']
        if attr[0] in ATTR_TYPE_MAP:
            attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
        elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"] and attr[1] in GAINS_MAP:
            gains.append(attr[1])
        else:
            continue

    if row["SkillID"] == WIND_PENDANT_SKILL_ID:
        gains.append(f"{row['SkillID']}-{row['SkillLevel']}")

    return attrs, gains


def get_embed_attr(row):
    attrs = {}
    for i in range(MAX_EMBED_ATTR):
        if not (attr := row[f'_DiamondAttributeID{i + 1}']):
            break
        if attr[0] not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
    return attrs


def get_enchant_attr(row):
    attrs = {}
    for i in range(MAX_ENCHANT_ATTR):
        if not (attr_type := row[f'Attribute{i + 1}ID']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Attribute{i + 1}Value1'])
    return attrs


def get_special_enchant(row, position):
    gains = []
    for k, v in SPECIAL_ENCHANT_MAP[position].items():
        if int(row['Level']) > k:
            gains.append(v)
            break
    return gains


def get_stone_attr(row):
    attrs = {}
    for i in range(MAX_STONE_ATTR):
        if not (attr_type := row[f'Attribute{i + 1}ID']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Attribute{i + 1}Value1'])
    return attrs, row['stone_level']


def get_set_attr(row):
    if set_attr := row['_SetAttrbs']:
        set_data = {}
        for k, v in row['_SetData'].items():
            if not v:
                continue
            count = k.split("_")[0]
            if count not in set_data:
                set_data[count] = []
            set_data[count].append(v['attr'])
        return set_attr['UiID'], set_data
    else:
        return "", {}


def build_equipment():
    stones = pd.read_json(STONES_DIR)
    stones = stones.set_index('index')
    equipments = pd.read_json(EQUIPMENTS_DIR, dtype=object)
    equipments = equipments.set_index('index')
    enchants = pd.read_json(ENCHANTS_DIR)
    enchants = enchants.set_index('index')

    # equips_config = json.load(open(EQUIPS_CONFIG_DIR, encoding="utf-8"))
    equipments_json = gr.JSON(value={}, visible=False)

    attribute_state = gr.State()

    gains_state = gr.State()

    with gr.Row():
        with gr.Column(scale=7):
            for label, equip in POSITION_TRANSLATE.items():
                sub_equipments = equipments[equipments['position'] == equip]
                sub_enchants = enchants[enchants['position'] == equip]

                with gr.Tab(label=label):
                    with gr.Row():
                        with gr.Column(scale=7):
                            with gr.Row():
                                equipment_dropdown = gr.Dropdown(choices=[""] + list(sub_equipments.index),
                                                                 label="装备",
                                                                 value="", scale=6)
                                strength_level = gr.Dropdown(choices=list(range(MAX_STRENGTH_LEVEL + 1)), label="精炼",
                                                             visible=False, scale=4)

                            with gr.Row():
                                enchant_dropdown = gr.Dropdown(choices=[""] + list(sub_enchants.index), label="附魔",
                                                               value="", visible=False, scale=6)

                                special_enchant_check = gr.Checkbox(visible=False, label="大附魔", scale=4)

                            with gr.Row():
                                embed_levels = []
                                for i in range(MAX_EMBED_ATTR):
                                    embed_level = gr.Dropdown(choices=list(range(MAX_EMBED_LEVEL + 1)), visible=False)
                                    embed_levels.append(embed_level)

                            with gr.Group(visible=False) as stone_group:
                                with gr.Row():
                                    stone_level = gr.Dropdown(choices=list(range(1, MAX_STONE_LEVEL + 1)),
                                                              label="五彩石等级", value=MAX_STONE_LEVEL, scale=4)
                                    stone_dropdown = gr.Dropdown(
                                        choices=[""] + list(stones[stones['stone_level'] == MAX_STONE_LEVEL].index),
                                        label="五彩石", value="", scale=6)
                                with gr.Row():
                                    stone_attrs = []
                                    for i in range(MAX_EMBED_ATTR):
                                        stone = gr.Textbox(visible=False)
                                        stone_attrs.append(stone)

                        with gr.Column(scale=3, min_width=200):
                            base_attr = gr.Textbox(label="基本属性", visible=False)
                            magic_attr = gr.Textbox(label="精炼属性", visible=False)
                            embed_attr = gr.Textbox(label="镶嵌属性", visible=False)
                            enchant_attr = gr.Textbox(label="附魔属性", visible=False)

                    equipment_json = gr.JSON(value={}, visible=False)

                def dropdown_func(position, equipment_map, enchant_map):
                    def inner(equip_name, enchant_name, stone_name, special_enchant, equip_attr):
                        if not equip_name:
                            equip_attr["base"] = {}
                            equip_attr["magic"] = {}
                            equip_attr["gains"] = []
                            equip_attr["embed"] = {}
                            equip_attr["enchant"] = {}
                            equip_attr["stone"] = {}
                            equip_attr['set_id'], equip_attr['set_data'] = "", {}
                            equip_attr["equip_name"] = ""
                            return equip_attr, gr.update(visible=False), gr.update(visible=False), gr.update(
                                visible=False), gr.update(visible=False), *[gr.update(visible=False) for _ in
                                                                            range(MAX_EMBED_ATTR)]

                        equip_row = equipment_map.loc[equip_name]
                        equip_attr["base"] = get_base_attr(equip_row)
                        equip_attr["magic"], equip_attr["gains"] = get_magic_attr(equip_row)
                        equip_attr["embed"] = get_embed_attr(equip_row)

                        if special_enchant:
                            equip_attr["gains"].extend(get_special_enchant(equip_row, position))

                        if enchant_name:
                            enchant_row = enchant_map.loc[enchant_name]
                            equip_attr["enchant"] = get_enchant_attr(enchant_row)
                        else:
                            equip_attr["enchant"] = {}
                        if stone_name:
                            stone_row = stones.loc[stone_name]
                            equip_attr["stone"], equip_attr["stone_level"] = get_stone_attr(stone_row)
                        else:
                            equip_attr["stone"], equip_attr["stone_level"] = {}, MAX_STONE_LEVEL

                        equip_attr['set_id'], equip_attr['set_data'] = get_set_attr(equip_row)

                        equip_attr['equip_name'] = equip_name
                        equip_attr['enchant_name'] = enchant_name
                        equip_attr['stone_name'] = stone_name

                        max_strength = int(equip_row['MaxStrengthLevel'])
                        if "strength_level" not in equip_attr:
                            equip_attr["strength_level"] = max_strength
                        else:
                            equip_attr["strength_level"] = min(max_strength, equip_attr["strength_level"])
                        strength_update = gr.update(choices=list(range(max_strength + 1)),
                                                    value=equip_attr["strength_level"], visible=True)
                        embed_updates = []
                        if "embed_levels" not in equip_attr:
                            equip_attr["embed_levels"] = [MAX_EMBED_LEVEL for _ in range(MAX_EMBED_ATTR)]

                        embed_attrs = [ATTR_TYPE_TRANSLATE[k] for k in equip_attr['embed']]

                        for k in range(MAX_EMBED_ATTR):
                            if k < len(equip_attr["embed"]):
                                embed_updates.append(
                                    gr.update(label=f"镶嵌-{embed_attrs[k]}", value=equip_attr["embed_levels"][k],
                                              visible=True))
                            else:
                                embed_updates.append(gr.update(value=0, visible=False))

                        enchant_update = gr.update(visible=not enchant_map.empty)
                        special_enchant_update = gr.update(visible=position in SPECIAL_ENCHANT_MAP)

                        stone_visible = position in STONE_POSITIONS
                        return equip_attr, enchant_update, special_enchant_update, gr.update(
                            visible=stone_visible), strength_update, *embed_updates

                    return inner

                equipment_dropdown.input(dropdown_func(equip, sub_equipments, sub_enchants),
                                         [equipment_dropdown, enchant_dropdown, stone_dropdown, special_enchant_check,
                                          equipment_json],
                                         [equipment_json, enchant_dropdown, special_enchant_check, stone_group,
                                          strength_level, *embed_levels])

                enchant_dropdown.input(dropdown_func(equip, sub_equipments, sub_enchants),
                                       [equipment_dropdown, enchant_dropdown, stone_dropdown, special_enchant_check,
                                        equipment_json],
                                       [equipment_json, enchant_dropdown, special_enchant_check, stone_group,
                                        strength_level, *embed_levels])
                stone_dropdown.input(dropdown_func(equip, sub_equipments, sub_enchants),
                                     [equipment_dropdown, enchant_dropdown, stone_dropdown, special_enchant_check,
                                      equipment_json],
                                     [equipment_json, enchant_dropdown, special_enchant_check, stone_group,
                                      strength_level, *embed_levels])

                special_enchant_check.input(dropdown_func(equip, sub_equipments, sub_enchants),
                                            [equipment_dropdown, enchant_dropdown, stone_dropdown,
                                             special_enchant_check, equipment_json],
                                            [equipment_json, enchant_dropdown, special_enchant_check, stone_group,
                                             strength_level, *embed_levels])

                def strength_level_func(equip_attr, level):
                    equip_attr["strength_level"] = level
                    return equip_attr

                strength_level.input(strength_level_func, [equipment_json, strength_level], equipment_json)

                def embed_level_func(k):
                    def inner(equip_attr, level):
                        equip_attr["embed_levels"][k] = level
                        return equip_attr

                    return inner

                for i, embed_level in enumerate(embed_levels):
                    embed_level.input(embed_level_func(i), [equipment_json, embed_level], equipment_json)

                def stone_level_func(level):
                    choices = list(stones[stones['stone_level'] == level].index)
                    return gr.update(choices=[""] + choices, value="", visible=bool(choices))

                stone_level.input(stone_level_func, stone_level, stone_dropdown)

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
                            v = int(v * embed_cof[n])
                            attrs[k] += v
                            embed_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

                        enchant_texts = []
                        for k, v in equip_attr['enchant'].items():
                            attrs[k] += v
                            enchant_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

                        stone_updates = []
                        for k, v in equip_attr['stone'].items():
                            attrs[k] += v
                            stone_updates.append(
                                gr.update(label=f"五彩石-{ATTR_TYPE_TRANSLATE[k]}", value=v, visible=True))
                        for _ in range(MAX_STONE_ATTR - len(stone_updates)):
                            stone_updates.append(gr.update(visible=False))

                        equips_attr[name] = {"attrs": attrs, "set": [equip_attr['set_id'], equip_attr['set_data']],
                                             "gains": equip_attr['gains'],
                                             "levels": {"strength": equip_attr["strength_level"],
                                                        "embed": equip_attr["embed_levels"],
                                                        "stone": equip_attr["stone_level"]},
                                             "names": {"equip": equip_attr['equip_name'],
                                                       "enchant": equip_attr['enchant_name'],
                                                       "stone": equip_attr['stone_name']}}

                        return gr.update(value="\n".join(base_texts), visible=bool(base_texts)), gr.update(
                            value="\n".join(magic_texts), visible=bool(magic_texts)), gr.update(
                            value="\n".join(embed_texts), visible=bool(embed_texts)), gr.update(
                            value="\n".join(enchant_texts),
                            visible=bool(enchant_texts)), *stone_updates, equips_attr

                    return inner

                equipment_json.change(equip_attr_func(label), [equipment_json, equipments_json],
                                      [base_attr, magic_attr, embed_attr, enchant_attr, *stone_attrs,
                                       equipments_json])

                # equip_config = equips_config.get(label, {})
                # names = equip_config.get("names", {})
                # levels = equip_config.get("levels", {})
                # equipment_dropdown.value = names.get("equip", "")
                # enchant_dropdown.value = names.get("enchant", "")
                #
                # strength_level.value = levels.get("strength", 0)
                # embed_level_list = levels.get("embed", [0 for _ in range(MAX_EMBED_ATTR)])
                # for i, embed_level in enumerate(embed_levels):
                #     embed_level.value = embed_level_list[i]
                #
                # stone_level.value = levels.get("stone", MAX_STONE_LEVEL)
                # stone_dropdown.value = names.get("stone", "")

        with gr.Column(scale=3):
            with gr.Row():
                with gr.Column(min_width=150):
                    equip_attr_box = gr.Textbox(label="装备属性")
                    equip_gain_box = gr.Textbox(label="装备效果")
                attr_box = gr.Textbox(label="角色属性")

    equip_box = gr.Textbox(label="当前配装", scale=7)

    def equips_attr_func(equips_attr):
        # json.dump(equips_attr, open(EQUIPS_CONFIG_DIR, "w", encoding="utf-8"), ensure_ascii=False)
        attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}
        gains = []

        equip_texts = []
        set_count = {}
        set_effect = {}

        for name in POSITION_TRANSLATE:
            if name not in equips_attr:
                continue
            equip_attr = equips_attr[name]
            if equip_attr['names']['equip']:
                equip_text = '\t\t'.join(equip_attr['names'].values())
                equip_texts.append(f"{name}: {equip_text}")

            for k, v in equip_attr['attrs'].items():
                attrs[k] += v
            gains.extend(equip_attr['gains'])

            set_id, set_data = equip_attr['set']
            if set_id not in set_count:
                set_count[set_id] = 0
                set_effect[set_id] = set_data
            set_count[set_id] += 1

        for set_id, set_data in set_effect.items():
            for count, effects in set_data.items():
                if int(count) > set_count[set_id]:
                    break
                for attr in effects:
                    if attr[0] in ATTR_TYPE_MAP:
                        attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
                    elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"] and attr[1] in GAINS_MAP:
                        gains.append(attr[1])
                    else:
                        continue

        attribute = BeiAoJue()
        equip_attr_texts = []
        for k, v in attrs.items():
            setattr(attribute, k, getattr(attribute, k) + v)
            if v:
                equip_attr_texts.append(f"{ATTR_TYPE_TRANSLATE[k]}: {v}")

        attr_texts = []
        for k, v in ATTRIBUTE_MAP.items():
            if attr := getattr(attribute, k):
                if attr > 2:
                    attr_texts.append(f"{v}: {round(attr)}")
                else:
                    attr_texts.append(f"{v}: {round(attr * 100, 2)}%")

        gains_texts = []
        gains_functions = []
        for gain in gains:
            gains_texts.append(GAINS_TRANSLATE[gain])
            gains_functions.append(GAINS_MAP[gain])
        return "\n".join(equip_attr_texts), "\n".join(gains_texts), "\n".join(attr_texts), "\n".join(
            equip_texts), attribute, gains_functions

    equipments_json.change(equips_attr_func, equipments_json,
                           [equip_attr_box, equip_gain_box, attr_box, equip_box, attribute_state, gains_state])
    return attribute_state, gains_state
