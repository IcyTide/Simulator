import json
from functools import cache

import requests

from ui.constant import MAX_BASE_ATTR, MAX_MAGIC_ATTR, MAX_EMBED_ATTR, MAX_ENCHANT_ATTR, MAX_STONE_ATTR, MAX_STONE_LEVEL
from ui.constant import EQUIPMENTS_DIR, ENCHANTS_DIR, STONES_DIR

ATTR_TYPE_MAP = {
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atStrengthBase": "strength_base",
    "atSpiritBase": "spirit_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atAllTypeCriticalStrike": "all_critical_strike_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_power_base",
    "atStrainBase": "strain_base",
    "atHasteBase": "haste_base",
    "atSurplusValueBase": "surplus",
}
EQUIP_ATTR_MAP = {
    "Overcome": "破防",
    "Critical": "会心",
    "CriticalDamage": "会效",
    "Haste": "加速",
    "Surplus": "破招",
    "Strain": "无双"
}

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

POSITION_TRANSLATE = {
    '帽子': 'hat',
    '上衣': 'jacket',
    '腰带': 'belt',
    '护腕': 'wrist',
    '下装': 'bottoms',
    '鞋子': 'shoes',
    '项链': 'necklace',
    '腰坠': 'pendant',
    '戒指1': 'ring',
    '戒指2': 'ring',
    '远程武器': 'tertiary_weapon',
    '近战武器': 'primary_weapon'
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
SPECIAL_ENCHANT_MAP = {
    "3": {
        12800: "15436-11",
        11500: "15436-10",
        10600: "15436-9"
    },
    "2": {
        12800: "22151-11",
        11500: "22151-10",
        10600: "22151-9"
    },
    "6": {
        0: "22169"
    },
    "10": {
        0: "22166"
    },
    "9": {
        0: "33247"
    },
}
STONE_ATTR_MAP = {
    "atSpiritBase": "根骨",
    "atStrengthBase": "力道",
    "atPhysicsAttackPowerBase": "攻击",
    "atPhysicsCriticalStrike": "会心",
    "atAllTypeCriticalStrike": "全会心",
    "atPhysicsCriticalDamagePowerBase": "会效",
    "atPhysicsOvercomeBase": "破防",
    "atMeleeWeaponDamageBase": "武器伤害",
    "atStrainBase": "无双",
    "atHasteBase": "加速",
    "atSurplusValueBase": "破招",
}

equip_params = {
    "client": "std",
    "pv_type": 1,
    "pz": 1,
    "page": 1,
    "per": 300,
    "min_level": 11000,
    "max_level": 15000
}

enchant_params = {
    "client": "std",
    "subtype": 1,
    "latest_enhance": 1
}


@cache
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

    result = {get_equip_name(row): get_equip_detail(row) for row in reversed(equips)}

    return result


def get_equip_name(row):
    name = row['Name']
    attrs = " ".join([EQUIP_ATTR_MAP[attr] for attr in EQUIP_ATTR_MAP if attr in row['_Attrs']])
    level = row['Level']
    return f"{name} ({attrs}) {level}"


def get_equip_detail(row):
    base_attrs, magic_attrs, embed_attrs = {}, {}, {}
    set_id, set_data = "", {}
    level = int(row['Level'])
    special_enchant = None
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
        elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"]:
            gains.append(attr[1])
        else:
            continue
    for i in range(MAX_EMBED_ATTR):
        if not (attr := row[f'_DiamondAttributeID{i + 1}']):
            break
        if attr[0] not in ATTR_TYPE_MAP:
            continue
        embed_attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])

    for k, v in SPECIAL_ENCHANT_MAP.get(row['SubType'], {}).items():
        if level > k:
            special_enchant = v
            break

    if row["SkillID"]:
        gains.append(f"{row['SkillID']}-{row['SkillLevel']}")

    if set_attr := row['_SetAttrbs']:
        set_id = set_attr['UiID']
        for k, v in row['_SetData'].items():
            if not v:
                continue
            count = k.split("_")[0]
            if count not in set_data:
                set_data[count] = []
            effect = {}
            attr = v['attr']
            if attr[0] in ATTR_TYPE_MAP:
                effect[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
            elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"]:
                effect['gain'] = attr[1]
            set_data[count].append(effect)
    return {
        "school": row['BelongSchool'],
        "kind": row['MagicKind'],
        "level": level,
        "max_strength": int(row['MaxStrengthLevel']),
        "base": base_attrs,
        "magic": magic_attrs,
        "embed": embed_attrs,
        "gains": gains,
        "special_enchant": special_enchant,
        "set_id": set_id,
        "set_data": set_data
    }


@cache
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


def get_stones_list(level):
    url = "https://node.jx3box.com/enchant/stone"
    params = {
        "client": "std",
        "level": level,
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
    stone_list = {}
    for label, pos in POSITION_TRANSLATE.items():
        equip_list[label] = get_equips_list(pos)
        enchant_list[label] = get_enchants_list(pos)
    for n in range(MAX_STONE_LEVEL):
        stone_list = {**stone_list, **get_stones_list(MAX_STONE_LEVEL - n)}
    json.dump(equip_list, open(EQUIPMENTS_DIR, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(enchant_list, open(ENCHANTS_DIR, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(stone_list, open(STONES_DIR, "w", encoding="utf-8"), ensure_ascii=False)
