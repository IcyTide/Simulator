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
    "duty": 1,
    "pz": 1,
    "page": 1,
    "per": 300,
    "min_level": 11000,
    "max_level": 15000,
    "BelongSchool": "通用,精简,霸刀",
    "MagicKind": "力道,外功"
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
    result = []
    res = requests.get(url, params=params).json()
    result.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        result.extend(res['list'])

    def get_equip_name(row):
        name = row['Name']
        attrs = " ".join([EQUIP_ATTR_MAP[attr] for attr in EQUIP_ATTR_MAP if attr in row['_Attrs']])
        level = row['Level']
        return f"{name} ({attrs}) {level}"

    for e in result:
        e['index'] = get_equip_name(e)
        e['position'] = position

    return result


def get_enchants_list(position):
    position_id = POSITION_MAP[position]
    url = f"https://node.jx3box.com/enchant/primary"
    params = enchant_params.copy()
    params['position'] = position_id
    res = requests.get(url, params=params)
    result = [e for e in sorted(res.json(), key=lambda x: x['Score'], reverse=True) if
              e['Attribute1ID'] in ATTR_TYPE_MAP]

    def get_enchant_name(row):
        if not row:
            return ""
        name = row['Name']
        attr = row['AttriName']
        return f"{name} {attr}"

    for e in result:
        e['index'] = get_enchant_name(e)
        e['position'] = position

    return result


def get_stones_list():
    url = "https://node.jx3box.com/enchant/stone"
    params = {
        "client": "std",
        "page": 1,
        "per": 100
    }
    result = []
    res = requests.get(url, params=params).json()
    result.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        result.extend(res['list'])
    result = [e for e in result if e['Attribute1ID'] in ATTR_TYPE_MAP and e['Attribute2ID'] in ATTR_TYPE_MAP and e[
        'Attribute3ID'] in ATTR_TYPE_MAP]

    def get_stone_name(row):
        name = row['Name']
        attrs = " ".join([STONE_ATTR_MAP[attr] for attr in row['_Attrs'] if attr in STONE_ATTR_MAP])
        return f"{name} ({attrs})"

    for e in result:
        e['index'] = get_stone_name(e)

    return result


if __name__ == '__main__':
    # equip_list = []
    # enchant_list = []
    # for position in POSITION_MAP:
    #     equip_list.extend(get_equips_list(position))
    #     enchant_list.extend(get_enchants_list(position))
    # json.dump(equip_list,
    #           open(EQUIPMENTS_DIR, "w", encoding="utf-8"), ensure_ascii=False)
    # json.dump(enchant_list,
    #           open(ENCHANTS_DIR, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(get_stones_list(), open(STONES_DIR, "w", encoding="utf-8"), ensure_ascii=False)
