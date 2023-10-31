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
    position = POSITION_MAP[position]
    url = f"https://node.jx3box.com/equip/{SUFFIX_MAP[position]}"
    params = equip_params.copy()
    params['position'] = position
    result = []
    res = requests.get(url, params=params).json()
    result.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        result.extend(res['list'])
    return result


def get_enchants_list(position):
    position = POSITION_MAP[position]
    url = f"https://node.jx3box.com/enchant/primary"
    params = enchant_params.copy()
    params['position'] = position
    res = requests.get(url, params=params)
    result = [e for e in sorted(res.json(), key=lambda x: x['Score'], reverse=True) if
              e['Attribute1ID'] in ATTR_TYPE_MAP]
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
    return result


if __name__ == '__main__':
    # for position in POSITION_MAP:
    #     json.dump(get_equips_list(position),
    #               open(os.path.join(EQUIPMENTS_DIR, f"{position}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    #     json.dump(get_enchants_list(position),
    #               open(os.path.join(ENCHANTS_DIR, f"{position}.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(get_stones_list(), open(STONES_DIR, "w", encoding="utf-8"), ensure_ascii=False)
