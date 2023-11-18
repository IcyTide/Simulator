import gradio as gr

from ui.constant import MAX_EMBED_ATTR, SPECIAL_ENCHANT_MAP, MAX_STONE_LEVEL, MAX_EMBED_LEVEL, \
    ATTR_TYPE_TRANSLATE, STONE_POSITIONS, STRENGTH_COF, EMBED_COF, MAX_STONE_ATTR, ATTR_TYPE_MAP, EQUIP_GAINS, \
    EQUIP_GAINS_NAME


def equipment_script(equipments, enchants, stones, equip_components):
    for equip, equip_component in equip_components['equips'].items():
        def update_equip(position):
            def inner(equip_name, enchant_name, special_enchant, stone_name, equip_attr):
                if not equip_name:
                    equip_attr["equip_name"] = ""
                    equip_attr["base"] = {}
                    equip_attr["magic"] = {}
                    equip_attr["embed"] = {}
                    equip_attr["gains"] = []
                    equip_attr["enchant"] = {}
                    equip_attr["stone"] = {}
                    equip_attr['set_id'] = ""
                    equip_attr['set_data'] = {}
                    return equip_attr, gr.update(visible=False), gr.update(visible=False), gr.update(
                        visible=False), gr.update(visible=False), *[gr.update(visible=False) for _ in
                                                                    range(MAX_EMBED_ATTR)]

                equip_row = equipments[position].loc[equip_name]
                equip_attr["base"] = equip_row['base']
                equip_attr["magic"] = equip_row['magic']
                equip_attr["embed"] = equip_row['embed']
                equip_attr['gains'] = equip_row['gains']

                if special_enchant:
                    for k, v in SPECIAL_ENCHANT_MAP[position].items():
                        if equip_row['level'] > k:
                            equip_attr['gains'].append(v)
                            break

                if enchant_name:
                    enchant_row = enchants[position].loc[enchant_name]
                    equip_attr["enchant"] = enchant_row['attr']
                else:
                    equip_attr["enchant"] = {}
                if stone_name:
                    stone_row = stones.loc[stone_name]
                    equip_attr["stone"] = stone_row['attr']
                    equip_attr["level"] = stone_row['level']
                else:
                    equip_attr["stone"] = {}
                    equip_attr["stone_level"] = MAX_STONE_LEVEL

                equip_attr['set_id'] = equip_row['set_id']
                equip_attr['set_data'] = equip_row['set_data']

                equip_attr['equip_name'] = equip_name
                equip_attr['enchant_name'] = enchant_name
                equip_attr['stone_name'] = stone_name

                if "strength_level" not in equip_attr:
                    equip_attr["strength_level"] = equip_row['max_strength']
                else:
                    equip_attr["strength_level"] = min(equip_row['max_strength'], equip_attr["strength_level"])
                strength_update = gr.update(choices=list(range(equip_row['max_strength'] + 1)),
                                            value=equip_attr["strength_level"], visible=True)
                embed_updates = []
                if "embed_levels" not in equip_attr:
                    equip_attr["embed_levels"] = [MAX_EMBED_LEVEL for _ in range(MAX_EMBED_ATTR)]

                enchant_update = gr.update(visible=not enchants[position].empty)
                special_enchant_update = gr.update(visible=position in SPECIAL_ENCHANT_MAP)

                stone_update = gr.update(visible=position in STONE_POSITIONS)

                embed_attrs = [ATTR_TYPE_TRANSLATE[e] for e in equip_attr['embed']]

                for n in range(MAX_EMBED_ATTR):
                    if n < len(equip_attr["embed"]):
                        embed_updates.append(gr.update(label=f"镶嵌-{embed_attrs[n]}",
                                                       value=equip_attr["embed_levels"][n], visible=True))
                    else:
                        embed_updates.append(gr.update(value=0, visible=False))

                return equip_attr, enchant_update, special_enchant_update, stone_update, strength_update, *embed_updates

            return inner

        update_components = [equip_component['equip_name'], equip_component['enchant_name'],
                             equip_component['special_enchant'], equip_component['stone_name']]
        for component in update_components:
            component.input(update_equip(equip),
                            [*update_components, equip_component['equip_attr']],
                            [equip_component['equip_attr'], equip_component['enchant_name'],
                             equip_component['special_enchant'], equip_component['stone_group'],
                             equip_component['strength_level'], *equip_component['embed_levels']])

        def update_strength_level(equip_attr, level):
            equip_attr["strength_level"] = level
            return equip_attr

        equip_component['strength_level'].input(update_strength_level,
                                                [equip_component['equip_attr'], equip_component['strength_level']],
                                                equip_component['equip_attr'])

        def update_embed_level(n):
            def inner(equip_attr, level):
                equip_attr["embed_levels"][n] = level
                return equip_attr

            return inner

        for i, embed_level in enumerate(equip_component['embed_levels']):
            embed_level.input(update_embed_level(i), [equip_component['equip_attr'], embed_level],
                              equip_component['equip_attr'])

        def update_stone_level(level):
            choices = list(stones[stones['level'] == level].index)
            return gr.update(choices=[""] + choices, value="", visible=bool(choices))

        equip_component['stone_level'].input(update_stone_level, equip_component['stone_level'],
                                             equip_component['stone_name'])

        def update_attr(position):
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

                equips_attr[position] = {"attrs": attrs, "set": [equip_attr['set_id'], equip_attr['set_data']],
                                         "gains": equip_attr['gains'],
                                         "names": {"equip": equip_attr['equip_name'],
                                                   "enchant": equip_attr['enchant_name'],
                                                   "stone": equip_attr['stone_name']},
                                         "levels": {"strength": equip_attr["strength_level"],
                                                    "embed": equip_attr["embed_levels"],
                                                    "stone": equip_attr["stone_level"]}}
                updates = [gr.update(value=equip_attr['equip_name']), gr.update(value=equip_attr['enchant_name']),
                           gr.update(value=equip_attr['stone_name']), gr.update(value=equip_attr['strength_level']),
                           *[gr.update(value=level) for level in equip_attr['embed_levels']],
                           gr.update(value=equip_attr['stone_level'])]
                return gr.update(value="\n".join(base_texts), visible=bool(base_texts)), gr.update(
                    value="\n".join(magic_texts), visible=bool(magic_texts)), gr.update(
                    value="\n".join(embed_texts), visible=bool(embed_texts)), gr.update(
                    value="\n".join(enchant_texts), visible=bool(enchant_texts)), *stone_updates, equips_attr, *updates

            return inner

        def update_attrs(equips_attr):
            name_texts = []
            attrs = {attr: 0 for attr in ATTR_TYPE_TRANSLATE}
            gains = []
            gain_texts = []

            set_count = {}
            set_effect = {}

            for position, equip_attr in equips_attr.items():
                if not equip_attr or not equip_attr['names']['equip']:
                    continue
                name_text = '\t\t'.join(equip_attr['names'].values())
                name_texts.append(f"{position}: {name_text}")

                for k, v in equip_attr['attrs'].items():
                    attrs[k] += v
                for e in equip_attr['gains']:
                    gains.append(EQUIP_GAINS[e])
                    gain_texts.append(EQUIP_GAINS_NAME[e])

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
                            attrs[ATTR_TYPE_MAP[attr[0]]] += int(attr[1])
                        elif (attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"] and
                              attr[1] in EQUIP_GAINS_NAME):
                            gains.append(EQUIP_GAINS[attr[1]])
                            gain_texts.append(EQUIP_GAINS_NAME[attr[1]])

            attr_texts = [f"{ATTR_TYPE_TRANSLATE[k]}: {v}" for k, v in attrs.items() if v]
            return "\n".join(name_texts), "\n".join(attr_texts), "\n".join(gain_texts), attrs, gains

        equip_component['equip_attr'].change(
            update_attr(equip),
            [equip_component['equip_attr'], equip_components['equips_attr']],
            [equip_component['base_attr'], equip_component['magic_attr'], equip_component['embed_attr'],
             equip_component['enchant_attr'], *equip_component['stone_attrs'],
             equip_components['equips_attr'],
             equip_component['equip_name'], equip_component['enchant_name'], equip_component['stone_name'],
             equip_component['strength_level'], *equip_component['embed_levels'], equip_component['stone_level']]
        ).then(
            update_attrs,
            equip_components['equips_attr'],
            [equip_components['names'], equip_components["attrs"], equip_components["gains"],
             equip_components['attr_state'], equip_components['gain_state']]
        )
