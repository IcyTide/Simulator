import requests
import pandas as pd


position_map = {
    "帽子": 3,
    "上衣": 2,
    "腰带": 6,
    "护腕": 10,
    "下装": 8,
    "鞋子": 9,
    "项链": 4,
    "腰坠": 7,
    "戒指": 5,
    "远程武器": 1,
    "近身武器": 0
}

suffix_map = {
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

params_template = {
    "client": "std",
    "pv_type": 1,
    "duty": 1,
    "pz": 1,
    "page": 1,
    "per": 200,
    "min_level": 9000,
    "max_level": 15000,
    "BelongSchool": "通用,精简,霸刀",
    "MagicKind": "力道,外功"
}


def get_equips_list(position):
    position = position_map[position]
    url = f"https://node.jx3box.com/equip/{suffix_map[position]}"
    params = params_template.copy()
    params['position'] = position
    res = requests.get(url, params=params)
    return res.json()['list']


attr_type_map = {
    "atMeleeWeaponDamageBase": "近战武器基础伤害",
    "atMeleeWeaponDamageRand": "近战武器浮动伤害",
    "atVitalityBase": "体质",
    "atPhysicsAttackPowerBase": "攻击",
    "atStrengthBase": "力道",
    "atPhysicsOvercomeBase": "破防",
    "atPhysicsCriticalStrike": "会心",
    "atPhysicsCriticalDamagePowerBase": "会效",
    "atHasteBase": "加速",
    "atSurplusValueBase": "破招",
    "atStrainBase": "无双"
}

attr_map = {
    "Overcome": "破防",
    "Critical": "会心",
    "CriticalDamage": "会效",
    "Haste": "加速",
    "Surplus": "破招",
    "Strain": "无双"
}
base_length = 6
magic_length = 12
diamond_length = 3


def get_equip_detail(equip, position):
    detail = {"ID": equip['ID'], "部位": position, "装分": equip['Level'], "名字": equip['Name'],
              "属性": "".join([attr_map[attr] for attr in attr_map if attr in equip['_Attrs']]),
              **{k: None for k in attr_type_map.values()}, **{f'镶嵌{k}': None for k in attr_type_map.values()}}
    for i in range(base_length):
        if not (attr_type := equip[f'Base{i + 1}Type']):
            break
        if attr_type not in attr_type_map:
            continue
        detail[attr_type_map[attr_type]] = (int(equip[f'Base{i + 1}Max']) + int(equip[f'Base{i + 1}Min'])) / 2

    for i in range(magic_length):
        if not (attr_type := equip[f'_Magic{i + 1}Type']):
            break
        attr_type = attr_type['attr']
        if attr_type[0] not in attr_type_map:
            continue
        detail[attr_type_map[attr_type[0]]] = (int(attr_type[1]) + int(attr_type[2])) / 2

    for i in range(diamond_length):
        if not (attr_type := equip[f'_DiamondAttributeID{i + 1}']):
            break
        if attr_type[0] not in attr_type_map:
            continue
        detail[f'镶嵌{attr_type_map[attr_type[0]]}'] = (int(attr_type[1]) + int(attr_type[2])) / 2
    return detail


if __name__ == '__main__':
    rows = []
    for position in position_map:
        for equip in get_equips_list(position):
            rows.append(get_equip_detail(equip, position))
    df = pd.DataFrame(rows).dropna(axis=1, how="all")
    df.to_excel("temp.xlsx", index=False)