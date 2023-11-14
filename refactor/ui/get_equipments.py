import json
import os

import requests

from ui.constant import *

POSITION_MAP = {
    "hat": 3,
    "jacket": 2,
    "belt": 6,
    "wrist": 10,
    "bottoms": 8,
    "shoes": 9,
    "necklace": 4,
    "pendant": 7,
    "ring": 5,
    "tertiary_weapon": 1,
    "primary_weapon": 0
}

SUFFIX_MAP = {
    3: 'armor',
    2: 'armor',
    6: 'armor',
    10: 'armor',
    8: 'armor',
    9: 'armor',
    4: 'trinket',
    7: 'trinket',
    5: 'trinket',
    1: 'weapon',
    0: 'weapon'
}

equip_params = {
    "client": "std",
    "pv_type": 1,
    "pz": 1,
    "page": 1,
    "per": 300,
    "min_level": 12000,
    "max_level": 15000
}

enchant_params = {
    "client": "std",
    "subtype": 1,
    "latest_enhance": 1
}


def get_equips_list(position):
    position_id = POSITION_MAP[position]
    url = f"https://node.jx3box.com/equip/{SUFFIX_MAP[position_id]}"
    params = equip_params.copy()
    params['position'] = position_id
    equips = []
    res = requests.get(url, params=params).json()
    equips.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        equips.extend(res['list'])

    result = {get_equip_name(row): get_equip_detail(row) for row in equips}

    return result


def get_equip_name(row):
    name = row['Name']
    attrs = " ".join([EQUIP_ATTR_MAP[attr] for attr in EQUIP_ATTR_MAP if attr in row['_Attrs']])
    level = row['Level']
    return f"{name} ({attrs}) {level}"


def get_equip_detail(row):
    base_attrs, magic_attrs, embed_attrs = {}, {}, {}
    set_id, set_data = "", {}
    gains = []
    for i in range(MAX_BASE_ATTR):
        if not (attr_type := row[f'Base{i + 1}Type']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        base_attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Base{i + 1}Max'])
    for i in range(MAX_MAGIC_ATTR):
        if not (attr := row[f'_Magic{i + 1}Type']):
            break
        attr = attr['attr']
        if attr[0] in ATTR_TYPE_MAP:
            magic_attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
        elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"] and attr[1] in EQUIP_GAINS:
            gains.append(attr[1])
        else:
            continue
    for i in range(MAX_EMBED_ATTR):
        if not (attr := row[f'_DiamondAttributeID{i + 1}']):
            break
        if attr[0] not in ATTR_TYPE_MAP:
            continue
        embed_attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])

    if row["SkillID"] == WIND_PENDANT_SKILL_ID:
        gains.append(f"{row['SkillID']}-{row['SkillLevel']}")

    if set_attr := row['_SetAttrbs']:
        set_id = set_attr['UiID']
        for k, v in row['_SetData'].items():
            if not v:
                continue
            count = k.split("_")[0]
            if count not in set_data:
                set_data[count] = []
            set_data[count].append(v['attr'])
    return {
        "school": row['BelongSchool'],
        "kind": row['MagicKind'],
        "level": int(row['Level']),
        "max_strength": int(row['MaxStrengthLevel']),
        "base": base_attrs,
        "magic": magic_attrs,
        "embed": embed_attrs,
        "gains": gains,
        "set_id": set_id,
        "set_data": set_data
    }


def get_enchants_list(position):
    position_id = POSITION_MAP[position]
    url = f"https://node.jx3box.com/enchant/primary"
    params = enchant_params.copy()
    params['position'] = position_id
    res = requests.get(url, params=params)
    enchants = [e for e in sorted(res.json(), key=lambda x: x['Score'], reverse=True) if
                e['Attribute1ID'] in ATTR_TYPE_MAP]

    result = {get_enchant_name(row): get_enchant_detail(row) for row in enchants}

    return result


def get_enchant_name(row):
    if not row:
        return ""
    name = row['Name']
    attr = row['AttriName']
    return f"{name} {attr}"


def get_enchant_detail(row):
    attrs = {}
    for i in range(MAX_ENCHANT_ATTR):
        if not (attr_type := row[f'Attribute{i + 1}ID']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Attribute{i + 1}Value1'])
    return {
        "score": row['Score'],
        "attr": attrs
    }


def get_stones_list():
    url = "https://node.jx3box.com/enchant/stone"
    params = {
        "client": "std",
        "page": 1,
        "per": 100
    }
    stones = []
    res = requests.get(url, params=params).json()
    stones.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        stones.extend(res['list'])
    stones = [e for e in stones if e['Attribute1ID'] in ATTR_TYPE_MAP and e['Attribute2ID'] in ATTR_TYPE_MAP and e[
        'Attribute3ID'] in ATTR_TYPE_MAP]

    result = {get_stone_name(row): get_stone_detail(row) for row in stones}

    return result


def get_stone_name(row):
    name = row['Name']
    attrs = " ".join([STONE_ATTR_MAP[attr] for attr in row['_Attrs'] if attr in STONE_ATTR_MAP])
    return f"{name} ({attrs})"


def get_stone_detail(row):
    attrs = {}
    for i in range(MAX_STONE_ATTR):
        if not (attr_type := row[f'Attribute{i + 1}ID']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Attribute{i + 1}Value1'])

    return {
        "level": row['stone_level'],
        "attr": attrs
    }


if __name__ == '__main__':
    equip_list = {}
    enchant_list = {}
    for pos in POSITION_MAP:
        equip_list[pos] = get_equips_list(pos)
        enchant_list[pos] = get_enchants_list(pos)
    json.dump(equip_list,
              open(EQUIPMENTS_DIR, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(enchant_list,
              open(ENCHANTS_DIR, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(get_stones_list(), open(STONES_DIR, "w", encoding="utf-8"), ensure_ascii=False)
